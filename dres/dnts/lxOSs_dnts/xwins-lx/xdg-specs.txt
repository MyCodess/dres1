______ XDG speces nots! also partly repeated/reference in other devnts as in gnome.txt, but OK _________________
- http://www.freedesktop.org/wiki/Specifications/
-! pacman -Ss xdg
- pacman -S xdg-user-dir , extra/xdg-utils ...
- man  xdg-desktop-menu , xdg-desktop-icon(1), xdg-icon-resource(1), xdg-mime(1) , xdg-open , ...  ##--> llinpath xdg
################################# XDG-Environment variables Allg for all : #########################################
-!! https://specifications.freedesktop.org/basedir-spec/latest/ar01s03.html  :   Environment variables :

	_______:  USER-Dirs (higher preference!):
- $XDG_DATA_HOME defines the base directory relative to which user specific data files should be stored. If $XDG_DATA_HOME is either not set or empty, a default equal to $HOME/.local/share should be used.
- $XDG_CONFIG_HOME defines the base directory relative to which user specific configuration files should be stored. If $XDG_CONFIG_HOME is either not set or empty, a default equal to $HOME/.config should be used.
- $XDG_CACHE_HOME defines the base directory relative to which user specific non-essential data files should be stored. If $XDG_CACHE_HOME is either not set or empty, a default equal to $HOME/.cache should be used.

	_______:  SYSTEM-/Global-Dirs (after user-dirs !):
- $XDG_DATA_DIRS defines the preference-ordered set of base directories to search for data files in addition to the $XDG_DATA_HOME base directory. The directories in $XDG_DATA_DIRS should be seperated with a colon ':'.
	- default-value:   If $XDG_DATA_DIRS is either not set or empty, a value equal to /usr/local/share/:/usr/share/ should be used.
- $XDG_CONFIG_DIRS defines the preference-ordered set of base directories to search for configuration files in addition to the $XDG_CONFIG_HOME base directory. The directories in $XDG_CONFIG_DIRS should be seperated with a colon ':'.
	- default-value:   If $XDG_CONFIG_DIRS is either not set or empty, a value equal to /etc/xdg should be used.
	- The order of base directories denotes their importance; the first directory listed is the most important. When the same information is defined in multiple places the information defined relative to the more important base directory takes precedent. The base directory defined by $XDG_DATA_HOME is considered more important than any of the base directories defined by $XDG_DATA_DIRS. The base directory defined by $XDG_CONFIG_HOME is considered more important than any of the base directories defined by $XDG_CONFIG_DIRS.
- $XDG_RUNTIME_DIR defines the base directory relative to which user-specific non-essential runtime files and other file objects (such as sockets, named pipes, ...) should be stored. The directory MUST be owned by the user, and he MUST be the only one having read and write access to it. Its Unix access mode MUST be 0700.
	- The lifetime of the directory MUST be bound to the user being logged in. It MUST be created when the user first logs in and if the user fully logs out the directory MUST be removed. If the user logs in more than once he should get pointed to the same directory, and it is mandatory that the directory continues to exist from his first login to his last logout on the system, and not removed in between. Files in the directory MUST not survive reboot or a full logout/login cycle.
	- The directory MUST be on a local file system and not shared with any other system. The directory MUST by fully-featured by the standards of the operating system. More specifically, on Unix-like operating systems AF_UNIX sockets, symbolic links, hard links, proper permissions, file locking, sparse files, memory mapping, file change notifications, a reliable hard link count must be supported, and no restrictions on the file name character set should be imposed. Files in this directory MAY be subjected to periodic clean-up. To ensure that your files are not removed, they should have their access time timestamp modified at least once every 6 hours of monotonic time or the 'sticky' bit should be set on the file.
	- If $XDG_RUNTIME_DIR is not set applications should fall back to a replacement directory with similar capabilities and print a warning message. Applications should use this directory for communication and synchronization purposes and should not place larger files in it, since it might reside in runtime memory and cannot necessarily be swapped out to disk.
--################ XDg-DIRs,... : #############################################################################
- see each section in this dnts for its DIRs...! here just more nts:
##________________________________________  ___________________________


