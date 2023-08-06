import logging
import os
import sys


def get_logger(name: str | None = None) -> logging.Logger:
    names = ["vm-manager"]
    if name:
        names.append(name)
    return logging.getLogger(".".join(names))


def set_console_handler(level: int, fmt: str | None = "> %(message)s", time_fmt: str | None = "%H:%M:%S"):
    logger = get_logger()
    if (c_handler := getattr(logger, "c_handler", None)) is not None:
        logger.removeHandler(c_handler)
    c_handler = logging.StreamHandler(sys.stdout)
    c_formatter = logging.Formatter(fmt, time_fmt)
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(level)
    logger.addHandler(c_handler)
    setattr(logger, "c_handler", c_handler)


def add_file_handler(filename: str):
    logger = get_logger()
    if (f_handler := getattr(logger, "f_handler", None)) is not None:
        if filename == f_handler.filename:
            return
        f_handler.close()
        os.rename(f_handler.filename, filename)
        logger.removeHandler(f_handler)
    f_handler = logging.FileHandler(filename)
    setattr(f_handler, "filename", filename)
    f_formatter = logging.Formatter("[%(levelname)s] [%(asctime)s] %(name)s - %(message)s")
    f_handler.setFormatter(f_formatter)
    f_handler.setLevel(logging.DEBUG)
    logger.addHandler(f_handler)
    setattr(logger, "f_handler", f_handler)


def debug(message: str):
    get_logger().debug(message)


def info(message: str):
    get_logger().info(message)


def error(message: str):
    get_logger().error(message)
    raise ErrorException(message)


class Logger:
    def __init__(self, name: str | None = None):
        names = []
        if self.__class__.__qualname__ != "Logger":
            names.append(self.__class__.__qualname__)
        if name:
            names.append(name)
        self.logger = get_logger(".".join(names))

    def _debug(self, message: str):
        self.logger.debug(message)

    def _info(self, message: str):
        self.logger.info(message)

    def _error(self, message: str):
        self.logger.error(message)
        raise ErrorException(message)


class ErrorException(Exception):
    pass


get_logger().setLevel(logging.DEBUG)
set_console_handler(logging.INFO)
add_file_handler("vm-manager.log")
