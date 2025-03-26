# ---  https://realpython.com/python-chainmap/

from collections import ChainMap
from collections import OrderedDict, defaultdict
"""
-  the primary use case of ChainMap is to provide an efficient way to manage multiple scopes or contexts and handle access priorities for duplicate keys. This feature is useful when you have several dictionaries that store duplicate keys and you want to define the order in which your code will access them.
- 
"""
# ==================== create/instantiate ChainMap : ==================================
def create_simple_chainmap():
    print("\n", '='*30, "create new ChainMap:")
	# ---  Use no arguments
    print('-'*10 , 1)
    print(ChainMap())

	# ---  Use regular dictionaries
    print('-'*10, 2)
    numbers = {"one": 1, "two": 2}
    letters = {"a": "A", "b": "B"}
    print(ChainMap(numbers, letters))
    print(ChainMap(numbers, {"a": "A", "b": "B"}))

	# ---  Use other mappings
    print('-'*10, 3)
    numbers = OrderedDict(one=1, two=2)
    letters = defaultdict(str, {"a": "A", "b": "B"})
    print(ChainMap(numbers, letters))

	# ---   create ChainMap objects using the class method dict.fromkeys(). This method can take an iterable of keys and an optional default value for all the keys:
    print('-'*10, 4)
    print(ChainMap.fromkeys(["one", "two","three"]))
    print(ChainMap.fromkeys(["one", "two","three"], 0))


# ==================== lookups / searches ChainMap : ==================================
def lookups():
	# ---  key lookup searches all the mappings in the target chain map until it finds the desired key. If the key doesn’t exist, then you get the usual KeyError. Now, how does a lookup operation behave when you have duplicate keys? In that case, you get the first occurrence of the target key:
    # - how does a lookup operation behave when you have duplicate keys? In that case, you get the first occurrence of the target key (starting from leftmost dict):
    print("\n", '='*30, "lookups:")
    for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
    vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
    pets = ChainMap(for_adoption, vet_treatment)
    print(pets["dogs"], pets.get("cats"), pets["turtles"])
    # This general behavior also applies to iteration:
    for key, value in pets.items(): print(key, "->", value, end=" , ")
    print()
    print(pets.keys()) # -so same order/overwritings for the keys()
    for k in pets.keys(): print(k, end=" , ")
    print()
    for v in pets.values(): print(v, end=" , ")
    print()


# ==================== std dict methods/ops : =========================================
def dict_ops():
    # --- ChainMap supports the same API as regular dictionaries for accessing existing keys.
    print("\n", '='*30, "dict-std-ops:")
    numbers = {"one": 1, "two": 2}
    letters = {"a": "A", "b": "B"}
    alpha_num = ChainMap(numbers, letters)
    print(alpha_num, alpha_num["two"], alpha_num.get("a"))


# ==================== modifications-1: update/add/delete/... : =======================
def modify1():
    # --- !! modifications will be ONLY on the FIRST dict!! : ChainMap allows you to update, add, delete, and pop, BUT ALL happens ONLY on the first dic!
    # - The difference with lookups is that these operations act on the FIRST mapping ONLY:
    # - Operations that mutate the content of a given chain map only affect the first mapping, even if the key you’re trying to mutate exists in other mappings in the list. For example, when you try to update "b" in the second mapping, what really happens is that you add a new key to the first dictionary.

    print("\n", '='*30, "modify1: add, delete, pop, clear : --------")
    numbers = {"one": 1, "two": 2}
    letters = {"a": "A", "b": "B"}
    alpha_num = ChainMap(numbers, letters)
    print(alpha_num)

    print("\n- Add a new key-value pair:")
    alpha_num["c"] = "C"
    print(alpha_num)
    
    print("\n- Update an existing key:")
    alpha_num["b"] = "b"
    print(alpha_num)
    
    print("\n- Pop keys:")
    alpha_num.pop("two")
    print(alpha_num)
    print('  -2try:    alpha_num.pop("a")  #--> Exception! moddifications ONLY on FIRST dict!')
    
    print("\n- Delete keys:")
    del alpha_num["c"]
    print(alpha_num)
    print('  -2try:   del alpha_num["a"]   #--> Exception! moddifications ONLY on FIRST dict!')
    
    print("\n- Clear the dictionary:")
    alpha_num.clear()
    print(alpha_num)


# ==================== modifications-2: readonly-org-dicts: ===========================
def modify2():
    # --- You can take advantage of the above/modify1-behavior to create updatable chain maps that don’t modify your original input dictionaries. In this case, you can use an empty dictionary as the first argument to ChainMap:
    # - Here, you use an empty dictionary ({}) to create alpha_num. This ensures that the changes you perform on alpha_num will never affect your two original input dictionaries, numbers and letters, and will only affect the empty dictionary at the beginning of the list.
    print("\n", '='*30, "modify2: readonly-org-dicts by updates: ---")
    numbers = {"one": 1, "two": 2}
    letters = {"a": "A", "b": "B"}
    alpha_num = ChainMap({}, numbers, letters)
    print(alpha_num)
    # modify it:
    alpha_num["comma"] = ","
    alpha_num["period"] = "."
    print(alpha_num)


