#!/usr/bin/env  python3
""" introspects_inquirys: locals(), globals(), dir(), obj.__dict__ , ...  """
#################### fixtures :  #############################################
s1 = "abc dEf gHi Xxx yy"
s2 = "kkk MmM NNN \t-\t rst wWw zZz"
l1=list(range(0,5))
l2=list(range(10,20))
tup1=tuple(range(20,25))
dic1={x: (x*3).upper() for x in "abcdef"}
set1=set(dic1.values())
##__  dic1={x: x**2 for x in range(0,5) }
##__  print ("-" * 20) ; print(s3) ; print(l1) ; print(tup1) ; print(dic1) ; print(set1) ; print ("-" * 20) ;
##---
##-------- Dicts-beautiy-printout, one-pair-per-line :
def printDictBeauty1(dict1):
    print ("------------------------------------")
    for k1 in sorted(dict1.keys()):
        ##--old-format-style:  print ("%15s  ==  %s" % (k1, dict1[k1]))
        print ("{:>15}  ==  {}".format(k1, dict1[k1]))
    print ("-"*30)
##---
##############################################################################
print("\n----------  dir()    :\n" ,  sorted(dir()))
print("\n---------- locals()  :\n" ,  sorted(locals().keys()))
print("\n---------- globals() :\n" ,  sorted(globals().keys()))
print("\n----------  locals() dict -str.format-output :")
ii=0;  ## loop-var MU&ST be pre-defined, otherwise: RuntimeError: dictionary changed size during iteration !
for ii in sorted(locals()):  print ("{:20s}  ==  {}".format(ii, locals()[ii]))
##__  print("\n----------  locals() dict :"); printDictBeauty1(locals());
