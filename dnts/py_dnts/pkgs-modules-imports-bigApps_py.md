packages/modules/libs-tree-structure
=======================================================


#####  ==========  urls/nts/infs:
    -! see docsRF_Tut--CH.6.Modules
    -! see docsRF_LangRef--5. The import system
##________________________________________  ___________________________


#####  ==========  DEFs / DIFFs:     class  <-->  module <-->  package: ==============
	- !!    class  <  module/file  < package/dir :

	_______:  package	== is a DIR, usu. containing a "__init__.py" file (pre-py-3.2 was MUST have), which can conatains several files/modules. The __init__.py files are required to make Python treat directories containing the file as packages.
	- regular package  :  A traditional package, such as a directory containing an __init__.py file and probably further modules/subdirs !
	- namespace package (pos--py-3.2)  : are basically only a DIR containing further modules/subdirs, without any __init__.py ! works just as a namespace-container! no other funcs! A PEP 420 [https://www.python.org/dev/peps/pep-0420] package which serves only as a container for subpackages.

	_______:  module	== is just a "*.py" file:
	- so an organizational unit of Python code in a *.py file, which can be importerd. So a file containing Python definitions and statements. 
	- The module-name (__name__) is the file name without suffix ".py" ! Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
	- One module/file can contains no/one/several class-definitions.
	- A module can be just standalone /OR inside a packge (dir-tree-containing-__init__.py). Non-package-modules should not have a __path__ attribute.
	- A Class inside a module/file can have the same name as the file/module /OR NOT ! A module can have the same name as the class inside it or NOT!
	- "import c1" ONLY loads the file c1.py into the current name-space, BUT eg the class c1 inside c1.py still can be accessed only by c1.c1 ! so eg obj1 = c1.c1() 
	- Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module.
	- Python code in one module gains access to the code in another module by the process of importing it.

	_______:  class 	== is the CODE-segment defined with "class"-KEYWORD and indented appropriately! the filename and classname need NOT be the same!!

	_______:  DIFFs: class  <  module <  package:
	-!! class ("class"-KEYWORD-defined in a .py file)   <  module/file  (.py file)  <  package/dir (DIR containing  "__init__.py" file):
	-! modules need NOT contain a class!! (see eg os.py, sys.py,...). in this case "import os" imports all stuff defined in os.py wihout indentations.
	if any class is defined there, it is NOT imported! to import this class then do eg: "import Scanner from re"
	--> !! so DIFF import C1  <-->  from C1 import C1    (assume C1 class is defined in the module/file C1.py):  --> see "import"-section here below!

	_______:  tree/listings of pkgs/modules on cmdlin :
    - pkgs-tree-listing of a Lib/...:  ca.:      tree -d  pkg1-path
    - modules-tree-listing:   tree  -P "*.py"    pkg1-path  ##--or exclude more dir with -I as:  -I "__pycache__|devtools|test"  
    - classes-names-listing-grep:   grep1  --include="*.py"   --exclude-dir="*devtool*"  -E "^class " -R    ./selenium/  | sort

##________________________________________  ___________________________


#####  ==========  "import"-tag : =================================================

	_______:  !! DIFF:  import os   <-->    from os import *      #see docsRF_Tut--CH.6.Modules , 6.4 Packages :
	- "import os" form :
		ONLY The imported module NAME is placed in the importing module’s global symbol table.
		ONLy load "os" into current app/main/modules, BUT current NAMESPACES are UNCHANGED!!:
		so still eg os.environ (NOT just environ)!! so this form does NOT enter the names of the functions defined in "os" directly in the current symbol table!! you can accesss them by eg os.chdir() ! but NOT just chdir() !
	- "from os import *" form :
		"os" MEMBERS are loaded+imported into the current NAMESPACE!! not-just-module-name! : so just  "environ" or "chdir()" , BUT NOT os.environ or os.chdir !!! then os.xxx does NOT exist, by this import-style,  in the namespace
		this variant imports names from a module directly into the importing module’s symbol table
	- "from package-X/module-X import item-Y" : the item-Y can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.  -! see ref.tut--6.4 + 6.4.1 Importing * From a Package
	- "import item.subitem.subsubitem" :each item except for the last must be a package; the last item can be a module or a package but can NOT be a class or function or variable defined in the previous item.
	--so:
	- fibo.py contains definition for func1(), then:
	-! import fibo : does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there.  so then: fibo.func1 is OK, BUT just func1 is error!!
	-! from fibo import *  --> then func1(..) (defined in fibo.py) is ok! (BUT no-good-style!): This imports all names except those beginning with an underscore into the current symbol table!!

	_______:  !! DIFF:  import C1  <-->  from C1 import C1    (assume C1 class is defined in the module/file C1.py) :  #see tut.ref--CH.6.Modules , 6.4 Packages :
	- import C1; x=C1()   --->  TypeError: 'module' object is not callabl !! must call "x=C1.C1()"  :
	  is because "import C1" imports ONLY the MODULE/file C1.py and NOT the class inside it!! so then you have to "x=C1.C1()" to instantiate a C1-Instance!!
	- from C1 import C1  ; x=C1()  --> OK. : because it imports the CLASS C1 from the module/file C1.py

	_______:  class imports:  eg in module m1.py are classes defined C1, C2, C3 :
	- NOT-working:  import m1.C2 !! but ok:  from m1 import C2 ; 

	_______:  search-path for imports/modules:  PYTHONPATH , sys.path :    - see ref.tut--6.1.2 The Module Search Path
	- sys.path is a normal python-list/[...] of DIR-entries  which are  searched to import/find modules IF the module not in sys.modules dictionary, so not alerady loaded !
	- When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.
	- sys.path : is a list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.
	- sys.path  ==  current-dir-of-module/-lib/-script  +  ${PYTHONPATH} + installation-dependent-defaults
	- sys.path.append("/aa/bb/cc") : so sys.path can be dynamically in code be adapted !
	- alias epypathlines='echo -e ${PYTHONPATH//:/"\n"}'  ##--in py-shell:  import sys;  print  (sys.path) ; #-prints the absolute-pathes!

	_______:  querying/listing imported modules / sys.modules :
	- sys.modules  dictionary maps module names to modules which have already been loaded. printDictBeauty1(sys.modules)
	- During import, the module name is looked up in sys.modules and if present, the associated value is the module satisfying the import, and the process completes. However, if the value is None, then a ModuleNotFoundError is raised. If the module name is missing, Python will continue searching for the module.
	-! so UNloading a module, then just: del sys.modules["aa.bb.cc"] 
	- filePath of a module loaded ? : import XXX; print (XXX.__file__)      ##--!-but The file attribute doesn't always exist. This is the case with modules which are statically linked C libraries.  see: python-course.eu/python3_modules_and_modular_programming.php.html
	- listing  lodaed builtin-modules into this interpreter:  import sys ; print(sys.builtin_module_names) ##--see pydoc sys !

	_______:  relative-import-pathes:
	- ONLY the import-form "from ..xx import yy" may be used by relative-imports!! NOT "import ..xx.yy" !! see docsRF_LangRef--5.7. Package Relative Imports !

	_______:  "from module1  import *"  form:
	- controlling this form of import:  define __all__ in the module1 and explicitly list the exported elements for "*"-import !
	- if __all__ is defined, then only the names explicitly listed there will be exported to "from module1  import *"
	- if __all__ = [] , then NOTHING will be imported by "from module1  import *" !

	_______:  reloading modules (also in  py-shell ): 
	- modules are loaded/imported ONLY once! no reloading! if you change them, then have to reload them: 
	py3:  import  importlib ; importlib.reload(XXX)
	py2:  reload(modulename)  /or restart py-shell!  ##--obsol!
	- reload a class inside a module (importlib.reload() works for modules, not a class-inside-a-module !):
	del sys.modules["MyPkg.MyModule"] ; from  MyPkg.MyModule   import MyClass1 ; ##so now the MyClass1 is reloaded ! 

	_______:  LIBs-import-helpers:
	pydoc importlib ; (pydoc imp : eher obsol; Since version 3.4 you should use the "importlib" module!)
##________________________________________  ___________________________


#####  ==========  Packages-Structure, py-Tree with modules+submodules, py-Pkg-Dirs....: =================================================
	- see ref.tut-- 6.4 Packages

	_______:  __init__.py  initialization files for packages/dirs/libs-trees:
	-!! ONLY dirs containing the file __init__.py are considered as Python-Package-Dirs!! otherwise they will be ignored by finding modules and classes!!
	-  __init__.py files are required to make Python treat the directories as containing packages!! see docsRF_Tut--CH-6.4-packages
	-  __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable
##________________________________________  ___________________________


#####  ==========  TIPs modules coding: =================================================

	_______:  running/testroutines of a module (as standalone run!)! both as an imported-module AND as standalone-run (with cmdline-args, eg as the module-test-routine) :
	if __name__ == "__main__":   import sys ; fib(int(sys.argv[1])) .... ##-see ref.tut--modules

	_______:  
	- dict of a module:  dir(moduleXX) ; eg: dir(sys) ##--lists all valid attributes and methods for that module. 
##________________________________________  ___________________________


#####  ==========  running a DIR(package) /OR a zip-py-file:

	-! put __main__.py file there and add the line "import run1" to it if eg  run1.py must run as default. : see pyCookBK--10.7
##________________________________________  ___________________________

