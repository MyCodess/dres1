'''
    Providing global logging services for the whole lib here!

    USAGE in your module:
    import <this module>
    logger1 = log.getlogger(__name__)
'''

import logging
import logging.config
from pathlib import Path


LOGGING_CONF_FILENAME = "log.conf"
LOGGING_CONF_FILEPATH = Path.joinpath(Path(__file__).parent, LOGGING_CONF_FILENAME)
LOGGING_PREFIX_NAME = "nsv."   # prefixed to all logger-names

TRACE = logging.DEBUG - 3
setattr(logging, 'TRACE', TRACE)
logging.addLevelName(TRACE, 'TRACE')
# so with above line, level=TRACE can be used in log-configfile, BUT effective ONLY for logger_root! not its handlers!

logging.config.fileConfig(LOGGING_CONF_FILEPATH)
logger1 = logging.getLogger(LOGGING_PREFIX_NAME + __name__)
logger1.debug("\n\n========== __START-LOGGING__  ===============")
logger1.debug("___ loading logging-configfile: %s", LOGGING_CONF_FILEPATH)


def trace(_logger: logging.Logger, msg: str) -> None:
    """
    A more detailed debug logging if more details are required
    set your logger.level = log.TRACE  to activate its repots
    or in the log-configfile : [logger_root] level=TRACE ! (NOT for its handlers!)
    """
    if _logger.getEffectiveLevel() <= TRACE:
        _logger.debug("-TRACE: %s", msg)


def getlogger(logger_name: str) -> logging.Logger:
    """creates/returns a logger identified with logger_name"""
    _logger11 = logging.getLogger(LOGGING_PREFIX_NAME + logger_name)
    setattr(_logger11, "trace", trace)
    return _logger11
