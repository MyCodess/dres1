#!/usr/bin/perl -Wl
##--II-	see:  perldoc-5.14.0/perltooc.html#Translucent-Attributes
#	class with tranparent/default inheritable values for objects

use warnings;
use strict;
no strict 'refs';  ##-kk
our $verbose; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
$verbose = 2 unless defined $verbose ;  ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

##########
{
	package Vermin;
# here's the class meta-object, eponymously named.
# it holds all class attributes, and also all instance attributes 
# so the latter can be used for both initialization 
# and translucency.
	our %Vermin = (   		# our() is new to perl5.6
		PopCount => 0,		# capital for class attributes
		color    => "beige",    # small for instance attributes		
	);
# constructor method
# invoked as class method or object method
	sub spawn1 {
		my $obclass = shift;
		my $class   = ref($obclass) || $obclass;
		my $self = {};
		bless($self, $class);
		$class->{PopCount}++;
		# init fields from invoking object, or omit if 
		# invoking object is the class to provide translucency
		%$self = %$obclass if ref $obclass;
		return $self;
	} 
# translucent accessor for "color" attribute
# invoked as class method or object method
	sub color {
		my $self  = shift;
		my $class = ref($self) || $self;
		# handle class invocation
		unless (ref $self) {
			$class->{color} = shift if @_;
			return $class->{color}
		}
		# handle object invocation
		$self->{color} = shift if @_;
		if (defined $self->{color}) {  # not exists!
			return $self->{color};
		} else {
			return $class->{color};
		} 
	} 
# accessor for "PopCount" class attribute
# invoked as class method or object method
# but uses object solely to locate meta-object
	sub population {
		my $obclass = shift;
		my $class   = ref($obclass) || $obclass;
		return $class->{PopCount};
	} 
# instance destructor
# invoked only as object method
	sub DESTROY {
		my $self  = shift;
		my $class = ref $self;
		$class->{PopCount}--;
		##-- print "__destroyed: " .  $self->color;
	}

##### more:
# detect whether an object attribute is translucent
# (typically?) invoked only as object method
	sub is_translucent {
		my($self, $attr)  = @_;
		return !defined $self->{$attr};  
	}
# test for presence of attribute in class
# invoked as class method or object method
	sub has_attribute {
		my($self, $attr)  = @_;
		my $class = ref($self) || $self;
		return exists $class->{$attr};  
	}
}
##############################

########### tests:
no strict;
use Data::Dumper;
#print Data::Dumper::Dumper {aa=>1,};
our $obj1=Vermin->spawn1;
print ref($obj1);
print Data::Dumper::Dumper  $obj1;



########## Tests-Debugs-Verbose: #####################################
#print "\n-------\n";
if ($verbose > 3 ) {
}
if ($verbose > 1 ) { print "\n" . ':' x 20 , __PACKAGE__ . " -- called from: $0 --END::::::\n"; }
1;
__END__
######################################################################

