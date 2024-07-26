##________________________________________  ___________________________


#####  ==========  FAQ in:   bash-2.05b.tar\bash-2.05b\doc\FAQ

	_______:  C2)  How does bash differ from the Korn shell, version ksh88?
Things bash has or uses that ksh88 does not:
	long invocation options
	[-+]O invocation option
	-l invocation option
	`!' reserved word
	arithmetic for command: for ((expr1 ; expr2; expr3 )); do list; done
	arithmetic in largest machine-supported size (intmax_t)
	posix mode and posix conformance
	command hashing
	tilde expansion for assignment statements that look like $PATH
	process substitution with named pipes if /dev/fd is not available
	the ${!param} indirect parameter expansion operator
	the ${!param*} prefix expansion operator
	the ${param:offset[:length]} parameter substring operator
	the ${param/pat[/string]} parameter pattern substitution operator
	variables: BASH, BASH_VERSION, BASH_VERSINFO, UID, EUID, SHLVL,
		   TIMEFORMAT, HISTCMD, HOSTTYPE, OSTYPE, MACHTYPE,
		   HISTFILESIZE, HISTIGNORE, HISTCONTROL, PROMPT_COMMAND,
		   IGNOREEOF, FIGNORE, INPUTRC, HOSTFILE, DIRSTACK,
		   PIPESTATUS, HOSTNAME, OPTERR, SHELLOPTS, GLOBIGNORE,
		   GROUPS, FUNCNAME, histchars, auto_resume
	prompt expansion with backslash escapes and command substitution
	redirection: &> (stdout and stderr), <<<, [n]<&word-, [n]>&word-
	more extensive and extensible editing and programmable completion
	builtins: bind, builtin, command, declare, dirs, echo -e/-E, enable,
		  exec -l/-c/-a, fc -s, export -n/-f/-p, hash, help, history,
		  jobs -x/-r/-s, kill -s/-n/-l, local, logout, popd, pushd,
		  read -e/-p/-a/-t/-n/-d/-s, readonly -a/-n/-f/-p,
		  set -o braceexpand/-o histexpand/-o interactive-comments/
		  -o notify/-o physical/-o posix/-o hashall/-o onecmd/
		  -h/-B/-C/-b/-H/-P, set +o, suspend, trap -l, type,
		  typeset -a/-F/-p, ulimit -u, umask -S, alias -p, shopt,
		  disown, printf, complete, compgen
	`!' csh-style history expansion
	POSIX.2-style globbing character classes
	POSIX.2-style globbing equivalence classes
	POSIX.2-style globbing collating symbols
	egrep-like extended pattern matching operators
	case-insensitive pattern matching and globbing
	`**' arithmetic operator to do exponentiation
	redirection to /dev/fd/N, /dev/stdin, /dev/stdout, /dev/stderr
	arrays of unlimited size
	TMOUT is default timeout for `read' and `select'
Things ksh88 has or uses that bash does not:
	tracked aliases (alias -t)
	variables: ERRNO, FPATH, EDITOR, VISUAL
	co-processes (|&, >&p, <&p)
	weirdly-scoped functions
	typeset +f to list all function names without definitions
	text of command history kept in a file, not memory
	builtins: alias -x, cd old new, fc -e -, newgrp, print,
		  read -p/-s/var?prompt, set -A/-o gmacs/
		  -o bgnice/-o markdirs/-o nolog/-o trackall/-o viraw/-s,
		  typeset -H/-L/-R/-Z/-A/-ft/-fu/-fx/-l/-u/-t, whence
	using environment to pass attributes of exported variables
	arithmetic evaluation done on arguments to some builtins
	reads .profile from $PWD when invoked as login shell
Implementation differences:
	ksh runs last command of a pipeline in parent shell context
	bash has brace expansion by default (ksh88 compile-time option)
	bash has fixed startup file for all interactive shells; ksh reads $ENV
	bash has exported functions
	bash command search finds functions before builtins
	bash waits for all commands in pipeline to exit before returning status
	emacs-mode editing has some slightly different key bindings

	_______:  C3)  Which new features in ksh-93 are not in bash, and which are?
