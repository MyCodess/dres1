__________ perls-quickiess/oneliners(1-5-liners)/very.short.code.snippets: _________________
- for longer code-parts see codesColl_devres in    /up1/w/docs_m/devres/codesColl_devres/perlsColl_devres
  here only shorties (1-5-liners or so)
##________________________________________  ___________________________


#####  ==========  properties.files into perl (shell.ENV.config.files into perl):
	---! kk-default:
		- set default values in a config file and read it into your pl-scripts
		- allow overwriting the defaults by individuell ENV-vars by: checking %ENV for eventuell existing keys of your default-params!
	- reading from file format: LEAD=fred FRIEND=barney,  so per line are several settings permitted.
		so converting properties into Array.of.Hashes   :see perldoc-5.14.0/perldsc.html#Generation-of-an-ARRAY-OF-HASHES :
		while ( <> ) { $rec = {}; for $field ( split ) { ($key, $value) = split /=/, $field; $rec->{$key} = $value; } push @AoH, $rec; }
	--- properties-files-/shell-ENV-files-sourcing, so read f1.props into a perl-prog and set the vars appropriately (interface between perl-prog and system or other progs!):
		(f1.props as: aa=xx , bb=yy ,.. ; each in own line; ignore comments as ^#...):
		perl -wle 'open(CFG1, "./f1.props") || die("cant open datafile: $!"); while (<CFG1>) { eval ("\$$_") unless (/^#/);} ; close (CFG1); print "$aa --- $bb";'
##________________________________________  ___________________________


#####  ==========  symbol.table printout-quickies:   current-main-symbol-tables-printout (visible in curr-main-scope):
		- see  perlmod.html  in refs: perldoc-5.14.0/perlmod.html
		- see  perl.by.exp Example 12.1.
		- {no strict 'refs'; while ( (my $n1, my $v1) = each %{ __PACKAGE__ . '::'} ) {print "$n1 == $v1\n"} }
		  print "\n------------------------------------------------___________\n";
		  {no strict 'refs'; while ( (my $n1, my $v1) = each %{"PL1::Data1::"} ) {print "$n1 == $v1\n"} }
		- {no strict; while(($key, $value) = each (%main::)){ print "$key:\t$value\n"; } }  # Look at main's symbol table of current main: Example 12.1--pbyexp4
		- /OR print Dumper \%main:: ;  /OR: for MyModule.pm: \%MyModule:: ; /OR certain var: $MyModule::v1 
		- for another package scope, replace %main:: with: %mypackage::
			print $mypack::myvar ; /OR for an array: print @mypack::myarray
##________________________________________  ___________________________


#####  ==========  Scalars, Scalar-DataTypes/-Data-Conversions, Array/hash/scalars...:
	- $var1 ist/contains a number??  :see perldoc-5.14.0/perldata.html#Scalar-values
##________________________________________  ___________________________


#####  ==========  libs-adds / INC...:
##________________________________________  ___________________________


#####  ==========  perl-cmdline/-shell-invoke-quickies: (see man perlrun)
	-! user-stdin-eingaben hintereinander testen,probieren:   perl -ln -e 'chomp; print "$_";' ##replace print-cmd with your test-stuf ....
	-!! replace xxx by yyy in myfiles* (rep.sh):    perl -p -i.bak -w -e 's/xxx/yyy/g' myfiles*
	---! INC-quick-listing / lib-dirs-currently??:
		- perl -wle  'print for (@INC) ;'      ##OR longer:   perl -e 'foreach (@INC) { print "$_\n" ;}'
		- perl -V     -->  see  @INC values  (or -VV for more details,....)
		- perl -wle  'print join qq/\n/, @INC;'
		- perl -we   'print "---INC-entries: @INC";'  | tr ' ' '\n'
	-! new-libs-including-test:     perl -W -e 'do "PL1/Data1.m" ; print "==## $@ -- $! --\n" if $!;'
##________________________________________  ___________________________


#####  ==========  IO/stdin-stdout,...:
	-- reading whole file into a var and eval/execute it: /IntermediatePerl_Ore/intermediateperl-CHP-10-SECT-2.html :
		sub load_common_subroutines {
		  open MORE_CODE, 'navigation.pm' or die "navigation.pm: $!";
		  undef $/; # enable slurp mode
		  my $more_code = <MORE_CODE>; close MORE_CODE;
		  eval $more_code  or die $@ if $@;
		}
	--- 
##________________________________________  ___________________________


#####  ==========  plerl-std-utils:
	- html2text-perldocs: .../perldoc-5.14.0 $find . -iname "*.htm*"  -exec  html2text -width 109 -o ../perldoc-5.14.0__txt/{}.txt  {} \;
##________________________________________  ___________________________


#####  ==========  apaches: vo17.suse.114--1108-setup-manually:
	-! manualy build+installed with: ./configure --prefix=/up1/optu/apache2 ; make ; make install ;
	- start: u1@vo17:/up1/optu/apache2/cgi-bin $/up1/optu/apache2/bin/apachectl -k start
##________________________________________  ___________________________


#####  ==========  sed with perl:
	- in-place substitutions from cmdline:  perl -pi.org  -e "s/oldstring/newstring/g;" *.c
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
--######################## regexps-quickies-onliners: ######################################
	-- repeated/double/redundant words /typo (eg 3 letters as '... the the ...'):   /(\w+)\s+\g1/g;   #as in printout:
		my $v1="abc adsfas the the me me adsf asdf";  my @regs1=($v1 =~  /(\w+)\s+\g1/g); $\="\n"; for (@regs1) {print}; 
	-- dateformat: finding/interpreting right date format of a String from a choice of 3 variations:
	 file:///up1/varu/varau/plvar/docsvar/perldoc-5.14.0/perlretut.html#Named-backreferences
	$fmt1 = '(?<y>\d\d\d\d)-(?<m>\d\d)-(?<d>\d\d)';
	$fmt2 = '(?<m>\d\d)/(?<d>\d\d)/(?<y>\d\d\d\d)';
	$fmt3 = '(?<d>\d\d)\.(?<m>\d\d)\.(?<y>\d\d\d\d)';
	for my $d qw( 2006-10-21 15.01.2007 10/31/2005 ){
		if ( $d =~ m{$fmt1|$fmt2|$fmt3} ){
			print "day=$+{d} month=$+{m} year=$+{y}\n";
		}
	}
	-- Title-Cased converting:   $capword  = =~ s/(\w+)/\u\L$1/g;
--####################### misc.coll.quickies.onliners.pl : ################################
	- return.value-for BOTH list+scalar-expected:     return (wantarray ? (undef, $errmsg) : undef) if $they_blew_it;
