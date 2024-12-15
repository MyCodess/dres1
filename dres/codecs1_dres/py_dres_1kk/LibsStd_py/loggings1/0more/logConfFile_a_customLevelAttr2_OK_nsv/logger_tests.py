'''
    Providing global logging services for integration tests!

    USAGE in your module:
    import logger_tests
    logger1 = logger_tests.getlogger(__name__)
    see also:
    - with-attr:   https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility
    - class-based: https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility/35804945#35804945
'''

import logging
import logging.config
from pathlib import Path


LOGGING_CONF_FILENAME = "log.conf"
LOGGING_CONF_FILEPATH = Path.joinpath(Path(__file__).parent, LOGGING_CONF_FILENAME)
LOGGING_PREFIX_NAME = "testing."
TRACE: int = logging.DEBUG - 5    # -Note: if less than 5, then logging does NOT show this level correctly !


# ==================  initializing logging module incl. custom method + config-file ... : =================
logging.addLevelName(TRACE, "TRACE")
logging.TRACE = TRACE
def trace(self, message, *args, **kws):
    """
        Note: the line-no/func-name shown by this method in the logging output 
        is NOT the effective/reat one, due to chained calls !! so, is NOT reliable!
        check just the logger-name/file-name for real source of the output !
        - if using _log() instead log(), which is better, then args ,and NOT *args !
    """
    if self.isEnabledFor(TRACE):   ##-I-worke also without this if !
        self._log(TRACE, message, args, **kws) 
logging.getLoggerClass().trace = trace    ##--OR-if-std-class,then: logging.Logger.trace = trace



# ----- config-file-assignment/-call:
logging.config.fileConfig(LOGGING_CONF_FILEPATH)


# ==================  returning the logger-instance: ===================================================
def getlogger(logger_name: str) -> logging.Logger:
    """creates/returns a logger identified with logger_name"""
    _logger11 = logging.getLogger(LOGGING_PREFIX_NAME + logger_name)
    return _logger11

logger1 = logging.getLogger(LOGGING_PREFIX_NAME + __name__)
logger1.debug("\n========== __START-LOGGING__ , config-file: %s ===============", LOGGING_CONF_FILEPATH)
