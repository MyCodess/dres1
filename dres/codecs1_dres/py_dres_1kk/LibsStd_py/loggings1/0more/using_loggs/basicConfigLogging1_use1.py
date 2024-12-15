""" call-me as module:  python -m using_loggs.basicConfigLogging1_use1 """

import logging
import  basicConfigLogging1

logger1 = logging.getLogger(__name__)

def logger_get1():
    logger1 = logging.getLogger(__name__)
    logger1.info("==========  logging WITH acquiring own logger by logging.getLogger() : ===========")
    logger1.debug("__ : %s", __file__)
    logger1.debug('just-a-debug-line')
    logger1.info('just-an-info-line')
    logger1.warning('just-a-warning-line')
    logger1.error('just-an-error-line')

if __name__ == "__main__":
    logger_get1()
