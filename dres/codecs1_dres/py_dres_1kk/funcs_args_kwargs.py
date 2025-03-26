
print ("\n=============== *args, **kwargs of funcs-args: ===========================")
note1 = """
- *-operator in func-arg f1(..., *args1):  input: expects single values bzw. *list1 ; output: converts single values into a tuple and forwards the tuple to the func named as args1 !
- *-operator prefixing a list: converts a list into single values!
- **-operator in func-arg:  input: expects named-args-syntax and: output: forward them to the func as a dict! (but itself does NOT expect a dict! only named-values bzw. **dict1)
- **-operator prefixing a dict: converts a dict into named-args-syntax!
- so by calling a func1(..., **kwargs1) with **mydict1 then you have access to mydict1 in func1 still as a dict but under new name: kwargs1 ! :")
---
- if they are NOT provided then they will be just empty, as:  () , {}
- so, for any access to kwargs-items, you must get sure that the key is there! otherwise runtimeerror !
---
- positional params (x,y) are MUST (except if default values)! otherwise runtimeerrors!
- even if posiitonals with default values, but if enought parameters, then first positionals are bedient
- positional args MUST be always before any named args !

"""
def f1(x, y=9, *a, **k):
    print("x:" ,x, "y:", y, "a/args:", a, "*a/args-values:", *a, "kwargs:", k, sep=" , ")  ##--OR-add:  , "**kwargs", {**k}
    # -2try: if 'k2' in k.keys():  print(x, y, a, k['k2'], sep=" -- ")

print("\n---1. args + kwargs param : --------")
print("- even if posiitonals with default values, but if enought parameters, then first positionals are assigned values! see y here!")
print("- *-operator in *args:     args MUST be provided as single values! *-op converts then the single values into a tuple and forwards it to the function:")
print("- **-operator in **kwargs: args MUST be provided in named-params-syntax as k1=v1, k2=v2, ... ! and not just a dict:")
f1(1,2, 3,4,5, k1=11, k2=22)

print("\n  - *-operator in *list1: converts the list into single elemnts!  compare:")
f1(1,2, [3,4,5], k1=11, k2=22)
f1(1,2, *[3,4,5], k1=11, k2=22)

print("\n  - **kwargs MUST be provided in named-params-syntax as k1=v1, k2=v2, ... ! and not just a dict:")
print("  - **-operator  for a dict: converts a dict into the named-params-syntax k1=v1, k2=v2, for the func-args and then forward it as a dict to the func!:")
f1(1,2, 3,4,5, {'k1': 11, 'k2': 22})   ##--watch k empty! kwargs must be provided as k=v, ...
f1(1,2, 3,4,5, **{'k1': 11, 'k2': 22})   ##--watch k empty! kwargs must be provided as k=v, ...

print("\n  - watch y values:")
f1(1,3,4,5,k1=11, k2=22)      ##--watch y ! so the second arg is y !
f1(1, (3,4,5), k1=11, k2=22)  ##--watch y !

print("\n---2. only args, NO kwargs/named-args : --------")
f1(1,2,3,4,5)

print("\n---3. No args, only kwargs/named-args : --------")
f1(1,2, k1=11, k2=22)

print("\n--4.- NO args, NO kwargs param : --------")
f1(1,2)

print("\n---5. NO args, NO kwargs, less positional : --------") ##--works only since y has default value
f1(1)

# =============
print("\n=============== using kwargs for named-args:")
def m1(x, y=0, **kw):
    print (x, y, kw.items())
m1(1)
m1(1,2)
m1(1, **{'y': 51, 'z': 52})
m1(1, **{'z': 51, 'y': 52})
m1(**{'x': 50, 'z': 51, 'y': 52})
# -2try--exc--double-y :   m1(1,2, **{'y': 51, 'z': 52})

