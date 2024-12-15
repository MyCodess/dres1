#!/usr/bin/env  python3

print("""\n========== ONLY one __init__ per class !!
    -!  Allg: if multiple methods of the same name in a class, then the LAST one overrides all others (unabhaengig von Arguments/Signatur) !! auch for __init__() : ===========
    - basically the constructor/__init__ is just a normal class-method with allg method features, so:
    - ONLY one constructor / __init__  ! if multiple, then the last one will overwrite the others and is the ONLY __init__ !
    - can be called explicitly on any obj ! BUT schould NOT! it is basically for the initial obj-creation !
    - as all methods, any further definition of a method with the same NAME, no mather what each aguments listing is, will just overwrite the previous definitions!
    """)
class A:
    def  __init__(self):      print("-no-params")
    def  __init__(self, a):   print("-01-params: ", a)
    def  __init__(self, x):   print("-01-params: ", x)
    def  __init__(self, a,b): print("-02-params-first-one--will-be-overwritten!: ", a, b)
    def  __init__(self, a,b):
        self.a1=a
        self.b1=b
        print("-02-params: ", a, b)

o1=A(1,2)          ##--II- all others will produce errors!:  o1=A(1) , o1=A() 
print(o1.a1, o1.b1)
o1.__init__(3,4)   ##--II-you can invoke __init__ also explicitly and reset the initial params of already created instance !
print(o1.a1, o1.b1)




##############################################################################
print("\n========== OOP:  __init__ and __del__ of the class: ==========")
class C1():
    def __init__(self, name):
        self.name = name
        print(self.name , "  C1 has been created!")

    def __del__(self):
        print (self.name , " C1 has been destroyed")


if __name__ == "__main__":
    print ("-" * 20, "base class init/del")
    x = C1("XX")
    y = C1("YY")
    z = x
    print("Deleting y")
    del y
    print("Deleting x. NOT deleting yet due to other reference to it ! :")
    del x
    print("Deleting z")
    del z

##############################################################################
print("\n========== OOP:  __init__ and __del__ of base  class must be explicitly called, if needed! : =========")
print("--- by defining __init__ method in the subclass, this OVERWRITES the baseclass __init__!! so if needed, must call explicitly super().__init__(...)")
print("--- but WATCH: if the derived class has NO __init__ at all, THEN the __init__ of the baseclass will be called , since it was NOT overwriten !!")
class C2(C1):
    __count__ = 0
    def __init__(self):
        ##--I-way1:  self.__class__.__count__  += 1 ; super().__init__(str(self.__class__.__count__) )
        type(self).__count__ += 1 ;  super().__init__(type(self).__count__)
        print(self.name , "  C2 has been created!")
    def __del__(self):
        super().__del__()
        print (self.name , " C2 has been destroyed")

if __name__ == "__main__":
    print ("-" * 20, "derived class init/del")
    o5 = C2()
    o6 = C2()
    del o5
    print ("-" * 40)

##############################################################################
print("\n========== C3 without any  __init__ method : =========")
print("--- WATCH: if the derived class has NO __init__ at all, THEN the __init__ of the baseclass will be called , since it was NOT overwriten !!")
class C3(C1): pass
if __name__ == "__main__":
    print ("-" * 20, "derived class withOUT any inits")
    c3 = C3("-c3-obj1-")   ##--WATCH: with no param here, then exception! since the init of C1 expects "name"-param !!
    print ("-" * 40)

##############################################################################
