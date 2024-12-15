#!/usr/bin/env  python3


""" ========== 'ABC' of Abstract Base Classes : ==============================
    /python-course.eu/oop/the-abc-of-abstract-base-classes.php.html

"""

print ("\n========== ABC1: without basic-implementation of abstract-method : ====================")
from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

##------------------------------------------------------------
class cl1(AbstractClassExample):pass

##--2try-ERROR:    -------------------------------------------
##--  un-comment following 2 lines to generate an Error, since an abstract class/subclass can NOT be instatiated whitout implementing all abstractmethos!
##--  a1 = AbstractClassExample(5)  ##--TypeError: Can't instantiate abstract class AbstractClassExample with abstract method do_something
##--  c1=cl1()
##----------------------------------

##------------------------------- now these ABC-classed can be instantiated :
class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42
    
class DoMul42(AbstractClassExample):
   
    def do_something(self):
        return self.value * 42
    
x = DoAdd42(10)
y = DoMul42(10)

print(x.do_something())
print(y.do_something())


###########################################################################################
print ("\n========== ABC2: with a basic-implementation of abstract-method : ====================")
from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        print("- Some implementation! in the abstract-class ....")
        
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("- The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()

##############################################################################################

