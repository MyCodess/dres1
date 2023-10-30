_________________ logging_StdLib_py : ____________________________________


#####  ==========  docs:
    PEP 282 – A Logging System   :   https://peps.python.org/pep-0282/
    https://docs.python.org/3/library/logging.html
    https://docs.python.org/3/tutorial/stdlib2.html#logging , RefTut--11.5 Logging
    https://docs.python.org/3/howto/index.html              ---> HowTo basics+advanced !
    https://docs.python.org/3/howto/logging.html
    https://docs.python.org/3/howto/logging-cookbook.html   ---> eg , vorlagen, code-snippets ...!
    pydoc logging
##________________________________________  ___________________________



#####  ==========  Concept/ components/... logging_py:
    _______:  logging-components:  loggers, handlers, filters, and formatters :  https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial :
    - !! see the image/diagramm on refDocs-howto : ./howto/logging.html#logging-flow  !!
    - Loggers  : expose the interface that application code directly uses.
    - Handlers : send the log records (created by loggers) to the appropriate destination.
    - Filters  : provide a finer grained facility for determining which log records to output.
    - Formatters : specify the layout of log records in the final output.
##________________________________________  ___________________________


#####  ==========  log-levels + funcs qcks/listing :
	- see pydoc logging   +  https://docs.python.org/3.11/tutorial/stdlib2.html#logging
    
    _______:  Levels-logging:
    /usr/lib/python3.11/logging/__init__.py  bzw. pydoc logging :
    CRITICAL 	= 50
    ERROR 		= 40
    WARNING 	= 30
    INFO 		= 20
    DEBUG 		= 10
    NOTSET 		= 0
    FATAL 		= CRITICAL
    WARN 		= WARNING

    _______:  funcs-levels:
    import logging
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')
##________________________________________  ___________________________


#####  ==========  loggers usage-hints:   ./logging.html#loggers :
    - ! loggers has got a tree-/baum-hierarchy based on their names, whereas dot "." defines the hierarchy in their names! so bar is a child of foo of root logger in logging.getLogger(foo.bar) !
    - ! so the best way defining loggers in each module:  logger = logging.getLogger(__name__) !
    --
    - module-based-logger:   logger = logging.getLogger(__name__)   ##--module-level logger, in each module which uses logging ; see:  file:///usr/share/doc/python/html/howto/logging.html#advanced-logging-tutorial
    - whole-app-based-logger (so multiple modules sharing one global logger ! in myapp-main.py):  def main(): logging.basicConfig(filename='myapp.log', level=logging.INFO) ; logging.info('Started') ...;
    - see /howto/logging.html#logging-from-multiple-modules  +  /howto/logging.html#configuring-logging-for-a-library
    --
    --- loggers-hierarchys  ,  logger.getLogger() :   see:  /howto/logging.html#loggers :
        - Return a logger with the specified name, creating it if necessary. If no name is specified, return the root logger.  ##--pydoc logging.getLogger
        - names are period-separated hierarchical structures.
        - Multiple calls to getLogger() with the same name will return a reference to the same logger object !
        - If a level is not explicitly set on a logger, the level of its parent is used instead as its effective level.
        - Hierarchy/inheritance of Loggers:  Child loggers propagate messages up to the handlers associated with their ancestor loggers. Because of this, it is unnecessary to define and configure handlers for all the loggers an application uses. It is sufficient to configure handlers for a top-level logger and create child loggers as needed. (You can, however, turn off propagation by setting the propagate attribute of a logger to False.) 
##________________________________________  ___________________________


#####  ==========  configs:
    - ! /howto/logging.html#configuring-logging  +  /howto/logging.html#configuring-logging-for-a-library  !
    - pydoc logging.config ,  logging.basicConfig  !!

    _______:  config-file for logging (instead in-code-config !):
    -! howto/logging.html#configuring-logging  see there logging.conf file !
    - logging.config.fileConfig('logging.conf')   ##--and then extra-conf-file logging.conf ! see above link for eg ! so: separation of configuration and cod !
    - !! Warning: see Warning ther for:  The fileConfig() function takes a default parameter, disable_existing_loggers, which disables all other loggers ... ;see there!

    _______:  in-code-configs: eg setting log-level for a logger in code :
    - in code, setting default log-level for your module: use basicConfig(level=xxx) as in:  logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    this call of :func:`basicConfig` MUST be the VERY first call of ANY logging-funcs in your app , before any other logging.info,... ! with the first call the logging global instance is cratead the the default-level will NOT be changed, not even with further logging.basicConfig() calls ! see https://docs.python.org/3/howto/logging.html#logging-to-a-file
    - on cmdline setting/overwriting default log-level:  ... --log=INFO ...  ##--see https://docs.python.org/3/howto/logging.html
    - getting/query cu-log-level of the app:   getattr(logging, loglevel.upper())
    - ! globally setting log-level bzw. globally instantiate logger for your WHOLE app:  define  logging.basicConfig in your very first lines of your-app-main.py : see https://docs.python.org/3/howto/logging.html#logging-from-multiple-modules
    - If a level is not explicitly set on a logger, the level of its parent is used instead as its effective level.
    - The root logger always has an explicit level set (WARNING by default).
##________________________________________  ___________________________


#####  ==========  Handlers :
    - ./howto/logging.html#handlers  +  ./howto/logging.html#useful-handlers :
    - eg: sending log-records to terminal + log-file + email : so three handlers are to be added to the logger-instance with logger.addHandler() !
    - eg: /howto/logging.html#configuring-logging  + see eg there for handler+formatter !
    - Logger objects/instances can add zero or more handler objects to themselves with an addHandler().
    - listing of handler in StdLib:  ./howto/logging.html#useful-handlers
    - ONLY methods which you need of handlers are: setLevel(), setFormat(), add-/removeFilter() !
    - NO-logging for now, then add NullHandler to your logger! eg: logging.getLogger('foo').addHandler(logging.NullHandler()) ;
##________________________________________  ___________________________

