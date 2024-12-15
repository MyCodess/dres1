#!/usr/bin/env  python3

""" Multiple Inheritance,  Diamond Problem , classmethods-inh, instanceMethods-inh, :
    https://www.python-course.eu/python3_multiple_inheritance.php
"""

##------------------- single-inh--base-classes: -----------------------
class A(object):
    def m(self): print("m of A called  for instance-class of: ", self.__class__.__name__)
    @classmethod
    def cm1(cls): print(cls.__name__)
    @classmethod
    def cm2(cls): print("A--cm2")

class B(A):
    def m(self): print("m of B called  for instance-class of: ", self.__class__.__name__)
    @classmethod
    def cm1(cls): print(cls.__name__)
    @classmethod
    def cm2(cls): print("B--cm2")
    
class C(A):
    def m(self): print("m of C called  for instance-class of: ", self.__class__.__name__)
    @classmethod
    def cm1(cls): print(cls.__name__)
    @classmethod
    def cm2(cls): print("C--cm2")

class D(A): pass

##------------------- multi-inh--sub-classes--: -----------------------
class BC   (B,C):   pass
class CB   (C,B):   pass
class DC  (D,C):  pass

##------------------- instances of multi-sub-classes--: ---------------
if __name__ == "__main__":
    bc1  = BC();
    cb1 = CB()
    dc1  = DC()   ##--II-WATCH here, takes the nearest method to the instance ! so NOT from A !! so: "good head": most specific version must be taken first !
    print ("------ bases view: ------------------------------------------:")
    print("BC.__bases__ :   ", BC.__bases__)
    print("CB.__bases__ :   ", CB.__bases__)
    print("DC.__bases__ :   ", DC.__bases__)
    print ("------ ObjCalls of overwritten-instance-methods: ------------:")
    bc1.m()
    cb1.m()
    dc1.m()
    print ("------ ObjCalls of overwritten-class-methods-cm2: ------------:")
    bc1.cm2()
    cb1.cm2()
    dc1.cm2()  ##--!-watch! the outpu! NOT A ! C is closer in the inh-tree, even if A is on the left-to-top !
    print ("=========== class-methods-using __name__ in cm1() =================:")
    print ("------ ObjCalls of overwritten-class-methods: ------------:")
    bc1.cm1()
    cb1.cm1()
    dc1.cm1()
    print ("------ classCalls of overwritten-class-methods: ------------:")
    BC.cm1()
    CB.cm1()
    DC.cm1()
    print ("============:")
    B.m(bc1)
    B.m(cb1)



