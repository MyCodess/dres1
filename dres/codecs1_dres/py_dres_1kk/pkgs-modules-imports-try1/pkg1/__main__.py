##__  
print (__file__ , __package__ , __name__ , sep="  :  ")

import sys
print("--- sys.path entries in:  ", __name__ ,"\n", "\n".join("{}".format(ii) for ii in sys.path) , "\n---", sep="")
##--1ok:   for ii in range(len(sys.path)): print(sys.path[ii])

import  imports1
#__  from . import  imports1

