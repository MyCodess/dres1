#!/usr/bin/env  python3
""" class-tree-printout -without using module inspect- , 
USAGE1:  [root-class-name] 
to list also the upper classes tree (MRO) set here the printUpperClasses=True

OK1:   python  -c  "import selenium.webdriver; import tree1 ; tree1.classtree(selenium.webdriver.remote.webdriver.WebDriver)"
OK1:   python  -c  "import selenium.common   ; import tree1 ; tree1.classtree(selenium.common.exceptions.WebDriverException)" 

""" 
##__  import selenium.webdriver

print ("------------ -Altern.1--recursive: -------------------------------------")
import sys
rootClassName = object
printUpperClasses = False  ## for printing also the upper classes set here printUpperClasses = True

#_  if (len(sys.argv) > 2): import  eval (sys.argv[2])
if (len(sys.argv) > 1): rootClassName = eval (sys.argv[1])

@staticmethod
def classtree(cls, indent="-|"):
    print (indent, cls.__name__ , end=" ")
    if printUpperClasses:  print(cls.mro(), end=" ")
    print ()
    for subcls in cls.__subclasses__():
        if subcls != type :
            classtree(subcls, indent+"-------|")

##__ classtree(BaseException)
##__  classtree(rootClassName)
print ("-------------------------------------------------")

print ("------------ -Altern.2--yield-from: ---------------------------")
@staticmethod
def get_subclasses(cls):
    for subclass in cls.__subclasses__():
        yield from get_subclasses(subclass)
        yield subclass
print ("-------------------------------------------------")


