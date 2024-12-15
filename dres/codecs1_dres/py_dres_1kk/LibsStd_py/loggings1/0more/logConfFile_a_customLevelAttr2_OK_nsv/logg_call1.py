"""
    call-it:  python -m loggLevel2.logg_call1
"""
from . import logger_tests

logger1 = logger_tests.getlogger(__name__)
logger1.debug("- d1")
logger1.trace("- t1")