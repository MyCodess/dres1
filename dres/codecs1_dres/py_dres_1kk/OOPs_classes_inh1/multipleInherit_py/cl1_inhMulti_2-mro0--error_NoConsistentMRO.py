
"""
for multi-inheritance of derived-classes: more-specific-base-clases MAY NOT come after more-general-ones !
otherwise: TypeError: Cannot create a consistent method resolution MRO ...!
"""
##------------ base-clases : -------------------------------
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass


##------------ derived-classes: ----------------------------
class C4(D,A): pass
print (C4.mro())
print("--II-NOT-working:    class C5(A,D): pass\n")
##--II-NOT-working:    class C5(A,D): pass ; print (C5.mro())

class C6(C,D): pass
print (C6.mro())
class C7(D,C): pass
print (C7.mro())

class C9(C,A): pass
print (C9.mro())
print("--II-NOT-working:   class C8(A,C): pass\n")
##--II-NOT-working:   class C8(A,C): pass ; print (C8.mro())

class C10(D,B): pass
print (C10.mro())
print ("--II-NOT-working:  class C11(B,D): pass")
##--II-NOT-working:   class C11(B,D): pass

