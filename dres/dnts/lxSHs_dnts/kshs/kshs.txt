_____________ KSH _______________________
=== LOOPs:
- For-Loop-Simulation with loop-variable in ksh88: ii=0 ; while (( ii < 3 )); do print "== $ii" ; (( ii += 1 )) ; done

	_______:  -- FOR-SQL-loops:  the best with: /nolog + script (+ in script conn  conn / as sysdba ..... exit)!
-!note: works in simple form only for logged-in-user (either ora92 OR ora817), NOT both!!
    otherwise you must also set ORACLE_HOME,... appropriately (see /app/oracle92/scripts/admin/dbshut_immediate.sh)
    so in the followings, replace $dbNamesList with user-ORA-instances; or set the rest either !!

	_______:  with a script ( easier than here-command; also with sqlplus  -S , if no messages needed):
    ---!!prefered alternative: withOUT user/pw on commandline, but in sql-script:
        -! for inst in $dbNamesList ; do export ORACLE_SID=$inst ; sqlplus [-S] /nolog @s3.sql ; done
         --> with: s1.sql: conn / as sysdba \n show user  \n define \n exit
         /OR complete ENV for one user:
         -! for srv in $dbNamesList ; do export ORACLE_SID=$srv ; unset userShellDone ; . $userShellFP ; print "================ Connecting>
    --- with user/pw on commandline:
        for inst in $dbNamesList ; do export ORACLE_SID=$inst ; sqlplus "/ as sysdba" @s1.sql ; done      # s1.sql MUST include exit-line, >
         --> with: s1.sql:    show user  \n define \n exit
    --- /OR with here-command loop for all instances :
        for inst in $dbNamesList ; do sqlplus "/ as sysdba" @<<EEE
> select sysdate from dual;
> EEE
> done
=== functions: (see 4.1.1. ore + Olczak-Ch08)
	---!! export of functions to 1)scripts 2)subshells   (are different!!):
		- functions are NOT exported to subshells or scripts as DEFAULT !!
		- exporting functions to scripts do: typeset -xf myfunc  (!! not -fx but -xf !!) 
		-  exporting functions to subshells: NOWAY, thes are not exported!!
				only way: put them in $ENV also with -xf , so that by invoking a subshell they are defined again !!
		- man ksh88 (solaris.8):
			Ordinarily, functions are unset (== undefined) when the  shell  executes  a
		 shell script. The -xf option of the typeset command allows a
		 function to be exported to SCRIPTS that are executed without
		 a  separate  invocation of the shell. Functions that need to
		 be defined across separate invocations of the  SHELL (== subshells) should
		 be specified in the ENV file with the -xf option of typeset.
	-!! diff: functions <-> scripts:
		- First, functions do not run in separate processes, as scripts  (so is like sourcing, except local vars in func)
		- Second, if a function has the same name as a script or executable program, the function takes precedence
	- "exit" from function, exits from caller (shell or script calling the func)
	- "return" returns ONLY from the func (back to the caller)
	- export of functions to subshells:
		- functions are NOT exported in ksh88; if want export, then use FPATH-functions and export FPATH
		- in ksh88:  typeset –fx works for scripts, but NOT for subshells! so functions are not exported at all to new shells (except using FPATH)???
		- in ksh93 can be exported: typeset –fx myFunc
		- NOTE: By default, functions are not available to subshells. This means that a regular function that was read in your working environment, .profile file, or environment file would not be available in a Korn shell script. To export a function, use the typeset –fx command:
			typeset –fx function-name
			To make a function available across separate invocations of the Korn shell, include the typeset –fx function-name command in the environment file.
	- export of variables:
		- All function variables, except those explicitly declared locally within the function with the typeset command, are inherited and shared by the calling Korn shell script.
	- no Definitions of functions in memeory: set +o nolog  (default)
	- local varialbles for functions: in function-body define local vars with:  typeset var1=value1
	- deleting/unsetting a functin: unset -f func1
	- lisintg of defined functions:  typeset -f == functions  ; only names-listing : +f
	- autoloading:
		- autoload == typeset -fu func-1 : the shell won't read in the definition of func-1 until it's actually called
		- where the definition of an autoloaded function? Shell uses the built-in variable FPATH for them!!
			FPATH: is a list of directories like PATH. The shell looks for a file called func-1 that contains the definition of function func-1 in each of the directories in FPATH.
