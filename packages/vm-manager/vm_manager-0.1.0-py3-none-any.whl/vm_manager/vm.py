from configparser import ConfigParser, SectionProxy
from difflib import unified_diff
from tempfile import mkstemp
from typing import cast
from vix import VixError, VixHost, VixSnapshot, VixVM

import os

from . import logger


class VMMeta(type):
    def __init__(self, name, bases, class_dict):
        super().__init__(name, bases, class_dict)
        self.cache = {}

    def __call__(self, vm_name: str, config: ConfigParser, host: VixHost):
        if vm_name in self.cache:
            instance = self.cache[vm_name]
            return instance
        instance = super().__call__(vm_name, config, host)
        self.cache[vm_name] = instance
        return instance


class VM(logger.Logger, metaclass=VMMeta):
    def __init__(self, vm_name: str, config: ConfigParser, host: VixHost):
        super().__init__(name=vm_name)
        self.vm_name = vm_name
        self.config = config
        self.load_options()
        self.host = host
        self.vm = None
        self.load_vm()
        self._snapshot = None
        self.dry_run = False

    @property
    def options(self) -> SectionProxy | None:
        if not self.has_options:
            return None
        return self.config[self.vm_name]

    @property
    def has_options(self) -> bool:
        return self.config.has_section(self.vm_name)

    def load_options(self):
        if not self.has_options:
            # self._debug(f"Did not load options for {self.vm_name} as it could not be found in the config file")
            return
        assert self.options is not None
        # self._debug(f"Loading options for {self.vm_name}")
        self.root_dir = self.options["root_dir"]
        self.username = self.options["username"]
        self.password = self.options["password"]
        self.is_clone = self.options.getboolean("is_clone", fallback=False)
        self.is_linked = self.options.getboolean("is_linked", fallback=False)
        self.source = self.options.get("source", fallback=None)
        self.read_only = self.options.getboolean("read_only", fallback=False)
        # self._debug(f"Finished loading options for {self.vm_name}")

    def load_vm(self):
        if self.vm is not None:
            # self._debug(f"Did not load {self.vm_name} as it is already loaded")
            return
        try:
            # self._debug(f"Loading VM for {self.vm_name}")
            self.vm = self.host.open_vm(self.vmx_path)
            # self._debug(f"Finished loading VM for {self.vm_name}")
        except VixError as e:
            (code,) = e.args
            if code != 4000:  # VM_NOT_FOUND
                raise
            # self._debug(f"Did not load VM for {self.vm_name} as it could not be found in the host")

    @staticmethod
    def get_vmx_path(vm_name: str, root_dir: str) -> str:
        return os.path.join(root_dir, vm_name, f"{vm_name}.vmx")

    @property
    def vmx_path(self) -> str:
        return self.get_vmx_path(self.vm_name, self.root_dir)

    @property
    def is_present_in_host(self) -> bool:
        if self.vm is None:
            self.load_vm()
        return self.vm is not None

    @property
    def is_present_in_config(self) -> bool:
        return self.options is not None

    @property
    def power_state(self) -> int:
        return cast(int, self.vm.power_state) if self.vm is not None else 0

    @property
    def tools_state(self) -> int:
        return cast(int, self.vm.tools_state) if self.vm is not None else 0

    @property
    def is_powerstate_powering_off(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_POWERING_OFF)

    @property
    def is_powerstate_powered_off(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_POWERED_OFF)

    @property
    def is_powerstate_powering_on(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_POWERING_ON)

    @property
    def is_powerstate_powered_on(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_POWERED_ON)

    @property
    def is_powerstate_suspending(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_SUSPENDING)

    @property
    def is_powerstate_suspended(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_SUSPENDED)

    @property
    def is_powerstate_tools_running(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_TOOLS_RUNNING)

    @property
    def is_powerstate_resetting(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_RESETTING)

    @property
    def is_powerstate_blocked_on_msg(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_BLOCKED_ON_MSG)

    @property
    def is_powerstate_paused(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_PAUSED)

    @property
    def is_powerstate_resuming(self) -> bool:
        return bool(self.power_state & VixVM.VIX_POWERSTATE_RESUMING)

    @property
    def is_toolstate_unknown(self) -> bool:
        return bool(self.tools_state & VixVM.VIX_TOOLSSTATE_UNKNOWN)

    @property
    def is_toolstate_running(self) -> bool:
        return bool(self.tools_state & VixVM.VIX_TOOLSSTATE_RUNNING)

    @property
    def is_toolstate_not_installed(self) -> bool:
        return bool(self.tools_state & VixVM.VIX_TOOLSSTATE_NOT_INSTALLED)

    def get_snapshot(self) -> VixSnapshot | None:
        if self._snapshot is not None:
            # self._info(f"Reusing cached snapshot for {self.vm_name}")
            return self._snapshot
        # else:
        # self._debug(f"No cached snapshot for {self.vm_name} found")
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not find snapshot for {self.vm_name} as it could not be found in the host")
            if not self.is_present_in_config:
                self._error(
                    f"Did not find snapshot for {self.vm_name} as its options could not be found in the config file"
                )
            if self.is_clone:
                self._error(f"Did not find snapshot for {self.vm_name} as it is a clone")
            assert self.vm is not None
            if self.vm.snapshots_get_root_count():
                self._info(f"Removing current snapshot for {self.vm_name}")
                snapshot = self.vm.snapshot_get_current()
                self.vm.snapshot_remove(snapshot)
                # self._debug(f"Finished removing current snapshot for {self.vm_name}")
        self._info(f"Creating new snapshot for {self.vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            self._snapshot = self.vm.create_snapshot()
        # self._debug(f"Finished creating new snapshot for {self.vm_name}")
        return self._snapshot

    def login(self):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not login to {self.vm_name} as it could not be found in the host")
            if not self.is_present_in_config:
                self._error(f"Did not login to {self.vm_name} as its options could not be found in the config file")
        self._info(f"Logging in to {self.vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            self.vm.login(self.username, self.password)
        # self._debug(f"Finished logging in to {self.vm_name}")

    def start(self, launch_gui: bool = False):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not start {self.vm_name} as it could not be found in the host")
            if self.is_powerstate_powered_on:
                self._error(f"Did not start {self.vm_name} as it is already powered on")
        self._info(f"Starting {self.vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            self.vm.power_on(launch_gui)
            self.vm.wait_for_tools()
        # self._debug(f"Finished starting {self.vm_name}")

    def restart(self, from_guest: bool = True):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not restart {self.vm_name} as it could not be found in the host")
            if not self.is_powerstate_powered_on:
                self._error(f"Did not restart {self.vm_name} as it is not powered on")
        self._info(f"Restarting {self.vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            self.vm.reset(from_guest)
        # self._debug(f"Finished restarting {self.vm_name}")

    def stop(self, from_guest: bool = True):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not stop {self.vm_name} as it could not be found in the host")
            if not self.is_powerstate_powered_on:
                self._error(f"Did not stop {self.vm_name} as it is not powered on")
        self._info(f"Stopping {self.vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            self.vm.power_off(from_guest)
        # self._debug(f"Finished stopping {self.vm_name}")

    def delete(self, delete_files: bool = True):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not delete {self.vm_name} as it could not be found in the host")
            if not self.is_present_in_config:
                self._error(f"Did not delete {self.vm_name} as its options could not be found in the config file")
            if self.read_only:
                self._error(f"Did not delete {self.vm_name} as it is read only")
            if self.is_powerstate_powered_on:
                self.stop()
        self._info(f"Deleting {self.vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            self.vm.vm_delete(delete_files)
        # self._debug(f"Finished deleting {self.vm_name}")
        self.vm = None

    def execute(self, script: str):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not execute script in {self.vm_name} as it could not be found in the host")
        self._info(f"Executing script: '{script}'")
        output = None
        if not self.dry_run:
            assert self.vm is not None
            fd, host_temp_path = mkstemp(text=True)
            guest_temp_path = self.vm.create_temp()
            self.vm.run_script(f'{script} >"{guest_temp_path}" 2>&1')
            try:
                self.vm.copy_guest_to_host(guest_temp_path, host_temp_path)
                with os.fdopen(fd) as file:
                    output = "  ".join(file.read().splitlines(keepends=True)).strip()
            finally:
                os.remove(host_temp_path)
                self.vm.file_delete(guest_temp_path)
        self._info("Finished executing script" + (f". Output:\n  {output}" if output else ""))

    def modify_computer_name(self, new_name: str):
        self._info(f"Modifying {self.vm_name} computer name")
        self.execute(f'wmic computersystem where name="%computername%" call rename name="{new_name}"')
        # self._debug(f"Finished modifying {self.vm_name} computer name")

    def modify_config(self, updates: dict[str, str]):
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not modify the config of {self.vm_name} as it could not be found in the host")
        self._info(f"Modifying {self.vm_name} config")
        if not self.dry_run:
            with open(self.vmx_path) as file:
                original = file.read().splitlines(keepends=True)
            config = dict(line.strip().split(" = ") for line in original)
            for key, value in updates.items():
                config[key] = f'"{value}"'
            updated = [f"{key} = {value}\n" for key, value in config.items()]
            with open(self.vmx_path, "w") as file:
                file.write("".join(updated))
            diff = unified_diff(original, updated, n=0)
            self._info("Diff:\n  " + "  ".join(list(diff)[3:]).strip())
        # self._debug(f"Finished modifying {self.vm_name} config")

    def clone(self, vm_name: str, host: VixHost | None = None):
        vm = None
        snapshot = None
        if not self.dry_run:
            if not self.is_present_in_host:
                self._error(f"Did not clone from {self.vm_name} as it could not be found in the host")
            if self.options is None:
                self._error(f"Did not clone {self.vm_name} to {vm_name} as its options could not be found in the config file")  # fmt: skip
            vm = VM(vm_name, self.config, host or self.host)
            if vm.is_present_in_host:
                self._error(f"Did not clone {self.vm_name} to {vm_name} as it already exists")
            if not vm.is_clone:
                self._error(f"Did not clone {self.vm_name} to {vm_name} as it is not a clone as specified in the config file")  # fmt: skip
            os.makedirs(os.path.dirname(vm.vmx_path), exist_ok=True)
            snapshot = self.get_snapshot()
        self._info(f"Cloning {self.vm_name} to {vm_name}")
        if not self.dry_run:
            assert self.vm is not None
            assert vm is not None
            self.vm.clone(vm.vmx_path, snapshot, vm.is_linked)
            vm.load_vm()
            vm.modify_config({"displayName": vm_name})
            vm.start()
            vm.login()
            vm.modify_computer_name(vm_name)
            vm.stop()
        # self._debug(f"Finished cloning {self.vm_name} to {vm_name}")
