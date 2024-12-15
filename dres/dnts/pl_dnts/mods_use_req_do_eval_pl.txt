_________  use/require/do/eval and modules.inclusion/libs-Einbindung by them; ________________________

	_______:  see  perldoc perlmod , perlmodlib
	- perldoc -f do + require + use + eval + Export
	- see IntermediatePerl_Ore_2ed_0603.chm : Ch.3 + 10! + 15 : Modules-Concept + Libs + SubModules + (+Cpan)
	- see Perl by Example, 4ed: Chapter 12. Moduls + Chapter 14. OOP
##________________________________________  ___________________________


#####  ==========  !! fazit use/require/do/eval:
-!!! fazit:  better:  use > require > do > eval  :so, take "use" pragma always for module.inclusion if possible! 

	_______:  same (more or less) and all worked (but WITHOUT use strict):
	BEGIN  {eval  `cat /up1/varu/varau/prjs/pl1/libs/PL1/Data1.pm` or die "==##===ERR:", $@;}
	BEGIN  {do "/up1/varu/varau/prjs/pl1/libs/PL1/Data1.pm"  or die "==##===ERR:", $@;}
	BEGIN  {do "PL1/Data1.pm"  or die "==##===ERR:", $@;}
	BEGIN  {require "PL1/Data1.pm";} ##--II- if modulename is defined as a var, then ONLY this require variation is ok, NOT the nex one!? so ok: our $testModule = "PL1/Data1.pm";  require $testModule;
	BEGIN  {require  PL1::Data1;}    ##--II- notice the diffs of two require-variations: 1)using " as:  "..."   2)full.filePath.notation:  ".../...pm"
	BEGIN  {use      PL1::Data1;}
	--- WITH use strict, worked ONLY if exported+imorted properly, as in:
	use PL1::Data1 qw(/.*/);  #based on already our @EXPORT_OK = qw(printData1 @a1 @a2 @a3 %h1 %h2 %h3); in Data1.pm
