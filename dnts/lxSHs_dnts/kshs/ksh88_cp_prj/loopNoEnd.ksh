#!/bin/ksh -m

rm a1.out
exec 1>| a1.out

typeset -xi ii=0;

while : ; do (( ii+=1 )) ; print - "--- $ii : $( date ) ======="; sleep 3 ; done 
