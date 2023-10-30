___________________ GraphQLs .... /_230204  : try1 : _________________________________________
- based on:  https://www.howtographql.com/graphql-python/1-getting-started/  , https://www.howtographql.com/basics/0-introduction/
##________________________________________  ___________________________


#####  ==========  /_230204 :  
##-- installs:
mkdircd  /up1/prjs/py1/wks/gql1
pip  install  django-filter  graphene-django  django-graphql-jwt  ##--org-line i py-venv:  pip install django==2.1.4 graphene-django==2.2.0 django-filter==2.0.0 django-graphql-jwt==0.1.5
##-- dj-prj:
django-admin  startproject  hackernews
cdlla  /up1/prjs/py1/wks/gql1/hackernews/
python manage.py migrate
python manage.py runserver
##-- config-dj-app:
vide-org ./hackernews/settings.py  :
	## INSTALLED_APPS = ( # After the default packages 'graphene_django',)
	##--at-END:   GRAPHENE = { 'SCHEMA': 'hackernews.schema.schema', }
##-- app1:
[u1@2209arx hackernews]$ python  manage.py   startapp links
vide-org  links/models.py
vi  ./hackernews/settings.py  ##-INSTALLED_APPS = ( # After the graphene_django app 'links',)
##-- Create the database tables for links-app:
python manage.py makemigrations
python manage.py migrate
##-- add new DB-sntries:
python manage.py shell ##--and create some links:
from links.models import Link
Link.objects.create(url='https://www.howtographql.com/', description='The Fullstack Tutorial for GraphQL')
Link.objects.create(url='https://twitter.com/jonatasbaldin/', description='The Jonatas Baldin Twitter')
##-- GraphQL-schema creation:
vi  links/schema.py  ##--...
#--->  not done realy the rest! ...
