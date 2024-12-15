"""
    https://requests.readthedocs.io/en/latest/user/quickstart/
    - see also for all http-verbs (get,post,put,...):  https://requests.readthedocs.io/en/latest/user/advanced/#http-verbs
"""

import requests
import pprint


def req_post1():
    print("\n====================  post-1: ====================")
    url1 = "https://httpbin.org/post?p1=v1&p2=v2"  ##-- also url-args can be sent with post! plus later the form-data !
    data1 = {"d1": "aa", "d2": "bb"}
    print("-- BOTH url-args + form/data-params together can be used with .post ! but data1 goes into form={...} und url-params into args !")
    resp1 = requests.post(url1, data=data1, timeout=(3.1,7) )
    print("\n------ resp.text: -----")
    print(resp1.text)
    print("\n------ resp.header: -----")
    pprint.pp(dict(resp1.headers), indent=4)
    print("\n-- resp1.encoding  :  ", resp1.encoding)
    print("\n-- resp1.request.path_url  :  ", resp1.request.path_url)
    print("\n------ json-builtin-decoder os requests : -----")
    pprint.pp(resp1.json())


def main1():
    req_post1()

if __name__ == "__main__": main1()
