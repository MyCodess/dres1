import logging
#from  loggConf import *
##logging.basicConfig(format='%(levelname)s : %(name)s : %(message)s : %(asctime)s', datefmt='%Y-%m-%d %H:%M:%S', filename='app2.log', filemode="w", encoding='utf-8', level=logging.DEBUG)

logger1 = logging.getLogger(__name__)
logger1.debug('just-a-debug-line')
logger1.info('just-an-info-line')
logger1.warning('just-a-warning-line')
logger1.error('just-an-error-line')
