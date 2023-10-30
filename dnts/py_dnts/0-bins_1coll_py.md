python.cmdlines/bins ..... 1coll ..._RF:
================================================

#####  ==========  py-cmdlines...:

    - __pycache__  removing all:   find   . -depth  -xdev -type d  -name __pycache__   -exec  rm -rf  {} \;  ##--/OR -ok instead -exec !

    _______:  pkgs-tree-listings ...:
    - pkgs-listing of a Lib/...:  ca.:      tree -d  pkg1-path
    - pkg-modules-tree-listing:   tree  -P "*.py"   -I "__pycache__|devtools"   pkg1-path  ##--or exclude more dir with -I ... !
##________________________________________  ___________________________



#####  ==========  file-import/readin  as a module into interactive-shell (any .py-file loading into pyShell):

    1- >>> exec(open("/up1/w1/dc1k/dres/codecs1_dres/py_dres_1kk/__data1/__data1.py").read())
    2- python  -i  /up1/w1/dc1k/dres/codecs1_dres/py_dres_1kk/__data1/__data1.py
    3- importing module-path but without ".py" AND replaced "/" with "." :
        echo  dc1k/dres/codecs1_dres/py_dres_1kk/__data1/__data1.py  |  sed -e 's@/@.@g'  ##--:  dc1k.dres.codecs1_dres.py_dres_1kk.__data1.__data1.py
        cd /up1/w1 ; python ;
        from dc1k.dres.codecs1_dres.py_dres_1kk.__data1.__data1    import *   ##--so without .py and replaced "/"
##________________________________________  ___________________________