=== invocation ksh. : UxExp-4ed: Table 12.16. Arguments to ksh
	- any set option can be used on the command line + -s (sort parameters), -c '..'(execute command)...
	- use -m ?? instead nohup
	- use #!/bin/ksh -e to exit on error and execute the ERR trap, if set; is disabled while reading profile.
		If a command has a non-zero exit status, execute the ERR trap, if set, and exit. This mode is disabled while reading profiles
	- with  #!/bin/ksh almost all set -opetions can be taken
=== set options, sets-queries...
	- skip remaining setup if shell non-interactive:	[[ -o interactive ]] || return 0
===!! priorities/presedence/order of shell-search-commands: (see ore_ksh88-4.1.1 Functions and ksh93_2ed.4.1.1 and  ksh93_2ed-appA.2):
	precedence for the various sources of commands:
	- ksh88:  key-words (if,for,...) > aliases > built-ins > function > Scripts and executable programs
	- however: bypassing aliases and taking original built-ins with "...", so by surrounding it in quotes: as in "cd" which is ANYWAD built-in cd !!  see ore_ksh88-7.3.1 Quoting
	- ksh93:  key-words (if,for,...) >  aliases > SPECIAL-built-ins > function > Non-special built-ins  > Scripts and executable programs :
		- SPECIAL-built-ins: . (dot), : , alias, break, continue, eval, exec, exit, export, login, newgrp, readonly, return, set, shift, trap, typeset, unalias, and unset) 
		- NON-SPECIAL-built-ins: the Rest, as cd and whence  (see ksh93_2ed.4.1.1 and CH07)
=== cmdLine-params, args, set:
- shifting/unsetting all cmdLine-params ($x): set --  /OR: set x ; shift /OR:  shift $#  /OR: while (( $# > 0 )) ; do shift ; echo "shift---$#" ;  done
- getting LAST argument of cmdline: eval \$$#  ; eg. eval echo \$$#
=== pathes in scripts (all WITHOUT sourcing '.' ;in sourcing $0 is ksh and scriptname is gone/replaced by ksh/shell):
	- my-absolut-path : echo `pwd`/`which $0`
=== file descriptors: see extra file
	- see UnixShellsByExp-4ed-11.13 + Table 11.19.exec ; and Ore-ksh88-ch07
	- see your notes in prjBinDir/notes
=== Exp/Env-listings: local, global ??
	- set	: loc+glob-VAR ; prints all variables: local + global
	- env command (==export built-in ?)	: glob-VAR ==export ; prints only global variables , so all environment (exported) variables
	- typeset : like export/env but + functions; prints all integers variables (loc+glob) + functions, and exported variables
=== Debugging/tracing:
- ksh -x s1.sh   /OR: -v
- trap 'echo ===[${LINENO}]:' DEBUG  #as first line in script; replace echo with ....
- trap 'print $LINENO ' DEBUG
- trap 'print Bad input' ERR
- typeset -ft :Turns on tracing. Traces execution in a function.
=== Arithmetics:
- mixing arithmethic and command-substitution (with $(cmd) instead of `cmd`), (see ksh_ore_cd_6.2. Numeric Variables and Arithmetic):
	print "Only $(( (365-$(date +%j)) / 7 )) weeks until the New Year!"
- supports relational operators as "truth values" of 1 for true and 0 for false:
	$((3 > 2)) has the value 1; $(( (3 > 2) || (4 <= 1) )) also has the value 1
