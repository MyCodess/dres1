#!/usr/bin/perl -W

use warnings;
use strict;
our $verbose = 2; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

##########  DB.connect + Select.query-1:
use DBI;
use Data::Dumper;
my $driver="DBI:mysql";
my $host="127.0.0.1";
my $database="world";
my $dbusername = 'dbu1';

#my $dns = 'DBI:mysql:database=world;host=localhost;port=3306';
#my $dns = 'DBI:mysql:database=world;host=127.0.0.1;port=3306';
my $dns = "${driver}:database=${database};host=${host};user=${dbusername}";
print "\n-- conneting to $dns : --------\n";
#
#my $sql1 = q{select * from City where CountryCode like 'IR%' order by 'Name';};
my $sql1 = q{select Name, Capital, LocalName, Population  from Country where Continent='Oceania';};
my $dbh;
my $sth;

#my @drivers = DBI->available_drivers();
#$dbh = DBI->connect('DBI:mysql:world', 'dbu1') or die "==##==Fatal-Error: can not connect DB";
#$dbh = DBI->connect('DBI:mysql:database=world;host=localhost;port=3306', 'dbu1') or die "==##==Fatal-Error: can not connect DB";
$dbh = DBI->connect($dns, $dbusername, "", { RaiseError => 1, PrintError => 1, AutoCommit => 0 })  or die "==##==Fatal-Error: can not connect DB" . DBI->errstr;
$sth = $dbh->prepare($sql1)  or die "==##==Fatal-Error: prepare sql1 failed: " . $dbh->errstr;
$sth->execute() or die "==##==Fatal-Error: execute sql1 failed: " . $dbh->errstr;;
#while ( my @row = $sth->fetchrow_array ) { print "@row\n"; }
$sth->dump_results();
$sth->finish();
$dbh->disconnect();



##############################


########## Tests-Debugs-Verbose: #####################################
#print "\n-------\n";
if ($verbose > 3 ) {
}
if ($verbose > 1 ) { print "\n" . ':' x 20 , __PACKAGE__ . " -- called from: $0 --END::::::\n"; }
1;
__END__
######################################################################
#print "-- @drivers --\n";
