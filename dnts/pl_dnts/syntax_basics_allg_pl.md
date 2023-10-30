_________ perl-basic.allgemin.syntax : loops/if/while/..., subs-definitions, ... : __________
-! perldoc  perlsyn , perlop   (+parts.of perldata, perlvar, perlsyn, perlop, perlsub)
##________________________________________  ___________________________


#####  ==========  Syntax.allg:
	- Operators-Precedence :see perlop !!
	-!! TIP: perl.shell/quick.interactive.trys:    perl -de 42   -->then just enter any perl stuff and try quick onliners...
		-! also TAB works there!! so in debug-prompt, eg:  DB<XX> print %main::<TAB>  ---> shows symbol.table.keys
##________________________________________  ___________________________


#####  ==========  operators.misc (notes from perlop for misc-operators):
	- "=>"  : => operator is a synonym for the comma except that it causes its left operand to be interpreted as a string ... #see  perldoc-5.14.0/perlop.html#Comma-Operator
##________________________________________  ___________________________


#####  ==========  "if" / conditionals/ ... : see perlfunc.html#Alphabetical-Listing-of-Perl-Functions
	-! see  perldoc -f -X   /bzw.  perldoc-5.14.0/functions/-X.html
	- -X : for testing if file/filehandle readable/writable/executable/... see listing in perlfunc.html#Alphabetical-Listing-of-Perl-Functions
##________________________________________  ___________________________


