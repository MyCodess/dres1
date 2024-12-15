"""
    Requests: Django-App login + query
    incl. csrftoken cookies + session-mgm,...
"""

import requests
import pprint
from getpass import getpass
login_url1 = "http://localhost:8000/auth/login/"
request_url1 = "http://localhost:8000/infoblox/records/aaaa/"

sess1 = requests.Session()
csrf_tok1 = sess1.get(login_url1).cookies['csrftoken']
form_fields1 = {'username': "u11", "password": "u11"}
header1 = {'X-CSRFToken': csrf_tok1}
cookies1 = {'csrftoken': csrf_tok1}

print("\n======== resp0-login: ========")
resp0 = sess1.post(login_url1, data=form_fields1, headers=header1, cookies=cookies1, timeout=(3.1,7) )
print("resp0-status:  ", resp0.status_code)
#pprint.pp(resp0.__dict__)
#_ print(type(resp0.cookies))
#pprint.pp(resp0.cookies.items())
pprint.pp(sess1.cookies.items)

print("\n======== resp1-query1: =======")
resp0 = sess1.post(login_url1, data=form_fields1, headers=header1, cookies=cookies1)
resp1 = sess1.get(request_url1)
print("resp1-status:  ", resp1.status_code)
#_ #resp1 = requests.post(request_url1, cookies=resp0.cookies)
##__  pprint.pp(resp1.__dict__)
print("\n- resp1.cookies.items() : ", resp1.cookies.items())
pprint.pp(resp1.cookies.items())
print("\n- sess1.cookies.items : ")
pprint.pp(sess1.cookies.items(), indent=4)
##__more:  pprint.pp(sess1.cookies.items)
##__more:  print("\n- sess1.cookies.keys() :")
##__more:  pprint.pp(sess1.cookies.keys())
##__more:  pprint.pp(sess1.cookies.values())
##__more:  pprint.pp(sess1.cookies.get_dict())
#_ print(resp0.text)
