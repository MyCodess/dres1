_________ info-usage _____________________________________________
--#################  usage of info: shortcuts/helps/cmds/....##########################

	_______:  see:
	-!! REFs/index-listings:
		info info ---> goto index !! : alphabetical listing of all the commands, variables, and topics
		info --> "h"  : Keys/shotcuts
	-!! keys-emulations : default is emacs, but if invoking "info --vi-keys" is vi-emulated !!!
	-!! abort-key for commands,..:  C-g  (as ESC in vi) bzw. C-u in vi-like
	-!! completion in Echo-Area: default TAB /vi-like: space !
	-!! diff: nodes (predefined structure, visible on the top)  <-->  menus (jump-point-entries inside the page with *)

	_______:  helps-/manuals-invokation:
	!! info info ---> goto index !! : alphabetical listing of all the commands, variables, and topics
	man info
	info -h  bzw. in info, then "h" ( then x for exit /OR C-x 1 : only h-window)
	info info
	info info-stnd  (OR info info :comprehensive Tutorial, but then mixed with emacs stuff!!)
	info --subnodes -o out.txt info-stnd  ##---> write entire "info info-stnd" to the file out.txt, including its subnodes!
	info --subnodes -o tar.info.txt  tar  ##---> write entire "info tar"  to the file tar.info.txt, including its subnodes!
	q bzw. :q  quit whole info
	x bzw. C-x 0 : close curr.win
	-- more:
	info -vi-keys xxx : binds functions to keys differently, to emulate the key bindings of `vi' and Less. (default keys are Emacs!!)
	konqueror:   info:tar
	abort-key for commands,..:  C-g  (as ESC in vi) bzw. C-u in vi-like
##________________________________________  ___________________________


#####  ==========  scrolling/browsing/blättern/back-u-forth/tree-reversing/...:
	--- page-scrolling/brwosing   (inside the cu-page)    (info -h : text-/lines-browsing  /Cursor Commands (inside.a.page):  3 Moving the Cursor) :
		goto page.top 	:  b/pos1/home		: (not node, but current page!!
		goto page.end 	:  e/End
		page-down:  space , pageUp: backspace/DEL    (info -h : page-scrolling /Scrolling Commands:  4 Moving Text Within a Window )
	--- history-browsing (your-hist):
		l : last.viewed-page/hist
		C-x C-b (`list-visited-nodes')  + x :exit  :Make a window containing a menu of all of the currently visited nodes.
	--- node.browsing /Node Commands (infopages-tree, predefined, NOT-your-hist!):   5 Selecting a Node
		n / [ / <PgDn> bzw. <NEXT>  : next-node   #!! also, SeiteX-button, nicht verwechseln mit pos1/end-buttons! see above! , (vi-mode: C-x n ) 
		p / ] / <PgUp> bzw. <PREVIOUS>  : prev-node  (NOT-your-history! but prev-node in the info-tree !)
		u : up.node   (in vi-mode: C-x u )
		t : top.node  (in vi-mode: M-t )
		C-x C-b (`list-visited-nodes')  + x :exit  :Make a window containing a menu of all of the currently visited nodes.
		g xxxx : goto.node with tab-completion (bzw. vi: space-completion)  Echo Area is only done for the nodes which reside in one of the Info files that were loaded in the current Info session;
		C-x C-b (list-visited-nodes)            Make a window containing a menu of all of the currently visited nodes
		-
		-!goto a subnode directly: put top.node in () before subnode:
			- eg subnode "recurse" in tar: "g"(tar.info.gz)recurse /OR "g"(tar)recurse
			-! directly from shell:  info '(tar)recurse'  /OR info '(tar.info.gz)recurse'
	--- menu-jumps/links-jumps : INFO: Help-M / 1.6 Menus and the `m' command :
		a menu is always identified by a line which starts with "* myMenuItem"
		The only menu you can use at any moment is the one in the node you are in.  To use a menu in any other node, you must move to that node first.
		each line that starts with a `*' identifies one subtopic.
		jumpt to a menu.potin:
			either got to it and RET /or:
			m + completion by space or tab
		TAB	: goto next link/submenu
		0-9 ...	: goto X menu.item
##________________________________________  ___________________________


#####  ==========  ------------------------------------------
##________________________________________  ___________________________


#####  ==========  Searching :

	_______:  in-cu-page-searching strings: 6 Searching an Info File
	s OR / :also regexp
	C-x n (`search-next')
	? : search backward
	R : Toggle between using regular expressions and literal strings for searching.
	S : `search-case-sensitively

	_______:  index.search , infopages-nodes-search: 7 Index Commands
	i : (index-search) Look up a string in the indices for this Info file, and select a node to which the found index entry points.
	, : (`next-index-match')
	M-/ ('tree-search') :  Recursively search this node and any subnodes listed in menus for a string.
	'M-}' ('tree-search-next')
	'M-{' ('tree-search-previous') Go forwards and backwards through the matches for an active tree search.

	_______:  apropos , from cmdline seach.
	info -k XXX /OR  info  --apropos=XXX
	M-x index-apropos	: If you don't know what manual documents something, try the `M-x index-apropos' command. It prompts for a string and then looks up that string in all the indices of all the Info documents installed on your system. It can also be invoked from the command line; see  --apropos.

	_______:  windowing/multiple.windows/   8.2 Window Commands :
	C-x o	: next.win
	M-x		:prev.win
	C-x 2	: split.win
	C-x	0	: delete.curr.win
	X-x 1	: keep only this win; close all other wins
##________________________________________  ___________________________


#####  ==========  more:
	< + > : first/last node in this file
	g xxx : goto.node.xxx
