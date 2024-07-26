___________________ perl-docs-nts: ______________________

	_______:  see  ref-docs-listings in:
	- perldoc perltoc
	--- abrv:
	- plo4		: Oreilly-Learning.Perl.4ed.2005 : first-basic-BK
	- pbyexp4	: Perl by Example, Fourth Edition : by Ellie Quigley
##________________________________________  ___________________________


#####  ==========  where-is-what/DIRs....:
	-!! perl -V ---> see a lot infos about curr-installed-perl !
	-! rpm -ql perl-doc > rpm_ql_perl-doc.log   --> -! perldoc-docs/pods in /usr/lib/perl5/5.12.3/pod   -->  perldoc  perltoc
	- man-pages of perl where??:  perl -V:man.dir    (output for vo17: /usr/share/man/man1 ...)
	- lib-modules   of perl where??:
	- zypper-check for perl stuff:    zypper  se -sd "*perl*edit"
##________________________________________  ___________________________


#####  ==========  perldoc/man/refDocs,...:
	-!! toc-of-perldocs / overview/ names of perldocs-html-chapters:
		perldoc  perl    (short) bzw.  ==  man perl
		perldoc perltoc  (very long/detailed toc-listing)
		perl.html#Reference-Manual
	-! html2text-perldocs/kk-grep-dir (mybe mktree before...):  ..../perldoc-5.14.0 $find . -iname "*.htm*"  -exec  html2text -width 109 -o ../perldoc-5.14.0__txt/{}.txt  {} \;
	--- perlfaq3-tips /perldoc-5.14.0/perlfaq3.html#How-do-I-do-(anything)?  :
		Basics			perldata, perlvar, perlsyn, perlop, perlsub
		Execution		perlrun, perldebug
		Functions		perlfunc
		Objects			perlref, perlmod, perlobj, perltie
		Data Structures	perlref, perllol, perldsc
		Modules			perlmod, perlmodlib, perlsub
		Regexes			perlre, perlfunc, perlop, perllocale
		Moving to perl5	perltrap, perl
		Linking w/C		perlxstut, perlxs, perlcall, perlguts, perlembed
		Various			http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz   (not a man-page but still useful, a collection of olddoc-essays on Perl techniques)
##________________________________________  ___________________________


#####  ==========  BigApps-/Modules-/LibsCreation-docs:
	- perldoc   perlmod  perlmodinstall  perlmodlib 
	- ImpatientPerl:  4 Packages and Namespaces and Lexical Scoping
	- IntermediatePerl_Ore_2ed_0603.chm : Ch.03 + 10 + 15
	- Perl by Example, Fourth Edition	: Chapter 12. Modularize It, Package It, and Send It to the Library!
	- Perl Best Practices : Chapter 17. Modules 
	- Learning Perl Objects, References & Modules By Randal L. Schwartz : Chapter.02+12
##________________________________________  ___________________________


#####  ==========  Autoloading + runtime-method-definitions dynamically docs:
	- IntermediatePerl_Ore/intermediateperl-CHP-14-SECT-3.html
	- perldoc AutoLoader + SelfLoader
