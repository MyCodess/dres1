#!/usr/bin/env  python

#####  ==========  
""" 1kk: subclasses-tree-printout, sorted, recursive,  without using module inspect !  """ 
import selenium
import selenium.common.exceptions
import selenium.webdriver.common.options
import selenium.webdriver.common
import selenium.webdriver.remote.webdriver

##__  

##__  print (f"------------ subclasses-tree of {baseCls1}, recursive-method : -------------------------------")
def subs1(cls1: type, indent1: int = 0) -> None:
    indent1Str = "------|" * indent1
    ##--/OR--with-TAB-for-vim-folding:    indent1Str = "\t" * indent1
    ret1 = (indent1Str + cls1.__name__  + "                    ::  " + str(cls1) + "  --module:  " + cls1.__module__ + "  --bases:  " + cls1.__bases__.__str__() + "  --mro:  " + cls1.__mro__.__str__())
    print (ret1)
    if hasattr (cls1, "__subclasses__") and cls1 != type :
        for s1 in sorted (cls1.__subclasses__(), key= lambda c: c.__name__):
            subs1 (s1, indent1 +1)

print ("\n==========  webdriver-tree : ===============================")
baseCls1 = selenium.webdriver.remote.webdriver.BaseWebDriver
subs1 (baseCls1, 0)

print ("\n==========  options-tree : ===============================")
baseCls1 =  selenium.webdriver.common.options.BaseOptions
subs1 (baseCls1, 0)

print ("\n==========  WebDriverException-tree : ===============================")
baseCls1 = selenium.common.exceptions.WebDriverException
subs1 (baseCls1, 0)

##________________________________________  ___________________________


