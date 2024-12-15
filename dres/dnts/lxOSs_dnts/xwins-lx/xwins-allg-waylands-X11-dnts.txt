___________________ Xwins-All/allg, .... ____________________________
##________________________________________  ___________________________


#####  ==========  docs/wps:
	man  X(1) /OR Xorg(1) ,
	man  xorg.conf(5), Xserver(1), 
	https://wiki.archlinux.org/index.php/Category:Graphical_user_interfaces  !!
	https://wiki.archlinux.org/index.php/General_recommendations#Graphical_user_interface
	https://wiki.archlinux.org/index.php/Wayland
	learning.lpi.org/en/learning-materials/102-500/106/106.1/106.1_01/index.html
##________________________________________  ___________________________


#####  ==========  !! Vocabs-/Dics-Tut for X-systems / GUIs on the top of OS :
	-!! Sequence/Dependencies/Sizes/Umfang:  GUI-Libs /XLibs  -->  X-Server / "Display server" --> "Display Managr" / "Login manager" /DM -->  "Window manager" / WM -->  "Desktop environment"
	- "GUI Libraris" /  "Widget toolkits" (as GTK , Qt):  Basis-Libs used by all !
	-  X-Server / "Display server" (as "X Window System X"==X11-Server==Xorg, /OR Wayland ):
		basic windows-functionalities for all others ...!  can be started by a "Display manager" /DM or "Window manager" /WM or "Desktop environment" /DE ! all need its services/funtionalities !
	- "Display manager" /DM / Login-Manager (as GDM, LightDM,  SDDM, ...):
		Is a graphical login manager which starts a session on a display server.
		Most "desktop environments" include a display manager for automatically starting the graphical environment and managing user logins. Users without a desktop environment can install one separately. Alternatively you may start X at login as a simple alternative to a display manager.
	- "Window manager" /WM (as Compiz for Gnome2, KWin for KDE4, IceWM, openBox, ...) : Only placement/posiotns of windows/icons/... :
		Window managers are X-Server-clients that control the placement and appearance of windows within a windowing system in a GUI.
		They determine the border, title bar, size, and ability to resize windows, ....
		A window manager (WM) is system software that controls the placement and appearance of windows within a windowing system in a graphical user interface (GUI). It can be part of a desktop environment (DE) or be used standalone.
		Prior to installing a window manager, a functional X server installation is required.
		https://wiki.archlinux.org/index.php/Window_manager
	- "Desktop environment" /DE  (as Gnome, KDE, Xfce, Unity, ...) : Full-GUI-Env (including Apps as Office/Editors/Bildbearbeitungs/....):
		Provides a complete GUI for a system by bundling together a variety of components. (can contain also its own "Window manager", as Compozit for Gnome)
		Although Xorg provides the basic framework for building a graphical environment, additional components may be considered necessary for a complete user experience. Desktop environments such as GNOME, KDE, LXDE, and Xfce bundle together a wide range of X clients, such as a window manager, panel, file manager, terminal emulator, text editor, icons, and other utilities.
	-!after the end of the boot process, so after the  OS booted up and terminal is there , then for X-/GUI-systems:
		-  login manager (== display manager, eg GDM / KDM / LightDM /...) shows a login-windows for users ! types: Console-DM (without X) or Graphical-DMs (need X, as Gnome GDM , ...) ; see  https://wiki.archlinux.org/index.php/Display_manager
########################### Login-Manager / Display-Manager for X : ########################################## 
##________________________________________  ___________________________


