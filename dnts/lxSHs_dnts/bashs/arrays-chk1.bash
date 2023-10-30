#!/bin/bash
##############-- Arrays-Testings---------
##--II- bash-indexed-arrays-test  :  see man bash  : +/^\s*Arrays\s*$
# explicit and implicit indexing may NOT be mixed!! otherwise index.auto.incrementing overwrites older values, because it starts obviously always with zero!!
# Referencing an array variable without a subscript is equivalent to referencing the array with a subscript of 0
# destroy: The unset builtin is used to destroy arrays. unset name[subscript] destroys the array element.  unset name,  where name is an array, or unset name[subscript], where subscript is * or @, removes the entire array.
##################################


echo
echo "========= array.auto.indexing + compound.assignment: ============"
##-I- auto.decleration also possible:  man: An  indexed  array  is  created  automatically if any variable is assigned to using the syntax name[sub-script]=value.
declare -a a2     ##-I- is optional, but do it!! ; man: To explicitly declare an indexed array, use declare -a name
a2=(aa bb cc dd)
echo "=== ${a2[2]}"
echo "=== ${a2[@]}"
echo "=== ${#a2[*]} Elements:  ${a2[*]}"

echo
echo "========= array.explicit.indexing: ============"
declare -a a3
a3[0]=v0
a3[1]=v1
a3[3]=v3       ##-I- index 2 just not-existing
echo "=== ${a3[1]}  --index.2-not-existing:-- ${a3[2]}"
echo "=== ${a3[@]}"
echo "=== ${#a3[*]} Elements:  ${a3[*]}"


##############
echo
echo "========= associative-arrays: ============"
##-I- declaration-ass.arrays:  man: Associative arrays are created using declare -A name
declare -A as1
as1[key0]=value0
as1[key1]=value1
as1[key2]=value2
echo "=== ${as1[key1]}"
echo "=== ${as1[@]}"
echo "=== ${#as1[*]} Elements:  ${as1[*]}"
echo

