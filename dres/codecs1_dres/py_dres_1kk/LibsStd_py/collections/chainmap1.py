from collections import ChainMap
"""
- ChainMap just puts together several dicts as one integrated one; overwrting chared key-values from right-to-left! so the leftmost/first-dict wins!
- ChainMap has ALL dict methods/attribs + a few more!
- ! updates/changes:  updating, adding, deleting, clearing, and popping keys, act ONLY on the FIRST mapping in the internal list of mappings.
---
- eg put all py-vars together in one dict:  pylookup = ChainMap(locals(), globals(), vars(builtins))
"""

def f1():
    cm1 = ChainMap({'a': 'AAA', 'b': 'BBB', 'c': 'CCC'},  {'a': 'DDD', 'b': 'EEE', 'f': 'FFF'})
    print("- final dict/key-values are updated/built/overwriten from rightmost-to-leftmost! so leftmost overwrites all:")
    print(cm1)
    # ok1:  for k, v in cm1.items(): print(k , " : ", v, end=" , ")
    for k in cm1: print(f"cm1[{k}]: {cm1[k]}",  end=" , ")
    print()

if __name__ == '__main__':
    # print("----------------------------------------------------------")
    print()
    f1()
    print()
