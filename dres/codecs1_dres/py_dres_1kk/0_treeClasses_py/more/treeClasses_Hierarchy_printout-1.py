#!/usr/bin/env  python3
""" class-tree-printout -without using module inspect- , 
USAGE1:  [root-class-name] 
to list also the upper classes tree (MRO) set here the printUpperClasses=True
""" 

print ("-------------------------------------------------")
import sys
rootClassName = object
printUpperClasses = False  ## for printing also the upper classes set here printUpperClasses = True

if (len(sys.argv) > 1): rootClassName = eval (sys.argv[1])

def classtree(cls, indent="-|"):
    print (indent, cls.__name__ , end=" ")
    if printUpperClasses:  print(cls.mro(), end=" ")
    print ()
    for subcls in cls.__subclasses__():
        if subcls != type :
            classtree(subcls, indent+"-------|")

##__ classtree(BaseException)
classtree(rootClassName)
print ("-------------------------------------------------")

