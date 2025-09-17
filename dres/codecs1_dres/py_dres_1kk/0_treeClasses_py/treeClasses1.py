#!/usr/bin/env  python

""" 
    1kk: SUBCLASSES-tree-printout (NOT parents-traverse!), traverses ONLY downwards/subclasses/childeren ! not upwards/parents! sorted, recursive!
    !! see also alternative/better: sphinx.ext.inheritance_diagram ,  sphinx.ext.graphviz , https://graphviz.org/ !
    USAGE: adapt the first section to your reqs! decide if you want module-traverse or a root-class-traverse!? if requrired, add imports,..!
        you need only adapt either of pkgname1/modname1/classeslist1 and then call its related func! but not needed to adapt all of them!
        if req, comment out module- or classeslist1 traverse! or not ...!
        pkg/dir bzw. modulename: ALL MUST be importable! so in your cu-dir or pypath/sys.dir or ... !! they will be geladen/imported !!
""" 
import pkgutil
import inspect
import importlib
from pathlib import Path
from pprint import pprint



#####  ==========  adapt this part to your base-class of the tree: ----------
# --- verbose / details :
mro1: bool = False         # -MRO printout?
details1: bool = False     # -details printout? : modile-file-path, ...

# --- your pkg/module/classes/pathes:
# -module-eg:
pkgname1="cryptography.hazmat.primitives"  # -just pkg-name! if wanted a dirpath instead, then have to just abit modify the pkg_tree_lib ! but it works also with only a dirpath!
modname1: str = "cryptography.x509"  # -module-name to traverse. MUST be importable!
# -classeslist-eg for tree of individual classe-name in a list:
# classeslist1-explicit-eg:  import cryptography.x509; classeslist1: list = [ cryptography.x509.GeneralName, cryptography.x509.ExtensionType ]
# classeslist1-explicit-pyRoot-eg:  classeslist1: list = [ object ]
# classeslist1-modname1-based-eg: mod1 = importlib.import_module(modname1); classeslist1: list = [ mod1.GeneralName, mod1.ExtensionType ] ; 
##________________________________________  ___________________________


#####  ==========  basic-subclasses-traverse recursively used by BOTH module-/classeslist-request-calls :
def subs1(cls1: type, indent1: int = 0) -> None:
    indent1Str = "------|" * indent1          ##--/OR--with-TAB-for-vim-folding:    indent1Str = "\t" * indent1
    ret1 = (f"|{indent1Str}{cls1.__name__}")
    if mro1: ret1 = (f"{ret1}    ,mro:  {cls1.__mro__.__str__()}")
    if details1: ret1 = f'{ret1} ,{str(cls1)}  ,-module: {cls1.__module__} ,-parents: {cls1.__bases__.__str__()}'
        # -OR--added-new-line for console:  ret1 = f'{ret1}\n|{"    "*(indent1+2)}{str(cls1)}  ,-module: {cls1.__module__} ,-parents: {cls1.__bases__.__str__()}'
    print (ret1)
    if hasattr (cls1, "__subclasses__") and cls1 != type :
        for s1 in sorted (cls1.__subclasses__(), key= lambda c: c.__name__):
            subs1 (s1, indent1 +1)
##________________________________________  ___________________________


#####  ==========  module-file-request:
def module_class_tree(modulename1):
    print(f"\n|------------ {modulename1} : ----------------")
    mod1 = importlib.import_module(modulename1)
    l1 = inspect.getmembers(mod1, inspect.isclass)
    for ii in l1:
        subs1 (ii[1] , 0)
    # __ print("-"*77, "\n")
##________________________________________  ___________________________


#####  ==========  classeslist-request:
def classes_tree(clslist1: list):
    for ii in clslist1:
        print(f"\n------------ subclasses-tree {ii} : ----------------")
        subs1 (ii, 0)
        print("-"*77, "\n")
##________________________________________  ___________________________


#####  ==========  pkg-recursive-req / pkg-tree:
def pkg_tree_lib(pkg1name: str):
    pkg1imp = importlib.import_module(pkg1name)
    pkg1dp: list[str] = pkg1imp.__path__
    moduleslist1 = [pkg1name+"."+x.name for x in pkgutil.iter_modules(pkg1dp) if not x.ispkg and not str(x.name).startswith("_")]
    pkgslist1 = [pkg1name+"."+x.name for x in pkgutil.iter_modules(pkg1dp) if  x.ispkg  and not str(x.name).startswith("_")]
    print("\n\n================== dirpath, moduleslist, pkgslist : ==================")
    print(pkg1dp)
    pprint(moduleslist1)
    pprint(pkgslist1)
    for ii in moduleslist1: module_class_tree(ii)
    for ii in pkgslist1: pkg_tree_lib(ii)
    # _1ok-mods-only:  moduleslist1 = [pkg1name+"."+x.name for x in pkgutil.iter_modules(pkg1dp) if not str(x.name).startswith("_")]
    # -ok-listing: for ii in pkgutil.walk_packages(pkg1dp): print(ii)
##________________________________________  ___________________________


#####  ==========  
if __name__ == "__main__":
    # __classeslist1:   classes_tree(classeslist1)
    # __module:         module_class_tree(modname1)
    # __package manually/os:  pkg_tree_os(pkg1DP)
    pkg_tree_lib(pkgname1)
##________________________________________  ___________________________



################### olds,more,....: #########################################################
#####  ==========  pkg-request-manually (os + files-selection...): deprecated! use iinstead the pkgutil based one in pkg_tree_lib !
# -! could use pkgutil stdlib eg:   pkg1 = pkgutil.walk_packages([ pkg1DP ]) ! but for now manually go through the files:
def pkg_tree_os(dp1: Path):
    import os
    ls1 =  os.listdir(pkg1DP)
    ls1.sort()
    print(ls1)
    ls1 = [pkgname1 + "."  + x.removesuffix('.py') for x in ls1 if str(x).endswith(".py")]
    print(ls1)
    for ii in ls1: module_class_tree(ii)
##________________________________________  ___________________________


# __ pkgname1: str = "cryptography.x509"
# __ pkg1DP: Path = Path(os.environ['USERPROFILE']) / 'var3/t3/t1var/docsvar/Py_docsvar/cryptography-main/src/cryptography/x509'
# __ pkgname1: str = "cryptography.hazmat.primitives.asymmetric"
# __ pkg1DP: Path = Path(os.environ['USERPROFILE']) / 'var3/t3/t1var/docsvar/Py_docsvar/cryptography-main/src/cryptography/hazmat/primitives/asymmetric'

