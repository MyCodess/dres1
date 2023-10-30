____________________ Xfce Desktop Environment dnts on 1912arx1 : ____________________

	_______:  hist-dnts:
	- Xfce 4.14 , /_200200
##________________________________________  ___________________________


#####  ==========  URLs:
https://xfce.org/
https://docs.xfce.org/
!!  https://wiki.xfce.org/faq  ---> also keyboard, chorcuts,...
https://wiki.archlinux.org/index.php/Xfce
##________________________________________  ___________________________


#####  ==========  global / system-wide configs (to set for all users): ??works??:

	_______:  check:
	$XDG_CONFIG_DIRS/xfce4/xfconf/  usu.  /etc/xdg/xfce4/xfconf/  : ??putting   ~u1/.config/xfce4/  there?? (could work for new created users
	$XDG_CONFIG_DIRS/Thunar/ , ... check just $XDG_CONFIG_DIRS/  ! xfce is pretty much XDG-conform !!
	/etc/skel/... :   Anything in here will be copied over to a new home-directory when a new user is created ; could work!? only new created users!
##________________________________________  ___________________________


#####  ==========  logout/restart/suspend/hibernate/...:
	- man xfce4-session-logout
	- logout:  xfce4-session-logout   --logout 
##________________________________________  ___________________________


#####  ==========  starting :
see https://docs.xfce.org/xfce/getting-started

	_______:  arx:
https://wiki.archlinux.org/index.php/Xfce  :
Starting : 
Choose Xfce Session from the menu in a display manager of choice,    or add exec startxfce4 to Xinitrc.
Note: Do not call the xfce4-session executable directly; startxfce4 is the correct command which, in turn, calls the former when appropriate.

	_______:  
- manually from vconsole:  startxfce4
- for auto-start add it to ~/.xinitrc or .xprofile ,... or so...; see arx-wiki https://wiki.archlinux.org/index.php/Xfce
- per login-manager/display-manager (as GDM,...): see https://docs.xfce.org/xfce/display_managers

	_______:  parallel X-sessions (eg u1 + m1 on two different vconsoles):
-!! startx /usr/bin/xfce4-session   ##--!!-BUT arx-wiki says not-calling session directly !?!? but through startxfce4 !?!?
##________________________________________  ___________________________


#####  ==========  xfconf ,  xfconf-query ....:
-!!!  https://docs.xfce.org/xfce/xfconf/start  --> read properly !!
-!! DEF : xfconf (tree-like) configuration system;  Root-IMMEDIATE-child-nodes  are called “channels”.All settings beneath the channel nodes are called “properties.”     https://docs.xfce.org/xfce/xfconf/start
- Both channel and property names are case-insensitive.
-!!   llinpath   xfce  ##bzw.   $ xfce4-<TAB> ....

	_______:  editing/modifying xfconf channels/properties:
    -!! see  https://docs.xfce.org/xfce/xfconf/start  :  Accessing Configuration Data :
    -1-  GUI :  Startmenu-->Settings ! : any changes are usu IMMIDIATELY propagated to the configuration system and vice-versa.
    -2-  cmdline:    xfconf-query  : https://docs.xfce.org/xfce/xfconf/xfconf-query
    -3-  GUI for more settings than in APPs selber :   Startmenu-->Settings--> "Settings Editor" bzw. xfce4-settings-editor  , basically eiditing configs in ~/.config/xfce4/ files   :   https://docs.xfce.org/xfce/xfce4-settings/editor
    -4-  manually edit config-files (BUT be carefull! ) in xml-files, which can be edited when Xfconf is NOT running , for user in ~/.config/xfce4/xfconf/xfce-perchannel-xml/ , 
        ~/.config/xfce4/   and aslo  settings-xmls  in  ~/.config/xfce4/xfconf/xfce-perchannel-xml/
        Settings are stored in XML files in ~/.config/xfce4/xfconf/xfce-perchannel-xml/ which can be edited by hand. However, changes made here will NOT take effect immediately.
        user-configs fully in ~/.config/xfce4/  which also shown/editable by Startmenu-->Settings--> "Settings Editor" bzw. xfce4-settings-editor 

	_______:  xfconf-query :  https://docs.xfce.org/xfce/xfconf/xfconf-query :
    -!?_1kk:  obv. ~/.config/xfce4/xfconf/xfce-perchannel-xml/*.xml files contain ALL the properties-vlaues/query-results/configs !?
    ! monitor/follow/trace changes live for certain channel :   xfconf-query -m <channel-name> ;## to see channel-names-listing, enter without param!
    List all available configuration channels:    xfconf-query -l ; xfconf-query -c xsettings -l ; xfconf-query -c xsettings -p /Gtk/FontName ; ...
    List all available properties in the channel thunar:          xfconf-query -c thunar -l 
    List all available properties + valuesin the channel thunar:  xfconf-query -c thunar -l -v
    List all properties and their values in the channel xfce4-panel below the property /panels (including it): xfconf-query -c xfce4-panel -p /panels -l -v
    monitoring any changes in thunar-confs and their values:    xfconf-query -c thunar  -m -v
    Hide Suspend and Hibernate from the logout dialog: xfconf-query -c xfce4-session -np '/shutdown/ShowSuspend' -t 'bool' -s 'false'  ;  xfconf-query -c xfce4-session -np '/shutdown/ShowHibernate' -t 'bool' -s 'false'
##________________________________________  ___________________________


#####  ==========  System-Apps of Xfce4
-!! see https://docs.xfce.org/  
xfdesktop   	:  Startmenu-->Settings--> "Desktop"  /OR right-click-on-desktop , Desktop Manager manages the desktop of Xfce. background image / color and drawing icons on the desktop. It can bring up an applications menu and a list of all running applications ...
Xfce4-session 	:  Startmenu-->Settings--> "Session and Startup" , is a session manager for Xfce. Its task is to save the state of your desktop (opened applications and their location) and restore it during a next startup. You can create several different sessions and choose one of them on startup.  https://docs.xfce.org/xfce/xfce4-session/start
xfsettingsd 	:  The settings daemon – process name is xfsettingsd – is an application that runs in the background to apply various settings in the desktop.
default-apps	:  Settings--> "Prefered Applications"  /OR  exo apps as exo-preferred-applications
StartMenu-Editor:  .Desktop Item Editor - exo as exo-desktop-item-edit allows a user to easily create and modify application launchers, or .desktop files in a GUI. https://docs.xfce.org/xfce/exo/desktop-item-edit
exo-open   		:  Open URLs and launch preferred applications
...

	_______:  bins:
-!!  lla /usr/bin/xfce4*  ##--as: xfce4-power-manager , xfce4-screensaver , xfce4-settings-manager , /usr/bin/xfce4-appfinder , xfce4-keyboard-settings , xfce4-mouse-settings , ...
##________________________________________  ___________________________


#####  ==========  Terminal / xfce4-terminal :
	-!!   man   xfce4-terminal   ; bzw.  xfce4-terminal  --help ;
	-!!  pacman -Ql xfce4-terminal  ;   

	_______:  profiles-nach-simuliert_1kk for xfce4-terminal :
	--- new profile by defining an alternative-config-file for starting of xfce4-terminal  1kk:  
		- mkdircd  /up1/varu/varau/wks/xdg-wk1/xfce4/ ;  cp  -a  ~/.config/xfce4/terminal/ . ;
		- modify /OR relink  terminalrc :   vi  ./terminal/terminalrc  ## chane eg to green the bg:  ColorBackground=#e8c9f17de163   ;/OR  cd ./terminal/ ;  rm   terminalrc  ; ln -s ./terminalrc-green  ./terminalrc  ;
		- XDG_CONFIG_HOME=/up1/varu/varau/wks/xdg-wk1/    xfce4-terminal --disable-server &  --> it wotked! now you could put an alternative terminalrc there and so basically having profiles so !!
		- nts:  ohne --disable-server  it does NOT work! then termnla still communicates with the xfce4-terminal-Server for preferences !!
	--- new profile by switching/copying terminalrc:
		###### ok1: !! works only with "ln" !! but NOT with "cp" !! 
		terms11(){
		cd  ~/.config/xfce4/terminal/   &&   rm  ./terminalrc  &&  ln -s ./terminalrc-${1}  ./terminalrc  ;
		xfce4-terminal --disable-server &
		read -t 2 ;
		cd  ~/.config/xfce4/terminal/   &&   rm  ./terminalrc  &&  ln -s ./terminalrc-a   ./terminalrc ;
		}

	_______:  system-global-configs :
	--- 2chk:
	- man xfce4-terminal  (whereas usu. XDG_CONFIG_DIRS is /etc/xdg/ ) :
		${XDG_CONFIG_DIRS}/xfce4/terminal/terminalrc : preferences which control the look and feel of xfce4-terminal.
		${XDG_CONFIG_DIRS}/xfce4/terminal/accels.scm : keyboard shortcuts configuration file for xfce4-terminal.
	- global-configs of terminal:  /usr/share/xfce4/terminal/terminal-preferences.ui ,  /usr/share/xfce4/terminal/  ##--but check with:   pacman -Ql xfce4-terminal
	- global-collor-schemes (shown in drop-down-selection in Preferences):   /usr/share/xfce4/terminal/colorschemes/

	_______:  user-configs :
	- user-configs saved in  (but better modify it with : ~/.config/xfce4/terminal  bzw.  $XDG_CONFIG_HOME/xfce4/terminal/terminalrc   
	- statrt-ini-file :   /home/u1/.config/xfce4/terminal/terminalrc
	- user--collor-schemes (shown in drop-down-selection in Preferences):   ~/.config/xfce4/terminal/colorschemes/
	- keyboard shortcuts :  ${XDG_CONFIG_DIRS}/xfce4/terminal/accels.scm

	_______:  colorscheme adding new ones (shown in drop-down-selection in Preferences): 
	- globally: cd /usr/share/xfce4/terminal/colorschemes/ ; sudo cp  black-on-white.theme  all-col1.theme ; sudo vi all-col1.theme ;
	- user-colorschemes : mkdir -p ~/.config/xfce4/terminal/colorschemes/  ; cp /usr/share/xfce4/terminal/colorschemes/black-on-white.theme ./my-col1.theme ; vi ./my-col1.theme ;
	--- testing params/tabs/... colors:
		- xfce4-terminal  --color-bg="#FFF8DC" ##--for colors see https://en.wikipedia.org/wiki/X11_color_names
		tryit:  xfce4-terminal  --working-directory=/tmp  --color-bg=yellow  --color-text=red   --tab --working-directory=/var   --tab --color-bg=blue  --color-text=white
		##---> so tha prams color/directory/... afftact the PREVIOUS/davor --tab param (bzw. one terminal pre first --tab is always there!!)
	--- infs-colors:
		see-also :
		https://en.wikipedia.org/wiki/X11_color_names               ##--the <X11root>/lib/X11/rgb.txt   file of X11 is not in arx with X.org , but see then :
		https://www.astrouw.edu.pl/~jskowron/colors-x11/rgb.html    ##-- <X11root>/lib/X11/rgb.txt  usu. in /usr/lib/X11/rgb.txt in case of using X11/Xfree86 instead of X.Org
		/usr/share/vim/vim82/rgb.txt   ##--same/similar to X11-rgb.txt !?
		-- infs:
		DIFF   X11-color and W3C-color, see  :https://en.wikipedia.org/wiki/X11_color_names#Clashes_between_web_and_X11_colors_in_the_CSS_color_scheme
		DIFF   X11/XFree86  and  X.Org see :  https://en.wikipedia.org/wiki/X_Window_System#X.Org_and_XFree86
##________________________________________  ___________________________


#####  ==========  Menu
	-!! Favorites:  add your own additional panel (by right-click on main-panal-startmenu-icon) and add your own favorites to it!
	  then you see its .desktop-files in   ~/.config/xfce4/panel/launcher-XX/...
##________________________________________  ___________________________


#####  ==========  Thunar / Xfce4 :
https://docs.xfce.org/xfce/thunar/start
https://wiki.archlinux.org/index.php/Thunar

	_______:  DIRs/config-DIRs /_1kk :
	find . -iname *thunar*
	~/.config/Thunar  ,   	~/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
	- configs/settings/properties of Thunar:  ~/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
	- bookmarks:  uses the standard GTK3-files-bookmarks:(also same file as nautilus-filesMgm):   ~/.config/gtk-3.0/bookmarks
	- user-custom-actions / user-new-actions-definition in    :  ~/.config/Thunar/uca.xml 
	- shortcuts/Hotkeys/keybindings [also defaults] :  ~/.config/Thunar/accels.scm
		- !! the out-commented ones are obv. defaults!! try them first before changing!! <Primary> was Ctrl in x13-ubt)
		- see also https://askubuntu.com/questions/403922/keyboard-shortcut-for-thunar-custom-actions
		-- shrtcuts-uue :
		(gtk_accel_path "<Actions>/ThunarWindow/open-parent" "BackSpace")  ##--go to parent DIR with backspace instead <Alt>left !
		(gtk_accel_path "<Actions>/ThunarActions/uca-action-1550010440854074-4" "F4")   ##--custom-action-4 with <F4>-Button for opening gnome-termnal !

	_______:  configs:
	- hidden-properties see  :  https://docs.xfce.org/xfce/thunar/hidden-settings
	  setting eg:  xfconf-query --channel thunar --property /misc-image-size-in-statusbar --create --type bool --set true  ##--OR editting thunar.xml ;
	- shortcuts/Hotkeys-Listing, but of Xfce :  xfconf-query -c xfce4-keyboard-shortcuts -l -v | cut -d'/' -f4 | awk '{printf "%30s", $2; print "\t" $1}' | sort | uniq
	--- configs-global: pacman -ql thunar ;  #bzw.: dpkg -L thunar
	--- config-user-properties query/setting/.... : 
		-! Thunar-config-stuff not by gsettings/dconfig, because it really belongs to  Xfce-Desktop, so then eg with xfconf-query ,..
		xfconf-query  -l -v  --channel thunar
		The quickest way to change/set a hidden settings is to run a command in the terminal-emulator.
		xfconf-query --channel thunar --property /property-name --create --type value-type --set new-value
		So to enable the image size in the statusbar, run the following command:
		xfconf-query --channel thunar --property /misc-image-size-in-statusbar --create --type bool --set true
		/OR xfconf-query  --channel thunar  --property /misc-exec-shell-scripts-by-default  --create --type bool  --set false
		_1kk: it writes to  ~/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml 
	--- hidden settings changing:
		xfconf-query --channel thunar --property  /misc-full-path-in-title  --create --type bool --set true
		xfconf-query --channel thunar --property  /misc-always-show-tabs --create --type bool --set true  #--> always show tab button!
		xfconf-query --channel thunar --property  /misc-small-toolbar-icons --create --type bool --set true
		->OR just add directly to your xml-config-file: ~/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
	--- 1coll/misc-config-lines:
	details-listing-view-(icons)-zoom-level/-size (latest-one, which is taken for next startup ):
	<property name="last-details-view-zoom-level" type="string" value="THUNAR_ZOOM_LEVEL_25_PERCENT"/>  ##-in ~/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml

	_______:  "sendto"-addies/configs:
	just add .desktop entries into eg: /usr/share/Thunar/sendto/  OR for user: ~/.local/share/Thunar/sendto/ WITH appropriate  mime, eg: MimeType=image/jpeg;
	see http://docs.xfce.org/xfce/thunar/send-to  :
	Like most other features of Thunar, the Send To menu can be easily extended by users and application developers with new targets, using standard desktop entry files.
	These files must be installed into one of the $XDG_DATA_DIRS/Thunar/sendto/ folders (see the XDG Base Directory Specification for details about the $XDG_DATA_DIRS variable).
	If you do not specify any MimeType your entry will show up for all file types. 
##________________________________________  ___________________________


#####  ==========  screensaver/xlock4/ ...
https://docs.xfce.org/apps/screensaver/start
https://docs.xfce.org/apps/screensaver/faq
xfce4-screensaver-command , xfce4-screensaver , v
vi /usr/bin/xflock4
