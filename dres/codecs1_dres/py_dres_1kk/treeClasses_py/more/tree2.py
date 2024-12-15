#!/usr/bin/env  python
""" class-tree-printout -without using module inspect- , 
""" 
##__  import selenium.webdriver

print ("------------ -Altern.1--recursive: -------------------------------------")
def subs1(cls1, indent1: int = 1) -> list:
    indent1Str = "----|" * indent1
    print (indent1Str, cls1.__name__)
    if hasattr (cls1, "__subclasses__") and cls1 != type :
        for s1 in cls1.__subclasses__():
            subs1 (s1, indent1 +1)

#subs1 (tuple, 1)
subs1 (object, 1)

print ("-------------------------------------------------")