- Arithmetic Conditionals  for use in if and while constructs (6.2.2-ore-cd):
	Another construct, closely related to $(( ...)), is ((...)) (without the leading dollar sign):
	We use this for evaluating arithmetic condition tests, just as [[...]] is used for string, file attribute, and other types of tests.
	((...)) is almost identical to $((...)). However, it was designed for use in if and while constructs.
	Instead of producing a textual result, it just sets its exit status according to the truth of the expression:0 if true, 1 otherwise.
	So, eg. ((3 > 2)) produces exit status 0, as does (( (3 > 2) || (4 <= 1) )), but (( (3 > 2) && (4 <= 1) )) has exit status 1 since the second subexpression isn't true.

	_______:  bc variations with scale (ksh88 has no floating calculations):
	- with coprocesses:  bc |& ; print -p "scale=2; $1" ; read -p ret ; print "======= $ret --" ;
	- only-ksh-builtin (in ksh88, no floating):  { print "$@ == $(( $@ ))" ; } #:(in ksh88 no scale/floating possible; always truncated!!)
##________________________________________  ___________________________


#####  ==========  Variable-Substitution:
	- (ksh_momento.htm :)
    +-------------------+---------------------------+-------------------+
    | Operation         | if par is unset or null   | else              |
    +-------------------+---------------------------+-------------------+
    | var=${par:-word}  | var= word                 | var= ${par}	    |
    | var=${par:=word}  | par= word ; var= word     | var= ${par}	    |
    | var=${par:+word}  | var becomes null          | var= word         |
    | var=${par:?word}  | word is printed on stderr | var= ${par}	    |
    +-------------------+---------------------------+-------------------+
	${parameter :-word } If parameter is set and is non-null then substitute its value; otherwise substitute word. 
	${parameter :=word } If parameter is not set or is null then set it to word; the value of the parameter is then substituted. Positional parameters may not be assigned to in this way. 
	${parameter :+word } If parameter is set and is non-null then substitute word; otherwise substitute nothing. 
	${parameter :?word } If parameter is set and is non-null then substitute its value; otherwise, print word and exit from the shell. If word is omitted then a standard message is printed. 
##________________________________________  ___________________________


