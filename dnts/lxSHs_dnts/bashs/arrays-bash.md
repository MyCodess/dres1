___________________________ bash-arrays-dnts : ____________________________________________________
##________________________________________  ___________________________


#####  ==========  ARRAYs-in-bash :

	_______:  see
	- man bash  : search.to-->  ^\s*Arrays\s*$ 
	-!! abs-guide.pdf--Chapter 27. Arrays  --> also great exp!!
	-!  devres/codesColl_devres_kk/shsColl_UxLx_devres_kk/bashs  +  devres/codesColl_devres/shsColl_UxLx_devres/bashs

	_______:  unsetting/destroying arrays:
	"unset" builtin is used to destroy arrays. unset name[subscript] destroys the array element.
	"unset a1", or unset a1[*], or  unset a1[@] removes the entire array.

	_______:  declaring/initializing  arrays:
	- arrays do NOT require explicit declarations, but better to do it!
	- explicit declarations with declare/local/readonly -a (indexed-array) bzw. -A (associative-array):   declare -a a1; /OR declare -a a1=(11 22 33 44 bb gg tt) ; echo ${a1[5]}
	- without explicit pre-declarations, just do assignments to whole array:    a2=( zero one two three four )
	- without explicit pre-declarations, just do assignments to indiviual (also NON-consequent-) elements:  a1[2]="aa"   a1[5]="bb" ##-so, a1[0] ,1,3,4 are just not set!
	  Contents of uninitialized array variable print blank (null variable).
	- DIFF:   declare  -a  (index-array)   <-->    declare  -A  (associative-array)
	- declaraing arrays also possible with:   declare/local/readonly -a bzw. -A ;
	- from stdin/file with read:  read  -a a5  bzw. read  -a a5 <t1.txt bzw. othe delimiters: read -d E -a a5 <t1.txt  #-ONLY ONE char is allowed as delimeter for "-d"

	_______:  setting/assigning-values to arrays and array elements:
	-! Array members need not be consecutive or contiguous. Contents of uninitialized array variable print blank (null variable).A
	--- entire-/full-array-settings:
		- a2=(aa bb cc dd)  ;  echo "${a2[2]} , ${a2[@]} , ${a2[*]} , ${#a2[*]}"
		- area2=( zero one two three four )  ;   echo ${area2[1]}  --> one
		-! a3=([17]=seventeen [24]=twenty-four)  ##--rest are undefined!
		-! stdin/file-based assignment/setting:  read  -a a5  bzw. read  -a a5 <t1.txt bzw. othe delimiters: read -d E -a a5 <t1.txt  #-ONLY ONE char is allowed as delimeter for "-d"
		-!!  base64_charset=( {A..Z} {a..z} {0..9} + / = )
			which is same as base64_charset=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 + / =)
			is using  "extended brace expansion"!  see eg ouput of:   echo {A..Z} ;  echo {2..14} 
	--- elements-settings:
		- a1[2]=bb ;
		-! a3=([17]=seventeen [24]=twenty-four)
		- math-/expr-setting:   a1[2]=$(( 2+3 ))  bzw.  area[6]=$(( ${area[11]} + ${area[51]} ))    #-bzw.  area[6]=`expr ${area[11]} + ${area[51]}`

	_______:  querying/dereferencing arrays and array-elements: 
	- ${a1[xx]} ,so use curly-bracket-notation!
	-! Array members need not be consecutive or contiguous.; so a1[2]=aa  a1[5]=bb is OK; the elements inbetween are just not set! (usefull in spreedsheet-processing/excel-imports/tab-imports/....)
	-! explicit and implicit indexing may NOT be mixed!! otherwise index.auto.incrementing overwrites older values, because it starts obviously always with zero!!
	-! dereferencing an array variable without a subscript is equivalent to referencing the array with a subscript of [0].  Array-Indexes are zero-based.
	- index/subscript "[x]" is optional for indexed-arrays!! if not specified, then bash take the next available index!  BUT associative-arrays do require the index/subscription!
	- If subscript is @ or *, the word expands to all members of the array.

	_______:  attribs-querying of arrays:
	- length of whole array / number of array-elements: ${#array[*]}   bzw.  ${#array[@]}   ##-DIFF:  echo ${#array} : Length of first element of array
	- lenght of first element (as string):  ${#array}  bzw. ${#array[0]}

	_______:  tips/usages/exp/qckys/...:
	- all of the script’s command line arguments into an array:   PARAMS1=( $* ) or PARAMS1=( "$@" )
##________________________________________  ___________________________

