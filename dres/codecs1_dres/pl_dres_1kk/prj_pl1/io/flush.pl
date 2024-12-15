#!/usr/bin/perl -W
##--flushing buffers , see perldoc-5.14.0/perlfaq5.html
#	STDERR is usu. anyway unbuffered by default.
#	try this with moving the while-block before unbuffering-block and see the difference!
#	newline "\n" does also the unbuffering.
#
use warnings;
use strict;

##--use Smart::Comments -ENV;  ##--II-  call it by: perl '-MSmart::Comments=###-d-' tpl2.pl
###-d- =====----- Start:  __PACKAGE__ . " called by " . $0 . " -----====="

########## 
my $count=0;

##-- now should alternate . and +
print "\n--- buffered output: ----\n";
while( $count < 16 )
{
	sleep 1;
	print STDOUT "-- $count out -- ";
	##- print STDERR "err.";   ##STDERR is usu. anyway unbuffered.
	print STDOUT " ===\n" unless  ++$count % 4;
}

##-- unbuffering two filehandles:
{
	my $previous_default = select(STDOUT);  # save previous default
	$|++;                                   # autoflush STDOUT
	select(STDERR);
	$|++;                                   # autoflush STDERR, to be sure
	select($previous_default);              # restore previous default
}

##-- now should alternate . and +
print "\n--- UNbuffered output: ----\n";
$count=0;
while( $count < 16 )
{
	sleep 1;
	print STDOUT "-- $count out -- ";
	##- print STDERR "err.";
	print STDOUT " ===\n" unless  ++$count % 4;
}

##############################


#print "\n-------\n";
###-d- =====----- END:     __PACKAGE__ . " called by " . $0 . " -------====="
1;
__END__
######################################################################

