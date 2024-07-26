
##--do NOT use/try super in direct subclasses of object !
##-2try: comment-out/in super() calls !! funny! strange! python-ridiculous !
print ("\n------------ super() with un-related-parent-classes! :---------------------------")
"""
- so the base-/parent-classes are NOT releted to each other! C1/C2 goes independantly to object!
- so two differen independant MRO-routes !
- ! WATCH!: only one tree-route inits are called upt to the top! the otherone NOT at all !
- ! it would NOT be the case if A and B classes were both subclassed from C1 !
- ! do NOT call super() in direct-derived classes of builtin.object (as C1 / C2) !! un-expected results!
- ! C3(), withOUT __init__(), will be ignored, based on the principle of super(): any child-class-method before any parent-method in the tree, even if not direct ancestor or the Parent more left located!
- !  the __init__() of object() will be the VERY last call ! due to MRO! check its MRO !
"""
##------------- first-level-base-classes: --------------
class C1():
    def __init__(self, *args):
        print("-- C1.init: ", self.__class__, *args)

class C2():
    def __init__(self, *args):
        print("-- C2.init: ", self.__class__, *args)

class C3(object):
    pass
    ##--!!-has not __init__(), so will be ignored! the __init__() of object() will be the VERY last call ! due to MRO! check its MRO !
    #-  based on the principle of super(): any child-class-method before any parent-method in the tree, even if not direct ancestor or the Parent more left located!

##------------- second-level-base-classes: --------------
class A(C1):
    def __init__(self, *args):
        print("-- A.init: ", *args)
        super().__init__()  ##--2try: comment-it-out !

##--!!-2try: same base-class as A and see the effect:   class B(C1):
class B(C2):
    # def __init__(self, ii): print("-- B.init", ii)
    def __init__(self, *args):
        print("-- B.init: ", *args)
        super().__init__()

##------------- derived-class: --------------
##--2try: class X(B, A):
class X(C3, A, B):
    def __init__(self, *args):
        print("-- X.init: ", self.__class__, *args)
        super().__init__(21, 22)

#######################################
#a1 = A(1); print("<<<<<")
#b1 = B(3,4); print("<<<<<")
x1 = X(5) ; print("<<<<<")

print (X.mro())

