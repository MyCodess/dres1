#!/usr/bin/env  python3

#################### fistures :  #############################################
l1=list(range(0,5))
tup1=tuple(range(20,25))
dic1={x: x.lower()  +"1" for x in "ABCDE" }
##__/OR:    dic1={x: x**2 for x in range(0,5) }
##__prints:  print(l1) ; print(tup1) ; print(dic1) ; print ("-" * 20)

##############################################################################
print ("-" * 20)
def f1(p1, *p2):
    print (p1, p2)
    print (p1, *p2)
    print ("---")
f1("par1", 11,12,13,14)
f1("par1", l1)
f1("par1", *l1)
print ("-" * 20)
