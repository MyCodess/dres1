#!/usr/bin/env  python

#####  ==========  itertools.chain() :
from itertools  import chain
l1=list(range(10,15))
l2=list(range(20,25))
l3=list(range(30,35))
tup1=tuple(range(20,25))
dic1={x: (x*3).upper() for x in "abcdef"}
set1=set(dic1.values())
dicList1 = {}
for xx in list("dins"): dicList1[xx] = list(range(ord(xx), ord(xx)+3))

iters1=(l1, l3)
print("----: org-lists:")
for xx in l1,l3: print(xx)           ##--same-as:   for xx in iters1: print(xx)
print("----: chain-lists:")
for xx in chain(l1,l3): print(xx)    ##--same-as:   for xx in chain(*iters1): print(xx)
print("----: concat-lists: roughly same as chain()")
for xx in l1+l3: print(xx)
print("----: iter-manually-lists: roughly same as chain() based on RefDocs-StdLibs")
for xx in  l1,l3:       ##--same as   iters1:
    for item1 in xx:
        print(item1)
##________________________________________  ___________________________


