##---"if xxx else yyy" : else-part will NOT be evaluated at all, IF compiled-code7runtime knows that if-part is true anyway !! so "y = 2 if 2>1 else non-exiting-varrrr" ; then y ==2 !! no problem ! see udemy1-mock4-Q.1
x=2 ; y = x if x>1 else non-exiting-varrrr ; print (y) ; ##--out1: 2
##---



