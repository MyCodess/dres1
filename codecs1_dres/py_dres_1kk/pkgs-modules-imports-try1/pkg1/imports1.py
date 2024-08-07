#!/usr/bin/env  python3
"""
    import-variations workouts !
    modules-and-packages loading/structure/.... workout1 ! for bigger apps/buildMgm/... !
"""
print ("----------\n", __file__ , __package__, __name__)

print("""
========== try various calls: as file/module/pkg/... and check their sys.path, ... ; eg :==========
--!!dnts: cu-dir in sys.path:
-- the definition of the cu-DIR changes, if you call as py-module (-m a.b.c) OR py-app (a/b/c.py) :
-- as script/app-call (python a/b/c.py) is the cu-dir, the FINAL parent-dir of the MODULE (of c.py, so .../a/b/)!
-- BUT as module-call (python -m a.b.c the cu-dir is the path of the ROOT-pkg (path/dir containing /a/ here!))
-- RELATIVE imports (., ..) are ONLy allowed, if called as module: so that py knows its pkg/parents!!
-- NO relative imports if called as py-app! as py-app it has NO parent-pkg but only parent-path/dir !
------ try them for DIFF between module-calls (-m a.b)   <--->  app-call/path-call (a/b/c.py) :
- just try diffs of sys.path for:   python  -m pkg1  <--->  python  pkg1/
- as py-script/py-app-call, OK:  python  pkg1/imports1.py ; /OR: python  pkg1/__main__.py  #--:OK, check sys.path!
- as py-script/py-app-call-subdir, OK:  python  pkg1/d1/d1_f1.py ; #--:OK, check its sys.path!
- as module-call, import-error:  python -m pkg1.__main__  ; /OR:  python -m pkg1.imports1  #--:import-error: check its sys.path! is different!
- as package-call, OK:   python pkg1 ;  #--:runs the __main__.py , BUT NOT the pkg1/__init__.py , due to running __main__.py!
- ! compare sys.path of AND if __init__.py is done if:   python -m  pkg1.d1.d12.d12_f12    <--->   python  pkg1/d1/d12/d12_f12.py
""")

print ("\n========== sys.path are where ALL imports/modules are searched: (curr-dir + $PYTHONPATH + installation-defaults) =========")
import sys
print("--- sys.path entries:")
for ii in range(len(sys.path)): print(sys.path[ii])

print ("\n========== multiple imports with different styles, all OK! : ===========================================")
from math import pi
from math import pi as mypi1   ##--I-multiple-times-imports, no-probelm, even as different identifiers !
##--I-  print (math.pi)  : now does NOT work! is shadowed by from math ....
print (pi)
print (mypi1)

print ("\n========== multiple same imports , all OK! the further ones will be ignored: ===========================")
import f1  ##--I-so f1.py must be here or find-able in $PYTHONPATH dirs !
import f1 ; import f1  ##--I-the further same imports will be just ignoreed ! NOT-reloaded !! so the counter-var will NOT be incremented!

print ("\n========== reloading imports in py3: ====================================================================")
from importlib import reload
reload( f1)

print ("\n========== querying imports : ==========================================================================")
import math
print("file:  ", f1.__file__, "\npackage:  ", f1.__package__)
print("file:  ", math.__name__, "\npackage:  ", math.__package__)
##__ print("dir(f1):   ",  dir(f1))

print ("\n========== classes imports : ===========================================================================")
from c1 import C2  ##--II-does NOT import c1.py !! but ONLY the Class C2 !! -and NOT-working :   import c1.C2
o2 = C2(21)
##-II- yet c1.C3(31) will NOT work! then, c1.py is NOT imported yet and the class C3 neither ! so first c1.py must be imported ! change the next two lines order and get errorr !!:
import c1
o3 = c1.C3(31)

print ("\n========== packaged-modules-imports : ==================================================================")
print("--dnts: in a pakcage-tree if you import deep-down a module, then ALL __init__.py files in the TREE will be executed, from top-to-down!! so, not only the one of the module-dir !!")
print("--check1: comment-out the further lines below, and you see that all __init__.py files are executed !!see docsRF_LanfRef--5.2.1. Regular packages ")
print("ALL __init__.py files in the TREE will be executed from top-to-down, and NOT only the one of the module-dir :")
print("- !! to see the effect of __init__.py try:   python -m pkg1.d1.d12.d12_f12  <--->   python  pkg1/d1/d12/d12_f12.py") 
import d1.d12.d12_f12
import d1.d12.d12_f12  ##--but it imports ONLY once !
##__chk1:  import d1.d1_f1
##__chk1:  print("file:  ", d1.d1_f1.__file__,   "\npackage:  ",  d1.d1_f1.__package__)
##__chk1:  d1.d1_f1.f1()
##__chk1--modules-loaded-listing:   print ("", sys.modules)


##----

