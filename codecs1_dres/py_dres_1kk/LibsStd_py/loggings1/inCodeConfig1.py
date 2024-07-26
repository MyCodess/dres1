"""
    /howto/logging.html#configuring-logging :
    here simple eg of in-code-config of a logger
    _______:  3 ways to configure logging:   html/howto/logging.html#configuring-logging :
    1- in-code-config :  create loggers/handlers/... in your code and call their methods of setLevel/setFormetter/...
    2- config-file : create a text-config-file and assign it to your root-logger with: logging.config.fileConfig(fname, ...)
    3- dict-configs : Creating a dictionary of configuration information and passing it to logging.config.dictConfig(config)
"""
import logging

# create logger
logger = logging.getLogger('simple_example')
print(logger.__dict__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()  # -StreamHandler() defaults to stdout/stderr! otherwise call it with (params...)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