#####  ==========  Login-Manager / Display-Manager   (as GDM, LightDM, ...):  
	https://wiki.archlinux.org/index.php/Display_manager
	"Display manager"Is a graphical "login manager" which starts a session on a display server.
	--- Loading the display manager / Login Manager (as GDM, ...):  
	To enable graphical login, enable the appropriate systemd service. For example, for SDDM, enable sddm.service.
	This should work out of the box. If not, you might have to reset a custom default.target symlink to point to the default graphical.target. See systemd#Change default target to boot into.
	After enabling SDDM a symlink display-manager.service should be set in /etc/systemd/system/. You may need to use --force to override old symlinks.
	$ file /etc/systemd/system/display-manager.service
	/etc/systemd/system/display-manager.service: symbolic link to /usr/lib/systemd/system/sddm.service
	--- Using systemd-logind
	In order to check the status of your user session, you can use loginctl. All polkit actions like suspending the system or mounting external drives will work out of the box.
	$ loginctl show-session $XDG_SESSION_ID
	--- Style-choice/Session configuration (whcich desktop styles stehen zur verfügugn? eg in ubuntu: gnome/gnome-classic/unity-mist/....):
	Many display managers read available sessions from /usr/share/xsessions/ directory. It contains standard desktop entry files for each DM/WM.
	To add/remove entries to your display manager's session list; create/remove the .desktop files in /usr/share/xsessions/ as desired.
	_________
	- A typical .desktop file will look something like:
	[Desktop Entry]
	Name=Openbox
	Comment=Log in using the Openbox window manager (without a session manager)
	Exec=/usr/bin/openbox-session
	TryExec=/usr/bin/openbox-session
	Icon=openbox.png
	Type=Application
	_________
	- eg GDM login-options for your Destop-Manager usu. in:  /usr/share/xsessions/ ; eg: /usr/share/xsessions/gnome-classic.desktop
	--- cmds: 
	loginctl   user-status  ##--man  loginctl
########################### X Window System /== X11 /== or just X , Xorg : ################################### 
##________________________________________  ___________________________


#####  ==========  X11-/Xorg-startup_config-files  
	learning.lpi.org/en/learning-materials/102-500/106/106.1/106.1_01/index.html
	man  xorg.conf(5), Xserver(1), X(1) and Xorg(1)

	_______:  X11 init-config-files:
	- user/admin-addies-configs:   /etc/X11/xorg.conf , /etc/X11/xorg.conf.d/  : !overwrites system-/distro-configs!  (keyboard, mouse,...) if exists! On modern Linux distributions, the X server will configure itself at runtime when the X server is started and so no xorg.conf file may exist.
	- distro/system/default-configs:     /usr/share/X11/xorg.conf.d/  : distro-org-config-files
	modified/admin/User-specified configuration files also reside in /etc/X11/xorg.conf.d/. 
	Configuration files provided by the distribution are located in /usr/share/X11/xorg.conf.d/. 
	The configuration files located within /etc/X11/xorg.conf.d/ are parsed prior to the /etc/X11/xorg.conf file if it exists on the system.

	_______:  Creating a Basic (new) Xorg Configuration File :
	see /LPIC1-102-500/learning.lpi.org/en/learning-materials/102-500/106/106.1/106.1_01/index.html  :
	To generate a permanent /etc/X11/xorg.conf file. Even though X will create its configuration after system startup on modern Linux installations!
	If there is already an X session running, you will need to specify a different DISPLAY in your command, for example:  $ sudo Xorg :1 -configure
	An xorg.conf.new file will be created in your current working directory. The contents of this file are derived from what the X server has found to be available in hardware and drivers on the local system. To use this file, it will need to be moved to the /etc/X11/ directory and renamed to xorg.conf:
	sudo Xorg -configure  ## some distros X , which is /usr/bin/X -> /usr/bin/Xorg ;
	sudo  mv      ~/xorg.conf.new    /etc/X11/xorg.conf
##________________________________________  ___________________________


