"""
inspect.getclasstree eigentlich does NOT returns the Tree, but only pairs of parent-classes only!
so, for each list-entry of the argument X :
    prints for each parent of X its base-/parent-class and then (repeatedly) direct-parents of X again!
    Each returned entry is a 2-tuple containing a class and a tuple of its base classes.
    see output for F here!
- !! so the REAL classTree is returned by MRO inspect.getmro(X) !
---
# -based-on:  https://pymotw.com/3/inspect/index.html
"""

import inspect
from pprint import pprint

import example
class C(example.B):
    pass
class D(C, example.A):
    pass
class E(C):
    pass
from io import StringIO
class S(StringIO):
    pass
class F(C, S, example.A):
    pass

# ================== example-tree eg: ==================================================
def print_example_tree():
    print('A, B->A, C->B->A, D->C+A , E->C->B->A , S->StringIO , F->C+S+A:')
    print("\n--- Tree of A:")
    pprint(inspect.getclasstree([example.A]))
    print("\n--- Tree of B:")
    pprint(inspect.getclasstree([example.B]))
    print("\n--- Tree of C:")
    pprint(inspect.getclasstree([C]))

    print("\n--- MRO of D:")
    print(inspect.getmro(D))
    print("\n--- Tree of D:")
    pprint(inspect.getclasstree([D]))

    print("\n--- Tree of E:")
    pprint(inspect.getclasstree([E]))
    print("\n--- Tree of S:")
    pprint(inspect.getclasstree([S]))

    print("\n--- MRO of F:")
    print(inspect.getmro(F))
    print("\n--- Tree of F:")
    pprint(inspect.getclasstree([F]), indent=4)
    # print_class_tree(inspect.getclasstree([example.A, example.B, C, D]))

# ================== print parent-classes of arg: ===========================================
def print_class_tree(tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent + 2)
    else:
        print('--' * indent, tree[0].__name__)
    return

# ================== main ==================================================================
if __name__ == '__main__':
    print_example_tree()
    # __ print_class_tree(inspect.getclasstree( [C, D], unique=True))
    print_class_tree(inspect.getclasstree( [example.A, example.B, C, D, F], unique=True))

