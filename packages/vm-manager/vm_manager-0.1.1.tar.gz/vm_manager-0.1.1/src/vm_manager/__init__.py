from .manager import VMManager
from . import logger


def main():
    logger.debug("vm-manager start")
    try:
        VMManager().parse_args()
    except logger.ErrorException as e:
        pass
    logger.debug("vm-manager end")
