#!/usr/bin/env   python
##-- see : https://realpython.com/primer-on-python-decorators/

##-- decorator/wrapper-func:
##--!! the decorator-inner-func (wrapper_deco1) ist the real-wrapper! the idecorator-func-itself (deco1) is only for returning the decorator-pointer to the inner-wrapper !
def deco1(func1):
    def wrapper_deco1(*args,  **kwargs):
        print ("- I am the decoratos-wrapper-func and do something more before/after calling the final-func, WITHOUT modifying the final-func !")
        print ("- PRE-final-func1! do something here BEFORE calling the final-func ... and then call the final func1 (un-modified):")
        print ("--- org-func-being-wrapped:   ", end="  ");
        retVal11_wrapped = func1(*args,  **kwargs)
        print ("- POS-final-func1! do something here AFTER final-func being executed ... and return !")
        return retVal11_wrapped
    return wrapper_deco1   ##--II-NOT wrapper_deco1() !! ONLY a poiner to the wrapper/inner-deco-func, to be executed later on by the real func!! not its execution-result!!


print ("\n=========== 1. NOT-using @/Decorator-syntax, decorating the final-func hello1() manually : ============")
def hello1():
    print (f"Hello  ! I'm the org-func")

hello1 = deco1(hello1)  ##--!!-NOT  deco1(hello1())   BUT  deco1(hello1) !! so just a pointer to the func hello1 ! NOT its execution with hello1() !!
hello1()


print ("\n=========== 2. Using @/Decorator-syntax : @deco1 (same result as above/manually): ==========================")
print ("- using the @/Decorator-syntax, which is ONLY a syntactic-sugar! but is the same as above:")
@deco1
def hello2():
    print (f"Hello ! I'm the org-func !")

hello2()

#################### with Arguments of org-func : ################################################
print ("\n=========== 3. Using @/Decorator-syntax + org-func-with-Arguments: ==========================")
@deco1
def hello3(firstname1, lastname1):
    print (f"Hello {firstname1} {lastname1} ! I'm the org-func, with-arguments !")
    return "-- returnVa-from-func-hello3"

retVal1 = hello3("kevin", lastname1="Happy")
print(retVal1)
print()

