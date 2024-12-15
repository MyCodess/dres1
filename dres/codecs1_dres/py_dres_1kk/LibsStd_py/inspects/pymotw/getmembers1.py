# inspect.getmembers() , https://pymotw.com/3/inspect/index.html

import inspect
from pprint import pprint

import example

print("inspect.getmembers return value is a list of tuples with two values: the name of the member, and the type of the member.")

# ################################################################# all members:
print("\n======================= all members:")
for name, data in inspect.getmembers(example):
    if not name.startswith('__'):
        print('{} : {!r}'.format(name, data))
# 1kk:
print("-------------")
membersList1 = [x for x in inspect.getmembers(example) if not str(x[0]).startswith("__")]
pprint(membersList1, width=160)

# ################################################################# filtered members:
print("\n======================= only Classes:")
print("-The predicate argument can be used to filter the types of objects returned! here filter the Classes only:")
for name, data in inspect.getmembers(example, inspect.isclass): print(f'{name} : {data}')
print("------------- only funcs:")
for name, data in inspect.getmembers(example, inspect.isfunction): print(f'{name} : {data}')

# ################################################################# classes inpect:
print("\n======================= classes inspect:")
# __all-members-of-class-A:  pprint(inspect.getmembers(example.A), width=160)
pprint(inspect.getmembers(example.A, inspect.isfunction), compact=True)

# ################################################################# obj/instances inpect:
print("\n======================= obj/instances inspect:")
a = example.A(name='inspect_getmembers')
pprint(inspect.getmembers(a, inspect.ismethod), width=160)

print("\n======================= doc/comments inspect:")
print(inspect.getdoc(example.B))
print(inspect.getcomments(example.B.do_something))
print(inspect.getcomments(example))

print("\n======================= source inspect:")
# -full class source:
print(inspect.getsource(example.A))
# -source of a certain func of a class:
print(inspect.getsource(example.A.get_name))


