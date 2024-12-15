#!/usr/bin/env  python3
import sys

print ("----------\n", __file__ , __package__, __name__)
print ("__d12_f12_imported_now__")
print("- sys-path in :", __name__)
for ii in range(len(sys.path)): print(sys.path[ii])

i1=5
l1=[]
def f1():
    print ("__test1-func")

##__  print (i11 + "--from-f1")
