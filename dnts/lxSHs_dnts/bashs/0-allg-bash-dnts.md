_________ bash > 3.x _________________________________

	_______:  here refs-docs:
	-!! .../BashGuide_TLDP_Advanced/abs-guide.pdf  : "Advanced Bash-Scripting Guide" / TLDP / author: 	Mendel Cooper
	- Oreilly: Bash_QRef_Ore_0607.pdf
	- man bash
##________________________________________  ___________________________


#####  ==========  bash-itselfi/help:
	-!!! bash-help-online:
		- help  <build-in-cmd...> ; ex help declare ; help set ; LIST of all possible build-ins:  bash -c help 
		- bash --help  : a list of help topics, except build-ins,...
		- bash -c help /OR help -s : all build-in commands  --> they can be asked with: help build-in-xx
		- help variables
		- help test  --> conditionals, symbols,...
		- help set /OR bash -c "help set"  --> options, shopt
		- help let --> arithmetic signs/comparision/...
	- echo $BASH_VERSION
	- which shell am I using right now in Lx?:  /bin/ls  -l  /proc/$$/exe  : see suse-/etc/profile
	- docs: info bach ; man bash ; bash --help
##________________________________________  ___________________________


#####  ==========  tips/misc-notes:
-!! dot.sourcing and original-script-name-invoked??: ${BASH_SOURCE[0]}  #if surced, $0 is "bash",.. : see kk-script!
-!!! value of var2 is the name for var3. you want the final/last value, so the value of var3:
	 eval var1=\$$var2   ##--see: bash_abs-guide-5.0.pdf: 9.5.  indirect referencing of variables
##________________________________________  ___________________________


#####  ==========  precedence of commands: see Bash_QRef_Ore_0607.pdf--p.31 : 
- non-posix-mode: 1-aliaes 2-keywords(if,for,...) 3-functions 4-Build-ins 5-scripts/executables in PATH
- posix-mode : 1-Keywords such as if and for 2-aliases ....
so: Aliases. You can’t define an alias whose name is a shell keyword (but you can define an alias that expands to a keyword, e.g., alias aslongas=while).
	When not in POSIX mode, Bash does allow you to define an alias for a shell keyword.
##________________________________________  ___________________________


