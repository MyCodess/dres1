

#####  ==========  itertools-chain for subclasses-tree:
from itertools import chain

baseCls1 = tuple
baseCls1 = object

def subs8(cls1, indent1: int = 0):
    indent1Str = "------|" * indent1
    ret1 = [cls1]
    if hasattr (cls1, "__subclasses__") and cls1 != type :
        ##__  ret1 = list( chain.from_iterable( [list(chain.from_iterable([[x], subs8(x)])) for x in cls1.__subclasses__()]))
        ret1 =  list( chain.from_iterable( [list(chain.from_iterable([[indent1Str + x.__name__ + "      :: " + str(x)], subs8(x, indent1+1)]))
                                           for x in sorted (cls1.__subclasses__(), key= lambda c: c.__name__)]))
    ##__ return  [cls1.__name__] + ret1
    return   ret1

print (baseCls1.__name__)
for ii in subs8(baseCls1, 1): print(ii)
##________________________________________  ___________________________

