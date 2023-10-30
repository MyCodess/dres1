#!/usr/bin/env  python3

#################### fixtures :  #############################################
##--str:
s1 = "abc dEf gHi Xxx yy"
s2 = "kkk MmM NNN \t-\t rst wWw zZz"
s3 = s1 + "\n" + s2
##--lists:
l1=list(range(10,15))
l2=list(range(20,25))
l3=list(range(30,35))
##--dicts,tuples,sets,...:
tup1=tuple(range(20,25))
dic1={x: (x*3).upper() for x in "abcdef"}
set1=set(dic1.values())
dicList1 = {}
for xx in list("dins"): dicList1[xx] = list(range(ord(xx), ord(xx)+3))
##__  dic1={x: x**2 for x in range(0,5) }
##__  print ("-" * 20) ; print(s3) ; print(l1) ; print(tup1) ; print(dic1) ; print(set1) ; print ("-" * 20) ;

##-------- Dicts-beautiy-printout, one-pair-per-line :
def printDictBeauty1(dict1):
    print ("------------------------------------")
    for k1 in sorted(dict1.keys()):
        ##--old-format-style:  print ("%15s  ==  %s" % (k1, dict1[k1]))
        print ("{:>15}  ==  {}".format(k1, dict1[k1]))
    print ("-"*30)
##---
##############################################################################

