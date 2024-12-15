__________ POds/Docs.Writongs in perls _______________________
##________________________________________  ___________________________


#####  ==========  modules for PODs:
	-! usage/help-text for your module, directly from the modules pod:   use Pod::Usage;
		- printing out your modules-pod fully, as usage/help:
		use Pod::Find qw(pod_where);    pod2usage( -input => pod_where({-inc => 1}, __PACKAGE__) );   #-see perldoc Pod::Usage
	-! testing your PODs:  Test::Pod
	- Pod::*
##________________________________________  ___________________________


#####  ==========  Utils/cmds for PODs:
	-  podchecker command is provided for checking Pod syntax for errors and warnings. 
	- pod<TAB> : pod2html    pod2man     pod2text    podchecker  podselect   pod2hpp     pod2latex   pod2.pl     pod2usage   podlint
