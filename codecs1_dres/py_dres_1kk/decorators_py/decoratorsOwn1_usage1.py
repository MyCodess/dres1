#!/usr/bin/env   python

from  decoratorsOwn1  import  deco1

print ("\n=========== Usage of own-decorator as an import-module : =======================")

@deco1
def decoModuleUsage1():
    print (f"I am outside the own-deco-file/-module, using the own-deco through importing it !")

decoModuleUsage1()

