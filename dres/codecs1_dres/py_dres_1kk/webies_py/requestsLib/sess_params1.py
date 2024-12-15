'''
    see/based:  https://requests.readthedocs.io/en/latest/user/advanced/#session-objects
    - incl-all-API-of-requests  :  A Session object has all the methods of the main Requests API.
    - persistent-params-throught-user-session  :  Session object allows you to persist certain parameters across requests. It also persists cookies across all requests made from the Session instance, 
    - DIFF:  session.params = ... (prsistent through all calls by the same session-object)  <--->  params=... (in URL-call): valid ONLY for this url-call! :
'''


import requests
import pprint

def req_sess_params1():
    print("\n====================  session + data-/params-added-to-sess: =============")
    s = requests.Session()
    s.params = {'key1': 'value1', 'key2': 'value2'}
    params1 = {'k1': 'v1', 'k2': 'v2'}
    nts11 =""""-- DIFF: Session.params={...} (sesseion-persistent)  <--->  URL-call: params=... (ONLY-for-this-call!):
    here the URL-params are ONLY valid for this call, even if it is called by the session-object! 
    but the Session.params setting above are session-valid/-persistent for the whole session, incl. further calls by the same session-obejct !"""
    print(nts11)
    print("\n-- get1--call-with-params-in-URL_call: as params=... inside URL-Call: ----------")
    r = s.get('https://httpbin.org/get', params=params1)
    print(r.text)
    print("\n-- get1--call-with-params-in-URL: same as before, but url-integrated-syntax: -----")
    r = s.get('https://httpbin.org/get?k11=v11&k22=v22')
    print(r.text)
    print("\n-- get1--call-withOUT-URL-params--even-with the same session-obj: check args-items, only session-params are persistent through session-calls: -----")
    r = s.get('https://httpbin.org/get')
    print(r.text)
    print("-- sess.cookies: ", s.cookies.items())
    print("-- resp.cookies: ", r.cookies.items())

def req_sess_headers1():
    s = requests.Session()
    print("\n====================  session-headers-add-data: =================")
    nts11="""-- Any dictionaries that you pass to a request method (eg here .get) will be merged with the session-level values that are set.
    The method-level parameters override session parameters (during being merged with them)!
    BUT method-level parameters will not be persisted across requests, even if using a session!
    TO omit/delete a session-level-key you can e.g. just set that key’s value to None in the method-level parameter. It will automatically be omitted.
    """
    print(nts11)
    s.headers.update({"h1":"v1", "h2":"v2"})   ##-- session-level values
    print("\n-- sess.headers: ", s.headers)
    r = s.get('https://httpbin.org/headers', headers={'h1': 'url-v11', 'url-h2': 'v22'})  ##--request method-level values : merged + overwrite with sesseion-values
    print("\n-- sess.headers: ", s.headers)
    print("\n-- resp.headers: ", r.headers)
    print(r.text)
    print("-- BUT method-level parameters will not be persisted across requests, even if using a session! check h1 here:")
    r = s.get('https://httpbin.org/headers')  ##--request method-level values : merged + overwrite with sesseion-values
    print(r.text)

def main1():
    req_sess_params1()
    req_sess_headers1()

if __name__ == "__main__": main1()
