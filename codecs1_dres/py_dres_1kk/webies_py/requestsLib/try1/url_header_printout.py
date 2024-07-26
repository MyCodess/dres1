"""
    usage11:  ... <url>
    prints the header of the URL out !
"""

import requests, sys

url1 = sys.argv[1]        ##--eg:  url1 = "https://jsonplaceholder.typicode.com/todos/1"
print (f"\nURL  ==  {url1}\n", "-"*50)
response = requests.get(url1)
for ii in sorted(response.headers, key = lambda s1: s1.casefold()) : print (f"{ii:30s} ==  {response.headers[ii]}")

