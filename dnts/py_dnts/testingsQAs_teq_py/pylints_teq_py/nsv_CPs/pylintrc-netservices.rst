===========================================
Pylint Usage for netservices
===========================================


TO-clarify/communicate:
---------------------------------------
- ! in der praxis wird angepasst ...! harmlos !
    - ! is for "New Code" ! how to exclude prev-codes? can not be based on regexp! so not using eg ignore-paths=.../ignore-patterns=... !
    - Pylint searches for a configuration file pylintrc in the current working directory as first option ! or PYLINTRC envvar!
    - putting pylintrc in the netservices-root, then it will be found automatically by pylint !
    - QA-dir for more...? tests/QAs/
    - typing !
    - --strict
    - my nts: #--... , FIXME, TODO
    - in praxis wird angepasst/...
    - max-line-length = 120 ?? otherwise with tag 
    - namespace packages??
    - re-generate-check:  pylint  --rcfile=./pylintrc-netservices    --generate-rcfile > rcgen1 ; 
    - LF !? see wiki + git !
    -
    -
    -
    -


Install, Setup, Docs:
---------------------------------------
    - install:   pip install pylint
    - VSCode plugin: Pylint , https://marketplace.visualstudio.com/items?itemName=ms-python.pylint
    - VSCode add the pylintrc file : "pylint.args": ["--rcfile=<file>"]
    - help (long listing of all pylint arguments):  pylint --help
    - docs:  https://pylint.readthedocs.io/

Usage, Run Pylint:
---------------------------------------
    - pylint   --rcfile=./misc/pylintrc-netservices  [options]  <MyDir / MyPackage / MyModule / ...>
        - e.g.:  pylint  --rcfile=./misc/pylintrc-netservices  --max-line-length=120  ./lib/
    - exclude/suppress warnings/messages for certain code line: ... #  pylint: disable=<msg-name>
        - e.g.:   import * from xxx    # <your comment/reason>  pylint: disable=wildcard-import (W0401)
    - overwriting options of pylintrc file via arguments on the command line:
        - e.g.: pylint --rcfile ./pylintrc-netservices --disable=invalid-name,missing-module-docstring  myfile.py
    - pylint directory/tree/recursive  will work if:
        - directory is a python package (i.e. has an __init__.py file), or
        - an implicit namespace package (then with --recursive or the option: recursive=yes)or
        - if directory is in the python path (e.g. in your venv).
    - more details in pylint docs: .../user_guide/usage/run.html
    - exit codes:  0 == no-errors/OK, 1 == fatal, 2 == error, 4== warning, 8 == refactor, 16 == convention/style-guide, 32 == wrong-usage
    -

Messages
---------------------------------------
    - pylint message format:
        - MESSAGE_TYPE:  LINE_NUM:[OBJECT:] MESSAGE
        - There are 5 kind of message types :
            * (C) convention, for programming standard violation
            * (R) refactor, for bad code smell
            * (W) warning, for python specific problems
            * (E) error, for probable bugs in the code
            * (F) fatal, if an error occurred which prevented pylint from doing further processing.
    - more info about a specific warning/msg:  pylint --help-msg=wildcard-import ;or msg-code as: pylint --help-msg=W0401
    - online messages descriptions:  https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html
    - list of pylint warnings:    pylint --list-msgs

Usefull/Common Commands & Notes:
---------------------------------------
    -
    -
    -
    -
##________________________________________  ___________________________

