#!/usr/bin/env  python3
""" loops-nested, break, continue, ...."""

##-------------------------------------------------
print("="*40)
print("========== nts: break/continue-in-nested-loops: breaks/continues ONLY the inner-most-loop!! and goes back to the OUTER-loop! for continue just replace break with it! :")
for ii in 1,2,3:
    print ("-",ii);
    for jj in 4,5,6:
        print ("--",jj)
        break
    print ("-pos-for2-jj-break")
print ("pos-for1")
print("="*40)

##-------------------------------------------------

print("=========== break-and-else-part:  after break, the else-part will NOT be executed!: =========")
ii=2
while ii<8:
    print(f"-- {ii}")
    if ii == 4:
        break
    ii +=1
else:
    print(f"--els-- {ii}")

print(f"================== {ii}=================")


