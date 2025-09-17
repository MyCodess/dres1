#!/usr/bin/env  python3


""" ========== properties get/set methods :  ==========
Two things are noteworthy:
- We just put the code line "self.x = x" in the __init__ method and the property method x is used to check the limits of the values.
- The second interesting thing is that we wrote "two" methods with the same name and a different number of parameters "def x(self)" and "def x(self,x)".
  We have learned in a previous chapter of our course that this is not possible.  It works here due to the decorating.
- see:  Bklein_Tuts_py:  /python-course.eu/python3_properties.php.html
"""

print ("\n========== properties defining by decorators: any access to the property x its get/set methods are implicitly/automatically applied !! :")
##--I- Syntax using decorators :
class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x + 1

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x + 2

j1=P(1100)
print (j1.x)
j2=P(-1)
print (j2.x)
j3=P(10)
print (j3.x)
j3.x=50
print (j3.x)
##--2try.ERROR: x-setter not callable:   j3.x(12) ; 
##--2try.ERROR: print (j3.__x)

##-------------------------------------------------
print ("\n========== rather javaesque-syntax without decorators, but still using property() method, to define the property (not-pythonic!) : ----------")
class P2:

    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x + 3

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)
##---
p2=P2(-20)
print (p2.x)
p2.x = 10
print (p2.x)

##-------------------------------------------------
print ("\n========== showing that:\n   - for props ALWAYS the getter/setter methods are applied, even in __init__ ! and:\n\
       - the prop x1 is NOT accesible directly as __x1 outside the class-definition ! NOT even through the instance-obj itself! : ----------" )
class C1:
    def __init__(self, p1):
        self.x1= p1

    @property
    def x1(self):
        return self.__x1 + 1   ##--II-just add something to its value, so that you can follow, the getter method here was applied by quering x1 value !

    @x1.setter
    def x1(self, p1):
        self.__x1 = p1 + 2  ##--II-just add something to its value, so that you can follow, the setter method here was applied by setting x1 value !

print ("\n--- the property x1 is internally/bytecode/compiler renamed in _C1__x1 , so _<classname>__<propertyname> ! so NOT even accessible through o1.__x1 !! ---")
o1= C1(0)
print (o1.x1)
print("o1-dict:  ", o1.__dict__)
o1.x1 = 2
print (o1.x1)
print("o1-dict:  ", o1.__dict__)
print ("\n--- here ONLY a new instance-var __x1 will be defined, which hat got nothing to do with the property x1 !: ---")
o1.__x1 = 30
print (o1.x1)
print (o1.__x1)
print (o1._C1__x1)
print("o1-dict:  ", o1.__dict__)

print ("-------------------------------------------\n")

