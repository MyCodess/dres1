#!/usr/bin/env  python3

""" Multiple Inheritance,  Diamond Problem , ...:
https://www.python-course.eu/python3_multiple_inheritance.php  ,   super() calls
http://www.srikanthtechnologies.com/blog/python/mro.aspx  :
- as most specific version must be taken first and then least specific (generic) version. So, calling process() from A, which is super class of C, is not correct as C is a direct super class of D. That means C is more specific than A. So method must come from C and not from A.
!! This is where Python applies a simple rule that says (known as good head question) when in MRO we have a super class before subclass then it must be removed from that position in MRO. !!

--- WATCH case d2 compared with d  :
d:   D. B.C.A.
d2:  D2.B.A.     ##--!!-and NOT C2 !
"""

class A:
    def __init__(self):
        print("A.__init__")
        ##__try-it:   super().__init__()  ##--II--comment this out/in, check the Diff !! do NOT call super() on direct-subclasses of "object" !

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()
    
class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class C2():
    def __init__(self):
        print("C2.__init__")
        ##__try-it:   super().__init__()  ##--II--comment this out/in, check the Diff !! do NOT call super() on direct-subclasses of "object" !

##------------------------  multi-inh-classes: ---------------------------

##-II-uncomment follwoing class to get error : TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C ! but OK: class D3(C,A): pass !
##__   class D3(A,C): pass

class D(B,C):
    def __init__(self):
        print("D.__init__")
        super().__init__()
        print(self.__class__.mro())

class D2(B,C2):
    def __init__(self):
        print("D2.__init__")
        super().__init__()
        print(self.__class__.mro())

##------------------------ run inits:
print("----") ; c1 = C()
print("----") ; d  = D()
print("----") ; d2 = D2()

