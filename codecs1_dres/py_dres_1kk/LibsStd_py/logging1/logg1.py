import logging

logging.basicConfig(format='%(levelname)s : %(message)s : %(asctime)s', datefmt='%Y-%m-%d %H:%M:%S', filename='app1.log', filemode="w", encoding='utf-8', level=logging.INFO)

logging.debug('just-a-debug-line')
logging.info('just-an-info-line')
logging.warning('just-a-warning-line')
logging.error('just-an-error-line')
