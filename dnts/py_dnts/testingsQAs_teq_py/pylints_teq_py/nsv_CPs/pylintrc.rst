===========================================
Pylint Usage for netservices
===========================================


Usage:
---------------------------------------
- inside your activated venv, incl. the setting of "DJANGO_SETTINGS_MODULE=netservices.settings.dev" and located in the project-root-folder (containing ./pylintrc):
- pylint  <module/package/directory/file/...>
- --- additional notes:  ----------
- instead of setting DJANGO_SETTINGS_MODULE you can do:  pylint  --django-settings-module=netservices.settings.dev  <dir/file/...>
- it traverses the DIR/Package/Tree, if they contain __init__.py ! otherwise have to set --recursive=yes
- if you are not in the project root directory, then have to specify the pylintrc location! e.g.:  pylint  --rcfile=../../pylintrc  --django-settings-module=<...> ...


More USAGE Examples/Tips/Notes/... :
---------------------------------------
- exclude certain file-names (--ignore <file-NAMES, comma separrated, NO-pathes!>):
    - e.g.: pylint  --rcfile=./pylintrc  ./tests/integration/   --ignore conftest.py,test_infoblox_client.py
    - to exclude a PATH or patterns use --ignore-paths resp. --ignore-patterns instead --ignore !

- exclude certain files (--ignore ...) AND overwrite certain options of pylintrc (--<option> <values>):
    - e.g.: pylint  --rcfile=./pylintrc  ./tests/integration/   --ignore conftest.py,test_infoblox_client.py  --notes fixme,TODO

- exclude/suppress warnings/messages for certain code line: ... #  pylint: disable=<msg-name>
    - e.g.:   import * from xxx    # <your comment/reason>  pylint: disable=wildcard-import (W0401)

- overwriting options of pylintrc file via arguments on the command line:
    - e.g.: pylint --rcfile ./pylintrc --disable=invalid-name,missing-module-docstring  myfile.py

- pylinrc location alternatives:
    - export  PYLINTRC=<path>
    - pylintrc or .pylintrc in the current working directory will be found as default!
    - If the current working directory is in a Python package, Pylint searches up the hierarchy of Python packages until it finds a pylintrc file. This allows you to specify coding standards on a module-by-module basis. Of course, a directory is judged to be a Python package if it contains an __init__.py file.
    - more alternatives see docs:   .../user_guide/usage/run.html

- pylint directory/tree/recursive  will work if:
    - directory is a python package (i.e. has an __init__.py file), or
    - an implicit namespace package (then with --recursive or the option: recursive=yes)or
    - if directory is in the python path (e.g. in your venv).
    - or using  --recursive=yes , --source-roots=<path,...> as commandline arguments!

- exit codes:  0 == no-errors/OK, 1 == fatal, 2 == error, 4== warning, 8 == refactor, 16 == convention/style-guide, 32 == wrong-usage
- more details in pylint docs: .../user_guide/usage/run.html


Install, Setup, Docs:
---------------------------------------
- Nothing extra required! All packages are already installed in your dev-venv !
- VSCode plugin: Pylint , https://marketplace.visualstudio.com/items?itemName=ms-python.pylint ; check the plugin-settings that the notifications are on!
- --- infos:
- install:   pip install  pylint  pylint_django
- help (long listing of all pylint arguments):  pylint --help
- docs:  https://pylint.readthedocs.io/


Pylint Messages:
---------------------------------------
- pylint message format:    MESSAGE_TYPE:  LINE_NUM:[OBJECT:] MESSAGE
- There are 5 kind of message types :
    - C : convention, for programming standard violation
    - R : refactor, for bad code smell
    - W : warning, for python specific problems
    - E : error, for probable bugs in the code
    - F : fatal, if an error occurred which prevented pylint from doing further processing.
- more info about a specific warning/msg:  pylint --help-msg=wildcard-import ;or msg-code as: pylint --help-msg=W0401
- online messages descriptions:  https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html
- list of pylint warnings:    pylint --list-msgs

