"""
    Python – Calling parent class __init__ with multiple inheritance, what’s the right way
    super() , mro(), ...
    https://itecnote.com/tecnote/python-calling-parent-class-__init__-with-multiple-inheritance-whats-the-right-way/
    ---
    There's two typical approaches to writing C's __init__:
    (old-style) ParentClass.__init__(self)
    (newer-style) super(DerivedClass, self).__init__()
    ---! RefDocsStdLibs--Built-in-Functions : class super :
    super([type[, object-or-type]])
    The object-or-type determines the method resolution order to be searched. The search starts from the class right after the type.
    For example, if __mro__ of object-or-type is D -> B -> C -> A -> object and the value of type is B, then super() searches C -> A -> object.
    -
    super().method(arg) inside a class definition  same.as ==  super(C, self).method(arg)
    so:  class C(B): def method(self, arg): super().method(arg)  #--same.as:  super(C, self).method(arg)
    The zero argument form only works inside a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined, as well as accessin
    ---
    recommend (NOT-RefDocs):  classes whose base class is object should not call super().__init__() ! but controverse! :
    This also means that you should never write a class that inherits from object and doesn't have an __init__ method.
    Not defining a __init__ method at all has the same effect as calling super().__init__().
    If your class inherits directly from object, make sure to add an empty constructor like so:
    class Base(object): def __init__(self): pass
    see https://itecnote.com/tecnote/python-calling-parent-class-__init__-with-multiple-inheritance-whats-the-right-way/ 
"""

print ("======================= direct __init__ calls with explicit class-name, WITHOUT super() : =====================================")
class A(object):
    def __init__(self):
        print("in...A")
        print("out--A")

class B(object):
    def __init__(self):
        print("in...B")
        print("out--B")

class C(A, B):
    def __init__(self):
        print("in...C")
        A.__init__(self)
        B.__init__(self)
        print("out--C")

c1=C()
print(C.mro())

print ("======================= direct __init__ calls with explicit class-name, but using super() in baseclasses : =====================================")
print ("--!try-watch: comment in/out the super() line in A and B ! he means: classes whose base class is object should not call super().__init__() !")
print ("--!also Note that B's init gets called twice! not desirable!")
class A(object):
    def __init__(self):
        print("in...A")
        ##__ try it:  super(A, self).__init__()
        print("out--A")

class B(object):
    def __init__(self):
        print("in...B")
        ##__ try it:  super(B, self).__init__()
        print("out--B")

class C(A, B):
    def __init__(self):
        print("in...C")
        A.__init__(self)
        B.__init__(self)
        print("out--C")

c1=C()
print(C.mro())


print ("======================= direct __init__ calls with explicit class-name, super() also in subclass : =====================================")
print ("--!try-watch: comment in/out the super() each class A/B/C einzelne and see the output !! very interesting !!")
print ("--!try-watch: specially in A delete super() line and see that B init is never called !!")
class A(object):
    def __init__(self):
        print("in...A")
        ##__ try it:  super().__init__()
        print("out--A")

class B(object):
    def __init__(self):
        print("in...B")
        ##__ try it:  super().__init__()
        print("out--B")

class C(A, B):
    def __init__(self):
        print("in...C")
        super().__init__()
        print("out--C")

c1=C()
print(C.mro())

