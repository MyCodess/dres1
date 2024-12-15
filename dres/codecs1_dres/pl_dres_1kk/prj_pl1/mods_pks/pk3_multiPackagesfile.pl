#!/usr/bin/perl -w
##--Package declarations (in the same file), var-scopes, brakets {}, ...
##	!! see in  0devNts/pl/pl_modlibs_use_req_xxx.txt  section: "--- MULTIPLE.packages-in-a.Single.File"

use warnings;
#use strict;

print "\n" . '=' x 40 . "\n";
##-- These variables are in package main BUT have file-scope (not main-scope, so accesible in the whole file)!!
#	!! see in  0devNts/pl/pl_modlibs_use_req_xxx.txt  section: "--- MULTIPLE.packages-in-a.Single.File"
#	better: use {} in addition to package-keyword, for package-scope-definition!! an here for "freiend"-package! (also do for "main" if several packages in same file!)
our $name="nameMain";     
our $num=100;

##=============================
package friend;
{ # Package declaration
	our $name="nameFriend";
	sub welcome {
		print "-- Welcome $name!\n";
		print "\$num is $num.\n";    # Unknown to this package
		#print "Where is $main::name?\n\n";
	}
}

##=============================
package main;        # Package declaration; back in main
&friend::welcome;    # Call subroutine
print "Back in main package \$name is $name\n";
print "Switch to friend package, Bye ",$friend::name,"\n";
print "Bye $name\n\n";


##=============================
package birthday;     # Package declaration

my $name="Beatrice";
print "Happy Birthday, $name.\n";
print "No, $::name and $friend::name, it is not your birthday!\n";

print "\n-------\n";

##=============================
package main;        # Package declaration; back in main
our $wel = &friend::welcome;
{$wel};

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