#####  ==========  XDG-user-dirs:
-! man  xdg-user-dirs-update , xdg-user-dir , user-dirs.dirs(5), user-dirs.defaults(5), user-dirs.conf(
##________________________________________  ___________________________


#####  ==========  icons/ desktop-icons/...:
- man  xdg-desktop-icon   ##-full:  http://www.freedesktop.org/wiki/Standards/desktop-entry-spec
-!  adding/removing desktop-icons:     man xdg-desktop-icon
##________________________________________  ___________________________


#####  ==========  XDG-xwins-misc:
-!! man xdg-settings , xdg-mime, xdg-open , ...#- llinpath xdg
##________________________________________  ___________________________


#####  ==========  XDG-cmds/utils:
-!! dpkg -L xdg-utils :
- ls /usr/bin/*xdg*
dg-desktop-icon  xdg-email          xdg-mime  xdg-screensaver  xdg-user-dir              xdg-user-dirs-update
xdg-desktop-menu  xdg-icon-resource  xdg-open  xdg-settings     xdg-user-dirs-gtk-update
################################# XDG-StartMenu-specs: #############################################################
##________________________________________  ___________________________


#####  ==========  see/help/docs/man XDG-startmenu:
	-! man  xdg-desktop-menu  install/uninstall/... : install new menu entries to the desktop's application menu.
	- http://www.freedesktop.org/Standards/menu-spec
	- XDG-Dir-Structure-Specs:  http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
##________________________________________  ___________________________


#####  ==========  infs/stats/Allg-xdg :
-!! expg xdg
- what is my current gui-session (x11 or wayland?, gnome/unity/..., ??):
expg xdg --->: XDG_SESSION_DESKTOP="gnome-classic" ,  XDG_SESSION_TYPE="x11" , ....
##________________________________________  ___________________________


#####  ==========  XDG-startmenu-Vars (Root-Main-VARs for roots of File-Locations/DIRs/tree of Startmenu + .desktop-entries ...) (see basedir-spec):
-!! see   http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

	_______:  concept:
	- starmenu is consisting of two parts:
		- menu-Definitions (defining of the menu-structure) : menu-file + merged-menu-filesc :  all in XDG_CONFIG-dirs
		- menu-files       ((konkret menu-items)/entries  ) : .desktop  + .directory files (konkret menu-items) : all in XDG_DATA-dirs

	_______:  ! preferences of startmenu-DIRs:
	- ALL XDG-path-vars are  preference-ordered!! so the first one in a path-var is prefered to the later oned defined there!!
	  The order of base directories denotes their importance; the first directory listed is the most important.
	- USER-dirs are preferenced to SYSTEM/global ones!!   The base directory defined by $XDG_DATA_HOME is considered more important than any of the base directories defined by $XDG_DATA_DIRS !
	- FIRST found files is the most important files
	- search id done in the same sequence as defined in $XDG-var !! First one found is taken !!
	-! some var are only a single-dir  (usu. the USER-vars), others can be a set of preference-ordered-base-directories, ordered in a path-syntax-with-colon-seperated (usu. the SYSTEM-vars)!

	_______:  USER-menu-dirs (usu. only a SINGLE dir is allowed to be assigned to the var!):
	- data:		$XDG_DATA_HOME		default:  $HOME/.local/share
	- configs:	$XDG_CONFIG_HOME	default:  $HOME/.config
	- cache:	$XDG_CACHE_HOME		default:   $HOME/.cache
	- runtime:	$XDG_RUNTIME_DIR

	_______:  SYSTEM/global-menu-dirs  (usu.  a set of preference-ordered-base-directories, a path-syntax-with-colon-seperated-value is allowed to be assigned to the var!):
	- data:		$XDG_DATA_DIRS		default:  /usr/local/share/:/usr/share/
	- configs:	$XDG_CONFIG_DIRS	default:  /etc/xdg
##________________________________________  ___________________________


#####  ==========  XDG-startmenu-Files-Locations :  .menu + .desktop-entires + .directory files :
- see details in:  http://standards.freedesktop.org/menu-spec/menu-spec-latest.html
-!! startmenu-strucrute contains TWO file-definitions: 1- menu-file (in CONFIG_DIRs) 2- the .desktop-items/entries in the menu (in DATA_DIRS) :

	_______:  menu-location / main-startmenu-structure
	- in  $XDG_CONFIG_DIRS/menus/${XDG_MENU_PREFIX}applications.menu
	-!!-also the file-name of the menu-file IS relevenat!! eg if it is called uue1-applications.menu ,then MUST be set: export XDG_MENU_PREFIX=gnome-  !! otherwise the menu-file is NOT found!!

	_______:  .desktop-items/entries in startmenu.
	- in $XDG_DATA_DIRS/applications/ , arx: /usr/share/applications/  :!!collected from all DIRs! not only the first found!!:
	Each directory in the $XDG_DATA_DIRS search path should be used (i.e. desktop entries are collected from all of them, not just the first one that exists).
	When two desktop entries have the same name, the one appearing earlier in the path is used. 
	-! tha location can be changed by  <DefaultAppDirs> element in th  menu-file !

	_______:  .directory files:     $XDG_DATA_DIRS/desktop-directories/  : contains directory entries which may be associated with folders in the menu layout!

	_______:  merge-default-dirs:   $XDG_CONFIG_DIRS/menus/applications-merged/	: The default merge directories included in the <DefaultMergeDirs> element. By convention, third parties may add new <Menu> files in this location to create their own sub-menus.
	- see details in: http://standards.freedesktop.org/menu-spec/menu-spec-1.1.html#merge-algorithm

	_______:  icons:  $HOME/.icons (for backwards compatibility), in $XDG_DATA_DIRS/icons and in /usr/share/pixmaps (in that order).  : see http://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html

	_______:  autostarts:	$XDG_CONFIG_DIRS/autostart :  examples of defaults and preferences:
	If the same filename is located under multiple Autostart Directories only the file under the most important directory should be use
	If $XDG_CONFIG_HOME is not set the Autostart Directory in the user's home directory is ~/.config/autostart/
	If $XDG_CONFIG_DIRS is not set the system wide Autostart Directory is /etc/xdg/autostart/	
	If $XDG_CONFIG_HOME and $XDG_CONFIG_DIRS are not set and the two files /etc/xdg/autostart/foo.desktop and ~/.config/autostart/foo.desktop exist then only the file ~/.config/autostart/foo.desktop will be used because ~/.config/autostart/ is more important than /etc/xdg/autostart/	
##________________________________________  ___________________________


#####  ==========  ubuntu-startmenus 14.10:

	_______:  System-menu-dirs:
	- menu-main-file-definition:	/etc/xdg/menus/xxx-applications.menu  bzw. really /etc/xdg/menus/gnome-applications.menu + ...  -->main-big-wehole-menu-structure , including classical-menu
	- menu-merge-dirs:				/etc/xdg/menus/applications-merged/
	- menu-autostarts:				/etc/xdg/autostart/*.desktop
	- menu-directories:				/usr/share/desktop-directories/
	- menu-items/.desktop-entries:	/usr/share/applications/*.desktop
	- menu-icons-dirs:				/usr/share/icons/
	-- eg /classicmenu-indicator-app is based on:
		/etc/xdg/menus/classicmenuindicatorsystem.menu
		/usr/share/applications/classicmenu-indicator.desktop

	_______:  User-menu-dirs:
	- menu-main-file-definition:	~/.config/menus/xxx-applications.menu          -->main-big-wehole-menu-structure , including classical-menu
	- menu-merge-dirs:				~/.config/menus/applications-merged/
	- menu-autostarts:				~/.config/autostart/*.desktop
	- menu-directories:				~/.local/share/desktop-directories/
	- menu-items/.desktop-entries:	~/.local/share/applications/*.desktop
	- menu-icons-dirs:				~/.local/share/icons/

	_______:  openning terminal-tabs for all XDG-Dirs:
	- XDG-System-Dirs:	gnome-terminal --title=XDG-Sys-dirs  --tab --working-directory=/etc/xdg/menus  --tab --working-directory=/usr/share/desktop-directories  --tab  --working-directory=/usr/share/applications  --tab
	- XDG-User-Dirs:    gnome-terminal --title=XDG-User-dirs --tab --working-directory=~/.config/menus/  --tab --working-directory=~/.local/share/desktop-directories/  --tab --working-directory=~/.local/share/applications/  --tab
##________________________________________  ___________________________


#####  ==========  uue-startmenu-setup-1503ubt manually adding menu-folders/items:
# could also use  "xdg-desktop-menu install ..." to add items, but here manully:
# fitst check XDG-CONFIG/DATA-Dirs considering also their default values:    xdg1-menus.sh  ##--see freedesktop.org/XDG-specs for following file-locations!
#--II- if you want to add uue-menu-entries System-wide, then add them, as defined in spec, not to XDG_xxx_HOME, but to the first existing XDG_xxx_DIRS (see XDG-Files-Locations nts here above)
u1@x13:~/.config$ ln -s /up1/.cuue/etc/apps/menu1-uue/menus/                       ##--main-menu-definition  : == $XDG_CONFIG_HOME/menus/${XDG_MENU_PREFIX}applications.menu
u1@x13:~/.local/share$ ln -s /up1/.cuue/etc/apps/menu1-uue/applications/           ##--menu-entries/.desktop-files ; if needed, move/merge the existing one to uue-etc ! == $XDG_DATA_HOME/applications/
u1@x13:~/.local/share$ ln -s /up1/.cuue/etc/apps/menu1-uue/desktop-directories/    ##--menu-subdir-1  ==  $XDG_DATA_HOME/desktop-directories/
################################# XDG-mimetypes ,  files-associations ... : #########################################
##________________________________________  ___________________________


#####  ==========  mimetypes-XDG / Default-Apps in XDG: =======================

	_______:  docs-infs:
	-!  man  xdg-mime
	-!  https://wiki.archlinux.org/title/Default_applications 
	-! whole thing pretty verdreht/...; maybe use utils as:  pacman -S extra/perl-file-mimeinfo #or ..
	   mimeopen -a   t1.txt  ##--lists all files-associations to mime .txt ! is from extra/perl-file-mimeinfo !
	- pacman -S  extra/perl-file-mimeinfo .... ;##-pacman -Ss mime

	_______:  DEFs / DIFFs:
	-DEF:- DEFAULT-Apps are also based on mimetypes-definitions, but can be set/get also explicitly, due to their mor common/mswin-usages, and are only a few! as Web-Browser,File-Browser,... !

	_______:  DIRs:
	https://wiki.archlinux.org/title/XDG_MIME_Applications#mimeapps.list :
	~/.config/mimeapps.list :	user overrides  ##-for the format see the above arx-link!
	/etc/xdg/mimeapps.list 	:	system-wide overrides
	/usr/local/share/applications/mimeapps.list , /usr/share/applications/mimeapps.list	 	:  distribution-provided defaults
	/etc/xdg/xfce-mimeapps.list defines system-wide default application overrides for Xfce

	_______:  DEFAULT-Apps (ubuntu-14.10):
	- listing/show all current default-apps:  xdg-settings --list
	- show default web-browser:   xdg-settings get default-web-browser
	- xdg-settings get default-web-browser
	- xdg-settings check default-web-browser firefox.desktop
	- set  default web-browser:   xdg-settings set default-web-browser google-chrome.desktop  ##--the .desktop-file must be existing in XDG-dirs !

	_______:  ubuntu-14.10-default-mimetypes:
	-! mimetypes for system/allusers:  sudo vi /usr/share/applications/defaults.list  #--: (in ubt is linkto /etc/gnome/defaults.list ) for more see XDG-nts ! in ubuntu-14.10
		esp. replace excel with gvim for all text/csv....
	-! mimetypes for user:    ~/.local/share/applications/mimeapps.list

	_______:  querys:
	xdg-mime  query  default inode/directory  ##-shows current default file browser!
	xdg-mime  query  filetype  t1.txt      #--> formal filetype of t1.txt ?? -->  text/plain
	xdg-mime  query  filetype  ./tests/    #--> inode/directory
	xdg-mime  query  default   text/plain  #--> which app is in this xWin-Env the default app for text??
	xdg-mime  query  default  inode/directory  #--> what is default file manager??
	xdg-mime  query  default   application/pdf

	_______:  settings mimetypes apps:
	xdg-mime  default gvim.desktop  text/plain           #--default-text-editor , check: xdg-mime  query  default   text/plain
	xdg-mime  default Thunar.desktop   inode/directory   #--default-file-manager, check: xdg-mime query  default  inode/directory
--################ xWin-cmdline-ing... ########################################################################
-!! man wmctrl  zenity  gdialog  dialog xdg-open ...
- openning files with their associated win-apps from cmdline:   xdg-open  <my-file> #eg:  xdg-open  aa.pdf
##________________________________________  ___________________________


#####  ==========  wmctrl : cmdline-workspace-mgm-and-indowing:
- wmctrl ; man wmctrl ; apt-get install wmctrl
--!!DIFF:  <workspace> >  <DESK> >  <WINdow> :
	WorkSpace: is consisting of eg. 4 DESKtops, and each DESKtop contains several WINdows (as terminal, gvim, thunar,...)
	DESK: ist DeskTop-Number starting with zero 0 !
	WIN: for a listing/titles of current WINdows use:  wmctrl  -l  ##--II not always the title contains the app-name or so,... check it with "wmctrl -l" !

	_______:  -- cmds-wmctrl-OK:
	- List all windows detail	: wmctrl  -l  ; also with PID, process,...:   wmctrl -p -G -l
	- switch to the DeskTop containing a window with the title *gedit*	: wmctrl  -a gedit
	- WIN-properties-change/toggle/...: toggle-maximizing of the window with title containing gedit:  wmctrl -r gedit -b toggle,fullscreen
##________________________________________  ___________________________


#####  ==========  zenity :
-!  zenity(1) is a useful dialog program for building scripts with wmctrl
  (for script-utilities see also: man gdialog , dialog )
--################ coll ##############################################################################################
##________________________________________  ___________________________


#####  ==========  !! statu in ubuntu 14.10 x64 on x13 /1503ubt , output by script-uue: ======================================
u1@x13:/usr/share/applications$ xdg1-menus.sh 
##________________________________________  ___________________________


#####  ==========  Current System XDG-Vars: ==============
declare -x XDG_CONFIG_DIRS="/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg"             ##-->  /etc/xdg/
declare -x XDG_CURRENT_DESKTOP="Unity"
declare -x XDG_DATA_DIRS="/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/"  ##-->  /usr/share/
declare -x XDG_GREETER_DATA_DIR="/var/lib/lightdm-data/u1"
declare -x XDG_RUNTIME_DIR="/run/user/1501"
declare -x XDG_SEAT_PATH="/org/freedesktop/DisplayManager/Seat0"
declare -x XDG_SEAT="seat0"
declare -x XDG_SESSION_DESKTOP="ubuntu"
declare -x XDG_SESSION_ID="c3"
declare -x XDG_SESSION_PATH="/org/freedesktop/DisplayManager/Session0"
declare -x XDG_SESSION_TYPE="x11"
declare -x XDG_VTNR="7"
##________________________________________  ___________________________


#####  ==========  
=   xdg1_config_sys_dirs  are:   /etc/xdg/xdg-ubuntu /usr/share/upstart/xdg /etc/xdg
=== xdg1_config_all_dirs  are:   /home/u1/.config/ /etc/xdg/xdg-ubuntu /usr/share/upstart/xdg /etc/xdg
=   xdg1_data_sys_dirs    are:   /usr/share/ubuntu /usr/share/gnome /usr/local/share/ /usr/share/
=== xdg1_data_all_dirs    are:   /home/u1/.local/share /usr/share/ubuntu /usr/share/gnome /usr/local/share/ /usr/share/
=   xdg1_all_dirs         are:   /home/u1/.config/ /etc/xdg/xdg-ubuntu /usr/share/upstart/xdg /etc/xdg /home/u1/.local/share /usr/share/ubuntu /usr/share/gnome /usr/local/share/ /usr/share/
u1@x13:/usr/share/applications$ date
Sa 14. Mär 13:21:57 CET 2015
u1@x13:/usr/share/applications$ uname -a
Linux x13 3.16.0-31-generic #43-Ubuntu SMP Tue Mar 10 17:37:36 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
u1@x13:/usr/share/applications$ 
##________________________________________  ___________________________


#####  ==========  
