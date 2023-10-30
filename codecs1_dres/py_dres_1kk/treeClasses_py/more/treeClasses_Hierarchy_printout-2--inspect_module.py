#!/usr/bin/env  python3
# coding:utf-8
##-- https://gist.github.com/guyskk/9545d7a6a31c2379c5a319bd37551775 :

""" class-tree-printout , using inspect module, works also for object/full-tree, ...  """

print ("-------------------------------------------------")
from inspect import getclasstree


def classtree(cls, indent=0, fillchar='-'):
    """
    Print class tree
    Args:
        cls: base class
        indent: indent size
        fillchar: fill char of indent
    """
    classes = subclasses(cls)
    tree = getclasstree(classes)
    print_tree(tree, indent, fillchar)


def fullname(cls):
    """Get fullname of cls"""
    if cls.__module__ in ['builtins', 'exceptions']:
        return cls.__name__
    return cls.__module__ + '.' + cls.__name__


def subclasses(cls):
    """Get all sub classes of cls and itself"""
    result = set()
    todos = [cls]
    while todos:
        cls = todos.pop()
        for subcls in cls.__subclasses__():
            if subcls is not type and subcls not in result:
                result.add(subcls)
                todos.append(subcls)
    return result


def print_tree(tree, indent=0, fillchar='-'):
    """Print the return value of inspect.getclasstree"""
    for entry in tree:
        if isinstance(entry, tuple):
            cls, bases = entry
            cls_name = fullname(cls)
            filling = fillchar * indent
            if len(bases) < 2:
                print(filling + cls_name)
            else:
                bases_name = ','.join([fullname(x) for x in bases])
                print(filling + '{}({})'.format(cls_name, bases_name))
        else:
            print_tree(entry, indent + 4, fillchar)


if __name__ == '__main__':
    print ("----------------- BaseException-tree: -----------")
    ##__ classtree(BaseException)
    print ("-------------------------------------------------")
    print ("----------------- object-tree : -----------------")
    classtree(object)
    print ("-------------------------------------------------")