New things in ksh-93 not in bash-2.05b:
	associative arrays
	floating point arithmetic and variables
	math library functions
	${!name[sub]} name of subscript for associative array
	`.' is allowed in variable names to create a hierarchical namespace
	more extensive compound assignment syntax
	discipline functions
	`sleep' and `getconf' builtins (bash has loadable versions)
	typeset -n and `nameref' variables
	KEYBD trap
	variables: .sh.edchar, .sh.edmode, .sh.edcol, .sh.edtext, .sh.version,
		   .sh.name, .sh.subscript, .sh.value, .sh.match, HISTEDIT
	backreferences in pattern matching (\N)
	`&' operator in pattern lists for matching
	print -f (bash uses printf)
	`fc' has been renamed to `hist'
	`.' can execute shell functions
	exit statuses between 0 and 255
	set -o pipefail
	`+=' variable assignment operator
	FPATH and PATH mixing
	getopts -a
	-I invocation option
	DEBUG trap now executed before each simple command, instead of after
	printf %H, %P, %T, %Z modifiers, output base for %d
New things in ksh-93 present in bash-2.05b:
	[n]<&word- and [n]>&word- redirections (combination dup and close)
        for (( expr1; expr2; expr3 )) ; do list; done - arithmetic for command
        ?:, ++, --, `expr1 , expr2' arithmetic operators
	expansions: ${!param}, ${param:offset[:len]}, ${param/pat[/str]},
		    ${!param*}
	compound array assignment
	the `!' reserved word
	loadable builtins -- but ksh uses `builtin' while bash uses `enable'
	`command', `builtin', `disown' builtins
	new $'...' and $"..." quoting
	FIGNORE (but bash uses GLOBIGNORE), HISTCMD
	set -o notify/-C
	changes to kill builtin
	read -A (bash uses read -a)
        read -t/-d
	trap -p
	exec -c/-a
	`.' restores the positional parameters when it completes
	POSIX.2 `test'
	umask -S
	unalias -a
	command and arithmetic substitution performed on PS1, PS4, and ENV
	command name completion
	ENV processed only for interactive shells
#####################################################################
##________________________________________  ___________________________


#####  ==========  FAQ in:   bash-3.0.tar\bash-3.0\doc\FAQ

	_______:  C2)  How does bash differ from the Korn shell, version ksh88?
