from .manager import VMManager
from . import logger


def main():
    logger.debug("vm-manager start")
    VMManager().parse_args()
    logger.debug("vm-manager end")