#####  ==========  defined/undef/true-false/...:
	- see perldoc -f undef , -f defined , perlsyn , -f exists , perlsyn.html#Truth-and-Falsehood
	-!! TEST.it:
		perl -lwe 'my $a1=0;  print defined $a1 ? "__def.a1": "__undef.a1"; print "__true.a1" if ($a1);'
		do.it with:  $a1; $a1=""; $a1="0"; $a1=0; and also not.defined:
		so:  $a1=""; $a1="0"; $a1=0;   are boolean false, BUT are defined !!  the rest is undefined AND also boolean false!
		for arrays test.it:  perl -lwe 'my @a1=();  print  @a1 ? "__def.a1": "__undef.a1"; print "__true.a1" if (@a1);'
	-!! DIFF/DEFF:   true/false-values   <-->   defined/"undef"-value :
		- "defined"       is always also "true"  BUT NOT vice versa!
		- "undef"-value   is always also "false" BUT NOT vice versa!
		- true/false:   $var=0/""/"0" are ALL false, but NOT undefined"undef"!!  "defined $var" returns true!! it is defined!!
		- "undef"-/"undefined"-value  bzw.  defined-/undef-funcs:
		- $a1=""; $a1="0"; $a1=0   are boolean false, but NOT "undef"! they are all defined!!
		- simple Boolean test will NOT distinguish between "undef" and 0/""/"0"/(). All are false!! but the latests NOT undefined!!
	--- true/false:
		- true/false?:  false are 0, "0", "", (), undef  ; All other values are then "ture"!
		  the number 0, the strings '0' and '' , the empty list () , and undef are all false in a boolean context. All other values are true.  ;see  perlsyn.html#Truth-and-Falsehood
		- When "false" evaluated as a string it is treated as '' , but as a number, it is treated as 0.
	--- defined/undef-funcs:
		-!! DIFF:  "undef param1"-func will UNDEFINES param1 !! BUT  "defined param1"-func ONLY evaluates param1, if it is defined!!!
		- undef EXPR   :   Undefines the value of EXPR, (do NOT use it for Hash; take "delete" instead). Always returns the undefined value.
			undef (with no EXPR) just returns "undefined"-value (eg at end of a sub).   :see perldoc -f undef
		- defined EXPR :   Returns true if EXPR is NOT undefined/"undef".valued (so is somehow defined, even "",0,.. are not undefined)  ;see perldoc -f defined
			!! This function allows you to distinguish "undef" from other values.  (A simple Boolean test will not distinguish among "undef", zero, the empty string, and "0", which are all equally false.
		-!! Arrays/hashed-defined:   "defined"-func NOT needed:
			"defined" on aggregates (hashes and arrays) is deprecated.   ;see  perldoc  -f defined 
			for arrays you do NOT need "defined @a1 ...."; just do "if (@a1)..." /OR "@a1 ? "__def.a1": "__undef.a1; ..."
			"my @a1=()" OR just "my @a1;"  are  undef and false!
##________________________________________  ___________________________


#####  ==========  Blocks, }-mnemics, ...:
	- +{ bzw. {;  :The leading +{ and {; always serve to disambiguate the expression to mean either the HASH reference, or the BLOCK. see perlref
##________________________________________  ___________________________


#####  ==========  Loops:
	-! see perlsyn.html  +  perldata.html + perlop
	--- foreach:
		- foreach keyword is actually a synonym for the "for"-keyword, so you can use foreach for readability or for for brevity.
		-! foreach (@array[ 4 .. 10 ])     { s/peter/paul/ }   ;see perldata
		-! foreach (@hash{qw[key1 key2]})  { s/peter/paul/ }   ;see perldata
	--- next/last/redo/break/continue in loops with a continue-block   :see perlsyn.html#Loop-Control :
			condition-evaluation	continue-block-execution
		next	yes		yes		:just starts the next iteration of the loop
		last	no		no		:immediately exits the loop in question
		redo	no		no		:restarts the loop block without evaluating the conditional again AND without executing the continue-block!
		break
		continue
	--- for
		-! Range-Operators with for:   #see perldoc-5.14.0/perlop.html#Range-Operators
			for (1..5) {print}; 
			for ("a".."d") {print};  #so, also with strings
			for ("aa".."ad") {print};  /OR  for ("ag".."cl") {print};
##________________________________________  ___________________________


#####  ==========  symbol.tables:       perldoc-5.14.0/perlmod.html#Symbol-Tables :
	- see also  pl_quicks-nts
	-! current-main-symbol.tables-printout (visible in curr-main-scope):
		while(($key, $value) = each (%main::)){ print "$key:\t ====> \t$value\n"; }   # Look at main's symbol table : Example 12.1--pbyexp4
		-!! also in any debug-prompt in bash:  perl -de 42  -->then:  DB<XX> print %main::<TAB>  -->you see keys-of-main.symbol.table /OR just enter the full onliner above.
	-! accessing/manipulating the package's symbol-table needs {no strict "refs"; ... }
	-! very-comprehensive, including all used packages:   use Dumpvalue; my $dumper = Dumpvalue->new; $dumper->set(globPrint => 1); $dumper->dumpValue(\*::);  #-see perldoc Dumpvalue
		/OR only main:  $dumper->dumpvars('main');
##________________________________________  ___________________________


#####  ==========  subs/funcs definitions:  see  perlsub :
	-! DIFF:  sub-arguments are in @_  !! so do NOT confuse with @ARGV  !!
	-! prototype: To call subroutines that have been declared with a prototype, the ampersand (&) MUST be omitted, or the subroutine will be treated like a normal user-defined subroutine rather than as a built-in, and the compiler will ignore the prototype. : Perl by Example--4ed--11.2.1. Prototypes 
	-! Subroutines whose names are in all upper case are reserved to the Perl core, as are modules whose names are in all lower case. A subroutine in all capitals is a loosely-held convention meaning it will be called indirectly by the run-time system itself, usually due to a triggered event.  perldoc-5.14.0/perlsub.html
	--- params/arguments:
		-! default values for params: sub f1(a,b) {my $a = $a || 5; ... }
		-!! array/hash-arg is passed-by-ref !! so NO copy or pass-by-value!! BUT may pass ONLY one list-arg (array/hash) and ONLY as the last arg!:
		  the first list-arg will soak up anything after it! for more than one list-arg, just pass them as pointer \@a1 or \%h1 !!
		  perl -wle 'my @a1=(10..14); print "@a1"; sub s1 {print "--sub.1:  @_"; $_[1]="XX"; print "--sub.2:  @_";}; s1(@a1); print "@a1";'
