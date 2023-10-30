## pydoc requests
## https://realpython.com/python-requests/

import requests
#import requests.api

resp1 = requests.get('https://api.github.com')
# resp1.encoding = 'utf-8'
# print (resp1.text)
# print (resp1.content)
# for k1 in sorted(resp1.text.keys()): print (k1)
# dic1 = dict(ast.literal_eval(resp1.text))
# dic1 = eval(resp1.text)  ##--II-OK-also! universal-way for formatted-str-->dict !
dic1 = resp1.json()
# print (type(dic1))
for k1 in dic1.keys():  print (f"{k1:<40}  ==  {dic1[k1]}")
