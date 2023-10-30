____________________ vconsole brightness/fonts/locale/KB/... (hier for xfce4-in-Arx-2004 ... __________________
- see also KB/Keyboard-dnts extra !
##________________________________________  ___________________________


#####  ==========  conf /docs:
https://wiki.archlinux.org/index.php/Linux_console
https://wiki.archlinux.org/index.php/backlight
man  vconsole.conf
/etc/vconsole.conf
##________________________________________  ___________________________


#####  ==========  fonts:
https://wiki.archlinux.org/index.php/Linux_console#Fonts
- man vconsole.conf ,  showconsolefont , setfont , 
- in   /etc/vconsole.conf  :         FONT=....

	_______:  Persistent-configuration : The FONT variable in /etc/vconsole.conf ,as  
	... , FONT=lat2-16 ,  FONT_MAP=8859-2 , ...

	_______:  manually/one-time in one tty/vconsole cmd:    
	setfont /usr/share/kbd/consolefonts/xxxx   ##--as  iso01.16.gz, ...  Font names are case-sensitive. 
	! setfont    With no parameter, setfont returns the console to the default font.
	!Note: setfont only works on the console currently being used. Any other consoles, active or inactive, remain unaffected.

	_______:  Persistent also as:   kernel-paramter (overwrites all others):
	 FONT=, FONT_MAP=, ...; see man vconsole.conf 
- fonts itself are provided by The kbd package , usu. in:   /usr/share/kbd/consolefonts/  bzw.  /usr/share/kbd/....
	those ending with .psfu or .psfu.gz have a Unicode translation map built-in. 
	Keymaps, the connection between the key pressed and the character used by the computer, are found in the subdirectories of /usr/share/kbd/keymaps/, see /Keyboard configuration for de
- showconsolefont : in a vconsole shows the  char-table of the current-font ! 
##________________________________________  ___________________________


#####  ==========  brightness / Backlight :
-!! https://wiki.archlinux.org/index.php/backlight
-!! if X / xfce is running, so  the NB-Hersteller-Keyboard-bightness-button works also for the vconsoles! but if NOT, then has no effect!!
	so th KB-Backlight/brightness-button is handeld by the X/Xfce !
- manaully editing the value :
	here on asus14/AMD-GPU , otherwise check first the entries in /sys/class/backlight/ !! :
	cat /sys/class/backlight/amdgpu_bl0/brightness            ##--current-brightness-value
	cat /sys/class/backlight/amdgpu_bl0/max_brightness        ##--MAx-possible-value
	sudo  echo 120 >|  /sys/class/backlight/amdgpu_bl0/brightness  ##--set brightness to 120
-!! OK-worked cmds from XFce-Power-Mgm (xfce wa running on other tty !):  
	man    xfpm-power-backlight-helper
	xfpm-power-backlight-helper  --help
	xfpm-power-backlight-helper  --get-brightness
	xfpm-power-backlight-helper  --get-max-brightness
	pkexec xfpm-power-backlight-helper  --set-brightness  50
	...
	pacman -Qo  xfpm-power-backlight-helper
	/usr/bin/xfpm-power-backlight-helper is owned by xfce4-power-manager 1.6.6-1
	....
- systemd  :  systemctl list-units  | grepi backlight   ##-->... so coul use them ;  man systemd-backlight@.service
- to make it persistent, probably must use systemD /OR kernel-params !? see   //wiki.archlinux.org/index.php/backlight
##________________________________________  ___________________________


#####  ==========  