# ====================  dict.update() compare to ChainMaps: ===========================
def compare_dictupdate():
    """
    - With .update() or **-op the last value you provide for a given key will always prevail/wins! NO duplicate keys! ...!
    - with ChainMap, external changes in the input dictionaries affect the underlying chain, which isn’t the case with update()/**-merged dictionaries.
    - performance:
    Now suppose you have n different mappings with at most m keys each. Creating a ChainMap object from them would take O(n) execution time, while retrieving a key would take O(n) in the worst-case scenario, in which the target key is in the last dictionary of the internal list of mappings.
    Alternatively, creating a regular dictionary using .update() in a loop would take O(nm), while retrieving a key from the final dictionary would take O(1).
    The conclusion is that, if you often create chains of dictionaries and only perform a few key lookups each time, then you should use ChainMap. If it’s the other way around, then use regular dictionaries unless you require duplicate keys or multiple scopes.
    """
    print("\n", '='*30, " merging dicts with **-op  bzw.  dict.update()  vs. ChainMaps: --------------")
    for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
    vet_treatment = {"cats": 2, "dogs": 1}   # - for distinct-eg:    vet_treatment = {"hamsters": 2, "turtles": 1}
    cm1 = ChainMap(for_adoption, vet_treatment)
    # Merge dictionaries with .update()
    pets = {}
    pets.update(for_adoption)
    pets.update(vet_treatment)
    # /OR just:    pets = {**for_adoption, **vet_treatment}
    print("- !! With .update() or **-op the last value you provide for a given key will always prevail/wins:")
    print(cm1)
    print("pets.update():  ", pets)

    print("- pos-modify of  for_adoption['dogs'] :")
    for_adoption['dogs'] = "XXXX"
    print(cm1)
    print(pets)
    print(for_adoption["dogs"], cm1["dogs"], pets["dogs"])


# ====================  ChainMap own method: .map : =================================
def chainmap_map():
    """ .map : public instance attribute:
    - ChainMap stores all the input mappings in an internal list. This list is accessible through a public instance attribute called .maps, and it’s user-updatable.
    -  ChainMap() without arguments, then the list will store an empty dictionary.
    """
    for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
    vet_treatment = {"dogs": 4, "turtles": 1}

    print("- .maps : a list of user-updatable dicts(mappings:")
    pets = ChainMap(for_adoption, vet_treatment)
    print(pets)
    print(pets.maps)

    print("- modifyping/add to the list .maps :")
    pets.maps.append({"hamsters": 2})
    print(pets)
    print(pets.maps)

    print("- modifyping/del off the list .maps :")
    del pets.maps[1]
    print(pets)
    print(pets.maps)

    print("- modifyping/reverse the order of the list .maps : so reversing the lookup-order:")
    pets.maps.reverse()
    print(pets)
    print(pets.maps)


# ====================  ChainMap own method: .new_child() : ===========================
def chainmap_new_child():
    """ .new_child():
    Returns a new ChainMap containing a new map followed by all of the maps in the current instance.
    If m is specified, it becomes the new map at the front of the list of mappings; if not specified, an empty dict is used, so that a call to d.new_child() is equivalent to: ChainMap({}, *d.maps).
    If any keyword arguments are specified, they update passed map or new empty dict. This method is used for creating subcontexts that can be updated without altering values in any of the parent mappings. /stdlib-ref
    """
    mom = {"name": "Jane", "age": 31}
    dad = {"name": "John", "age": 35}
    family = ChainMap(mom, dad)
    print(family)
    son = {"name": "Mike", "age": 0}
    familyson = family.new_child(son)
    print(family)
    print(familyson)


# ====================  ChainMap own method: .parents : ===============================
def chainmap_parents():
    """ .parents  : public instance attribute:
    returns a new ChainMap instance with all the mappings except the FIRST one ! skip the first dictionary !
    This property returns a new ChainMap instance with all the mappings in the underlying chain map except the first one. This feature is useful for skipping the first mapping when you’re searching for keys in a given chain map:
    """
    print("\n", '='*30, ".parents :")
    mom = {"name": "Jane", "age": 31}
    dad = {"name": "John", "age": 35}
    son = {"name": "Mike", "age":  0}
    family = ChainMap(son, mom, dad)
    print(family)
    p1 = family.parents
    print(p1)


# ====================  py-vars-lookup: ===============================================
input = 42  # -keep it here, to be as global-var! masking/overwriting the builtin input() func in the following ChainMap :
def py_vars_lookup():
    """
    When Python is looking for a name, it searches the local, global, and built-in scope sequentially, following that same order until it finds the target name. Python scopes are dictionaries that map names to objects.
    """
    import builtins
    # Shadow input with a global name
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    print("Retrieve input from the global namespace: due to the above seq. in pylookup mapping, the global var input has masked the  builtin input() func:")
    print(pylookup["input"])
    # Remove input from the global namespace
    del globals()["input"]
    # Retrieve input from the builtins namespace
    print(pylookup["input"])

# ################### main: #################################################
print()
# __  create_simple_chainmap()
# __  lookups()
# __  dict_ops()
# __  modify1()
# __  modify2()
# __  compare_dictupdate()
# __  chainmap_map()
# __  chainmap_new_child()
# __  chainmap_parents()
py_vars_lookup()
print()

