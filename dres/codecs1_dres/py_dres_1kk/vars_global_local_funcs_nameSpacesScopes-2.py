
""" 
    --- funcs-references! as:  a=f() ,which returns a pointer to g() !
    watch the diff between a and a() then !!
    --- also global tag scope (base and sub funcs):
    global tag in base-func does NOT exist/extend into the sub-func if write-access to the var!
    move the first two lines of f() into g() and watch the diff !!
    also: global tag in f() does NOT apply in g() if any write-access of var in g() !
    also: play with global/nonlocal-tag and see ... !
"""

print ("\n====================== all var-changes in base-func : ========================")
var=1
def f():
    global var
    var +=1
    def g():
        return var
    return g

a = f()
b = f()
###
print("a : ",a , "b : ",b)
print ("A-  ", a is b)
print ("B-  ",  b())
print ("C-  ",  a())
print ("D-  ", a is not None)
print("a() : ",a() , " , b() : ",b())
print("a() : ",a() , " , b() : ",b())
print("- global var:  ", var)
var +=1
print("- global var:  ", var)
print("a() : ",a() , " , b() : ",b())
print("- global var:  ", var)

print ("\n====================== all var-changes in sub-func  : ========================")
var=1
def f():
    def g():
        global var
        var +=1
        return var
    return g

a = f()
b = f()
###
print("- global var:  ", var)
print("a : ",a , "b : ",b)
print ("A-  ", a is b)
print ("B-  ",  b())
print("- global var:  ", var)
print ("C-  ",  a())
print ("D-  ", a is not None)
print("- global var:  ", var)
print("a() : ",a() , " , b() : ",b())
print("a() : ",a() , " , b() : ",b())
var +=1
print("- global var:  ", var)
print("a() : ",a() , " , b() : ",b())
print("- global var:  ", var)

print ("\n====================== nonlocal var of base-func:     ========================")
var=1
def f():
    var = 100
    def g():
        nonlocal var
        var +=1
        return var
    return g

a = f()
b = f()
###
print("a : ",a , "b : ",b)
print ("A-  ", a is b)
print ("C-  ",  a() )
print ("B-  ",  b() )
print ("B-  ",  b() )
print ("B-  ",  b() )
print ("D-  ", a is not None)
print("a() : ",a() , " , b() : ",b())
print("a() : ",a() , " , b() : ",b())
print("a() : ",a() , " , b() : ",b())
print("- global var:  ", var)

