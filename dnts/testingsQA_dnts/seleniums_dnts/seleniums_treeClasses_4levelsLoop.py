#!/usr/bin/env  python

"""
    -!! NON-recursive, ONLY 4-levels-loop of class-hierarchy of selenium
"""

import selenium
import selenium.common.exceptions
import selenium.webdriver.common
import selenium.webdriver.remote.webdriver


def allSubClasses1(s1):
    indent1="-| "
    print (indent1 , s1.__name__ , " \t :" , s1)
    if hasattr (s1, "__subclasses__"):  ##--!?-- and s1 != type
        for s2 in s1.__subclasses__():
            print (indent1 * 2, s2.__name__ , " \t :" , s2)
            if hasattr(s2, "__subclasses__") and s2 != type :
                for s3 in s2.__subclasses__():
                    print (indent1 * 3, s3.__name__ , " \t :" , s3)
                    for s4 in s3.__subclasses__():
                        print (indent1 * 4, s4.__name__ , " \t :" , s4)


print ("\n\n---------- selenium.webdriver.remote.webdriver.BaseWebDriver : ----------")
allSubClasses1(selenium.webdriver.remote.webdriver.BaseWebDriver)

print ("\n\n---------- selenium.common.exceptions.WebDriverException : ----------")
allSubClasses1(selenium.common.exceptions.WebDriverException)

##__  print ("\n\n---------- selenium.webdriver.remote.webdriver.WebDriver : ----------")
##__  allSubClasses1(selenium.webdriver.remote.webdriver.WebDriver)
#allSubClasses1(object)
#print(allSubClasses1(tuple))

#print ("\n\n---------- object (testy) : ----------")
#allSubClasses1(object)

