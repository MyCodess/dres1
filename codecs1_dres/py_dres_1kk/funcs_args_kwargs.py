
print ("\n=============== *args, **kwargs of funcs-args: ===========================")
note1 = """
- args will be forwarded to the func as a tuple of args (x,y,z)
- *args : are then the tuple elements, as: x, y, z
- kwargs  will be forwarded to the func as a dict {key:val, ...}
- **kwargs will be then each dict-element as k1=v1 , ...
- if they are NOT provided then they will be just empty, as:  () , {}
- so, for any access to kwargs-items, you must get sure that the key is there! otherwise runtimeerror !
- positional (x,y) are MUST (except if default values)! otehrwise runtimeerrors!
- even if posiitonals with default values, but if enought parameters, then first positionals are bedient
- positionals MUST be always before any named args !

"""
def f1(x, y=9, *a, **k):
    print("x:",x, "y:", y, "args:",a, "args-values:",*a, "kwargs:",k, sep=" , ")
    # -2try: if 'k2' in k.keys():  print(x, y, *a, k['k2'], sep=" -- ")

print("\n---1. args + kwargs param : --------")
f1(1,2, 3,4,5, k1=11, k2=22)
f1(1, 3,4,5, k1=11, k2=22)
f1(1, (3,4,5), k1=11, k2=22)
print("\n---2. only args, NO kwargs param : --------")
f1(1,2, 3,4,5)
print("\n---3. No args, only kwargs param : --------")
f1(1,2, k1=11, k2=22)
print("\n--4.- NO args, NO kwargs param : --------")
f1(1,2)
print("\n---5. NO args, NO kwargs, less positional : --------") ##--works only since y has default value
f1(1)

