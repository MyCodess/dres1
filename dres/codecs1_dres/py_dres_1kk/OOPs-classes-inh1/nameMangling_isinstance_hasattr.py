#!/usr/bin/env  python3

print("\n=================== name-mangling : priv/protect/CLASS/...: ===========================")
print("--- hasattr() also for CLASS ok!  class-attr is also obj-attr !")
class A:
    CVAR1 = 1
    __CVAR3 = 3
    def __init__(self):
        self.att1 = 11
        self._att2 = 22
        self.__att3 = 33
    def __m1(self): print("--private-method-__m1()-called!")
a1 =A()
print(hasattr(A, "CVAR1"))      ##--->  true,  class itself as first param ok! second MUST be a string !!
print(hasattr(a1, "CVAR1"))     ##--->  true,  class-attr is also obj-attr !
print(hasattr(a1, "att1"))      ##--->  true,  
print(hasattr(a1, "_att2"))     ##--->  true,  protected/_ attrib accessible

print("\n---------- private-attributes and their name mangling for both class+obj : -----------")
print("--- private-attribute is internally renamed/mangled into  _<className><attribName> ,which should NOT be used to access, but is possiblle!")
print(hasattr(A,  "__CVAR3"))    ##--->!  False !  private-attrib accessible only through name-mangling as:
print(hasattr(A,  "_A__CVAR3"))  ##--->!  True !   accessible only through name-mangling !
print(hasattr(a1, "__CVAR3"))    ##--->!  False !  private-attrib accessible only through name-mangling as:
print(hasattr(a1, "_A__CVAR3"))  ##--->!  True !   accessible only through name-mangling !
print(hasattr(a1, "__att3"))    ##--->  false, private/__  attrib NOT accessible ! 
print(hasattr(a1, "_A__att3"))    ##--->  True !   accessible only through name-mangling !
print("a1-dict:  ", a1.__dict__)
print("A--dict:  ", A.__dict__)

print("\n---!WATCH!:  BUT name-manglin is NOT used if you add an instance variable outside the class code. !!:")
a1.__v5 = 5     ##--II- access to this only by:  a1.__v5 ! BUT NOT through mangling as a1._A__v5  !!
print(hasattr(a1, "__v5"))      ##--->!! True! only way to acces it!
print(hasattr(a1, "_A__v5"))    ##--->  False ! private , but NOT name-mangled!! 
print("a1-dict:  ", a1.__dict__)

print("\n---------- private-methods calls: -------------")
print("---!WATCH!:  private-methods ONLY through an instance + name-mangling can be called! NOT-directly through the CLASS! due to self-param! except: class-/staticmethods?? !")
a1._A__m1()
##--EE-error:  a1.__m1()
##--EE-error:  A.__m1()
##--EE-error:  A._A__m1()
print("--------------------------------------------------------------------")
##__  exit()

print("\n================ isinstance /inh /polymorph: ===============================")
print("--- subclass isinstance of baseclass, but NOT vice versa :")
class A:    pass
class B(A): pass
class C(B): pass

a1=A()
b1=B()
c1=C()

print (isinstance(a1, C), isinstance(c1, A))   ##-- false, true
print("--------------------------------------------------------------------")


print("\n=================== hasattr() : priv/protect/CLASS/...: ===========================")
class C1:
    V1 =1
    def __init__(self):
        self._p1 = 5
        self.__p2 = 7

print ("--- hasattr classname")
print(hasattr(C1, "V1"))    ##--!!-claso classname as first param ok! the second param MUST be a string!!
print(hasattr(C1, "_p1"))   ##--I-class has no instance-atrr-access without instanciation !!
print(hasattr(C1(), "_p1"))  ##--!!-now it is instance with () !!

print ("--- hasattr obj-name")
o1= C1()
print(hasattr(o1, "_p1"))
print(hasattr(o1, "__p2"))  ##--!!-private-attribs NOT accessible directly! only through name-mangling!
print(hasattr(o1, "_C1__p2"))  ##--!!-private-attribs accessible only through name-mangling : _<className>attribName  !
print("--------------------------------------------------------------------")

