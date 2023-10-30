__________ debugging perl _______________________________________________

	_______:  see:
	- perldebtut (its see.also:  perldebguts, re, DB, Devel::DProf, dprofpp, Dumpvalue, and perlrun)
	- perldoc re , perldebguts, perlrun
	- Dumpvalue - provides screen dump of Perl data
	- Perl_Hacks_TipsToolsForProgrammingDebuggingSurviving_Ore_0603.chm: Chapter 6. Debugging , Hacks 51-59
##________________________________________  ___________________________


#####  ==========  kk-debug/verbose/test:
	---!! take Smart::Comments !! see its nts!
	---!! KK.Comments.Filter.Debugging (similar Smart), see: prj_pl1/debugs/DebugComments1.p*
	--- kk.traditional.manual.debug/verbose/test all or one package/class, depending on debug.var OR ENV.var:
		our $dbg=$ENV{"pldbg"} unless defined $dbg ; $dbg += 0;
		if ($dbg > 2) {...}
		- call:
		pldbg=5  Person.pm  #verbose all classes
		perl -e '$Person::dbg=3 ;  do "Person.pm" or die $! , $@;'  #verbose only Person.pm
##________________________________________  ___________________________


#####  ==========  Debuger.Modules/.packages and Helpers:

	_______:  !! Smart::Comments  /CPAN   :easy way to insert debugging and tracking code into a program. Best of all, when you're finished debugging, you don't have to remove them.  ;see Perl_Hacks.chm : Hack 54. Debug with Comments 
	--- debug.levels--uue:
		- uue-debug-sign:  ###-d- ,  ###-dd- , ... so:  ###-dd*-
		- level.1 : ###-d-
		- level.2 : ###-dd-
		- level.3 : ###-ddd-
	--- printout-of-levels:
		- printout only debug.level.1 :	perl  '-MSmart::Comments qw(###-d-)' myapp.pl     /bzw.  -MSmart::Comments=###-d-
		- printout only debug.level.3 :	perl  '-MSmart::Comments qw(###-ddd-)' myapp.pl   /bzw.  -MSmart::Comments=###-ddd-
		- printout all  debug.levels  :	perl  '-MSmart::Comments qw(###-dd*-)' myapp.pl   /bzw.  '-MSmart::Comments=###-dd*-'
			OR per.ENV        use Smart::Comments  -ENV;   ##-and in shell:  export Smart_Comments="###-dd*-"
		- printout only debug.level.1+2 :
			in.code:       use Smart::Comments  qw(###-dd?-);  /OR  use Smart::Comments  qw(###-d-  ###-dd-);
			per.cmdline:   perl  '-MSmart::Comments qw(###-dd?-)' myapp.pl
			per.ENV        use Smart::Comments  -ENV;   ##-and in shell:  export Smart_Comments="###-dd?-"
	---!! debug.sign-changing/-adapting:
		-!! the debug-lines-sign MUST start with "###" at least, to work !!
		- use Smart::Comments  "###-d-" ;           #-OR  qw(###-d-);
		- use Smart::Comments  qw(###-d-  ###-dd-);      #-OR   '###-d-', '###-dd-';
		- use Smart::Comments  "###-dd*-";        #-also reexp ok obviously
		- per.cmdline:   perl  -MSmart::Comments=###-d-  myapp.pl    #-OR  perl  '-MSmart::Comments qw(###-dd*-)' myapp.pl  #-OR perl  '-MSmart::Comments "###-d-" '  myapp.pl
		- per.ENV-var (in case of -ENV) in shell:  export Smart_Comments="###-dd*-"   ##-in code must be:   use Smart::Comments  -ENV;
	---!! Usage--uue:
		-1. in code:  use Smart::Comments  -ENV;    ##-so is debugging-printouts DEactivated for now!!
		-2a GLOBLALLY Activating (so for all modules/packages, so for the WHOLE app, all ) of debugging-printouts:
		    do in the shell:   export Smart_Comments="###-dd*-"  (or any level you want),
		    and then invoke your app just normal, eg: perl myapp.pl
		-2b INDIVIDUALLY Activating (so ONLY for the first package on the commandline):
		    perl '-MSmart::Comments=###-dd*-'  myapp.pl
	--- best usage for ONE/individual modules/scripts (so not globally for a whole Application consisting of many modues/packages/...):
		do NOT include the line  use Smart::Comments "###-dd*-";  in your code,   /OR only put:  'use Smart::Comments  -ENV;'
		and then for debugging, invoke your app with:   perl '-MSmart::Comments "###-dd*-" '  myapp.pl
		so, then there is no need to modify the code for Prod at all any more !!
		Of course, this ONLY enables smart comments in the application file itself, not in any modules that the application loads.
		for global activation do:  export Smart_Comments="###-dd*-"  bzw.   export Smart_Comments=1
		!! still to be flexible, include a tagging line in your code as "##--useSmartComm use Smart::Comments;" , which can be replace later by sed with "use Smart::Comments;", if needed ...
	--- DEactivating smart-comments , if is activated in code  by:
		-!! WITHOUT-codes-modifications, but GLOBALLY for the whole codes by overwriting Comments.pm with onliner-file of  "1;" :
			cd <libdir-containing-smart> && mv Smart/Comments.pm  Smart/Comments.pm.org  &&   echo "1;" >|   Smart/Comments.pm   ##--again reactivating: cp -f Smart/Comments.pm.org  Smart/Comments.pm
			! cat /dev/null ... does NOT work ! perl needs  "1;" 
		- /OR:  sed -i s/^\s*(use\s+Smart::Comments.+)$/##--useSmartComm  $1/; ...
		- /OR   POE-Component-Server-BigBrother-0.08/tools/disable_smart_comments  in CPAN (basically doing the same as sed)
	--- assertions/tests/checks/...:
		-!! EXACTLY only ONE space may be after debugging-sign and assertion:/verify:/... symbol!!
		    otherwise the line will be considered as a normal "### LABEL : EXPRESSION" and will be evaluated and the result of assertion-expression will be printed as "1" or "0" without die/exception!!

	_______:  Carps:
	-!! set "$Carp::Verbose=1"  bzw.  " perl -MCarp=verbose script.pl" to force Carp to stack.backtrace.massaging (or include "-MCarp=verbose" in the PERL5OPT Env.var )!!  :see perldoc  Carp

	_______:  Devel::Debug
##________________________________________  ___________________________


#####  ==========  dbg.configs/.inits/.options/starts :     perldoc-5.14.0/perldebug.html#Debugger-Customization
	- PERLDB_OPTS   environment variable
	- perldb :
		- .perldb may be in the current directory, or in the home directory.
		-! permissions must be 600 : it must be owned by the superuser or the current user, and writable by no one but its owner.
		- .perldb is processed before processing PERLDB_OPTS !!
		- comments with "#..."
		eg, setting Hist-options in .perldb:    parse_options("HistFile=dbgpl.hist  HistSize=100" );
		or other options:          parse_options("NonStop=1 LineInfo=db.out AutoTrace=1 frame=2");
		or define some aliases:    $DB::alias{'len'}  = 's/^len(.*)/p length($1)/';
		! set breakpoints on lines 4 and 6 immediately after debugger initialization:   push @DB::typeahead, "b 4", "b 6";
	- (PERL5DB ,but for more detailes changes to the debuger-invokation, /usr/lib/perl5/5.14.2/perl5db.pl ; see  perldebguts )
##________________________________________  ___________________________


#####  ==========  variables printing/....:
	--- printing vars:
		-! best (esp for hash...):  x \%h1  /OR  x $obj1  #if $obj1 is a hash;
		- x, v, p, X, V   : print vars; for diffs see perldebug
##________________________________________  ___________________________


#####  ==========  API/DB-package, coding DB-methods in your source: (executed if invoked "perl -d"):
	- set breakpoint here:        $DB::single=2;
##________________________________________  ___________________________


#####  ==========  regexp-debug:
	- see: 
		- perldebug.html#Debugging-Regular-Expressions
		- perldebguts.html#Debugging-Regular-Expressions
		- re.html  , perldoc re
	- perl -Dr ....      : If your perl is compiled with -DDEBUGGING , you may use the -Dr flag on the command line
	- use re 'debug' ; bzw,  use re 'Debug' with options...  #see perldoc re
	- use re qw(Debug MATCH);  #same.as:  use re  ("Debug", "MATCH");   #see more Debug-options in:  re.html#'Debug'-mode AND also there "SYNOPSIS"
##________________________________________  ___________________________


#####  ==========  OO-debugs / OO-methods-debugs:
	- see  perldoc-5.14.0/perltoot.html#Debugging-Methods
##________________________________________  ___________________________


#####  ==========  steps-/tips-perlHacks_ore:0603.chm--chapter.6:
	--- compilation errors finding:
		- check compiling:  perl -wc t1.pl  ; then run it.
		- Add the   __END__   somewhere (if error.line  not very clear,...) and run again
		  /OR with  =cut (POD-directive)  comment out only certain blocks/sections 
	- warn() instead print( ) because it goes to STDERR by default, which makes it redirectable separately.
	- chomp; : forgotten chomp() on $_ or STDIN is a common error!
	- 
##________________________________________  ___________________________


#####  ==========  Utils.Debug.helps, errors.helps:
	--- splain : explains the error messages of your script ; paste in your error message to it, and it'll explain it for you:
		- perl program 2>diag.out ;  splain [-v] [-p] diag.out
		- perl program  1>&2  |  splain [-v] [-p]   #but if no other ouputs, except errors! eg by compiling-errors
	--- diagnostics :   perldoc diagnostics
		- use diagnostics;
	--- errorno:   %! bzw. %ERRNO
		-!DIFF: $!  (latest vurrent error; What just now went bang?)   <-->  %!  (keys of all error-names and their values)
		- see  perldoc -v '%!'  ,  '$!' ; perldoc  Errno
		- Each element of "%!" has a true value only if $! is set to that value.
		- printout all errorno and their values:  print Data::Dumper::Dumper \%!;
		  all values are usu. Zero except if an error happened and the appropriate error-key ist set to a non-zero value!
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
