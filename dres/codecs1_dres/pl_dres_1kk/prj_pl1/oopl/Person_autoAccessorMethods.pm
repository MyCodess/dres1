package Person;
##--II- auto.generated.getter.setter.methods for OO-classes   :see perldoc-5.14.0/perltoot.html#Autoloaded-Data-Methods
#	kk: BUT so works only scalars. so needs modifications for arrays (eg @peers here in %fields)
#	also warnings by clean-up/garbage.collector, due to DESTROY auto.call. so why kk added DESTROY to %fields.
#	!! not really great! disouraged/corrected in the later perldocs!!
#
use strict;
use warnings;
use Carp;
our $dbg=$ENV{"pldbg"} unless defined $dbg ; $dbg += 0;

our $AUTOLOAD;  # it's a package global
my %fields = (
	name        => undef,
	age         => undef,
	peers       => undef,
	DESTROY     => undef,         ##--II- kk.added due to warnings! ok?
);

sub new {
	my $class = shift;
	my $self  = {
		_permitted => \%fields,
		%fields 
	};
	bless $self, $class;
	return $self;
}

######## autogenerating of getter+setter-methods for all permitted fields in  keys %fields bzw. _permitted :
sub AUTOLOAD {
	my $self = shift;
	my $type = ref($self) or croak "$self is not an object";
	my $name = $AUTOLOAD;
	$name =~ s/.*://;   # strip fully-qualified portion
	unless (exists $self->{_permitted}->{$name} ) {
		croak "==##== Can't access `$name' field in class $type";
	}
	if (@_) {
		return $self->{$name} = shift;
	} else {
		return $self->{$name};
	}
}

##- sub DESTROY { my $self = shift; if ($dbg > 2) {print "__ " , $self->name , " was destroyed!\n"}   #{ while ( my ($key, $value) = each %> }

########################################################
############### kk:
if ($dbg > 0) {&test1();}  ##--II- actually should depend on a test.flag, but here just as example for debugging mechanism!
sub test1(){
	my $myclass = __PACKAGE__ ;
	my  $_objname;
	no strict ;#'refs';
	for (my $ii=1; $ii <6 ; $ii++){
		$_objname= "obj" . $ii;
		${$_objname} = ${myclass}->new();
		$$_objname->name("name$ii"); $$_objname->age($ii +10); $$_objname->peers(qw(p1 p2 p3));
		local $,=" -- "; print  "__ $_objname " , __PACKAGE__ , $$_objname->name , $$_objname->age , $$_objname->peers . "\n";
	}
}

1;
