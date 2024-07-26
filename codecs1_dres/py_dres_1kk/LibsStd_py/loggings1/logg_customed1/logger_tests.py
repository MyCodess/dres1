'''
    Providing global logging services for integration tests!

    USAGE in your module:
    import logger_tests
    logger1 = logger_tests.getlogger(__name__)
'''

import logging
import logging.config
from pathlib import Path
from typing import Any

# log1 = logging.getLogger(); log1.
LOGGING_CONF_FILENAME = "log.conf"
LOGGING_CONF_FILEPATH = Path.joinpath(Path(__file__).parent, LOGGING_CONF_FILENAME)
LOGGING_PREFIX_NAME = "testing."
TRACE: int = logging.DEBUG - 5


# ############# initializing logging module with logger-class-... : ##################################
logging.TRACE = TRACE  # -OR: setattr(logging, 'TRACE', TRACE)
logging.addLevelName(TRACE, 'TRACE')


class Loggered(logging.getLoggerClass()):   # -OR-if-all-defaults, then: class Loggered(logging.Logger):
    """Logger subclass with customized features"""
    TRACE: int = TRACE

    # =====================================================================================
    def trace(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """more detailed outputs; customized debugging lines in problem cases and runtime errors"""
        # __ print("---KWs:  ", kwargs, " , ---args: ", args)
        if self.isEnabledFor(TRACE):
            kwargs['stacklevel'] = kwargs.get('stacklevel', 1) + 1  # === if 'stacklevel' in kwargs: kwargs['stacklevel'] += 1 else: kwargs['stacklevel'] = 2
            self.log(TRACE, msg, *args, **kwargs)    # -OR: self._log(TRACE, msg, args, **kwargs)
            
            # --- other variations of setting stacllevel, but all partly correct (if not more wrapping of log()-call):
            # - BUT stacklevel NOT good as log()-argument and NOT good with fix setting! then:
            #  problem if this already in kwargs was and so error ! or if log-call more wrapped ...!
            # self.log(TRACE, str(self.findCaller(stacklevel=2)), *args, **kwargs)
            # -!-OK-for-msg:  msg = str(self.findCaller(stacklevel=2)) + "\n" + msg
            # -!!!-OK-fully: self.log(TRACE, msg, *args, **kwargs, stacklevel=2 ) #-not-ok fi log() wrapped more!


    # =====================================================================================
    def log_obj_list(self, level, msg, list1 , keys_list=None, *args, **kwargs):
        """
        formatted log of a list of dictionaries or objects,
        printing keys_list-values of the list1; e.g. for infoblox-records-lists
        list1: list of dicts or objects
        keys_list: list of key-name to be logged out; if None, then ALL key-values
        """
        if self.isEnabledFor(level):
            line1 = "______________________________________________________________________________\n"
            str1 = f"\n{line1}--- {msg} : ---\n"
            if not keys_list:
                if isinstance(list1[0], (dict)):
                    keys_list = list1[0].keys()
                else:
                    keys_list = list1[0].__dict__.keys()
            for item1 in list1:
                str1 += "{"
                for key1 in keys_list:
                    if isinstance(item1, (dict)):
                        str1 += f" '{key1}': {item1[key1]},"
                    else:
                        str1 += f" '{key1}': {getattr(item1, key1)},"
                str1 += " }\n"
            str1 += line1
            kwargs['stacklevel'] = kwargs.get('stacklevel', 1) + 1  # === if 'stacklevel' in kwargs: kwargs['stacklevel'] += 1 else: kwargs['stacklevel'] = 2
            self.log(level, str1, *args, **kwargs)

    
    # ============== only-dict_lits: =======================================================================
    def log_dicts_only_list(self, level, list1 , keys_list, *args, **kwargs):
        """formatted log of a list of dictionaries, printing keys_list-values; e.g. for infoblox-records-lists"""
        if self.isEnabledFor(level):
            str1 = "_"*78 + "\n"
            for item1 in list1:
                str1 += "{"
                for key1 in keys_list:
                    str1 += f" '{key1}': {item1[key1]},"
                str1 += " }\n"
            str1 += "-"*78 + "\n"
            kwargs['stacklevel'] = kwargs.get('stacklevel', 1) + 1  # === if 'stacklevel' in kwargs: kwargs['stacklevel'] += 1 else: kwargs['stacklevel'] = 2
            self.log(level, str1, *args, **kwargs)

    # ============== only-obj_lists: =======================================================================
    def log_obj_only_list(self, level, list1 , keys_list, *args, **kwargs):
        """formatted log of a list of objects, printing attr_list-values of obj-attr; e.g. infoblox-records-obj-lists"""
        if self.isEnabledFor(level):
            str1 = "_"*78 + "\n"
            for item1 in list1:
                str1 += "{"
                for key1 in keys_list:
                    str1 += f" '{key1}': {getattr(item1, key1)},"
                str1 += " }\n"
            str1 += "-"*78 + "\n"
            kwargs['stacklevel'] = kwargs.get('stacklevel', 1) + 1  # === if 'stacklevel' in kwargs: kwargs['stacklevel'] += 1 else: kwargs['stacklevel'] = 2
            self.log(level, str1, *args, **kwargs)

    
logging.setLoggerClass(Loggered)
# -??: required, adding trace() to logging itself also, as logging.trace=trace  !?!?

# =====================================================================================

# --- configfile-parsing:
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

# ###############  olds_1coll ... : ###############################################################
'''
# - setattr(logging.Logger, 'TRACE', TRACE)
# - setattr(logging.Logger, 'trace', Loggered.trace)

    # ############### not needed any more! use instead the 'stacklevel' in kwargs, py>3.4 :
    def trace_with_callerInfos(self, msg: str, caller_infos, *args: Any, **kwargs: Any) -> None:
        """more detailed outputs; customized debugging lines in problem cases and runtime errors"""
        print("KWs:  ", kwargs, " ,args: ", args)
        #print(self.LogRecord())
        if self.isEnabledFor(TRACE):
            if caller_infos: msg = str(caller_infos) + msg
            if "logger" in kwargs:
                print ("__org-caller: "+ str(kwargs["logger"].findCaller(stacklevel=2)))
                self.log(TRACE, "__org-caller: "+ str(kwargs["logger"].findCaller()), *args, **kwargs)
            self.log(TRACE, msg, *args, **kwargs)   # -OR: self._log(TRACE, msg, args, **kwargs)
            #self.log(TRACE, self.findCaller())
'''