baseCls1=tuple  ##--I-just set it to your class, to list all its sub-classes ! here tuple class as exp !
baseCls1=object


#####  ==========  flat-listing of all subclasses of cls1 :
##__ print ("\n-------------------- 1- all subclasses flat-listing of cls1, non-recursive, set-solution flat, no-tree: -------------")
def get_all_subclasses_1(python_class):
    """
    all subclasses FLAT listing, but NOT-Tree! just listing all flat !
    Helper function to get all the subclasses of a class.
    :param python_class: Any Python class that implements __subclasses__()
    """
    python_class.__subclasses__()

    subclasses = set()
    check_these = [python_class]

    while check_these:
        parent = check_these.pop()
        if hasattr (parent, "__subclasses__") and parent != type :
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    check_these.append(child)

    return sorted(subclasses, key=lambda x: x.__name__)

##__for listing uncomment this:   for ii in (get_all_subclasses_1(baseCls1)): print (ii)
##________________________________________  ___________________________


#####  ==========   2- recursive, generating a list of all subclasses-tree of cls1 :
def get_all_subclasses_2(cls):
    all_subclasses = []
    for subclass in sorted(cls.__subclasses__(),  key=lambda x: x.__name__):
        all_subclasses.append(subclass)
        if  hasattr (subclass, "__subclasses__") and subclass != type :
            all_subclasses.extend(get_all_subclasses_2(subclass))
    return all_subclasses

##__for listing uncomment this: for s11 in get_all_subclasses_2(baseCls1): print (s11)
##________________________________________  ___________________________


#####  ==========  3- yield solution, flat-printout
def get_subclasses(cls1):
    if  hasattr (cls1, "__subclasses__") and cls1 != type :
        for subclass in cls1.__subclasses__():
            yield from get_subclasses(subclass)
            yield subclass

##__for s11 in (get_subclasses(object)): print (s11)
##________________________________________  ___________________________

