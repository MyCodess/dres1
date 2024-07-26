""" call-me:  python -m d1.f1 """

import logging
import pprint
import logger_tests

logger11 = logger_tests.getlogger(__name__)
#_ print(logger11.__dict__)
#_ logger11.level = log.TRACE
# print("- logger11-attr : ", logger11.level, logger11.getEffectiveLevel(), logger11.isEnabledFor(logging.DEBUG), logger11.isEnabledFor(logging.TRACE) )

# print(logging.TRACE)
# pprint.pp(logger11.__dict__)
# pprint.pp(logger11.__dir__())

#logger11.debug("___debug-from-%s", __file__)

# - logger11.trace("___trace-from")
#logger11.trace("___trace-from",   stack_info=True)
#logger11.trace("___trace-from", logger=logger11,  stack_info=True)
#logger11.trace("___trace-from", caller_infos=logger11.findCaller())

d1 = {}
for ii in "abcd": d1[ii] = ii  # -just a dummy test dict!
dicts_list1 = [d1, d1, d1]
logger11.log_dicts_only_list(logging.TRACE, dicts_list1, ['b', 'c'])

class C1: pass
obj1 = C1(); obj1.x=11; obj1.y=12; obj1.z=13
obj2 = C1(); obj2.x=21; obj2.y=22; obj2.z=23
objs_list1 = [obj1, obj2]
logger11.log_obj_only_list(logging.TRACE, objs_list1, ['x', 'y'])

# =============== selected-keys-logging: =============================
logger11.log_obj_list(logging.TRACE, "selected-keys-logging", dicts_list1, ['b', 'c'])
logger11.log_obj_list(logging.TRACE, "selected-keys-logging", objs_list1,  ['x', 'y'])

# ===============all keys logging : =================================
logger11.log_obj_list(logging.TRACE, "all keys logging", dicts_list1)
logger11.log_obj_list(logging.TRACE, "all keys logging", objs_list1)
