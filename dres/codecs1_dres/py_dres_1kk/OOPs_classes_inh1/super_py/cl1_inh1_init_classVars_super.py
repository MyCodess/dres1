#!/usr/bin/env  python3

print("\n========== __init__  of baseclass will NOT be called automatically from subclass-init ! + instances_counter--clacc_var : ==========")
print("====== class-var as instances_counter ! WATCH: its changes in subclass C2 !! : ==========")
print("--- WATCH: the private-vars in objs.__dict__ , and their renamings/name-mangling !")

##--------------------- baseclass C1: ---------------------------------------------)
class C1(object):
    cvar1 = 0   ##--Count-Instances class-var !

    def __init__ (self):
        self.__class__.cvar1  +=  1    ##--II- replace the line with:   C1.cvar1 +=  1 , and then the subclass C2 and C1 have same one classvar cvar1 !!
        self._initname =   "_i_name--protect-" + str(self.__class__.cvar1)
        self.__initname =  "__i_name-private-" + str(self.__class__.cvar1)
        print ("-- C1 __init__ done:  ", self.__class__.__name__ )
    
    def set1(self, p1="name1"):
        self.name1=p1
    
    def get1(self):
        return self.name1

##---------------------  subclass C2: ---------------------------------------------)
##--------------------- subclass (does NOT call baseclass-init : ------------------)
class C2 (C1):
    def __init__ (self):
        super().__init__()    ##--II- if comment-out this line, see the baseclass-init will NOT be automatically executed !
        ##__  print("-!WATCH:  NOT needed the self-param in super().method1() call!! same as C1.method1(self)")
        print ("--- C2 __init__ done:  ", self.__class__.__name__ , super().cvar1 , self.__class__.cvar1)

    ##__ def __str__(self):
        ##__  return ("___str_method_test1" + str(C1.cvar1) + str(self.__class__.__base__))


##---------------------  instances of C1 + C2 : -----------------------------------)
if __name__ == "__main__":
    print ("\n------ C1 instances : ---------------------------------------")
    j1= C1();  j1.set1("Obj-1"); print ("-- j1-dict:  ", j1.__dict__)
    j2= C1();  j2.set1("Obj-2"); print ("-- j2-dict:  ", j2.__dict__)
    print ("-- C1.cvar1:  ", C1.cvar1)
    
    print ("\n------ C2 instances : ---------------------------------------")
    print ("---!! WATCH: the class-var cvar1 in C1 and C2 by this acccess style of self.__class__.cvar1 !!\n     the subclass C2 gets its own attribiute C2.cvar1 independent of C1.cvar! but starting from  C1.cvar value ! ")
    j5= C2();  j5.set1("--- Obj-5"); print ("--- j5-dict--subclass_C2:  ", j5.__dict__)
    j6= C2();  j6.set1("--- Obj-6"); print ("--- j6-dict--subclass_C2:  ", j6.__dict__)
    print("-- C2-dict:\n", C2.__dict__)
    print("-- C1-dict:\n", C1.__dict__)

    print ("\n====== dicts/dirs infos : ------------------------------------")
    print("-- C1-dict:\n", C1.__dict__)
    print("\n-- C1-dir:\n", dir(C1))
    print("\n--- C2-dict:\n", C2.__dict__)
    print("\n--- C2-dir:\n", dir(C2))

    ##__  print ("\n---------- str , repr : ------"); print (j5); print (j5.__class__ , id(j5)); print (j5.__str__()); print (j5.__repr__());
    print ("--------------------------------------------------------------")
