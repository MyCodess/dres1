__________  common.stuff for all schell-scriptngs: ____________
exit 3
##________________________________________  ___________________________


#####  ==========  Interactive-Widget-Shells: Dialog-/Menu.oriented-/Widgets-Shell.Scripts, Terminal-Attribs-Customizing,...:
-! dialog : in a terminal, displays text user interface widgets. It uses the curses or ncurses library.
	eg: dialog --title "Delete file" --backtitle "Linux Shell Script Tutorial Example" --yesno "Are you sure?" 7 60
	eg: dialog --clear --calendar "Please choose a date..." 0 0 7 7 1981
	see samples in its source-code
-! tput :  set terminal features : Move the cursor around the screen, Get information about terminal, color, underline, bold, ...
	eg: tput rev #reverse.video ; tput rest #reset-back-to-default; tput cup 23 4 #setting cursort to ... ; man tput ; man 5 terminfo
-! Bash Socket Programming : under bash you can open a socket to pass some data through it. 
	eg: 
-! expect :  is command that "talks" to other interactive programs according to a script. ; man expect ;
- setleds : allows you to set the keyboard leds.
	eg. setting NumLock on: setleds -D +num ; man setleds
- logger command writes entries in the system log file such as /var/log/messages. ; man logger
- setterm command can set various terminal attributes.
	eg: setterm -underline on; 
- smbclient: Sending Messages To MS-Windows Workstations.
	eg: echo "${Message}" | smbclient -M host2 

	_______:  with X.widgets (GTK/QT):
- notify-send Command : send desktop notifications to the user via a notification daemon from the command line
	eg: notify-send "backup done" ; notify-send --help
- zenity commadn will display GTK+/Gnome dialogs box, and return the users input.
	eg: zenity -title  "Enter domain"  --entry --text "Enter the domain you would like to see whois" ;
- kdialog is just like zenity but it is designed for KDE/QT apps.
	eg: kdialog --dontagain myscript:nofilemsg --msgbox "File: '~/.backup/config' not found."
-- other KDE/Gnome/Xwidget  commands:
	gmessage - a GTK-based xmessage clone.
	xmessage - display a message or query in a window (X-based /bin/echo)
	whiptail - display dialog boxes from shell scripts
	python-dialog - Python module for making simple Text/Console-mode user interfaces
##________________________________________  ___________________________


#####  ==========  resources:
-! for loggers, dyn-functions,... see: suse.103: /etc/sysconfig/network/scripts/functions and functions.common
##________________________________________  ___________________________


#####  ==========  SHs-comm:
- which shell am I using? in Lx: /bin/ls -l /proc/$$/exe   #see /etc/profile suse.10
##________________________________________  ___________________________


#####  ==========  eval/dyn-definitions:
- from /etc/sysconfig/network/scripts/functions.common in suse.103:
	eval ${level}_mesg\(\) \{ :\; \}  #- set level dynamically to your funcion name, .. see the source in suse
##________________________________________  ___________________________


#####  ==========  absolute path of the invoked script

	_______:  -- NOT SOURCED scripts absolute path:
#--I- if needed, do: "cd -P ..." and "pwd -P ..." instead jsut cd , due to links,... depends on what you want,....
#- onliner: 
	# eg: myInvoke="../tests/s1" ;  echo "$(cd -- ${myInvoke%/*} && pwd)/${myInvoke##*/}"   /OR
	# DIR="$( cd "$( dirname "$0" )" && pwd )"
#- /OR as function/script:
	#------
	myInvoke="$0"
	myBasename="$(basename $0)"
	myDirname="$( dirname $myInvoke )"
	myAbsoluteDirname="$(cd $myDirname && pwd)"
	echo $myAbsoluteDirname
	myFP=${myAbsoluteDirname}/$myBasename
	ls -l $myFP
	echo ========= $?
	echo --------- $myFP
	##-----
#- OR UwFe:  SCRIPT=`basename $0 .sh` ; SCRIPT_DIR=$( cd -P -- "$( dirname -- "$( command -v -- "$0" )" )" && pwd -P ) ;  scriptFilePAth=$SCRIPT_DIR/$SCRIPT
- absolute path of current running script?? (ufe-fit): SCRIPT_DIR=$( cd -P -- "$( dirname -- "$( command -v -- "$0" )" )" && pwd -P )
#- with links, but without using newer bash-features as -P , to be compatilble..:
	SCRIPT_PATH="${BASH_SOURCE[0]}";
	if([ -h "${SCRIPT_PATH}" ]) then
	while([ -h "${SCRIPT_PATH}" ]) do SCRIPT_PATH=`readlink "${SCRIPT_PATH}"`; done
	fi
	pushd . > /dev/null
	cd `dirname ${SCRIPT_PATH}` > /dev/null
	SCRIPT_PATH=`pwd`;
	popd  > /dev/null

	_______:  -- SOURCED scripts absolute path:
	-!! works just for certain bashes (with $BASH_SOURCE defined)
	- physical path (no link-path):
	echo "absolute physical path:  $(dirname $(readlink -f ${BASH_SOURCE[0]}))"
	- invocation path (including links, if the case):
	echo "absolute path:  $(cd $(dirname ${BASH_SOURCE[0]}); pwd)"
##________________________________________  ___________________________


#####  ==========  
