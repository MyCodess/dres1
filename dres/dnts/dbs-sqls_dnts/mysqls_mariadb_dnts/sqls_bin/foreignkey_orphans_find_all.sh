#!/bin/sh

# check_constraints.sh
# --------------------
# Check foreign key contraints on MySQL database. on ALL TBALES os a database!!
# 
# Written by Frank Vanderhallen, licensed under GPL. 
# see http://dev.mysql.com/doc/refman/5.5/en/innodb-foreign-key-constraints.html

if [ -z "$1" ]
then
	echo "\nUsage:\n\t $0 [-h <host>] [-u user] [-p <passwd>] <database> \n"
	exit
fi

CONSTRAINTS=`mysqldump $* | grep "CREATE\|CONSTRAINT" | sed 's/ /+/g'`

for c in $CONSTRAINTS
do
	if [ "`echo $c | cut -d '+' -f 3`" = "CONSTRAINT" ]
	then
		CONSTRAINT=`echo $c | cut -d '+' -f 4 | tr -d '\`'`
		CHILD_KEY=`echo $c | cut -d '+' -f 7 | tr -d '()\`,'`
		PARENT_TABLE=`echo $c | cut -d '+' -f 9 | tr -d '\`'`
		PARENT_KEY=`echo $c | cut -d '+' -f 10 | tr -d '()\`,'`
		QUERY="select c.$CHILD_KEY from $CHILD_TABLE as c left join $PARENT_TABLE as p on p.$PARENT_KEY=c.$CHILD_KEY where c.$CHILD_KEY is not null and p.$PARENT_KEY is null;"
		echo "Checking table '$CHILD_TABLE' constraint '$CONSTRAINT'"
		#mysql --verbose $* -e "$QUERY"
		mysql  $* -e "$QUERY"
	else
		CHILD_TABLE=`echo $c | cut -d '+' -f 3`
	fi
done

