from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser as _ArgumentParser, Namespace
from configparser import ConfigParser
from typing import Any, Sequence
from vix import VixHost, VixVM

import sys
import time

from .vm import VM
from . import logger


class ArgumentParser(_ArgumentParser):
    def _check_value(self, action, value):
        if isinstance(value, list) and not value:
            return
        return super()._check_value(action, value)


class VMManager(logger.Logger):
    def __init__(self, name: str | None = None):
        super().__init__(name)
        # fmt: off
        # Parser for initial arguments
        self.init_parser = ArgumentParser(add_help=False)
        self.init_parser.add_argument("-c", "--config-file", default="vm-manager.ini", metavar="PATH", help="config file path")
        self.init_parser.add_argument("-H", "--hostname", metavar="HOST", help="vix host hostname")
        self.init_parser.add_argument("-P", "--port", type=int, default=0, metavar="PORT", help="vix host port")
        self.init_parser.add_argument("-u", "--username", metavar="USER", help="vix host username")
        self.init_parser.add_argument("-p", "--password", metavar="PASS", help="vix host password")
        self.init_parser.add_argument("-S", "--service-provider", type=int, default=1, metavar="NUM", choices=(1, 2, 3, 4, 10, 11), help="vix host service provider (1 = default, 2 = vmware_server, 3 = vmware_workstation, 4 = vmware_player, 10 = vmware_vi_server, 11 = vmware_workstation_shared)")
        self.init_parser.add_argument("-s", "--separator", default="then", metavar="SEP", help="separator between commands")
        self.init_parser.add_argument("-l", "--log-file", default="vm-manager.log", metavar="PATH", help="log file path")
        self.init_parser.add_argument("-v", "--verbose", action="store_true", help="generate more detailed output")
        self.init_parser.add_argument("-d", "--dry-run", action="store_true", help="simulate commands only")
        
        # Parser for commands
        self.parser = ArgumentParser(parents=[self.init_parser], description="manage one or more vms using various commands", formatter_class=ArgumentDefaultsHelpFormatter)  # fmt: skip
        self.subparsers = self.parser.add_subparsers(title="commands", dest="command", required=True)
        self.commands: dict[str, Namespace] = {}
        self.add_command("list", help="list available vms", allow_actions=False, callback=self.list_callback)
        self.add_command("wait", help="pause execution (tip: use wait to add some delay between execution of multiple commands)", allow_actions=False, arguments=[(["seconds"], {"type": int, "metavar": "SECS", "help": "number of seconds to wait"})], callback=self.wait_callback)
        self.add_command("execute", help="execute command in one or more vms", choices_expr="is_present_in_host & on", arguments=[(["script"], {"help": "command to run"})], callback=self.execute_callback)
        self.add_command("start", help="start one or more vms", choices_expr="is_present_in_host - on", arguments=[(["-g", "--launch-gui"], {"action": "store_true", "help": "launch gui while starting vm"})], callback=self.start_callback)
        self.add_command("stop", help="stop one or more vms", choices_expr="is_present_in_host & on", arguments=[(["-f", "--force-shutdown"], {"action": "store_true", "help": "force shutdown vm"})], callback=self.stop_callback)
        self.add_command("delete", help="delete one or more vms", choices_expr="is_present_in_host & is_present_in_config - read_only", arguments=[(["-k", "--keep-files"], {"action": "store_true", "help": "keep vm files in filesystem"})], callback=self.delete_callback)
        self.add_command("clone", help="clone one or more vms from their respective sources", choices_expr="source_is_present_in_host & is_present_in_config & clone - is_present_in_host", callback=self.clone_callback)
        # fmt: on

    def add_command(self, name: str, help: str, allow_actions: bool = True, choices_expr: str | None = None, arguments: list[tuple[list[str], dict[str, Any]]] | None = None, **defaults):  # fmt: skip
        command = Namespace(name=name, help=help, allow_actions=allow_actions, choices_expr=choices_expr)
        parser = self.subparsers.add_parser(name, description=help, help=help)
        if arguments:
            for args, kwargs in arguments:
                parser.add_argument(*args, **kwargs)
        if allow_actions:
            # fmt: off
            parser.add_argument("-a", "--all", action="store_true", help=f"{name} all vms")
            command.choose_actions = [
                parser.add_argument("-e", "--except", nargs="+", dest="exceptions", help=f"which vm(s) not to {name}", metavar="vm"),
                parser.add_argument("vm_names", nargs="*", help=f"which vm(s) to {name}", metavar="vm")]
            # fmt: on
        parser.set_defaults(**defaults)
        self.commands[name] = command

    def list_callback(self):
        self._debug("Running list command")
        vms = self.select_vms("is_present_in_host")
        if len(vms) > 0:
            self._info("Available vms:\n" + "\n".join(vms))
        else:
            self._info("No available vms")
        self._debug("Finished running list command")

    def wait_callback(self):
        self._debug("Running wait command")
        self._info(f"Waiting for {self.namespace.seconds} seconds")
        time.sleep(self.namespace.seconds)
        self._debug("Finished running wait command")

    def execute_callback(self):
        self._debug("Running execute command")
        for vm_name in self.selected_vms:
            vm = self.vms[vm_name]
            vm.login()
            vm.execute(self.namespace.script)
        self._debug("Finished running execute command")

    def start_callback(self):
        self._debug("Running start command")
        for vm_name in self.selected_vms:
            vm = self.vms[vm_name]
            vm.start(self.namespace.launch_gui)
        self._debug("Finished running start command")

    def stop_callback(self):
        self._debug("Running stop command")
        for vm_name in self.selected_vms:
            vm = self.vms[vm_name]
            vm.stop(self.namespace.force_shutdown)
        self._debug("Finished running stop command")

    def delete_callback(self):
        self._debug("Running delete command")
        for vm_name in self.selected_vms:
            vm = self.vms[vm_name]
            vm.delete(not self.namespace.keep_files)
        self._debug("Finished running delete command")

    def clone_callback(self):
        self._debug("Running clone command")
        for vm_name in self.selected_vms:
            source = self.config[vm_name]["source"]
            vm = self.vms[source]
            vm.clone(vm_name)
        self._debug("Finished running clone command")

    def parse_args(self, args: Sequence[str] | None = None):
        # Parse initial arguments
        self.args = [args] if isinstance(args, str) else sys.argv[1:] if args is None else args
        self.namespace = Namespace()
        self.namespace, self.args = self.init_parser.parse_known_args(self.args, self.namespace)

        # Configure logger
        logger.add_file_handler(self.namespace.log_file)
        if self.namespace.verbose:
            logger.set_console_handler(logger.logging.DEBUG)

        # Load config
        self.config = ConfigParser(default_section="default")
        self.config.read(self.namespace.config_file)

        # Initialize host
        host_tuple = (self.namespace.hostname, self.namespace.port)
        credentials = (self.namespace.username, self.namespace.password)
        self.host = VixHost(self.namespace.service_provider, host_tuple, credentials)

        # Initialize VMs
        self.vms = {}
        for vm_or_name in self.config.sections() + self.host.find_items():
            vm = VM(vm_or_name, self.config, self.host)
            vm.dry_run = self.namespace.dry_run
            self.vms[vm.vm_name] = vm

        # Parse commands
        self.selected_vms = []
        sep = self.namespace.separator
        while sep in self.args:
            i = self.args.index(sep)
            self.parse_command(self.args[:i])
            self.args = self.args[i + 1 :]
        self.parse_command(self.args)

    def parse_command(self, args: Sequence[str]):
        self._debug(f"Parsing command: {args}")

        # Prepare commands
        self.classify_vms()
        for command in self.commands.values():
            if command.choices_expr is None:
                continue
            command.choices = self.select_vms(command.choices_expr)
            if not command.choices:
                continue
            for action in command.choose_actions:
                action.choices = command.choices

        # Parse arguments
        self.parser.parse_args(args, self.namespace)

        # Process selected vms
        command = self.commands[self.namespace.command]
        if command.allow_actions:
            is_present_in_host = self.vm_classes["is_present_in_host"]
            vm_names = set(self.namespace.vm_names)
            for vm_name in vm_names - is_present_in_host:
                self._info(f"Skipping {vm_name} as it is not present in host")
            vm_names &= is_present_in_host
            choices = set(command.choices)
            if self.namespace.all:
                vm_names |= choices
            if self.namespace.exceptions:
                vm_names -= set(self.namespace.exceptions)
            if vm_names:
                self.selected_vms = sorted(vm_names)

        # Execute callback
        if hasattr(self.namespace, "callback"):
            self.namespace.callback()
        self._debug(f"Finished parsing command {args}")

    def classify_vms(self):
        self.vm_classes = {key: set[str]() for key in ["all", "read_only", "is_present_in_host", "is_present_in_config", "on", "off", "clone", "source_is_present_in_host"]}  # fmt: skip
        for vm_name, vm in self.vms.items():
            self.vm_classes["all"].add(vm_name)
            if vm.read_only:
                self.vm_classes["read_only"].add(vm_name)
            if vm.is_present_in_host:
                self.vm_classes["is_present_in_host"].add(vm_name)
            if vm.is_present_in_config:
                self.vm_classes["is_present_in_config"].add(vm_name)
            if vm.is_powerstate_powered_on:
                self.vm_classes["on"].add(vm_name)
            if vm.is_powerstate_powered_off:
                self.vm_classes["off"].add(vm_name)
            if vm.is_clone:
                self.vm_classes["clone"].add(vm_name)
                if vm.source in self.vm_classes["is_present_in_host"]:
                    self.vm_classes["source_is_present_in_host"].add(vm_name)

    def select_vms(self, expr: str) -> list[str]:
        result = eval(expr, {}, self.vm_classes)
        return sorted(result)
