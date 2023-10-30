#!/usr/bin/env  python3
""" django-class-tree-printout -without using module inspect- , 
    USAGE1:   ... <root-class-name>  ; exp:  ... django.db.models.base.Model 
    to list also the upper classes tree (MRO) set here the printUpperClasses=True
    ! there is basic-ROOT-django-class! so you can printout always a specific branch of django-hierarchy !
""" 

print ("-------------------------------------------------")

##------ required for django-setup()-call : --------
##-- django.setup() ist required to be called to setup django-env !
import sys, os, django
sys.path.append("/up1/prjs/py1/etc/django_p11")  ##--setup rewuires a dummy/empty prj !
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_p11.settings'
django.setup()
##-----------------------------------------

##- exp for cmdline-param1 :
rootClassName = django.db.models.base.Model   ##--OR: django.db.models.fields.Field

printUpperClasses = False    ## for printing also the upper classes set here printUpperClasses = True

if (len(sys.argv) > 1): rootClassName = eval (sys.argv[1])

def classtree(cls, indent="-|"):
    print (indent, cls.__name__ , end=" ")
    if printUpperClasses:  print(cls.mro(), end=" ")
    print ()
    for subcls in cls.__subclasses__():
        if subcls != type :
            classtree(subcls, indent+"-------|")

##__ classtree(BaseException)
classtree(rootClassName)
print ("-------------------------------------------------")

##__  import  django
##__  import  django.db
##__  import  django.db.models
##__  from    django.db.models.base import Model
##__  import  django.db.models.fields

