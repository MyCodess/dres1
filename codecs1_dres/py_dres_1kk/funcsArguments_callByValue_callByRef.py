#!/usr/bin/env  python3
"""funcs-arguments/params: call-by-value/ref!?
https://www.python-course.eu/python3_list_manipulation.php#Extending-and-Appending-Lists-with-the-'+'-Operator
https://www.python-course.eu/python3_passing_arguments.php#Side-effects
"""

print ("=============== call-by-value/ref: =======================================")
print ("--------------------1a--IMMUtable-args, so call-by-value-------")
def ref_demo(x):
    """ IMMUtable arguments are always cal-by-value !
    by read-access of the argument-var, then all the same (as lang as no new assignments to it).
    by write-access / assigments then x points to a new object!"""
    print("-- x=",x," id=",id(x))
    x=42
    print("-- x=",x," id=",id(x))
x=1
print("- x=",x," id=",id(x))
ref_demo(x)
print("- x=",x," id=",id(x))
exit
print ("--------------------1b--IMMUtable-args, so call-by-value-------")
def callVal1(a,b):
    a += 10 ; b +=10 ;
    print ("--", a,b, id(a))
def callVal2(x,y):
    x += 20 ; y +=20 ;
    print("-- ", x, y, id(x))
x=1 ; y=2 ; 
print("- ", x, y, id(x))
callVal1(x,y)
callVal2(x,y)
print("- ", x, y, id(x))

print ("--------------------2---MUtable-args, so call-by-Ref---------")
def f1(l1:list):
    l1[1] +=10
    print ("--", l1, id(l1))
l2 = list(range(5))
print("-", l2, id(l2))
f1(l2)
print("-", l2, id(l2))

print ("--------------------2b--MUtable-args, so call-by-Ref---------")
def f1(l1):
    ##__  refCalls, and in-place-lists-extensions, so WITH-side-effect of changing org-argument:
    l1 += [21,22]
    l1.append(31)
    l1.extend([41,42,43])
    print ("--", l1, id(l1))
l2 = list(range(5))
print("-", l2, id(l2))
f1(l2)
print("-", l2, id(l2))

print ("--------------------2b--MUtable-args, but with copy-assignment-----")
def f1(l1):
    ##__ copy-assigment of lists! expensive, but no side-effect! so the org-argument is NOT changed:
    l1 = l1 +  [21,22]
    print ("--", l1, id(l1))
l2 = list(range(5))
print("-", l2, id(l2))
f1(l2)
print("-", l2, id(l2))

print ("-------------------------------------------------------------")
