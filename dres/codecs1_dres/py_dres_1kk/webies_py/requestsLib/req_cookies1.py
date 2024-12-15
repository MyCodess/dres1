'''
    see/based:  https://requests.readthedocs.io/en/latest/user/advanced/#session-objects
    - A Session object has all the methods of the main Requests API.
    - connection-poolingi-TCP  :  Session will use urllib3’s connection pooling. So if you’re making several requests to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase
    ---
    - DIFF : session-cookies  (RAM/memory/non-persistent)  <--->  response-/server-/browser-/...cookies as to be saved/persistent !
'''


import requests
import pprint

def req_cooky1():
    print("\n====================  cookies-1: ====================")
    print("To send your own cookies to the server, you can use the cookies parameter:")
    url1 = "https://httpbin.org/cookies"
    cooky1 = {"c1": "v1", "c2": "v2"}
    resp1 = requests.get(url1, cookies=cooky1)
    pprint.pp(resp1.json())
    print(resp1.request.path_url)
    print("\n------ resp.text: -----")
    print(resp1.text)

def req_cookyijar1():
    print("\n====================  RequestsCookieJar-1: ====================")
    print("Cookies are returned in a RequestsCookieJar, which acts like a dict but also offers a more complete interface,")
    jar1 = requests.cookies.RequestsCookieJar()
    jar1.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    jar1.set('tasty_cookie2', 'yum2', domain='httpbin.org', path='/cookies')
    jar1.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')  ##--!-this cooky will NOT be sent for the url1 !
    url1 = 'https://httpbin.org/cookies'
    resp1 = requests.get(url1, cookies=jar1)
    print(resp1.text)

def req_sess_cooky1():
    print("\n====================  session-get1 -empty-cookies: ==============")
    s = requests.Session()
    r = s.get('https://httpbin.org/cookies')
    print(r.text)
    print("\n====================  session-get1 + set-sess-cookies : =========")
    s.cookies.set("sessc1", "v1")  ##--here this app is setting the cooky and sending to the server!
    s.cookies.set("sessc2", "v2")
    s.get('https://httpbin.org/cookies/set/sesscooky1/v1')  ##--just a hhtpbin.org-convention to ask its server to set a cooky and return back in its reponse! per URl, here the server is setting the cooky! just per httpbin.org-conv ! not-std !
    s.get('https://httpbin.org/cookies/set/sesscooky2/v2')
    r = s.get('https://httpbin.org/cookies')
    print(r.text)
    print("\n-- resp.cookies: ", r.cookies.items())
    print("\n-- sess.cookies: ", s.cookies.items())
    print("\n-- resp.headers: ", r.headers)
    print("\n-- sess.headers: ", s.headers)


def main1():
    req_cooky1()
    req_cookyijar1()
    req_sess_cooky1()

if __name__ == "__main__": main1()
