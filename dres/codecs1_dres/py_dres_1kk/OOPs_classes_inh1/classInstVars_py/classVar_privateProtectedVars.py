

print("""==========
    - private attribs of both class and instance are internally renamed to  _<classname><attrib-name> !
    - so both are not otherwise visible for read/write outside the Class!
    - you should NOT access them on this way, even if they are accesible! but just per instance-/class-methods as set...!
    - here accessed them so just to learn/presentation !
-----""")

class C1:
    _v1 = 1
    __v2 = 2
    def __init__(self):
        self._p1  = 3
        self.__p2 = 4   ##--CHK1-:  rename p2 to v2 and the class-var __v2 will be not accessible any more though o1._C1__v2  !

o1 = C1()
print ("-- C1-dict:\n",  C1.__dict__ , "\n")
print ("-- o1-dict:\n",  o1.__dict__ , "\n")
print("-- privs: C1._C1__v2 , o1._C1__v2 , o1._C1__p2 : ",  C1._C1__v2 , o1._C1__v2 , o1._C1__p2)

