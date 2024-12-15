#!/usr/bin/perl -w
##--II- from:  perldoc-5.14.0/perltoot.html#Constructors-and-Instance-Methods
#	with class.data-access from the instance by REFs
#	call eg, debug all classes:     pldbg=5  Person.pm   /OR 
#	call eg, debug class Person: :  perl -e '$Person::dbg=3 ;  do "Person.pm" or die $! , $@;'
#	!! here ist class-debugging! for per instance-debugging see  /perldoc-5.14.0/perltoot.html#Debugging-Methods

package Person;
use warnings;
use strict;

############# class.data:
my $Census = 0;  #- counter of number of active instances

############# debugging (class.global.debugging):
##--II- debug flag either for all classes by $ENV{"pldbg"} OR only this class by $dbg=XX
#	?2do? sub debugit($)  to access this debug.class.member?:
our $dbg=$ENV{"pldbg"} unless defined $dbg ; $dbg += 0;


##################################################
## the object constructor, WITH class.data-access as reference:
##################################################
sub new {
	my $class = shift;
	my $self  = {};
	$self->{NAME}     = undef;
	$self->{AGE}      = undef;
	$self->{PEERS}    = [];
	$self->{"_CENSUS"} = \$Census;      # "private" class.data
	#$self->{"DBG"} = 0;     #if pro-instance-debug-flag needed!? but basically not!
	++ ${ $self->{"_CENSUS"} };
	if ($dbg > 2) {print "__ " , ${$self->{"_CENSUS"}} , ". Obj was creted!\n"}   #{ while ( my ($key, $value) = each %$self ) {print "$key => $value\n"; } }
	bless ($self, $class);
}

##############################################
## methods to access per-object data        ##
##                                          ##
## With args, they set the value.  Without  ##
## any, they only retrieve it/them.         ##
##############################################
sub name {
	my $self = shift;
	if (@_) { $self->{NAME} = shift }
	return $self->{NAME};
}

sub age {
	my $self = shift;
	if (@_) { $self->{AGE} = shift }
	return $self->{AGE};
}

sub peers {
	my $self = shift;
	if (@_) { @{ $self->{PEERS} } = @_ }
	return @{ $self->{PEERS} };
}

sub population {
	my $self = shift;
	if (ref $self) { return ${ $self->{"_CENSUS"} }; }
	else { return $Census; }
}

sub DESTROY {
	my $self = shift;
	if ($dbg > 2) {print "__ " , $self->name , " was destroyed!\n"}   #{ while ( my ($key, $value) = each %$self ) {print "$key => $value\n"; } }
	-- ${ $self->{"_CENSUS"} };
}


############### kk:
if ($dbg > 0) {&test1();}  ##--II- actually should depend on a test.flag, but here just as example for debugging mechanism!
sub test1(){
	my $myclass = __PACKAGE__ ;
	my  $_objname;
	no strict 'refs';
	for (my $ii=1; $ii <6 ; $ii++){
		$_objname= "obj" . $ii;
		${$_objname} = ${myclass}->new();
		$$_objname->name("name$ii"); $$_objname->age($ii +10); $$_objname->peers(qw(p1 p2 p3));
		local $,=" -- "; print  "__ $_objname " , __PACKAGE__ , $$_objname->name , $$_objname->age , $$_objname->peers ,  $$_objname->population . "\n";
	}
}
1;  # so the require or use succeeds
