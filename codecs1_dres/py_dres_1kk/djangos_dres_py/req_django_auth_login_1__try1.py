## pydoc requests
## https://realpython.com/python-requests/

import requests
import pprint
from getpass import getpass

##--URL-test-without-login:  resp1 = requests.get('https://api.github.com')  ##-or use: httpbin.org/
##__ resp0 = requests.get("http://localhost:8000/auth/login/", auth=("u11", "u11"))   ##--OR interactive-PW-query with:  auth=("u11", getpass())
#_ resp0 = requests.get("http://localhost:8000/infoblox/records/aaaa/", auth=("u11", "u11"))   ##--OR interactive-PW-query with:  auth=("u11", getpass())
#_ print("login-status:  ", resp0.status_code)

##__  resp1 = requests.get("http://localhost:8000/infoblox/records/aaaa/")
login_url1 = "http://localhost:8000/auth/login/"
request_url1 = "http://localhost:8000/infoblox/records/aaaa/"

sess1 = requests.Session()
sess1.auth = ("u11", "u11")
resp0 = sess1.post(login_url1, {'username': "u11", "password": "u11"})
pprint.pp(resp0.__dict__)
print("__cookies-k:  ", sess1.cookies.keys())
csrftoken1 = sess1.cookies['csrftoken']
#sess1.get("http://localhost:8000/auth/login/")  ##__ , auth=("u11", "u11"))
##__ resp1 = sess1.get("http://localhost:8000/auth/login/")
#_ resp0 = sess1.post(login_url1, {'username': "u11", "password": "u11"})
resp0 = sess1.post(login_url1, {'username': "u11", "password": "u11", 'csrfmiddlewaretoken': csrftoken1})
print("resp0-status:  ", resp0.status_code)
print("resp0:  ", resp0.text)
#_ resp1 = sess1.get("http://localhost:8000/infoblox/records/aaaa/")  ##__  , auth=sess1.auth)
#_ print("resp1-status:  ", resp1.status_code)

#_  print('--- nts: resp1.content is "bytes" and resp1.text is "str" ! so none of them can be directly converted to dict! but with "eval":')
#_  print("response.content-type  :  ", type(resp1.content))
#_  print("response.text-type     :  ", type(resp1.text))

#print(resp0.text)
#_print(resp1.text)
#pprint.pp(dict(eval(resp1.text)), indent=4, sort_dicts=True)
