___________ perl regular.exp + reg.quickies.col / reg.oneliners : _________________

	_______:  see:
	-!! QRef: perlreref  +! its listing in "see-also" !!  perlreref ist the central-quick-ref-doc
	- perlretut , perlre , 
##________________________________________  ___________________________


#####  ==========  rules/notes/...:

	_______:  !! matching principals (greedy? alternate-options "|", ...):    perlretut.html :
	Principle 0: Taken as a whole, any regexp will be matched at the earliest possible position in the string.
	Principle 1: In an alternation a|b|c... , the leftmost alternative that allows a match for the whole regexp will be the one used.
	Principle 2: The maximal matching quantifiers ?, * , + and {n,m} will in general match as much of the string as possible while still allowing the whole regexp to match.
	Principle 3: If there are two or more elements in a regexp, the leftmost greedy quantifier, if any, will match as much of the string as possible while still allowing the whole regexp to match. The next leftmost greedy quantifier, if any, will try to match as much of the string remaining available to it as possible, while still allowing the whole regexp to match. And so on, until all the regexp elements are satisfied.
	Principle 3b: (updated considering non-greedy modifiers): If there are two or more elements in a regexp, the leftmost greedy (non-greedy) quantifier, if any, will match as much (little) of the string as possible while still allowing the whole regexp to match. The next leftmost greedy (non-greedy) quantifier, if any, will try to match as much (little) of the string remaining available to it as possible, while still allowing the whole regexp to match. And so on, until all the regexp elements are satisfied.

	_______:  !! $ (end.of.line-char)   <-->   \n   (new.line-char):
	-  $ occurs before "\n" ! so it matches:  "\n" =~ /^$/;    ##-because "$" anchors before "\n"  :see perlretut.html

	_______:  hints:
	-!! $`, $&, and $´ are tempting, but dangerous. Their very presence anywhere in a program slows down every pattern match because the engine must populate these variables for every match. 
	    instead use the variables @- and @+ for matched substrings ... !
##________________________________________  ___________________________


#####  ==========  Multiline.flag /.../m , multiline- and singleline-matchings; modifies /s and /m:
	-! see Perl_Cookbook_TomChristiansen_Ore_2ed_0308. --Recipe 6.6 Matching Within Multiple Lines 
	-! see perldoc-5.14.0/perlretut.html#Using-character-classes  +  devres-kk-exp :
	The two modifiers //s  and //m  affect two aspects of how the regexp is interpreted:
	1) how the '.' character class is defined, and
	2) where the anchors ^ and $ are able to match. Here are the four possible combinations:
		- no modifiers (//): Default behavior. '.' matches any character except "\n" . ^ matches only at the beginning of the string and $ matches only at the end or before a newline at the end.
		- s modifier (//s): Treat string as a single long line. '.' matches any character, even "\n" . ^ matches only at the beginning of the string and $ matches only at the end or before a newline at the end.
		- m modifier (//m): Treat string as a set of multiple lines. '.' matches any character except "\n" . ^ and $ are able to match at the start or end of any line within the string.
		- both s and m modifiers (//sm): Treat string as a single long line, but detect multiple lines. '.' matches any character, even "\n" . ^ and $ , however, are able to match at the start or end of any line within the string.
##________________________________________  ___________________________


#####  ==========  regexp-debug:
- see:  perldoc-5.14.0/perldebguts.html#Debugging-Regular-Expressions  bzw.  perldoc-5.14.0/perldebug.html#Debugging-Regular-Expressions
