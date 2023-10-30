#!/usr/bin/perl -w
#
use strict;

################### call: perl -i $0  t1.txt
while(<ARGV>){   # Open ARGV for reading
	tr/a-z/A-Z/;
	print;    # Output goes to file currently being read in-place
	close ARGV if eof;
}



__END__
############## byExp--Ch.10s:
#
#
##################################
##################################
##################################
while(<>){
print "$. :\t$_";
if (eof){ print "-" x 30,  " EOF of $ARGV --\n"; close(ARGV); }
}

##################################
unless ( $#ARGV == 0 ){ die "==## Usage: $0 <argument>: $!\n"; }
open(PASSWD, "t1.txt") || die "Can't open: $!";
our $username=shift(@ARGV);
while(my $pwline = <PASSWD>){
unless ( $pwline =~ /$username:/){ die "$username is not a user here. $. -- $pwline --\n";}
}


##################################
die "$0 requires an argument.\n" if $#ARGV < 0 ; # Must have at least one argument
print "@ARGV\n";      # Print all arguments
print "$ARGV[0]\n";   # Print first argument
print "$ARGV[1]\n";   # Print second argument
print "There are ", ($#ARGV + 1) ," arguments.\n"; # $#ARGV is the last subscript
print "$ARGV[$#ARGV] is the last one.\n";  # Print last arg

##########
#while (<ARGV>) { print "\n -------------- $ARGV :" ; print; };
print "@ARGV\n";      # Print all arguments
