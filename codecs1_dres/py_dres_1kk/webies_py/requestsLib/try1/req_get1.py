## pydoc requests
## https://realpython.com/python-requests/

import requests
import pprint

##--URL-test-without-login:
resp1 = requests.get('https://api.github.com')  ##-or use: httpbin.org/

print('--- nts: resp1.content is "bytes" and resp1.text is "str" ! so none of them can be directly converted to dict! but with "eval":')
print("response.content-type  :  ", type(resp1.content))
print("response.text-type     :  ", type(resp1.text))

print("\n========= using pprint to output the eval(response.text()): ==============")
pprint.pp(dict(eval(resp1.text)), indent=4, sort_dicts=True)

# resp1.encoding = 'utf-8'
# print (resp1.text)
# print (resp1.content)
# for k1 in sorted(resp1.text.keys()): print (k1)
# dic1 = dict(ast.literal_eval(resp1.text))
# dic1 = eval(resp1.text)  ##--II-OK-also! universal-way for formatted-str-->dict !
print("\n========= response.json : ============================================")
print(resp1.json())

print("\n========= response.json--formatted: ==================================")
dic1 = resp1.json()
# print (type(dic1))
for k1 in dic1.keys():  print (f"{k1:<40}  ==  {dic1[k1]}")

