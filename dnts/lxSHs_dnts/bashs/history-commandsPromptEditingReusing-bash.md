____________________ History + commandline-editing/reusing bash-dnts : _____________________________________________
##________________________________________  ___________________________


#####  ==========  History of cmds in shell:  also "Event Designators" =====================================

	_______:  short no-hist nts:
	-!! diff: hist-list (current in buffer/RAM) <--> hist-file (saved after exit) !!
	- ONLY no Hist-file, but do hist in current shell, (do NOT save/persist hist-cmds for later! ): <space>  unset HISTFILE  ; is obviously sufficient!
	- no hist at all ! not-now for this shell AND not-saving hist for later! :  <space> set +o history

	_______:  NO-Hist after logout or for other shells:
	- short-on-liner for no-Hist-Trace:  '  export HISTCONTROL=ignoreboth ;  unset HISTFILE ; ' /OR:
	export HISTFILESIZE=0	#no line in histFILE after logout ; still okay for current shell
	export HISTSIZE=200	# only relevant for the current shell

	_______:  FullHist/restrict-Protocolling:
	set -o history
	shopt -s histappend
	unset  HISTCONTROL  /OR  export HISTCONTROL=""   #!!!
	unset  HISTIGNORE ; /OR  HISTIGNORE=" *pwd*" #for umgehen? ;
	export HISTFILESIZE=10000 , HISTSIZE=1000 (if? HISTFILE=...
	export HISTTIMEFORMAT=" %F %T "  /OR eg HISTFILE=/tmp/.hs_o10
	--- /OR as alias/script for switching from No-Hist to FULL-HIST-Save-With-ignore-tag.notSpace! (eg as ~/.alias)
	--- from Prj-FIT-2008:
	set +o history  # first do NOT hist these lines! later is reset!
	HISTFILE=/tmp/.hs_o10 ; HISTFILESIZE=10000 ; HISTIGNORE=" *pwd*" ; HISTSIZE=10000 ; HISTTIMEFORMAT=" %F %T " ;
	export HISTFILE HISTFILESIZE  HISTIGNORE  HISTSIZE  HISTTIMEFORMAT
	unset HISTCONTROL
	shopt -s histappend
	set -o history

	_______:  HISTIGNORE is a  colon-separated  list  of patterns used to decide which command lines should be saved on the history list.
	Each pattern is anchored at the beginning of the line and must match the complete line (NO implicit `*' is appended).
	eg: export HISTIGNORE="pwd:ls"  ##-no-hist for cmds STARTING with pwd or ls !
	eg: export HISTIGNORE="*pwd*"  ###-no-hist for cmds CONTAINING  pwd !
	eg: export HISTIGNORE=" *pwd*"  ###-no-hist for cmds STARTING with space and tehn CONTAINING  pwd !

	_______:  sharing history betwwen different terminals (so seeing each command in one terminal window, then in other one history too (good??)):
	- shopt -s histappend ; PROMPT_COMMAND='history -a'

	_______:  shortcuts+cmds for bash-cmd-history (fc -l ...) : HISTORY EXPANSION :
	- man bash : "HISTORY EXPANSION"
	- fc -l -20
	- !! : put last command in prompt.line
	- ^^ - repeat previous command with substitution
	- !nnn : put cmd-No.nnn in the prompt-line ; see numbers with fc -l
	- !string    : put last cmd starting with string in prompt-line
	- !?string   : last cmd containing string
	- 
##________________________________________  ___________________________


#####  ==========  history-cmds-editing/-reusing , moving-through-hist-cmds in an interactive shells;  bash-Command-Line-Editing-with-history : "Word  designators" =======================
	-! "M" is "ESC" , "C" is Ctrl  (here at least in arx/Lv13)!

	_______:  !! diff : not confusing with bash-command-history-searching/browsing/reusing, which means bash-command-history (next section)
	here is only about the current cmdline-editing, AND also eg params from last cmdline,....
	-!! diff: so
	- Word  designators (cmdline-arguments) provide a way to reference specific arguments (words) from a command line stored in the history file
	- Event designators : are cmdline-history (also with !! , !nnn , !$ , ...)
	-! A colon (:) separates the event designator and the word designator. if needed (see below, eg:
	   !!:2    means 2nd argument of the last command
	   !121:3  means third argument of the command in history with No 121

	_______:  !! see:
	- man bash: sections:  READLINE : "Readline Key Bindings", "keymap", ..
	- Browsing-History-full-listing in man bash: "Readline Command Names": so following sections as "Commands for Manipulating the History" ...
	- full listing in: Bash_Cookbook_Ore_1ed_0705.pdf : Reference Lists : Readline ...: emacs Mode
	   bzw. Bash_Ore_3ed_0503.pdf i: B.9. emacs Mode Commands
	- Learning-Bash-Ore--Ch2 : 2.3. emacs Editing Mode ...
	- help bind  , bzw. bin in man bash

	_______:  settings/configs:
	-!! depends also on "keymap" and "editing-mode"  , if emacs/vi !! : set -o emacs /vi ; default is emacs (and uue is using emacs-cmdline-editing)
	-!  keymapping is also controled/configured by /etc/inputrc  bzw. ~/.inputrc : Control the behaviour of the readline library used e.g. by the bash in the interactive mode for line editing.
	-!! listing of current shortcuts/key-bindings:  bind -p
	- uue-keyBindings-Mode:  emacs-keymaps (bash-default, also for uue; see also extra nts for keybindings-coll):
	- clear screen: ctrl-l  (NOT the terminal-history-buffer!)
-- "Commands for Moving" / browsing/search/goto in  history:
	-! see man bash  /"Commands for Moving" /"Readline Command Names"  bzw. /"Commands for Manipulating the History" ; (or eg /C-r , /C-s ...)
	- ctrl+R / ctrl-S search history-cmds  backward / forward , BUT:
		-!!  ctrl-S conflict with Terminal ctrl-S for freeze-input + Ctrl-Q to quit the frozen state ! have to do "stty -ixon" in terminal to disable Ctrl-S of Terminal-keys !
	- ctrl+A/E/B/F : beginn/end/back/forw. movment
	- CTRL-P / CTRL-N (or the up and down arrow keys): previous/next cmdline-history-entry
	- CTRL-K / CTRL-U : erase the entire line from curson upto the END(=Kill)/Begin
	--
	last cmd STARTING with "echo":  !echo  ##--> it prints this line tho your cmd-prompt !
-- cmdline-args-reusing/recalling/browsing-hist-cmds:
	-!! see man bash /"Commands for Manipulating the History" 
	- last-argument-of-last-cmd:   ESC-. bzw.  ESC-_  (M-., M-_) : yank/insert-last-arg of last cmd at surrent-cursor-location (point)
	- first-argument-of-last-cmd:  ESC Ctrl-y
	- nth-argument-of-last-cmd:    ESC Ctrl-[n]-y BUT in kde-konsole was Alt-[n-]-Ctr-y all keep-gedruckt, so also keep ALT pressed to the end!!  / man: yank-nth-arg (M-C-y) , usu. the second word!
	  so for nth-arg then easier with "history expansion":  !!:n   (see below)
	- 2nd-argument-of-last-cmd insert here: ESC-2 ESC Ctrl-y , see man bash /yank-nth-arg
-- words-editing
	ESC-DEL  Kill one word backward 
	ESC-D    Kill one word forward 
	CTRL-Y   Retrieve ("yank") last item killed 
-- completions:
	ESC-?  List the possible completions 
	ESC-$  Attempt variable completion 
	ESC-!  Attempt command completion 

	_______:  reusing of arguments/params of last cmds , cmdline-history-expansion:  "Word Designators"
	-! see man bash : "HISTORY EXPANSION" :  "Word Designators"
	- def: Word designators provide a way to reference specific arguments (words) from a command line stored in the history file.
	-!! not confusing with command history "!" (as !! , !121 ,...)
	- !^ , !$ , !* , !!:2 : the first/last/all/2nd argument of the last command ; eg:  echo !*  ; eg:
		sudo cp /etc/apache2/sites-available/siteconfig   /home/fred/siteconfig.bak
		echo !^ !!:2    #-equivalent to:   echo cp /etc/apache2/sites-available/siteconfig
	-!! diff  !2  (command-No.2 in bash-history)  <-->  !!:2  (2nd argument of the last command )
	- !$:s/a/b/  : last-arg-of-last-cmd but replace firtst a with b
	  !$:s//a/b/ : same as above, but all occuruncies of a replce with b

	_______:  bind eg:
	- The \C refers to the control key. The \M sequence refers to the 'meta' key (special on some keyboards, or usually the Alt key or the Escape key).
	- eg: $bind "\C-b":backward-word : change Control-B to go backwards word by word
	- eg: set Control-E to run emacs, you would use the following: $bind -x '"\C-e"':emacs
	- inputrc:  To have key bindings in bash enabled every time, you can either set the information in the .inputrc file (which then affects all Readline-enable d applications), or you can place specific bash bindings in your startup scripts.
