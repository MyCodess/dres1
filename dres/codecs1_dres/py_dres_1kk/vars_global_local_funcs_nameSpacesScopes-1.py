#!/usr/bin/env  python3
""" global-local-funcs-vars and their scopes:

A variable defined or assigned value inside of a function is local unless it is explicitly marked as global.
In other words, we can refer/read-access to a variable name in any enclosing scope, but
we can only rebind variable names in the local scope by assigning to it or in the module-global scope by using a global declaration.

Any variable which is changed or created, so write-access, inside a function is local, if it hasn't been declared as a global variable.
To tell Python, that we want to use the global variable, we have to explicitly state this by using the keyword global !!
A variable can't be both local and global inside a function.
https://www.python-course.eu/python3_global_vs_local_variables.php
https://www.python-course.eu/python3_functions.php#Local-and-Global-Variables-in-Functions
https://towardsdatascience.com/but-its-not-declared-40501fb1e943
"""

print ("===================== global-local-funcs-vars: =====================")
print ("\n---only-read-access-inside-func:---------------------")
def f():
    """As there is no local variable s, i.e. no assignment/write-access to s, the value from the global variable s will be used:"""
    print("-",s)      # read-acces ! so free occurrence of global s in f
s = "Global-1-"
f()
print(s)

print ("\n---write-access-inside-func:---------------------------")
def f(): 
    """As there is an assignment/write-access to s, a new LOCAL variable created! Assigning a value to it, means, creating a local variable :"""
    s = "Local-1-"     # write-access! so now s is local in f ! Assigning a value to it, means  creating a local variable s (except if pre-declared as global !)
    print("-",s)
s = "Global-1-"
print(s)
f()
print(s)

print ("\n---global-keyword-inside-func:--------------------")
def f():
    """As pre-declared global s, so even with an assignment/write-access , s is GLOBAL :"""
    global s
    print("-",s)
    s = "Local-1-"  ##--write-access-but-pre-declared-as-global !, pre-declared as global, so s is global in f !!
    print("-",s) 
s = "Global-1-"
print(s)
f()
print(s)

print ("\n---combination-global-local:----------------------")
def foo(x, y):
    """wild combination of local and global variables and function parameters:"""
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print("-",a,b,x,y)

a, b, x, y = 1, 15, 3,4 
print(a, b, x, y)
foo(17, 4)
print(a, b, x, y)

print ("\n---nested-funcs-global-vars------------------------")
def f():
    """Global Variables in Nested Functions:
    what will happen, if we use the global keyword inside nested functions?
    We can see that the global statement inside the nested function g does not affect the local-variable 'city' of the enclosing-function f, i.e. it keeps its value 'Hamburg'.
    We can also deduce from this example that after calling f() a variable 'city' exists in the module namespace and has the value 'Geneva'.
    This means that the global keyword in nested functions does not affect the namespace of their enclosingnamespace!
    """
    city = "Hamburg"
    def g():
        global city
        city = "Geneva"
    print("Before calling g: " + city)
    g()
    print("After calling g: " + city)

f()
print("Value of city in main: " + city)

print ("\n---nonlocal:-----------------------------------------")
def f():
    city = "Munich"  #--II-comment-out this line to get error, due to DIFF between nonlocal and global!! if do it AND change nonlocal to global, then again fine/no-error! but other var-scopes !
    def g():
        nonlocal city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
city = "Stuttgart"
f()
print("'city' in main: " + city)

print ("\n---nonlocal-replaced-by-global:----------------------")
def f():
    city = "Munich"
    def g():
        global city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
city = "Stuttgart"
f()
print("'city' in main: " + city)

print ("\n---ERROR:-mixed-global-local-in-same-scope---------------")
def f(): 
    """As there is an assignment/write-access to s withOUT-global-declaration, so s is local, but the next line generates an ERROR, since th local s here not defined yet :")
    first access s with a print(s) function, hoping to get the global value, and then assigning a new value to it? Assigning a value to it, means creating a local variable s. So, we would have s both as a global and a local variable in the same scope, i.e. the body of the function. Python fortunately doesn't allow this ambiguity. So, it will raise an error, as we can see in the following example:")"""
##__    print("- un-comment this line to generate the error! ",s)    # here yet global s, but error due to next line local s, write-access-without-global-decleration !
    s = "Local-1-"      # This makes s local in f, so the previous print-line generates ERROR ! local and global in same scope NOT-allowed !
    print("-",s)
s = "Global-1-" 
print(s)
f()
print(s)

print ("--------------------------------------------------")

print ("---------- 3 scopes: global, nonlocal, local :----")
"""
--- 3 Scopes of Python :     https://towardsdatascience.com/but-its-not-declared-40501fb1e943 :
    - "global"  :  In the main part of the script. By default, this already contains the built-ins. You can access all global variables with glo
    - "nonlocal" (for nested-funcs) :  the outer function, if this is a nested function
    - "local"   :  Within the current function. You can access all local variables with locals() . Within the main script, locals() == globals()
    -!! The scope of a variable is defined at compile-time !! NOT at run-time !!
"""
def foo():
    min = lambda n: "enclosing"
    def bar():
        """Bar is enclosed by 'foo'"""
        print(min([1, 2, 3]))
    def baz():
        """Baz is also enclosed by 'foo'"""
        min = lambda n: "local"
        print(min([1, 2, 3]))
    bar()
    baz()
print(min([1, 2, 3]))
min = lambda n: "global"
print(min([1, 2, 3]))
foo()
print(min([1, 2, 3]))


print ("------------ global: ---------------------------")
x = "global"
def f1():
    x="local-f1"
def foo():
    global x
    x = "local"
f1()
print(x)  # gives "global"
foo()
print(x)  # gives "local"
##---- to get sure:
x = "global"
def foo():
    globals()["x"] = "local"
foo()
print(x)  # gives "local"
print ("--------------------------------------------------")


print ("------------ nonlocal : ------------------------")
x = "global"
def foo():
    x = "enclosing"
    def bar1():
        x = "local"
    def bar2():
        nonlocal x
        x = "local"
    bar1()
    print(x)  # gives "enclosing"
    bar2()
    print(x)  # gives "local"
print(x)  # gives "global"
foo()
print(x)  # gives "global"
print ("--------------------------------------------------")

print ("------------- funcs-pointer/-references keeps their vars-context between calls (for global+nonlocal-vars of course): -------------------------------------")
def f1(x):
    x += 100
    def f2():
        nonlocal   x ##--II- remove "nonlocal" and initialize it to "local"-calue, and see its value is NOT kept during calls! to get sure you can do:    if not ("x" in dir()): x=200
        x += 2
        return x
    return f2
x =f1(1)
y =f1(10)
print (x())
print (x())
print (y())
print (y())
print ("--------------------------------------------------")
