"""
    https://requests.readthedocs.io/en/latest/user/quickstart/
    - see also for all http-verbs (get,post,put,...):  https://requests.readthedocs.io/en/latest/user/advanced/#http-verbs
"""

import requests
import pprint

def req_get1():
    print("\n====================  get-1: ====================")
    url1 = "https://httpbin.org/get?p1=v1&p2=v2"
    data1 = {"d1": "aa", "d2": "bb"}
    print("-- BOTH url-args + params together can be uses as args for get ! check the resp.url !")
    resp1 = requests.get(url1, params=data1, timeout=(3.1,7) )
    print("\n------ resp.text: ----- (resp.text is str, but resp.content iy byte type! check also resp.raw for streaming!)")
    print(resp1.text)
    print("\n------ resp.header: -----")
    pprint.pp(dict(resp1.headers), indent=4)
    print("\n-- resp1.encoding  :  ", resp1.encoding)
    print("\n-- resp1.request.path_url  :  ", resp1.request.path_url)
    print("\n------ resp.cookies: -----")
    print(resp1.cookies.items())

def main1():
    req_get1()

if __name__ == "__main__": main1()
