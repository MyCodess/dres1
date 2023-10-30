__________ OS.Interactions, OS.dependent stuff, OS-Setup-/Installation/SystemConfigs of pl ... ________________________
##________________________________________  ___________________________


#####  ==========  Perl.System.Configs-from.inside.code:
	- perldoc Config
	- use Config; print Config::myconfig();  print Config::config_sh();  print Config::compile_date(); ...
##________________________________________  ___________________________


#####  ==========  System-/OS-Interacts:
	--- executing.cmds.in.OS/Shell-alternatives:
		-! qx// (shell-cmds-execution with backticks ):
			qx/STRING/ :  STRING  is interpolated and then executed as a system command with /bin/sh or its equivalent.
			eg  perl -we  "print qx{pwd; date;  ls -l};"
			for STDERR/STDOUT/... 	see  perldoc-5.14.0/perlop.html#Quote-Like-Operators   --> qx/STRING/
		- IO-filehandle-piping with OS.cmds: 
			open(NET, "netstat -i -n |")    || die "can't fork netstat: $!";   while (<NET>) {print;}; ...; close(NET);
		- <<`EOF`; for OS.cmds! see  perlop :  perldoc-5.14.0/perlop.html#Quote-and-Quote-like-Operators  -->  <<EOF  bzw.  Backticks
	--- funcsStd/subs/... for OS-interacts
	- qx
	- readpipe - execute a system command and collect standard output
##________________________________________  ___________________________


#####  ==========  OS.ENV.vars and pl:  ENV.vars queries/handling out of perl-scripts,...:
	-! %ENV contains your current environment. Setting a value in "ENV" changes the environment for any child processes you fork... #see perldoc -v '%ENV'
	--- printout  ENV:
		- while (($key,$value) = each %ENV) { print "$key=$value\n"; }
		- use Data::Dumper; print Dumper \%ENV;
	--- ENV-vars query/set/modify/...:
		- ENV.vars-query/set:  '%ENV ;eg $ENV{"USER"}   bzw as list: @ENV{"USER", "HOME"} bzw. setting: $ENV{"NewLibsPath"}="/lib/xx/yy"  ;see perldoc -v '%ENV'
		- undefining PATH / unsetting ENV-vars:  	$ENV{PATH} = undef;  /OR =""; ...
##________________________________________  ___________________________


#####  ==========  Modules.Std for Shell-/OS-Commands executing:
	- ExtUtils::Command - utilities to replace common UNIX commands in Makefiles etc.
	-! File::Spec - portably perform operations on file names ; eg: concatanate "dirPath" and "fileName" with the appropriate / or \ depending on OS.
	- Shell - run shell commands transparently within perl
##________________________________________  ___________________________


#####  ==========  FilesHandling on MsWin/Dos/Unix/ ...; IOs and OS-dependencies:
    -!! EOL independece of OS:  instead \n bzw. \r\n  use the input-record-separator "\/"   #see perlfaq5
    -
##________________________________________  ___________________________


#####  ==========  Shell(bash) <==> Perl:
	- regex-shell-vs-perl  : perl.cookbook--Recipe 6.9 Matching Shell Globs as Regular Expressions  : Table 6-2. Shell globs and equivalent Perl wildcard patterns
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
