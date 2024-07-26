#!/usr/bin/env  python3

print("\n========== using the defined class C1 in other module here, and checking the class-var features : ==========")
print("========== !! WATCH !: DIFF between write-and-read-acces to class vars through its instance!: ==========")
from cl1_classVar_instanceCounter_readWriteAccess  import C1

j1= C1();
j2= C1();

print (j1.CVAR1)
print (j2.CVAR1)
print  ("\n---------- write-access to class-var directly through class-name:  so for ALL instances the class-var is also changed: ----------")
C1.CVAR1=10
C1.CVAR2=20
print (j1.CVAR1)
print (j2.CVAR1)
print (j1.CVAR2)
print (j2.CVAR2)
##__  print ("\nclass C1  dict:", C1.__dict__)

print  ("\n---------- instances-dicts: ----------")
j1.set1("Obj-1"); print (j1.get1()) ; print (j1.__dict__)
j2.set1("Obj-2"); print (j2.get1()) ; print (j2.__dict__)

print  ("\n---------- !! watch: the WRITE-access to class-var through instance so does NOT work!! there a new instance-var with the same name will be defined! : ---------- ")
j1.CVAR1=13
print (j1.CVAR1)
print (j2.CVAR1)
print (j1.__dict__)
print (j2.__dict__)
##__  
print ("\nclass C1  dict:", C1.__dict__)
print  ("\n---------- !! watch:  WRITE-access to class-var through instance so would work, through its __class__ attrib ! : ----------")
j1.__class__.CVAR1=55
j1.__class__.CVAR2=65
print (j2.CVAR1)  ##--II-so it was changed for j2  also !!
print (j1.__dict__)
print (j2.CVAR2)  ##--II-so it was changed for j2  also !!
print (j2.__dict__)
print ("\nclass C1  dict:", C1.__dict__)
print  ("----------------------------------------------------------------")

