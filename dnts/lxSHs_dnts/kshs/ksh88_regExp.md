___________ RegExp-KSH88-Shell / patternMatching-KSH88
##________________________________________  ___________________________


#####  ==========  notes/exp ksh88-regExp:
- ranges must be in [] as in [0-9]
	- eg: VAX/VMS operating system end in a semicolon followed by a version number,
	  e.g., fred.bob;23. Listing them:	ll -d  *\;[1-9]*([0-9])
- all files starting with one/more f :	#ll -d +(f)*
- all files starting wit ff or ts : 	#ll -d @(ff|ts)*
- all starting with o but not old : 	#ll -d o!(ld)
- files end in .el with an optional c :	#ll -d *.el?(c)
- !(*.c|*.h|Makefile|README)	: matches anything that does not match any of the four possibilities.
- 
##________________________________________  ___________________________


#####  ==========  Ore-ksh88-ch.04.3:
Table 4.2: Regular Expression Operators Operator Meaning 
*(exp) 0 or more occurrences of exp 
+(exp) 1 or more occurrences of exp 
?(exp) 0 or 1 occurrences of exp 
@(exp1|exp2|...) exp1 or exp2 or... 
!(exp) Anything that doesn't match exp [8]
[8] Actually, !(exp) is not a regular expression operator by the standard technical definition, though it is a handy extension.
Table 4.3: Regular Expression Operator Examples Expression Matches 
x x 
*(x) Null string, x, xx, xxx, ... 
+(x) x, xx, xxx, ... 
?(x) Null string, x 
!(x) Any string except x 
@(x) x (see below) 
##________________________________________  ___________________________


#####  ==========  ksh versus egrep/awk:
.3.2.2 Korn shell versus awk/egrep regular expressions
Table 4.4 is an expansion of Table 4.2: the middle column shows the equivalents in awk/egrep of the shell's regular expression operators. 
Table 4.4: Shell Versus egrep/awk Regular Expression Operators Korn Shell egrep/awk Meaning 
*(exp) exp* 0 or more occurrences of exp 
+(exp) exp+ 1 or more occurrences of exp 
?(exp) exp? 0 or 1 occurrences of exp 
@(exp1|exp2|...) exp1|exp2|... exp1 or exp2 or... 
!(exp) (none) Anything that doesn't match exp 
These equivalents are close but not quite exact. Actually, an exp within any of the Korn shell operators can be a series of exp1|exp2|... alternates. But because the shell would interpret an expression like dave|fred|bob as a pipeline of commands, you must use @(dave|fred|bob) for alternates by themselves.
For example:
@(dave|fred|bob) matches dave, fred, or bob.
*(dave|fred|bob) means, "0 or more occurrences of dave, fred, or bob". This expression matches strings like the null string, dave, davedave, fred, bobfred, bobbobdavefredbobfred, etc. 
+(dave|fred|bob) matches any of the above except the null string.
?(dave|fred|bob) matches the null string, dave, fred, or bob.
!(dave|fred|bob) matches anything except dave, fred, or bob.
It is worth re-emphasizing that shell regular expressions can still contain standard shell wildcards. Thus, the shell wildcard ? (match any single character) is the equivalent to . in egrep or awk, and the shell's character set operator [...] is the same as in those utilities. [9] For example, the expression +([0-9]) matches a number, i.e., one or more digits. The shell wildcard character * is equivalent to the shell regular expression * (?).
[9] And, for that matter, the same as in grep, sed, ed, vi, etc.
A few egrep and awk regexp operators do not have equivalents in the Korn shell. These include:
The beginning- and end-of-line operators ^ and $.
The beginning- and end-of-word operators \< and \>.
Repeat factors like \{N \} and \{M , N \}.
The first two pairs are hardly necessary, since the Korn shell doesn't normally operate on text files and does parse strings into words itself.
