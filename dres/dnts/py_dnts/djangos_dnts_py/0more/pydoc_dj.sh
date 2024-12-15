#!/usr/bin/bash
##--I-problem with pydoc for SOME django-modules, as pydoc  django.db.models, since the __init__ s are executed by imports and so exceptionss....
##--!!-BUT do NOT set these VARs globally, otherwise eg DJANGO_SETTINGS_MODULE specifies the current active module!
#- however django.setup() requires certain (dummy) django-project-tree/-settings and this must be executed before pydoc for django-modules !
#- so here just a dummy django-project-tree for that as djgPrj11_DN :
#
p1=${1:?"USAGE:  ... <python-component-name for pydoc> ; eg:  ... django.db.models ; eg ... django.db.models.fields.DateField"}
#
##--1.-methodOK-OK  with a dummy prj settings.py: ---------------------
## a dummy/empty django-prj-tree incl. its settings.py  is required for setup() in manage.py eg for pydoc django.db.models , ... :
##__  export  djgPrj11_DN=django_p11
##__  export  djgPrj11_DP="${prjEtcDP}/${djgPrj11_DN}"
##__  export  PYTHONPATH="${djgPrj11_DP}:${PYTHONPATH}"
##__  export  DJANGO_SETTINGS_MODULE="${djgPrj11_DN}.settings"
##----------------- 1END dummy-prj
#
##--2.method: with django dafult settings.py : -----------------------
export  DJANGO_SETTINGS_MODULE=django.conf.global_settings
python  -c "import django, pydoc ; django.setup() ; pydoc.cli()"  $@