#####  ==========  Regular Exp.:

	_______:  Pattern-matching Operators /Table 4.5:
	${variable#pattern} If the pattern matches the beginning of the variable's value, delete the shortest part that matches and return the rest.
	${variable##pattern} If the pattern matches the beginning of the variable's value, delete the longest part that matches and return the rest.
	${variable%pattern} If the pattern matches the end of the variable's value, delete the shortest part that matches and return the rest.
	${variable%%pattern} If the pattern matches the end of the variable's value, delete the longest part that matches and return the rest.

	_______:  exp: with path=/home /billr/mem/long.file.name  :
	Expression             Result
	$path              /home/billr/mem/long.file.name
	${path#/*/}              billr/mem/long.file.name
	${path##/*/}                       long.file.name
	${path%.*}         /home/billr/mem/long.file
	${path%%.*}        /home/billr/mem/long
- ${variable##*/} is actually equivalent to the UNIX utility basename(1).
##________________________________________  ___________________________


#####  ==========  history:
-- Repeating the Last Command Explicitly: “r” (bash/csh equivalent is “!!”) which is a built-in alias that repeats the last command issued.
	/OR: 	alias \!\!='fc -e -'
-- replacing in last command and executing: 	fc -e - old=new
	or, you could use the Korn shell shortcut like this:  r  old=new
	or even using the alias specified above:  !! 26=25

	_______:  - cursor keys for history:
  >I have trouble getting some keys to work properly. First I do "set -o emacs". Now
  >the arrowkeys print 'A', 'B', 'C' and 'D' respectively. The delete key prints '~'
  >(tilde). Also, I would like to get alternatives in tab completion. The tab
  >completion works when the completed word is unambigous, but when there are several
  >alternatives, I would like to get a list of these alternatives.
  >
	Did you get the ksh88 or the ksh93 version? In ksh88, you can use the arrow keys
	in emacs mode by defining aliases: alias __A=^P alias __B=^N alias __C=^F alias
	__D=^B where ^P, ^N, etc are the control characters (in vi, you press ctrl-V
	Ctrl-P and so on ; in 88 in emacs for ^P do: \ and then ctrl+p ), so:
	alias __A=^P  #(whereas in 88 ^P means \ then  ctrl+p)
	alias __B=^N
	alias __C=^F
	alias __D=^B
	alias __E=^A
	--- /OR: from .kshrc: (for ksh88)
	case $- in
	  *i*)  # cusorkey definitions for emacs-option in ksh
			alias __A=`echo "\020"` # up arrow = ^p
			alias __B=`echo "\016"` # down arrow = ^n
			alias __C=`echo "\006"` # right arrow = ^f
			alias __D=`echo "\002"` # left arrow = ^b
			alias __E=`echo "\001"` # line home = ^a
			export VISUAL=emacs
			;;
	  *) ;; # andernfalls nichts einstellen
	esac
	---
	#########################
	# command completition
	#########################
	I like much vi editor for all its capabilities (buffers...), but I
	personnaly find that the emacs mode is much more user friendly for line
	editing in ksh. One of its greatest interest is almost undocumented : you
	may have aliases to use the arrow keys for line editing. Try these five
	lines in your .kshrc (or whatever filename your ENV variable contains) :
	set -o emacs
	alias __A=^P            # cursor up
	alias __B=^N            # cursor down
	alias __C=^F            # cursor right
	alias __D=^B            # cursor left
	The first __ (double _) replaces the ^[ sent by the vt100 mode function keys
	in 7bits mode. The followings are CONTROL-letter characters (one char only)
	that you insert in vi with CTRL-V+CTRL-letter.
	After that log again and you may use the arrow keys to navigate in the
	commands history and through the lines. You may never wanna come back to vi
	mode...
	-----
##________________________________________  ___________________________


#####  ==========  misc-notes:

	_______:  converting man pages into text to view them with vi:
	man ksh | sed -e 's/_^H//g' -e 's/+^H_/+-/g' > ksh.man   :but for ^H do: \ and then ctrl-H
	/OR in viwm:
	- runtime ftplugin/man.vim ; ans then eg. :Man cat  ,then :w cat.man
	-

	_______:  which version of ksh am i using? : file:///W:/Docs/Unix/Books_Ux/UnixBookshelf_CD_30ed/korn/ch01_04.htm
	- set -o emacs, then press CTRL-V  /OR
	- echo ${.sh.version}  : wenn nich definiert oder error -> nicht ksh93, sondern 88 /OR
	- what /bin/ksh
	- CDE-version in: /usr/dt/bin/dtksh  (93)

	_______:  The following code snippet can be used in ksh to give a bash like prompt:
	export HOSTNAME=`/bin/hostname`
	PS1='[$USER\@$HOSTNAME ${PWD##/*/}]$ '
	/OR from .kshrc:  export PS1="$LOGNAME@$HOSTNAME:\${PWD}# "
-!! escaping instead of ctrl-V : \ and then escape char
-!!-diff:
	- $( cmd ) : == `cmd` ;eg  $(ls)
	- $(( arithm. ))	:eg xx=$((5+3)) && echo $xx
	- (( arith-condition )) with 0==true and 1==false ;eg ((3 > 2)) produces exit status 0  ; see 6.2.2
	- [[ string-condition ]] :see 5.1.4.1. String comparisons
- hiding user-input (eg pw,...):  stty -echo ; read pw1?'password?' ; stty echo ; ...
- standard way to make error messages with echo: echo "error-message..." 1>&2 : UPT-3ed: 35.17 + 36.16
