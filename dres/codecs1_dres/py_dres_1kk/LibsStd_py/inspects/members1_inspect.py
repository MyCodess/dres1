import inspect

l1: list = list(range(0,5))
d1 = {1: 1, 2: 2}
# all methods,...:  print(inspect.getmembers(l1))

# -list all non __ funcs of obj1:   
for ii in [x for x in inspect.getmembers(l1) if not str(x[0]).startswith("__")]:
    print(ii)