Things bash has or uses that ksh88 does not:
	long invocation options
	[-+]O invocation option
	-l invocation option
	`!' reserved word
	arithmetic for command: for ((expr1 ; expr2; expr3 )); do list; done
	arithmetic in largest machine-supported size (intmax_t)
	posix mode and posix conformance
	command hashing
	tilde expansion for assignment statements that look like $PATH
	process substitution with named pipes if /dev/fd is not available
	the ${!param} indirect parameter expansion operator
	the ${!param*} prefix expansion operator
	the ${param:offset[:length]} parameter substring operator
	the ${param/pat[/string]} parameter pattern substitution operator
	variables: BASH, BASH_VERSION, BASH_VERSINFO, UID, EUID, SHLVL,
		   TIMEFORMAT, HISTCMD, HOSTTYPE, OSTYPE, MACHTYPE,
		   HISTFILESIZE, HISTIGNORE, HISTCONTROL, PROMPT_COMMAND,
		   IGNOREEOF, FIGNORE, INPUTRC, HOSTFILE, DIRSTACK,
		   PIPESTATUS, HOSTNAME, OPTERR, SHELLOPTS, GLOBIGNORE,
		   GROUPS, FUNCNAME, histchars, auto_resume
	prompt expansion with backslash escapes and command substitution
	redirection: &> (stdout and stderr), <<<, [n]<&word-, [n]>&word-
	more extensive and extensible editing and programmable completion
	builtins: bind, builtin, command, declare, dirs, echo -e/-E, enable,
		  exec -l/-c/-a, fc -s, export -n/-f/-p, hash, help, history,
		  jobs -x/-r/-s, kill -s/-n/-l, local, logout, popd, pushd,
		  read -e/-p/-a/-t/-n/-d/-s, readonly -a/-n/-f/-p,
		  set -o braceexpand/-o histexpand/-o interactive-comments/
		  -o notify/-o physical/-o posix/-o hashall/-o onecmd/
		  -h/-B/-C/-b/-H/-P, set +o, suspend, trap -l, type,
		  typeset -a/-F/-p, ulimit -u, umask -S, alias -p, shopt,
		  disown, printf, complete, compgen
	`!' csh-style history expansion
	POSIX.2-style globbing character classes
	POSIX.2-style globbing equivalence classes
	POSIX.2-style globbing collating symbols
	egrep-like extended pattern matching operators
	case-insensitive pattern matching and globbing
	`**' arithmetic operator to do exponentiation
	redirection to /dev/fd/N, /dev/stdin, /dev/stdout, /dev/stderr
	arrays of unlimited size
	TMOUT is default timeout for `read' and `select'
	debugger support, including the `caller' builtin
	RETURN trap
	Timestamps in history entries
	{x..y} brace expansion
Things ksh88 has or uses that bash does not:
	tracked aliases (alias -t)
	variables: ERRNO, FPATH, EDITOR, VISUAL
	co-processes (|&, >&p, <&p)
	weirdly-scoped functions
	typeset +f to list all function names without definitions
	text of command history kept in a file, not memory
	builtins: alias -x, cd old new, newgrp, print,
		  read -p/-s/var?prompt, set -A/-o gmacs/
		  -o bgnice/-o markdirs/-o trackall/-o viraw/-s,
		  typeset -H/-L/-R/-Z/-A/-ft/-fu/-fx/-l/-u/-t, whence
	using environment to pass attributes of exported variables
	arithmetic evaluation done on arguments to some builtins
	reads .profile from $PWD when invoked as login shell
Implementation differences:
	ksh runs last command of a pipeline in parent shell context
	bash has brace expansion by default (ksh88 compile-time option)
	bash has fixed startup file for all interactive shells; ksh reads $ENV
	bash has exported functions
	bash command search finds functions before builtins
	bash waits for all commands in pipeline to exit before returning status
	emacs-mode editing has some slightly different key bindings

	_______:  C3)  Which new features in ksh-93 are not in bash, and which are?
New things in ksh-93 not in bash-3.0:
	associative arrays
	floating point arithmetic and variables
	math library functions
	${!name[sub]} name of subscript for associative array
	`.' is allowed in variable names to create a hierarchical namespace
	more extensive compound assignment syntax
	discipline functions
	`sleep' and `getconf' builtins (bash has loadable versions)
	typeset -n and `nameref' variables
	KEYBD trap
	variables: .sh.edchar, .sh.edmode, .sh.edcol, .sh.edtext, .sh.version,
		   .sh.name, .sh.subscript, .sh.value, .sh.match, HISTEDIT
	backreferences in pattern matching (\N)
	`&' operator in pattern lists for matching
	print -f (bash uses printf)
	`fc' has been renamed to `hist'
	`.' can execute shell functions
	exit statuses between 0 and 255
	`+=' variable assignment operator
	FPATH and PATH mixing
	getopts -a
	-I invocation option
	printf %H, %P, %T, %Z modifiers, output base for %d
	lexical scoping for local variables in `ksh' functions
	no scoping for local variables in `POSIX' functions
New things in ksh-93 present in bash-3.0:
	[n]<&word- and [n]>&word- redirections (combination dup and close)
        for (( expr1; expr2; expr3 )) ; do list; done - arithmetic for command
        ?:, ++, --, `expr1 , expr2' arithmetic operators
	expansions: ${!param}, ${param:offset[:len]}, ${param/pat[/str]},
		    ${!param*}
	compound array assignment
	the `!' reserved word
	loadable builtins -- but ksh uses `builtin' while bash uses `enable'
	`command', `builtin', `disown' builtins
	new $'...' and $"..." quoting
	FIGNORE (but bash uses GLOBIGNORE), HISTCMD
	set -o notify/-C
	changes to kill builtin
	read -A (bash uses read -a)
        read -t/-d
	trap -p
	exec -c/-a
	`.' restores the positional parameters when it completes
	POSIX.2 `test'
	umask -S
	unalias -a
	command and arithmetic substitution performed on PS1, PS4, and ENV
	command name completion
	ENV processed only for interactive shells
	set -o pipefail
##________________________________________  ___________________________


#####  ==========  
