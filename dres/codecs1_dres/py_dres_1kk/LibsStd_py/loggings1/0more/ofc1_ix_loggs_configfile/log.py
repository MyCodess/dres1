'''
    Providing global logging services for the whole lib here!

    USAGE in your module:
    import <this module>
    logger1 = log.getlogger(__name__)
'''

import logging
import logging.config
from pathlib import Path
from typing import Any


LOGGING_CONF_FILENAME = "log.conf"
LOGGING_CONF_FILEPATH = Path.joinpath(Path(__file__).parent, LOGGING_CONF_FILENAME)
LOGGING_PREFIX_NAME = "nsv."   # prefixed to all logger-names
TRACE: int = logging.DEBUG - 3


# ############# initializing logging module with logger-class-... : ##################################
class Loggered(logging.Logger):
    """Logger subclass with customized features"""
    TRACE: int = TRACE

    def trace(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """more detailed outputs; customized debugging lines in problem cases and runtime errors"""
        self.log(TRACE, msg, *args, **kwargs)


setattr(logging, 'TRACE', TRACE)
logging.addLevelName(TRACE, 'TRACE')
# with above line, level=TRACE can be used in log-configfile, BUT effective ONLY for logger_root! not its handlers!
logging.setLoggerClass(Loggered)
logging.config.fileConfig(LOGGING_CONF_FILEPATH)
# ############# #####################################################


logger1 = logging.getLogger(LOGGING_PREFIX_NAME + __name__)
logger1.debug("\n\n========== __START-LOGGING__  ===============")
logger1.debug("___ loading logging-configfile: %s", LOGGING_CONF_FILEPATH)


def getlogger(logger_name: str) -> logging.Logger:
    """creates/returns a logger identified with logger_name"""
    _logger11 = logging.getLogger(LOGGING_PREFIX_NAME + logger_name)
    return _logger11

# ###############
# - setattr(logging.Logger, 'TRACE', TRACE)
# - setattr(logging.Logger, 'trace', Loggered.trace)
