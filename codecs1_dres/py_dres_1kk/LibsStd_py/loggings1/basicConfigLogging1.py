"""
    logging.basicConfig(....) directly using, WITHOUT any additional conf-file, ....
    see /library/logging.html , logging.basicConfig(**kwargs)
    --- nts:
    - ! The call to basicConfig() should come before any calls to debug(), info(), etc. Otherwise, those functions will call basicConfig() for you with the default options !!
    --- args-nts:
    - default logging-handler is stdout/console/StreamHandler() if nothing else specified by  filename=xxx or handlers=xxx !
    - "filename" arg REPLACES the default-handler (console/stdout) with a FileHandler(filename)! so ONLY file-logging and NO-stdout-logging!
    - "handlers" arg of basicConfig is always a list/iterator!s [xx, ...] even if only one handler !
"""

import logging

FORMAT1_SHORT = '%(levelname)s :: %(message)s :: %(filename)s :: %(name)s'
FORMAT1_LONG = '%(levelname)s :: %(message)s :: %(asctime)s :: %(name)s :: %(pathname)s'   ##--I-more-fields/attribs of Formatter/LogRecods see: /library/logging.html#logrecord-attributes
FORMAT1 = FORMAT1_SHORT
DATEFORMAT1 = '%Y-%m-%d %H:%M:%S'
LOGFILE1 = 'app1.log'

""" =========== console-logging-ONLY (stdout/stderr): =========================================
    - NO handler define in basicConfig ! since the default-handler is StreamHandler() ! and StreamHandler() with no-args defaults to stdout/stderr :
    - if no-args of  filename=xxx or handlers=xxx, then default handler is  StreamHandler() to stdout/stderr !
    - if using the args filename=xxxx or handlers=xxx, then the default-handler (stdout) is overwritten/deactivated !!
    --- the below call of basicConfig is same-as:
    - /OR: logging.basicConfig(format=FORMAT1, datefmt=DATEFORMAT1, encoding='utf-8', level=logging.DEBUG, handlers=[logging.StreamHandler()])
    - /OR: console_handler1 = logging.StreamHandler() ; logging.basicConfig(format=FORMAT1, datefmt=DATEFORMAT1, encoding='utf-8', level=logging.DEBUG, handlers=[console_handler1])
"""
# #_2try:  logging.basicConfig(format=FORMAT1, datefmt=DATEFORMAT1, encoding='utf-8', level=logging.DEBUG)


""" =========== File-logging-ONLY (no stdout/stderr): ======================================
    - using basicConfig(filename=xxx, ....) sends all to the logfile! the default-handler (stdou) is then deactivated !
    - with filename=xxx you have defined a FileHandler, so nothing goes to the console/stdout!
    -  filemode="w" : overwrites the logfile by each run !
    --- same as:
    file_handler1 = logging.FileHandler(LOGFILE1, mode='w',  encoding='utf-8')
    file_handler1.level = logging.DEBUG
    logging.basicConfig(format=FORMAT1, datefmt=DATEFORMAT1, encoding='utf-8', level=logging.DEBUG, handlers=[file_handler1])
"""
# #_2try:  logging.basicConfig(format=FORMAT1, datefmt=DATEFORMAT1, filename=LOGFILE1, filemode="w", encoding='utf-8', level=logging.DEBUG)


""" =========== BOTH-file+console-logging with basicConfig() : ================================
"""
logging.basicConfig(format=FORMAT1, datefmt=DATEFORMAT1, encoding='utf-8', level=logging.DEBUG, handlers=[logging.FileHandler(LOGFILE1, mode='w'), logging.StreamHandler()])

def logger_module1():
    logging.info("==========  logging directly with logging-module-funcs, WITHOUT acquiring own logger: ===========")
    logging.debug('just-a-debug-line')
    logging.info('just-an-info-line')
    logging.warning('just-a-warning-line')
    logging.error('just-an-error-line')


def logger_get1():
    logger1 = logging.getLogger(__name__)
    logger1.info("==========  logging WITH acquiring own logger by logging.getLogger() : ===========")
    logger1.debug('just-a-debug-line')
    logger1.info('just-an-info-line')
    logger1.warning('just-a-warning-line')
    logger1.error('just-an-error-line')

if __name__ == "__main__":
    logger_module1()
    logger_get1()
