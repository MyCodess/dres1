#!/usr/bin/env  -S  gawk -f
#

#####  ==========  min/max-lenght of lines in <$1> :
BEGIN {print "__Sta1__" ;  min = 1000 ; max = 0 ; }
{
	if (length($0) < min) { min = length($0) }
	if (length($0) > max) { max = length($0) }
}
END{ print "min-line-lenght == "  min  "  ,max-line-length == "  max }
###________________________________________  ___________________________


############################## oneLiners-awk : ###################################################
#####  ========== oneLiners-from-awk-RefDocs-GNU :
##-- empty-lines-deleting:    awk 'NF > 0' data
##-- print lines 3 and 4 of inputfile :    awk '{if (NR >2  && NR <5) {print $0; } }'  t3   ;
##-- print lines [2-to-5] of inputfile:    awk '{if (NR >=2  && NR <=5) {print $0; } }'  t3 ;
##-- Print a sorted list of the login names of all users: awk -F: '{ print $1 }' /etc/passwd | sort
##-- Count the lines in a file: awk 'END { print NR }' data
##-- Print the even-numbered lines in the data file: awk 'NR % 2 == 0' data

###________________________________________  ___________________________
#