#####  ==========  Arithmetic-OPs /Mathematical-OPs in bash:

	-! see man bash --->  /^\s*Arithmetic Expansion   bzw.   /^\s*ARITHMETIC EVALUATION     bzw.    /\(\(expression
	- https://www.shell-tips.com/bash/math-arithmetic-calculation/
	---!! variations/alternatives for math-OPs (ordered in prefered-approches):
		-! nts:  
		-! the absolute recommended way for bash>3.0-ver is: $((...)) , so "Arithmetic Expansion"  !! 
		- The $((...)) notation is what is called the "Arithmetic Expansion" while the ((...)) notation is called a "Compound Command" used to evaluate an arithmetic expression in Bash.
		  The Arithmetic Expansion notation should be the preferred way unless doing an arithmetic evaluation in a Bash if statement￼, in a Bash for loop￼, or similar statements.
		$(( ))  :  "Arithmetic Expansion" : echo $(( (10+2)/(3*2) )) ;  ii=2 ; echo $(( ++ii*3/2 ))
		((  ))  :  "compound command" only for "if" statements instead of  [[ ...]], for if-arithmetic-conditions!
		let
		declares -i ...  ##--Using declare -i force a variable to be an arithmetic context only. It is like prefixing the variable assignment with the let command every time.
		printf  : also floating-point-OPs !   printf  "%.3f\n"   "$((10**3 * 2/3))e-3"
		$[...]  :  obsol/legacy/old-bashes !
		expr    :  obsol/legacy
		cmds/utils:  bc, awk 
	---
	- $(( ... ))  ##--NEW-ab-bash-4.x?? , in a standalone-cmd in cmdline even do NOT need ":" as for old-variant of $[ ... ]
	- old-obsol-variant:  $[ ... ]
	- eg:  (( (10+2)/3*2 )) ;  (( n11 = (10+2)/3 )) ; echo $n11 ;
##________________________________________  ___________________________


#####  ==========  RegExp in shell/bash:

	--->!! see "Pattern Matching" in man bash !
	-!! DIFF: default-wildcards (*,?,[..])  <--->   extended-wildcards when extglob shell option is enabled : X(pattern-list)
	-!! shell-wildcards are DIFFERENT than grep,...! (so shell * == .* in egrep, ...)
	-exp:  ll !(t1*|dd*)  (list all except t1... or dd...)
##________________________________________  ___________________________


#####  ==========  readin lines from a file/stdin/user-input/from.array/...:

	-! see: help read; 
	- raadin one line from a file:   read aa <t1.txt ; echo $aa
	- readin t1.txt line for line and do cmds:     ii=0; while read LINE  ; do (( ii++ )); echo "=== $ii : $LINE"; done  <t1.txt
	- readin-from-filedescriptor-3 instead stdin:  while read LINE <&3 ; do echo $LINE; ...; done
	- readin-from-file-into-an-array:
		read -a a2 <t1.txt ; echo ${a2[1]}             ##-- also could use another delimiter than newline with "-d <delim>"! see:  help read
		read -d EEE -a a5 < t1.txt  ; echo ${a5[*]}    ##-- using EEE sign instead of NewLine, to read the file
##________________________________________  ___________________________


#####  ==========  if/test/conditions, Relational operators, comparison, [] , [[]] ...:

	_______:  !! diff if "cmd"  <->  test/[...]  <-> [[...]]  <-->  ((...))  :see bash.Ore--5.1.4. Condition Tests:
	- [[...]] is newer and available in bash.version>2.05
	- [[...]] is identical to [...] except that word splitting and pathname expansion (as * ?...) are NOT performed on the words within the brackets.
	- test is same as [...]
- AND/OR verknuepfungen:  inside test [ ... ] do it with -a/-o , outsides test but with &&/||

	_______:  Relational operators /Comparisons:
	- String comparisons  : > = < =  != .... (!! not == but =)  :seebash.Ore--5.1.4.1 String comparisons 
	- Artithmetic Comparison:     :see bash.Ore--6.3. Integer Variables and Arithmetic 
		- either -lt -gt ... in Arithmetic Conditionals  [] ,[[]], test , /OR:
		- in ((...)) again > = < != .... as by Strings!   :see 6.3.1. Arithmetic Conditionals 
		-! so (( 2 < 3 ))  is the same as [ 2 -lt 3 ]
	-!!! Artithmetic or string comarison:
		[[ 5 > 31 ]] && echo "true- $?"  ||  echo "false- $?" 	#--> true  (string 5 is after string 3xxx)
		(( 5 > 31 )) && echo "true- $?"  ||  echo "false- $?"   #--> false (5 is less than 31)

	_______:  String-Comarison/match with regex without egrep,...:
	- if [[ "${MYFILENAME}" == *.jpg ]] .....  # see bash-cookbook--6.7Testing with Pattern Matches
	- [[ $PATH == */home/u1/bin:* ]] && echo yy || echo nn  #-I- extglob must be enabled!: shopt -s extglob
	- if [[ "$FN" == *.@(jpg|jpeg) ]]  #- with shopt -s extglob , also enabled!
	-!! see in man bash :  [[ expression ]] and then == for normal regex and even =~ with ext.regex as in sed...
	-!! see also bash-cookbook---6.7 + 6.8-Testing with Regular Expressions
	-! stronger with =~ for regex:  [[ $PATH =~ [:|^]up1/.cuue/bin[:|$] ]] && echo yy || echo nn

	_______:  exp/tips:
	[ 1 > 2 ]    && echo y  ---> y  ##is strin compare! (numerical either -gt /OR put in ((...)) an then normal <,>,...)
	(( 1 > 2 ))  && echo y  ---> N  ##numerical compare!
##________________________________________  ___________________________


#####  ==========  ENVvariables-/vars--Handling, Manipulating Vars , Var-Substitutions (${...:-...}, ...): 

	_______:  see:
	-! see man bash -->  "Parameter Expansion"
	-!! comprehensive: "Advanced Bash-Scripting Guide.pdf":   abs-guide.pdf--Chapter 10. Manipulating Variables
	-  Bash_QRef_Ore_0607.pdf
    -!! diff:    ${!XX*} bzw. ${!XX@}  (var-Names-globing)    <-->    ${!full-variable-name} (var-referencing/eval-ersatz)
       :see below for more/eg!  + man bash ,in: Parameter Expansion --> ${!prefix@}  (by / must be escaped!!)
       also see man bash:  ${!prefix*}  bzw. ${!prefix@}
    -!! listing of all variable-NAMES starting with uue: echo ${!uue@} ; /OR in-lines: echo ${!uue@} | tr ' ' '\n' ;
        -!! unset all VARS of eg prj* : unset $(echo ${!prj@})
    -!! eg:  unset all prj* vars:    unset ${!prj*}
    -!! variables-referencing without using "eval" (so "eval"-alternative for referencing VARs and Var-Names in bash-3.x):
        eg:  export aa=11 ; export bb=aa ; echo ${!bb} ---> 11
        - so Bash provides a special syntax that lets one variable indirectly reference another, eg:
        eg:  greet="hello, world" ; friendly_message=greet  (so aliasing greet-variable) ; echo ${!friendly_message} (so using the alias) ; it prints out: 	hello, world
        - obviously MUST be exported!! so "export ..." ! not only "set ..." !
        -!! eg current-file-name as var-name/counter even in a sourced-script:
            export myname_org_cu="${BASH_SOURCE[0]##*/}"  ; myname_cu=${myname_org_cu//./_} ; declare -xi ${myname_cu}=${!myname_cu:-0}
    -!! "expg"-alternative (BUT works only for prefix* eg uue* vars , and NOT for eg *uue* vars!): for all variables of name "uue*" print name===value:
        for ii1 in ${!uue*} ; do echo -e "${ii1} \t== ${!ii1}" ; done
    -!! String-Substitution in var-values:  see man bash -->  "Parameter Expansion"  ${parameter/pattern/string}
    - Dir-Name without path:  dn=${PWD##*/}  :Take the current directory name and remove the longest character string ending with /, which removes the leading pathname and leaves the tail
    - fileName-only (without path), a cmd basename :  ${0##*/}   ##--filename from filePath ; cut longest marching "*/" and return the rest !
    --
    - echo eg a backspace/newline/bell/...:   echo    abc$'\b'de  ;  echo    abc$'\n'de  ;  echo    abc$'\a'de ; ... see man bash  /^QUOTING
##________________________________________  ___________________________


#####  ==========  I/O Redirections, file-descriptors, exec ...:

    -!! see man bash  --> goto /REDIRECTION$ ($ for endofline)
    -! see BKs_Bash/TLDP_BashGuideAdvanced/abs-guide.pdf : Chapter 20: I/O Redirection + Appendix E: A Detailed Introduction to I/O and I/O Redirection
       http://www.tldp.org/LDP/abs/html/io-redirection.html
    -! see UnixShellsByExample_PTR_4ed_0409.chm  : 13.7 Standard I/O
    - see bash-cookbook: ch.2+3 ,sec-15.12
    --
    -! curr File-Descriptorsll and where they point to for the current shell/prcess:  ll /dev/fd/  (for each shell ll shows different/its.own FDs !!)
    - for new user-created-descriptor-numbers use ONLY 2< MyNo <10 ; otherwise conflict-probelms with shell-generated-NOs ! see man bash
    - swaping STDERR and STDOUT:
        - myscript  3>&1  1>&2  2>&3   (and close it: 3>&- )
        - from perl-docs:  mycmd  3>&1 1>&2 2>&3 3>&-   ##-- perldoc-5.14.0/perlop.html#Quote-Like-Operators  : qx/STRING/
        - OR to a logfile:   myscript  3>&1 1>stdout.logfile 2>&3- | tee -a stderr.logfile  #bash-cookbook-2.20
    - saving stdout / making a copy of stdout:
        exec 3>&1  (then eg echo aaa >&3 )  ; copy of stdin:  exec &3<  ;
        -!! DO NOT forget to close a descriptor, when not needed anymore:  3>&- or 3<&-
        -- /OR better with an additional descriptor, eg redirection stderr and back: (ore_cookbook 15.12 + 15.9)
        # save the "old" STDERR:
        exec 3>&2
        # Redirect any output to STDERR to an error log file instead:
        exec 2> /path/to/error_log
        # script with "globally" redirected STDERR goes here: ....
        # Turn off redirect by reverting STDERR and closing FH3
        exec 2>&3-
    -! back-directing stdout to the terminal/screen/console : exec > /dev/tty  (eg after a previous exec >myfile)
    -! exec <myfile  : reads myfile and executes its lines instead of the current shell and exits from the shell!
    -! Sequence-of-redirection very relevant!! see man bash -> /REDIRECTION$ :
        - eg: stdout+stderr redirecting:
        ls > dirlist 2>&1   #directs BOTH 1/stdout and 2/stderr to dirlist. BUT:
        ls 2>&1 > dirlist   #directs only the standard output to file dirlist!!  because the standard error  was  duplicated  from  the standard output before the standard output was redirected to dirlist.
    -- BOTH stdin+stderr redirecting: (see man bash --> Redirecting Standard Output and Standard Error):
        ... &>myfile  (/OR  >&myfile  BUT not prefered!) , which is the SAME as the expanded/Bourne-shell version:
        ... >myfile  2>&1
        -- APPENDING both stdin+stderr:
        ... &>>myfile	same as:
        ... >>myfile  2>&1
    -- HERE-document as stdin:
    <<EOF (/OR -EOF /OR "EOF" ... : - for ignoring tabs, "EOF" for NO var-expansions)
    .....
    EOF
##________________________________________  ___________________________


#####  ==========  set/shopt-options:
-! sub-shells NEVER change any set-options in the parent (./source of course does it!!)

	_______:  resetting to the previous status, after changings eg in a script:
	1-! short+complete: !! (\n in env-var-substituions are NOT visible, but are there!! so need NOT sed,...)
		oldSets="$(set +o)"  /OR  ="$(shopt -po)" ;..... later after changes again reseting back: $( echo $oldSets)  ;#-!- echo IS required, due to invisible \n
		oldShopts="$(shopt -p)"  ;..... later after changes again reseting back: $( echo $oldShopts)  ;#-!- echo IS required, due to invisible \n
	2- other alternatives
	2.1- (half-method but shorter:) "$-" contains the current optins; so: oldSets="$-" ; later: set -"$oldSets"
		However: it reets ONLY the old-on-options (not off ones, if they are changed)!!
		the "set -o"-cases in the current sub-script are NOT reset to the old status.
		the "$-" contains ONLY "on"-options!!
	2.2- complete reset, but longer: set +o  --> outputs a reusable full description;
		so save it to a tmp-script and recall it again at the end.
##________________________________________  ___________________________


#####  ==========  Pathname Expansion : eg for ls ...:
- ls all except *old* : ls !(*old*)
-! see:  man bash and /Pathname Expansion
##________________________________________  ___________________________


#####  ==========  key-bindings, bind, readline:
- bind -x '"\C-t":"echo $(( 2 + 3 ))"'  --> binding to a favorite script
- resetting/re-reading of binding-rc-file:   bind -f ~allu/.ee11/inputrc
- binding to a macro/text/...:  bind '"\C-t":"Test-Text-1"'
##________________________________________  ___________________________


#####  ==========  !!:*, !!...-list in man pages:  man bash /designator : they are word/event designators; bashOre-2.6 :History Expansion
	- !!:0/n/^/$/x-y/*/x*  :zerothWord/nthWord/zerothArg/lastArg/wordX-wordY/allArgs/x-$
	- each tocken is a WORD from 0-n including the command itself.
	- for only arguments use ^/$/* .So ^==1 , $==lastWord/Arg , *==1-$==allWordsExceptZeroth , x*==x-$
##________________________________________  ___________________________


#####  ==========  aliases replacing/processing: (bash-Ore; 3.2)
	- noloop : if back to the first alias, replacing is stopped
	- only first word of cmdLine is check for aliases. except:
	- If the value of an alias (the right side of the equal sign) ends in a blank, then bash tries to do alias substitution on the next word on the command line
	  So, first only for the second word in the cmdLine. But if it has space again at the end, then go further wilth replacing,....
##________________________________________  ___________________________


#####  ==========  functions:
	-!! exporting funcs:
		-!! FIRST define the func, and AFTER this do export -f func1 /OR declare -fx func1
		-!! if you do export/declare-x before defining, your definition is NOT exported!!
		-!! it do works also with set -o BEFORE defining the func1
	-!! do NOT use "declare -x" inside functions!! When used in a function, "declare" makes NAMEs local, as with the `local' command!! see: help declare
	- defining functions on cmdLine, eg: function findname(){  find "$1" -iname "*$2*" ; }
	-! carfuel if the first word is already as alias or function defined. it will bw replaced again. So unset this before redefining!
- PS1="\u \W \$" or PS1="\u \w \$" (long path)
- special chars / tocken processing in cmd-line: ( )  <  >  ; | & and IFS-chars (defaults: SPACE TAB  NEWLINE)
-! Command-Line Processing bash-Ore-7.3 :
- order of precedence on cmdLine processing (bash-Ore-4.1): 1-aliases 2-keywords as if,for,... 3-functions 4-builb-in commands as cd,echo,type,... 5-scripts and executables, which has to be searched/find in PATH ;
	 So: 1-alias, 2-keyword, 3-function, 4-builtin, or 5-file/script/exe
	 - use type / type -t <name> to see more about the name
##________________________________________  ___________________________


#####  ==========  built-ins:
- list of current active build-ins: enable -p
- builtin , command : running (overwriten) built-ins
##________________________________________  ___________________________


#####  ==========  jobs:
-! reactivating suspended jobs (with ctrl-Z OR with suspend) from another shell, were you do NOT see jobs listing: kill -s SIGCONT  <PID-of-suspended-job)
##________________________________________  ___________________________


#####  ==========  for do ... loops :
	- std:  for ii in 1 3 6 ; do echo $ii ; .... ; done
	- laufVar (also with autoIncrement):
		for (( ii=0  ; ii<10 ; ii++  ))   ; do echo $ii ; done ;
		for (( ii=10 ; ii    ; ii--  ))   ; do echo $ii ; done ;
		for (( ii=0  ; ii<10 ; ii=ii+2  )); do echo $ii ; done ;
	- laufVar with seq:  for ii in $( seq 6 2 12); do echo $ii ; done #/OR:  for ii in $(seq 1 20) ; do echo "___${ii}__" ; done
	- any sequence:  SEQ=( 1 1 2 3 5 8 13 ) ; for (( IDX = 0; IDX < ${#SEQ[*]}; IDX++ )) ; do echo -n "${SEQ[$IDX]} is " ...; done
##________________________________________  ___________________________


#####  ==========  case...esac :

	_______:  ! diff ;;  <->  ;&   <->   ;;&  at the end of each match.cmd.list!!
	;;   : continue with next loop.run
	;&   : keep.on current.loop.run with cmd.lis in the next xx)
	;;&  : keep.on current.loop.run the next possible match, if any! basically eith *) then defining a always.>
for ii in * ; do
    case $ii in
        varau) echo "======= $ii ---" ;;&
        varsys) echo "__ $ii ---" ;;
        *) echo "== $ii --" ;;
    esac
done

	_______:  man bash : case:
		case word in [ [(] pattern [ | pattern ] ... ) list ;; ] ... esac
A case command first expands word, and tries to match it against each pattern in turn, using the same matching rules as for pathname  expansion  (see  Pathname  Expansion below).
The word is expanded using tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution and quote removal.
Each pattern examined is expanded using tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, and process substitution.
If  the nocasematch  shell  option  is enabled, the match is performed without regard to the case of alphabetic characters.
When a match is found, the corresponding list is executed.
If the ;; operator is used, no subsequent matches are attempted after the first pattern match.
Using ;& in place of ;; causes execution to continue with the list associated  with  the  next set of patterns.
Using ;;& in place of ;; causes the shell to test the next pattern list in the statement, if any, and execute any associated list on a successful match.
The exit status is zero if no pattern matches.  Otherwise, it is the exit status of the last command executed in list.
##________________________________________  ___________________________


#####  ==========  getopts:
	-! see (excert man bash in):  help getopts   + !see abs-guide.pdf--Ch.15-Internal-Commands !!
	-!! see :   devres/codesColl_devres_kk/shsColl_UxLx_devres_kk/bashs
	-!! DIFF:  getopts  (bash-builtin WITH "s" at end)   <-->  getopt  (/usr/bin/getopt withOUT "s")
	- $OPTIND is the argument pointer index (next index, which will be read in the nexet loop)
	- $OPTARG is the (optional) argument attached to an option.
	- A colon following the option name in the declaration tags that option as having an associated argument.
	-!!  "-" identifies an option/getopts-argument: getopts will not process arguments without the prefixed -, and will TERMINATE option processing at the first argument encountered lacking them.! see abs-guide.pdf--Ch.15-Internal-Commands !!
	-!! If an option expects an argument (flag ":"), then it will grab WHATEVER is next on the command-line (even if it is the next option-flag)!
