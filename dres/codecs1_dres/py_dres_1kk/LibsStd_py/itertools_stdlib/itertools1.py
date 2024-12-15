#!/usr/bin/env  python
##--- itertools StdLib: !! see the TABLE in  pyRefDocs-StdLibs--library.pdf for itertools / FUNCTIONAL PROGRAMMING MODULES !!
##=========================================================================

#####  ==========  data1 :
l1=list(range(10,15))
l2=list(range(20,25))
l3=list(range(30,35))
tup1=tuple(range(20,25))
dic1={x: (x*3).upper() for x in "abcdef"}
set1=set(dic1.values())
dicList1 = {}
for xx in list("dins"): dicList1[xx] = list(range(ord(xx), ord(xx)+3))
##________________________________________  ___________________________



#################  Infinite iterators of itertools StdLib: ###########################################
import itertools
print("===============================================================")

#####  ==========  itertools.count(start, step) ,an Infinite iterator :
def count1(start1, step1):
    print ("\n--- itertools.count(start, step) returns an endless loop-var-iterator: -----------")
    print ("- so never do: for ii in  count(n, m) ! is ENDLESS !")
    it11= itertools.count(start1, step1)
    print(next(it11), end=" , ")
    print(next(it11), end=" , ")
    print(next(it11), end=" , ")
    newList11 = [next(it11), next(it11), next(it11)]
    print (newList11)
count1 (10, 2)
##________________________________________  ___________________________


#####  ==========  itertools.cycle(start, step) ,an Infinite iterator :
def cycle1(iter1):
    print ("\n--- itertools.cycle(iterable) returns an endless loop-var-iterator: -----------")
    it11= itertools.cycle(iter1)
    newList11 = []
    for ii in range (8): newList11.append(next(it11)*2)
    print (newList11)
cycle1 ("ABC")
##________________________________________  ___________________________


#####  ==========  itertools.repeat():
def repeat1():
    print ("\n---  itertools.repeat : repeat the same ...: ------------")
    it11= itertools.repeat(10, 2)  ##--repeats 3 time the same 10 ! and then StopIteration excep !
    print(next(it11), end=" , ");  print(next(it11), end=" , ")
    ##--This-time-then StopIteration : print(next(it11), end=" , ")
    print()
repeat1()
##________________________________________  ___________________________



#################  Iterators terminating on the shortest input sequence /itertools StdLib: #############
#####  ==========  itertools.accumulate : sum/func1 of all ...:
def f1(x, y): return y-x
def accum1(iterable11, func11=None):
    print ("\n---  itertools.accumulate() : sum/func1 of all ...: ------------")
    print (iterable11 , " :  org-iterable1" )
    it11 = itertools.accumulate(iterable11, func11)
    for ii in range(len(iterable11)): print(next(it11), end=" , ")
    print()
accum1(l1)    ##--I-default-func is just sum !
accum1(l1, f1)
accum1(l1, lambda x,y : y-x)
##________________________________________  ___________________________


#####  ==========  itertools.compress
def compress1(l11, l22):
    print ("\n---  itertools.compress ...: ------------")
    it11 = itertools.compress (l11, l22)
    newList11 = []
    for ii in it11: newList11.append(ii)
    return newList11
print (compress1 ("ABCDE", [0,1,0,1,0,1,0,1]))
print (compress1 ("ABCDE", [0,1]))
##________________________________________  ___________________________

print("===============================================================")
