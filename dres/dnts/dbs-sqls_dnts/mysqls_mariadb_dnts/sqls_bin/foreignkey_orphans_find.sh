#!/bin/sh
# find-fk-conflicts.sh
# (c) 2004 Turadg Aleahmad, licensed under GPL
# USAGE: $0   child_table child_key parent_table parent_key
#    eg: $0   child1  col1_id   parent1  id
# see http://dev.mysql.com/doc/refman/5.5/en/innodb-foreign-key-constraints.html

# NOTE: set this
db="db1"
dbuser=dbu1

child_table=$1
child_key=$2
parent_table=$3
parent_key=$4

query="SELECT $child_table.$child_key FROM $child_table LEFT JOIN $parent_table
ON ( $child_table.$child_key = $parent_table.$parent_key)
WHERE $child_table.$child_key IS NOT NULL AND $parent_table.$parent_key IS NULL; "

mysql --verbose -u $dbuser -e "$query" $db

