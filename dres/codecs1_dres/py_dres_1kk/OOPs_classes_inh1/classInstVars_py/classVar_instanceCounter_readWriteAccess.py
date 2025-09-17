#!/usr/bin/env  python3

print("\n========== !!TRICKY!: DIFF: read-OR-write access to Class-vars through the instance !! : =========== ")
print("---!! obj1.CVAR1 reads the class-attrib C1.CVAR1 ")
print("---!! BUT write-access : obj1.CVAR1 = 5 creates a NEW instance-atrib !! ")
print("---!! so obj1.CVAR1 += 2 which is basically obj1.CVAR1 = obj1.CVAR1 +1 : reads the class-var CVAR1 (read-access), then creates a new instance-attrib CVAR1 (due to write-acces), and then adds two to it !! ")
print("---!! so obj1.CVAR1 read-access: reads the class-var! obj1.CVAR1 = 20 : creates a new instance-var and leaves the class-var UNchanged! ")
print("---!!-WATCH: so DIFF  by write-access:  obj1.CVAR1 = 20   and   obj1.__class__.CVAR1 = 20 !! the first creates new instance-var, the second modifies the class-var !")
print("---!! from-inside-a-class-method to access the classvar, do:  type(self).CVAR1  /OR directly classname: C1.CVAR1 !")
print("---!! by read-acces both are the same, IF there is NO instance-attrib CVAR1 ! so then both access the class-var CVAR1 !!")
print("---!! see also mock3-udemy-Q.21-explanation in  in Mocks_udemy_1kk-pcap-220114/mock3_saved-udemy_pcap_1kk/ !\n")


class C1:
    CVAR1 = 1
    def __init__(self): 
        self.v1 = 20
obj1 = C1()
print("\n--- READ-access to classvar:")
print("- 4 ways for read-access of a class-var: ", obj1.CVAR1,  obj1.__class__.CVAR1, C1.CVAR1, type(obj1).CVAR1)
##__   
print("- C1-dict: ", C1.__dict__); print("- obj1-dict: ", obj1.__dict__)

print("\n--- WRITE-access to classvar:")
print("\n--- WRITE-access to classvar through obj1 directly :")
obj1.CVAR1 += 10
print("-  obj1.CVAR1,  obj1.__class__.CVAR1 : ", obj1.CVAR1,  obj1.__class__.CVAR1, C1.CVAR1)
##__   
print("- C1-dict: ", C1.__dict__); print("- obj1-dict: ", obj1.__dict__)

print("\n--- WRITE-access to classvar through obj1-class/__class__ :")
obj1.__class__.CVAR1 += 3
print("-  obj1.CVAR1,  obj1.__class__.CVAR1 : ", obj1.CVAR1,  obj1.__class__.CVAR1, C1.CVAR1)
##__   
print("- C1-dict: ", C1.__dict__); print("- obj1-dict: ", obj1.__dict__)

print("\n========== class-var--instance-counter included in each instance-name: ========== ")
class C1:
    CVAR1 = 0
    def __init__ (self):
        self.__class__.CVAR1 +=  1
        self._initname =  "i_name-" + str(self.__class__.CVAR1)
        print ("__init1_done__ ")
    def set1(self, p1="name1"):
        self.name1=p1
    def get1(self):
        return self.name1

##----------------------------------------
if __name__ == "__main__":
    j1= C1();  j1.set1("Obj-1"); print (j1.__dict__)
    j2= C1();  j2.set1("Obj-2"); print (j2.__dict__)
    print ("class-var--instance-counter == ", C1.CVAR1)

print ("----------------------------------------------------\n ")


print("\n================== DIFF: read-write-acces to class-vars by instance : =========================")
##--II-see Mock5_udemy1_Question_24+22+explanation !!
class Class1:
    var = 1
    _var = 2

    def __init__(self):
        self.prop = 1
        self._prop = 2

    def m1():
        print("--m1-without-params-self! ")

o1 = Class1()
print(o1.__dict__)
o1.var += 1       ##--II- it first READS the class-var "var" (read-access-by-instance-OK!), BUT by modifying/writing this, it defines/sets a new instance-variable o1.var = 2
print("-- Class1.var , o1.var : ", Class1.var , o1.var)
print(o1.__dict__, "\n")
print(Class1.__dict__)
Class1.m1()

print("\n========== obj-vars with unmodified/same-values are saved only ONCE for all/several objs !: ----------------")
##--II-see Mock5_udemy1_Question_24+22+explanation !!
o2= Class1()
print( "o1 and o2 different Objs!: ", id(o1) == id(o2), id(o1),  id(o2))
print( "- o1-/o2-props same-id()??: ", id(o1.prop) == id(o2.prop) , id(o1.prop), id(o2.prop) )
o2.prop = 2
print( "- o1-/o2-props same-id()??: ", id(o1.prop) == id(o2.prop) , id(o1.prop), id(o2.prop) )
o2.prop = 1
print( "- o1-/o2-props same-id()??: ", id(o1.prop) == id(o2.prop) , id(o1.prop), id(o2.prop) )
o1.prop = 5  ; 
o2.prop = 5  ; 
print( "- o1-/o2-props same-id()??: ", id(o1.prop) == id(o2.prop) , id(o1.prop), id(o2.prop) )
print("===========================================================================\n")


