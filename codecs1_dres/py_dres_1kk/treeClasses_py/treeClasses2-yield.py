
#####  ==========  4- yield solution: tree-printout
baseCls1 = object

##__  print (f"------------ subclasses-tree of {baseCls1}, yield-recursive-method : ----------------------")
def subs1(cls1: type, indent1: int = 1):
    indent1Str = "------|" * indent1
    ##--ret1 = (indent1Str + " " + cls1.__name__ + "                    --module:  " + cls1.__module__ + "  --bases:  " + cls1.__bases__.__str__() + "  --mro:  " + cls1.__mro__.__str__())
    ret1 = (indent1Str + cls1.__name__  + "                    ::  " + str(cls1) + "  --module:  " + cls1.__module__ + "  --bases:  " + cls1.__bases__.__str__() + "  --mro:  " + cls1.__mro__.__str__())
    yield  ret1
    if  hasattr (cls1, "__subclasses__") and cls1 != type :
        for subclass in sorted (cls1.__subclasses__(), key= lambda c: c.__name__):
            yield from subs1(subclass, indent1+1)

for s11 in (subs1(baseCls1)): print (s11)
##__  print ("-------------------------------------------------")
##________________________________________  ___________________________

