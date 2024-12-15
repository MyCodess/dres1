#
##	USAGE:  call this source-filter-package by
#	DebugComments1.pl   /OR 
#	best:  comment out "use DebugComments1"-statement there and call it by:   perl -MDebugComments1  DebugComments1.pl   /OR
#		perl -MDebugComments1=##-d  DebugComments1.pl  #to redefine the debugSymbol to you own one!
#	perl -MDebugComments1 -e 'BEGIN { $DebugComments1::ds = "##-d";} ; do  "DebugComments1.pl" or die $!'
#
#	"use DebugComments1;" in that script, makes possible, writing debug-lines in the source code as comment-lines starting with "##__ "
#	debug-lines may contain any legal "print"-params. Anything after "##__ " will be passed to a print-statement!
#	eg:  ##__ "--v1: " , $v1 , " --a1: ", "@a1"
#
#	you could set your own debugging-symbol for your code, eg to "##-d", by:  BEGIN { $DebugComments1::ds = "##-d";}

package DebugComments1;
use strict;
use warnings;

#__ print "\n---Start--- " , __PACKAGE__ . " --called from: $0 ----------\n";
use Filter::Simple;
our $ds = "##__" unless defined $ds ;  ##--II- ds == Debug-Symbol  ; for your own debug-symbols, redefine this as:    BEGIN { $DebugComments1::ds = "#myDebugSymbol";}

FILTER {
	##__ print "\n---Args: ", @_ ;  ##--!!- first-arg/$_[0] is the packagename!! 
	#shift;  ##--II- packag.name parameter is NOT needed, so just skip it.
	$ds = $_[1]  if defined $_[1];     ##--II- so in the use-stmt the user could redefine the debugSmbol by eg:  use DebugComments1 "##-d";
	s/^${ds}\s*(.*)/print "\n___ ", ( $1 );/gm;
};  ##--II-  !! the semicolon here is ABSOLUTELY needed! otherwise FILTER will NOT be executed!!

#__ print "\n---END----- " , __PACKAGE__ . " --called from: $0 ----------\n";
1;  ##--II-  !! the 1; here as last line is ABSOLUTELY needed!
#############################################################
__END__
##--II-:  nts:
#----- short-filter-package:
#	instead FILTER sub, this package could be shotened, for smaller FILTER, to:
#	use Filter::Simple sub { s/^##__\s*(.*)/print "\n___ ", ( $1 );/gm; };
#	see perldoc Filter::Simple
#-----
#
