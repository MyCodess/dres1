____________________ try2--/:230823 -django, https://www.w3schools.com/django/ _________________________

--- 

#####  ==========  /:230823 :  coll/protocs-django-try2-/:230823  :
    -! based on   https://www.w3schools.com/django/
    - /up1/mnt/VARUfs/varu/varau/wks/django2/myworld/
    --- users + ... misc:
    - dj-admin-user created: u1 + "u1" , u1@loc1.test
    
    _______:  menv:
2023-08-23T18:11:21 CEST
/up1/varu/varau/wks/django2
[u1@2209arx django2]$ python  -m venv myworld
source ./myworld/bin/activate
(myworld) [u1@2209arx django2]$ python -m pip install  Django
(myworld) [u1@2209arx django2]$ django-admin  --version   ##--:  4.2.4
(myworld) [u1@2209arx myworld]$ python -m pip install  selenium

    _______:  project-create:
(myworld) [u1@2209arx django2]$ cdlla myworld/
(myworld) [u1@2209arx myworld]$ django-admin startproject my_tennis_club
http://127.0.0.1:8000/

    _______:  app-create
(myworld) [u1@2209arx my_tennis_club]$ python manage.py  startapp members

    _______:  view-add + url-mapping to the app:
- add view-method:
(myworld) [u1@2209arx my_tennis_club]$  vi my_tennis_club/members/views.py  ##--add members-method :  def members(request): return HttpResponse("Hello world!")
- add urls-mapping:
vi my_tennis_club/members/urls.py: 
vi my_tennis_club/my_tennis_club/urls.py   ##-include members/urls.py

    _______:  Template-add (like asp-files...) + add app "members" to the project "my_tennis_club" ! so for more static-HTMLS including a few dynamic-django-tags:
[u1@2209arx my_tennis_club]$ mkdir members/templates
[u1@2209arx my_tennis_club]$ vi members/templates/myfirst.html
vi  my_tennis_club/members/views.py  ##--> add template file there instead HttpResponse(...)
- add app to the project:
vi my_tennis_club/settings.py  ##--add members to the INSTALLED_APPS !
(myworld) [u1@2209arx my_tennis_club]$ python manage.py  migrate  ##--inform the django-engine about the new app!
- so, start the server and check the url:
python  manage.py runserver  ; ##-->  127.0.0.1:8000/membe

    _______:  models/DB:
https://www.w3schools.com/django/django_models.php
--- create model-subclass/DB-tablei-als-Objects--ORM:
vi my_tennis_club/members/models.py ##--.... Table-ORM
- for checks: start your SQLite-Browser-in-ReadOnly for  here the swlite-DB and follow the changes !
--- Migrate == (prepare) DB-sync / writing into DB :
- migrate-prepare:  manage.py makemigrations members  ##--only generates my_tennis_club/members/migrations/0001_initial.py , BUT NOT yet into DB !
- migrate-do /write-to-DB:  python  manage.py migrate  ##--writes/syncs into DB ! checkt it with DB-Browser!
---
- !! sql-stmts-view : just to see the SQL-Stmts which were executed:  python  manage.py sqlmigrate members 0001  ##--or adapt 0001 to the one carried out! here was:  /migrations/0001_initial.py !

    _______: inserts-DB /add records:
https://www.w3schools.com/django/django_insert_data.php
from members.models import Member
member = Member(firstname='Emil', lastname='Refsnes')
member.save()
#- https://www.w3schools.com/django/django_insert_data.php
# - Add Multiple Records:
member1 = Member(firstname='Tobias', lastname='Refsnes')
member2 = Member(firstname='Linus', lastname='Refsnes')
member3 = Member(firstname='Lene', lastname='Refsnes')
member4 = Member(firstname='Stale', lastname='Refsnes')
member5 = Member(firstname='Jane', lastname='Doe')
members_list = [member1, member2, member3, member4, member5]
for x in members_list:  x.save()
##________________________________________  ___________________________

