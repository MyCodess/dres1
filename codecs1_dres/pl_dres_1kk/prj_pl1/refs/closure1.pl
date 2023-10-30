#!/usr/bin/perl

use warnings;
use strict;
our $verbose = 2; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 

our $ref1;

if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

##--II- closures maintain their "my"-values in their block associated with an anonymous sub!!:
##--    Variations here: not.Named , named, with.params closures
##--	for OO.closurs see /perldoc-5.14.0/perltoot.html#Closures-as-Objects

####### closure--not.named: #######################################
##--II- in noName-Variation, then the pointer to the inner anonymous sub (here $ref1) MUST be a package/global var, so that you do have a REF pointing to it!!
print "\n========== closure--anonymous/not.named ===========\n";
my $name="global-name";
{   my $name = "-name-1-";  # Lexical variables
	my $age = 86;
	my $counter = 1;
	$ref1 = sub{ print "$name is $age. ";  $name = "-name-2-" ; ++$age; return $counter++;};  # anonymous subroutine
}
print &{$ref1} . " --\n"; # Call to subroutine outside the block
print &{$ref1} . " --\n"; # Call to subroutine outside the block
print &{$ref1} . " --\n"; # Call to subroutine outside the block
print "$name is back\n";


####### closure--named: ############################################
print "\n========== closure--named =========================\n";
sub s1(){
	my $name = "-name-3-";  # Lexical variables
	my $age = 50;
	my $counter = 1;
	my $ref2 = sub{ print "$counter : $name is $age.\n";  $name = "-name-4-" ; ++$age; return $counter++;};  # anonymous subroutine
	return $ref2;
}
my $closure2 = &s1();
&$closure2();
&$closure2();
&$closure2();
print "$name is back\n";


####### closure--named.with.params: see perlref ####################
##--II- ONLY my-vars in the BLOCK (here $x) are maintained, for EACH invokation, NOT the ones inside the anonymous sub (here $y) !!
print "\n========== closure--named.with.params =============\n";
sub newprint {
	my $x = shift;
	return sub { my $y = shift; print "$x, $y!\n"; };
}
my $h = newprint("Howdy");
my $g = newprint("Greetings");
# Time passes...
&$h("world");
&$g("earthlings");


#print "\n-------\n";
############# Tests-Debugs-Verbose:
if ($verbose > 3 ) {
}
if ($verbose > 1 ) { print "\n" . ':' x 20 , __PACKAGE__ . " -- called from: $0 --END::::::\n"; }
1;
