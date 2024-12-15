_______________  django-REST-API try1 /_230119  :  _________________________________


#####  ==========  try1-coll django-REST-API based on  https://realpython.com/api-integration-in-python/ /_230119  :

	_______:  --- install Lib:
    [u1@2209arx ~]$    pip install djangorestframework
    lla   ~/.local/lib/python3.10/site-packages/rest_framework/

	_______:  -- create+conf a django-test-prj + app for countires-exp:
    - create pri+app-tree:
    [u1@2209arx wks]$ django-admin   startproject  countryapi
    [u1@2209arx countryapi]$ python manage.py   startapp  countries
    vi countryapi/settings.py   ##--> INSTALLED_APPS : [...,     "rest_framework", "countries"]
    - model:
    gvim ./countries/models.py  ##--add modes
    - DB-write:
    [u1@2209arx countryapi]$ python manage.py   makemigrations
    [u1@2209arx countryapi]$ python manage.py  migrate  ##--create a new table in the database
    [u1@2209arx countryapi]$ python  manage.py   loaddata  countries.json   ##-writes data from json-file into the DB!
    ....
    see the above URL for the rest ...
##________________________________________  ___________________________
