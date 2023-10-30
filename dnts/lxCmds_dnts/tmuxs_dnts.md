____________________________ tmux-dnts , 1coll-nts,... __________________________
- 200400	:  1start
##________________________________________  ___________________________


#####  ==========  invoking/starting pre-defined terms/... with tmux, eg :
	--- eg starting tmux with 3 panes (splitted-windows), from cmdline, eg: 
	- from bash:         tmux new-session \; split-window -h \; split-window -v \;
	- from-inside-tmux:  tmux new-window \; split-window -h \; split-window -v \;
	- working-dir for each pane/split:   tmux new-session\; split-window -h -c /var/  \; split-window -c /tmp/ \;
	---  coloured-bg/fg per panes by starting tmux with:
	- for colour-names-listing see man tmux ---> fg=colour /OR just  a hexadecimal RGB string such as ‘#ffffff’ , so ‘#RRGGBB’ Red-green-Blue ! for RGB-clour-table see https://www.rapidtables.com/web/color/RGB_Color.html
	- tmux start-server \; new-session \; split-window -h \; split-window -v \; rename-window aa11\; set -w window-style bg=blue \;
	- colors-per-pane with RGB  : tmux    new-session \; split-window -h \; split-window -v \; rename-window aa11\; set  window-style bg="#FFFF00" \;  set -pt:.0 window-style bg='#ccffff' \;
	- colors-per-pane with color-names : tmux  new-session \; split-window -h \; split-window -v \; rename-window aa11\; set -w window-style bg=red \;  set -pt:.0 window-style bg=blue \;
	- tmux -2  start-server \; new-session \; split-window -h \; split-window -v \; rename-window aa11\; set -w window-style bg=brightyellow \;  set -pt:.0 window-style bg=brightcyan \;
	- RGB colours eg: white ##FFFFFF , black #000000 , lightyellow #FFFFCC , lightgray #E0E0E0 ,  lightcyan #CCFFFF , gray #808080 , yellow #FFFF00 ; see https://www.rapidtables.com/web/color/RGB_Color.html
