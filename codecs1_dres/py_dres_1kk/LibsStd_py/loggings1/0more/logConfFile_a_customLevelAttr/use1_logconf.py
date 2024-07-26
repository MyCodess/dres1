import log
import logging

logger11 = log.getlogger(__name__)
#_ print(logger11.__dict__)
#_ logger11.level = log.TRACE
print("logger11.level : ", logger11.level)
print("logger11.effectivelevel : ", logger11.getEffectiveLevel())
#print(log.TRACE)

logger11.debug("___debug-from-%s", __file__)
logger11.trace(logger11, "___trace-from")