--################# features of use/require/do/eval pragmas : #################################

	_______:  use <MODULE> :
	as require, but plus import. so: BEGIN { require Module; Module->import( LIST ); }
	except if:   use Module ();  which is only:  BEGIN { require Module }  #so no import.
	The BEGIN forces the require and import to happen at COMPILE time.
	The import is not a builtin; it's just an ordinary static method.
	"use" does NOT accept a variable as a module name.

	_______:  require <EXPR> :
	demands that a library file be included if it has NOT already been included.
	The file is included via the do-FILE mechanism, which is essentially just a variety of eval with the caveat that lexical variables in the invoking script will be invisible to the included code
	-! the file will NOT be included twice under the same specified name. which files we've brought in and then brings them in only once!! /IntermediatePerl_Ore/intermediateperl-CHP-10-SECT-4.html

	_______:  do <EXPR> : 
	- Uses the value of EXPR as a FILENAME and executes the contents of the file as a Perl script.
	-! do operator acts as if the code from navigation.pm were incorporated into the current program, although in its OWN scope block {script.pl},
	   so that lexicals (my variables) and most directives (such as use strict) from the included file do NOT come into the main program!  IntermediatePerl_Ore/intermediateperl-CHP-10-SECT-3.html
	--- do--use : perldoc-5.14.0/functions/do.html  :
		inclusion of library modules is better done with the use and require operators, which also do automatic error checking and raise an exception if there's a problem.
		You might like to use do to read in a program configuration file. Manual error checking can be done this way: ...
		-!! eg OK-path:  perl -lw -e 'do "PL1/Data1.pm" ;'  ## PL1-dir is in libs-dir in @INC as /up1/varu/varau/prjs/pl1/libs ... /OR give the absolute path WITH .pm/.pl so full path; all in "";

	_______:  eval <EXPR / BLOCK> :
	--!! DIFF  eval-EXPR/"..."  <-->  eval-BLOCK/{...}
		- see code.exp + perldoc -f eval !!  : eval, whose parameter is a string expression OR a perl-block. : see IntermediatePerl_Ore/intermediateperl-CHP-2-SECT-3.html
		- eval-BLOCK/{...}	--> complie-time-handling! -->!! PREFERED one!! more secure + faster+ performance!
		- eval-EXPR/"..."	--> runtime-handling! :  compiles and executes code from a string at runtime.: so flexible BUT dangerous! so avoid!!
		- If the code to be executed doesn't vary, you may use the eval-BLOCK form to trap run-time errors without incurring the penalty of recompiling each time.  : perldoc -f eval
	-!! Trapping Errors with eval :  IntermediatePerl_Ore/intermediateperl-CHP-2-SECT-2.html

	_______:  ? vars-scopes/-access from main-script to the included-module-vars/-funcs:
			my-vars	our-vars  access	(my- and our-vars in included package/module, eg in module M1.pm)
	- use:		No	Yes
	- require:	No	Yes-but only with full path $package::var (no import func is executed! so no system-table-mods!!)
	- do:		No	yes	(also uses @INC bzw. PERL5LIB ... to find the file
	- eval:		No	yes
--############### compares and diffs of use/require/do/eval: #################################

	_______:  use <--> require:
	-!! take use if possible!! see perldoc!
	-!!	use Module;       exactly ==  BEGIN { require Module; import Module; }
		use Module LIST;  exactly ==  BEGIN { require Module; import Module LIST; }
		use Module ();    exactly ==  BEGIN { require Module; }
		see perlmod
	- "use" doesn't accept a variable as a module name. "require" accepts, BUT ONLY in file.path.notation (so  replace '::' by '/' and .pm , as "PL1/Data1.pm")
	- In general, use Module () is recommended over require Module , because it determines module availability at compile time, not in the middle of your program's execution. An exception would be if two modules each tried to use each other, and each also called a function from that other module. In that case, it's easy to use require instead. : perlmod
	- Because the use statement implies a BEGIN block, the importing of semantics happens as soon as the use statement is compiled, before the rest of the file is compiled. This is how it is able to function as a pragma mechanism, and also how modules are able to declare subroutines that are then visible as list or unary operators for the rest of the current file. This will not work if you use require instead of use.  :perlmod
	-! Inclusion of library modules is better done with the "use" and "require" operators, which also do automatic error checking and raise an exception if there's a problem. : perldoc -f do

	_______:  do <--> require:
	-!! require avoids multiple reads!!:
		the require operator keeps track of the files Perl has read.[] Once Perl has processed a file successfully, it simply ignores any further require operations on that same file. IntermediatePerl_Ore/intermediateperl-CHP-10-SECT-4.html
	- syntax error in the required file causes the program to die; thus, the many die $@ if $@ statements are unnecessary.

	_______:  do <--> eval :  (to read in files; in "do EXPR", then EXPR is always a filepath! ):
	-!!kk: take: "do" instead "eval" ever possible!! use always do for files instead eval!!
	-! kk: not really huge diff! short: if you have <filename>-param, then use "do", otherwise eval {...} is ok. although if do not know, what exactly is to be included, then you need eval.
	-!! do 'stat.pl';  ==  eval `cat stat.pl`;  except that it's more efficient and concise, keeps track of the current filename for error messages, searches the @INC directories, and updates %INC if the file is found.  See "Predefined Names" in perlvar for these variables.  It also differs in that code evaluated with "do FILENAME" cannot see lexicals in the enclosing scope; "eval STRING" does.  It's the same, however, in that it does reparse the file every time you call it, so you probably don't want to do this inside a loop. : perldoc -f do:
	- 1.diff: do 'string' interprets 'string' as a file name, while eval 'string' interprets 'string' as Perl code:
		$ perl -e  'do   "print qq(foo\n)"  or die qq($! $@)'	##---> No such file or directory  at -e line 1.
		$ perl -e  'eval "print qq(foo\n)"  or die qq($! $@)'	##---> foo
	- 2.diff: do ... cannot see lexical variables in the enclosing scope, while eval "STRING" can; so a bit diffs concerning my+our-vars-contexts
	-!! "do" will read in the file each time! so multiple readins could happen!! "require" and "use" avoid it!!
--########### codecs: use/require/do/eval: ##############################		
##________________________________________  ___________________________


#####  ==========  "use"-usage and INC-adaption-variations:   see IntermediatePerl_Ore/intermediateperl-CHP-10-SECT-5.html
	-- use-only: use ::up1::varu::varau::prjs::prj2::lib::PL1::Data1;
	-- use with short.path/lib.path.mods:
		- BEGIN { unshift @INC, '/home/u1/perl-lib'; }; ...; use PL1::Data1;  /OR
		- use lib qw(/home/u1/perl-lib); #extends also @INC as above!  /OR
		-! if do NOT know exact path yet: use FindBin qw($Bin); #: now the current bin-dir-fullpath is in $Bin
			perl -wle 'use FindBin qw($Bin); print $Bin ; system ("ls $Bin/libs");'
	-- use+I:	use PL1::Data1; ...  #called by  shell>  perl -I/up1/varu/varau/prjs/prj2/lib  ./use1.pl
	-- use+ENV:	shell>  PERL5LIB=/up1/varu/varau/prjs/prj2/lib   ./use1.pl
	-- use+lib.std.dir.INC-as.root:  cd	/usr/lib/perl5/site_perl/5.12.3  ; ln -s /up1/varu/varau/prjs/prj2/lib/PL1/
	-- use NOt for import, but directly in current-script-context:
		just delete "package"-declaration in the .pm-module!
		then all vars,... are in the system table of current script! 
	-- accessing/manipulating the package's symbol-table needs {no strict "refs"; ... }
	-- own library precedence over those in listed in the @INC array, put in your prog:  unshift(@INC,".");
##________________________________________  ___________________________


#####  ==========  require-usage:
	- require checks also @INC ! so followings ok if module in @INC-path :
	-! DIFF:  notice the diffs of the following two require-notaions:   1)using " as:  "..."   2)full.filePath.notation:  ".../...pm" :
	-- require "filePath"  :  require "PL1/Data1.pm";   ##--II- ok also if "PL1/Data1.pm in @INC-path!
	-- require PackagePath :  require  PL1::Data1;       ##--II- ok if in @INC ! also notice the above note for Notation-diffs 
	-- require var         :  my $modulePath = "PL1/Data1.pm";  require $modulePath;   ##--II- works ONLY with the Module.File.Path , NOT with Module.Package.Path (so NOT with: $modulePath = "PL1::Data1";)
	  so if modulename is defined as a var, then ONLY this require variation is ok, NOT the nex one!? so ok: our $testModule = "PL1/Data1.pm";  require $testModule;
