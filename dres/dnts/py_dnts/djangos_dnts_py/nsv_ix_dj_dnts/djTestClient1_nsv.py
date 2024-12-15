from django.test import Client, TestCase
from pprint import pprint
from django.urls import reverse

# - declare -x DJANGO_SETTINGS_MODULE="netservices.settings.test"
# - from django.conf import settings ;  settings.configure()

class ArecordTests(TestCase):
    def test_1(self):
        c = Client()
        # -OK1 :  response = c.post("/auth/login/?next=/",  {"username": "u11", "password": "u11"})
        resp1 = c.post("/auth/login/?next=/infoblox/records/a/",  {"username": "u11", "password": "u11"})
        #__          pprint(resp1.__dict__)
        print("-- resp1.status_code :: ", resp1.status_code)
        assert   resp1.status_code == 200
        self.assertIs(resp1.status_code, 200)
        # print("-- resp1.content---------------\n :: ", resp1.content)
        
        resp1 = c.get(reverse("core:infoblox/records-a"))
        print("-- resp1.status_code :: ", resp1.status_code)
        assert   resp1.status_code == 200
        #__ pprint(resp1.__dict__)
        
    def test_2(self):
        c = Client()
        # --OK in shell, BUT not on cmdline with manage.py test ...! obv. due to creation of new database and then so missing the user! :
        resp1 = c.post("/auth/login/?next=/infoblox/records/a/",  {"username": "u11", "password": "u11"}, follow=True)
        print("-- resp1.status_code :: ", resp1.status_code)
        print("-- resp1.content---------------\n :: ", resp1.content)
        print("\n ============= second-get: ==============")
        resp1 = c.get("/infoblox/records/a/")
        print("-- resp1.status_code :: ", resp1.status_code)
        print("-- resp1.content---------------\n :: ", resp1.content)
        
##--------------- in shell ok:  python manage.py shell : -------------------
"""
#####  ==========  /:240528 :  dj-test-client in dj-shell, getting arecords:
# in setings.py:  ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']
# djprj1 : python manage.py shell

from django.test import Client, TestCase
from django.contrib.auth.models import User     ##-!- due to ModelAdmin base, have to authtenticate, even if login not activated!
from django.conf import settings
import pprint
def pp1(dic1): pprint.pprint(dic1, indent=4, width=120, sort_dicts=True)

c1 = Client()
userXX = User.objects.get_or_create(username="dummy-user-xx")[0]
userXX.is_staff = True
userXX.is_superuser = True   ##-here really not required; but OK!
userXX.save()
c1.force_login(user=userXX, backend=settings.AUTHENTICATION_BACKENDS[0]) 

resp1 = c1.get("/infoblox/records/a/", follow=True)
##-- resp1.__dict__ , context_data , ... :
pp1(c1.__dict__)
pp1(resp1.__dict__)
pp1(resp1.__dict__['context_data'])

##-- context_data['cl'] , QuerySet :
pp1(resp1.context_data['cl'].__dict__)
qs1 = resp1.context_data['cl'].queryset
rl1 = resp1.context_data['cl'].result_list
for ii in qs1: print(ii.name, ii.ipv4address, ii.ref, sep="  ,  ")   ##-OR: for ii in resp1.__dict__['context_data']['cl'].queryset: print(ii.name, ii.ipv4address, ii.ref, sep="  ,
for ii in rl1: print(ii.name, ii.ipv4address, ii.ref, sep="  ,  ")   ##-OR: for ii in resp1.__dict__['context_data']['cl'].result_list: print(ii.name, ii.ipv4address, ii.ref, sep="
##________________________________________  ___________________________


##------ view.model query directly, OK1:
from core.views.infoblox import ARecordView
arec1 = ARecordView()
arecsAll = arec1.model.objects.all()
arecsAll
type (arecsAll)    ##-- django.db.models.query.QuerySet
for ii in arecsAll: print(ii)
for ii in arecsAll: print(ii.__dict__)
for ii in arecsAll: print(ii.name, ii.ref, ii.view_id, ii.ipv4address, sep="  ::  ")
#-more-infs/introsp/...:
sorted(arec1.__dir__())
sorted(arecsAll.__dir__())
arec1.list_display     ##--  ['view', 'name', 'ipv4address']

##------ login-credentials-ok:
In [1]: from django.test import Client, TestCase
In [2]: c=Client()
In [3]: c.login(username="u11", password="u11")
Out[3]: True
In [4]: resp1 = c.get("/infoblox/records/a/")
In [5]: print("-- resp1.status_code :: ", resp1.status_code)
-- resp1.status_code ::  200
In [6]: print("-- resp1.content---------------\n :: ", resp1.content)
... OK !

##------ login-dummy! dummy-user + result_list query per client-response:
from django.test import Client, TestCase
from django.contrib.auth.models import User
userXX = User.objects.get_or_create(username="dummy-user-xx")[0]
i#-ok1:  userXX = User.objects.create_user("dummy-user-xx")
c = Client()
from django.conf import settings ;
c.force_login(user=userXX, backend=settings.AUTHENTICATION_BACKENDS[0])
resp1 = c.get("/infoblox/records/a/", follow=True)
print("-- resp1.status_code :: ", resp1.status_code)
print("-- resp1.content---------------\n :: ", resp1.content)
##-- results-query!! :
import pprint
pprint(resp1.context_data)
pprint.pprint(resp2.__dict__['context_data'], indent=4, width=120, sort_dicts=True)
results = resp1.context_data['cl'].result_list
for ii in results: print(ii.name, ii.ref, ii.view, ii.ipv4address, sep="  ::  ")

##---- test.Client in djprj1:
in setings.py:  ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']
djprj1 : python manage.py shell
In [1]: from django.test import Client, TestCase
In [2]: c = Client()
In [4]: resp1 = c.get("/ix1", follow=True)
In [5]: print("-- resp1.status_code :: ", resp1.status_code)
In [6]: print("-- resp1.content---------------\n :: ", resp1.content)
In [7]: import pprint
In [8]: pprint.pprint(resp1.__dir__())
In [9]: sorted(resp1.__dict__)
In [13]: resp1.context
In [14]: resp1.context_data
In [16]: pprint.pprint(resp1.context_data, indent=4, width=120, sort_dicts=True)
        # pprint.pprint(resp2.__dict__['context_data'], indent=4, width=120, sort_dicts=True)
#- object_list :
In [17]: resp1.context_data['object_list']
In [18]: resp1.context_data['object_list'][1].__dict__
In [19]: resp1.context_data['object_list'][0].ipv4address
In [32]: resp1.context_data['arecord_list'][0].__dict__
In [36]: resp1.context_data['arecord_list'][0].ipv4address

"""
