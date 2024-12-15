"""
    https://requests.readthedocs.io/en/latest/user/advanced/#request-and-response-objects
    - for session-cookies-in-header see here the cookies-modules !
"""

import requests
import pprint

def req_headers_query1():
    resp = requests.get('https://www.google.com/')
    print("\n==================== access/query the headers the SERVER sent back to us: server response-header: ===============")
    pprint.pp(dict(resp.headers), indent=4)
    print("\n==================== access/query the headers the WE sent to the server:  our    requests-header: ===============")
    print("- The Response object contains all of the information returned by the server and ALSO contains the Request object you created originally.")
    pprint.pp(dict(resp.request.headers))

if __name__ == "__main__":
    req_headers_query1()