#####  ==========  X11-/Xorg-xprofile/xinitrc/... start-profiles ... (/Xorgs/xinit/xinitrc/startx/config-X), users + glob ones :

	_______:  see for xinitrc / xprofile :
	https://wiki.archlinux.org/index.php/Xinit
	https://wiki.archlinux.org/index.php/Xprofile 
	- see also:  man startx  bzw..  view /usr/bin/startx  , The  startx  script is a front end to xinit(1) 
	- man xinit 

	_______:  Xinitrc ...:
	- ~/.xinitrc    ,   /etc/X11/xinit/xinitrc
	- global-initrc-file: /etc/X11/xinit/xinitrc  
	- user-initrc-file:   $HOME/.xinitrc  bzw. xprofile 

	_______:  X11-profiles:   xprofile  , ~/.xprofile , /etc/xprofile  :  pre-Loginmanager-configs!! pre-Xwin-Start! :
	- xprofile file, ~/.xprofile and /etc/xprofile, allows you to execute commands at the beginning of the X user session - before the window manager is started.  The xprofile file is similar in style to xinitrc.
	https://wiki.archlinux.org/index.php/Xprofile
	allows you to execute commands at the beginning of the X user session - before the window manager is started.
	The xprofile files are natively sourced by the following display managers:  GDM, LightDM, LXDM , SDDM
##________________________________________  ___________________________


#####  ==========  X11-/Xorg-adaptions, qckys,...:
- deactivating virtual-terminals (ctrl+alt+Fx) : in /etc/X11/xorg.conf.d/xxx (eg: 10-MyKioskAddies.conf), see man xorg.conf(5) : 
	Section "ServerFlags"
    	Option  "DontVTSwitch"  "True"
	EndSection  
-
##________________________________________  ___________________________


#####  ==========  cmdlines/-tools-for-xwins-X11:
	--- diagnose for X11 problems/infos :
	-!  man Xorg  ##/OR "X" in some distros ,which is same:  /usr/bin/X -> /usr/bin/Xorg
	- wininfo - window information utility for X
	- xdpyinfo - X-DisPlaY INFOrmation utility for X
	- xvidtune - video mode tuner for Xorg ; 
	- cu-screen-resolution?:  xvidtune -show
	- xwininfo - window information utility for X
	- xrandr : change-resolution/size/orientation of Screen;  is used to set the size, orientation and/or reflection of the outputs for a screen. It can also set the screen size.
	---
	-!! xdotool : simulating keyboard/mouse-inputs for win-manages : lets you programmatically (or manually) simulate keyboard input and mouse activity, move and resize windows, etc. It does this using X11's XTEST extension and other Xlib functions. ; see man xdotool
	- Remmina : remote desktop client to save your connections for all different remote Protocols (remote-X, VPN, spice, RDB,..) ...
########################### Waylands : ######################################################################## 
##________________________________________  ___________________________


#####  ==========  Wayland-OR-X11 is my-session/system using ??:
	--- Determining whether you are using Wayland OR  X11  /_190300-fedora :  (all-worked-ok! x13-ubt):     https://docs.fedoraproject.org/en-US/fedora/f29/system-administrators-guide/Wayland/
		- One way to determine if you’re running in Wayland, is to check the value of the variable $WAYLAND_DISPLAY. To do this type:
			$ echo $WAYLAND_DISPLAY  ##--->... 	wayland-0 ....
		If you are not running under Wayland the variable will not contain any values.
		- You can also use loginctl to show you what tpe of session is running:
			To determine your session number, simply typing loginctl should provide your session details.
			loginctl  ;  ##bzw.  loginctl  list-sessions  ;
			loginctl  show-session  <YOUR_SESSION_NUMBER>  -p Type  ;  ##/OR  loginctl  show-session  <YOUR_SESSION_NUMBER>  -all  | grepi type
		- There is also a legacy X11 server provided with Wayland for compatibility purposes. To determine what applications are running in this mode, you can run the following command:
			$ xlsclients
		- x13-ubt: what is my current gui-session (x11 or wayland?, gnome/unity/..., ??):
			expg xdg --->: XDG_SESSION_DESKTOP="gnome-classic" ,  XDG_SESSION_TYPE="x11" , ....
			also check:   echo $WAYLAND_DISPLAY  ;   expg wayland ;   expg x11 ;    expg gnome ;
	--- Disabling wayland :
		- for gnome-shell (Gnome 3.xx) with GDM login-manager:  vi /etc/gdm3/custom.conf ---> WaylanEnable=false ;
########################### ============================================== ################################### 
##________________________________________  ___________________________


#####  ==========  
