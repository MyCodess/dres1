
#!/bin/sh

# check_constraints.sh
# --------------------
# Check foreign key contraints on MySQL database.
# Modified foreign key dependency checker script posted by Frank Vanderhallen.
# This script supports composite keys.
#
# Written by Frank Vanderhallen and modified by Lupus Arctos, licensed under GPL.
# http://dev.mysql.com/doc/refman/5.5/en/innodb-foreign-key-constraints.html



if [ -z "$1" ]
then
echo "\nUsage:\n\t./`uname $0` <database> [-h <host>] [-u user] [-p <passwd>]\n"
exit
fi

CONSTRAINTS=`mysqldump $* | grep "CREATE\|CONSTRAINT" | sed 's/, /,/g' | sed 's/ /+/g'`

for c in $CONSTRAINTS
do
if [ "`echo $c | cut -d '+' -f 3`" = "CONSTRAINT" ]
then

CONSTRAINT=`echo $c | cut -d '+' -f 4 | tr -d '\`'`
CHILD_KEY=`echo $c | cut -d '+' -f 7 | tr -d '()\`'`
PARENT_TABLE=`echo $c | cut -d '+' -f 9 | tr -d '\`'`
PARENT_KEY=`echo $c | cut -d '+' -f 10 | tr -d '()\`'`

declare -a PARENT_KEYS=($(echo $PARENT_KEY|sed 's/,/ /g'))
declare -a CHILD_KEYS=($(echo $CHILD_KEY|sed 's/,/ /g'))

let PARENT_KEYS_LASTIDX=${#PARENT_KEYS[@]}-1
let CHILD_KEYS_LASTIDX=${#CHILD_KEYS[@]}-1

JOINON=
CHILD_TABLE_KEY=
for k in `seq 0 $PARENT_KEYS_LASTIDX`; do
 JOINON=`echo $JOINON p.${PARENT_KEYS[k]}=c.${CHILD_KEYS[k]}`
 CHILD_TABLE_KEY=`echo $CHILD_TABLE_KEY c.${CHILD_KEYS[k]}`
 if [ $k != $PARENT_KEYS_LASTIDX ]; then
 JOINON=`echo $JOINON and`
 CHILD_TABLE_KEY=`echo $CHILD_TABLE_KEY,`
 fi
 if [ $k == 0 ]; then
 CHILD_WHEN=`echo p.${PARENT_KEYS[k]} is not null`
 PARENT_WHEN=`echo c.${CHILD_KEYS[k]} is null`
 fi
done

QUERY="select $CHILD_TABLE_KEY from $CHILD_TABLE as c left join $PARENT_TABLE as p on $JOINON where $CHILD_WHEN and $PARENT_WHEN;"
echo "Checking table '$CHILD_TABLE' constraint '$CONSTRAINT'"
#mysql -v $* -e "$QUERY"
mysql $* -e "$QUERY"
else
CHILD_TABLE=`echo $c | cut -d '+' -f 3`
fi
done
