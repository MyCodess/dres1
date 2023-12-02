import logging
import logging.config

logging.config.fileConfig("logging1.conf")
logger1 = logging.getLogger(__name__)

logger1.debug(f"logger1-attribs: {logger1.level} , {logger1.name}")
logger1.debug('just-a-debug-line')
logger1.info('just-an-info-line')
logger1.warning('just-a-warning-line')
logger1.error('just-an-error-line')
logger1.warning('---------------- END ---------------------')