##________________________________________  ___________________________


#####  ==========  do-usage:
	-- do: read-in a param/config file:
		- BEGIN {our $configfile1_FP = '/up1/varu/varau/prjs/prj2/bin/dats.pl' ; do "$configfile1_FP" or die "could not parse the config-file: $configfile1_FP , $@ , $!";}
		- or just in code (probably compiler-warns if strict): 
		our $configfile1_FP = '/up1/varu/varau/prjs/prj2/bin/dats.pl' ; do "$configfile1_FP" or die "could not parse the config-file: $configfile1_FP , $@ , $!";
		-!! same as : eval `cat /up1/varu/varau/prjs/prj2/bin/dats.pl`;  warn $@ if $@;
	-- read in config files: system first, then user : perldoc-5.14.0/functions/do.html :
		for $file ("/share/prog/defaults.rc", "$ENV{HOME}/.someprogrc") {
			unless ($return = do $file) {
				warn "couldn't parse $file: $@" if $@;
				warn "couldn't do $file: $!"    unless defined $return;
				warn "couldn't run $file"       unless $return;
			}
		}
		-- OR short/kk:
		for my $file (@appConfigFiles) {do "$file" or die " -- Error: could not parse the config file $file \n -- $@ , \n -- $!"}    #-eg: our @appConfigFiles = qw(aaaaaa bbbbb); 
##________________________________________  ___________________________


#####  ==========  eval-usage (eg reading app-config-files):
	-- read in properties-/shell.ENV.config-file (ignore comments): containing ONLY env-var-settings + comments!:
		while (<>) { eval ("\$$_") unless (/^#/); warn $@ if $@;}  ##-OR:  eval ('$'."$_") ...
	-- read in perl-config-file (so "$" for vars is there in the config-file, and values are enclosed in "..." !):
		no strict; while (<>) { eval; warn $@ if $@;}  #call:  s1.pl  c1.cfg 
	-- STDIN-eval (so kindof a perl-shell): Example 18.69/perlByExp.4ed:
		while(<STDIN>){
			$result=eval ;  # eval evaluates the expression $_
			warn $@ if $@;  # If an error occurs, it will be assigned to $@
			print "$result\n if $result";
			print "> "; # Print the prompt
		}
	-- HERE-doc-eval: Example 18.71. /perlByExp.4ed:
		eval<<"EOF";
			chdir "joker" || die "Can't cd: $!\n";
		EOF
		print "The error message from die: $@";
		print "Program $0 still in progress.\n";
	--
