________________________ Utils_SysAdmin-Sys, ProfiUsersUtils-ad1 : _________________________________________
##________________________________________  ___________________________


#####  ==========  uue-steps-addies/installs/...:
-! busybox install + links !
-!!  termux  !!! + addons: pkg install vim man ....  see extra-dnts !
##________________________________________  ___________________________


#####  ==========  UtilsSysAdminApps-ad1 :
https://busybox.net/downloads/BusyBox.html
http://www.landley.net/toybox/
##________________________________________  ___________________________


#####  ==========  termux !!  --->see extra-dnts here !!      (almost a full-Lx, if you install additional packages!):
##________________________________________  ___________________________


#####  ==========  busybox  in GS5neo :
	- use:   export  PATH=$PATH:/sbin/.magisk/busybox: ##--then vi/awk/sort/sed/.... are in the PATH !
	- pathes: physically:  sbin/.magisk/mirror/bin/busybox   , links-eg:   /sbin/vi  -> /sbin/busybox  /OR  /sbin/.magisk/busybox/vi  -> /sbin/.magisk/mirror/bin/busybox , .... 
	--nts:  busybox is basically just only ONE big binary physically installed in  /sbin/.magisk/mirror/bin/busybox ,  which depending on how it is called (which parameter), behaves differently, as the parameter.
	- physically it is one-big-executable installed in   /sbin/.magisk/mirror/bin/busybox
	- links-of-unix-tools (vi, awk, sed,....) for easier access are provided in    /sbin/.magisk/busybox/   and non-ersistent in /sbin/  , eg: /sbin/vi  -> /sbin/busybox
	- to call tools directly do export  PATH=$PATH:/sbin/.magisk/busybox  ; ##then you can call directly ls/vi/awk/... , as their links are there !
	-- help:
		- calling busybox with NO params directly, gives you a list of all compiled cmds:   /sbin/.magisk/mirror/bin/busybox
		- busybox --list ; 
		- man:   https://busybox.net/downloads/BusyBox.html
	--- pathes infos:
	/sbin/.magisk/busybox  vi  #same-as  /sbin/.magisk/vi , workes as calling vim in ubuntu, BUT all tools with reduced options !! eg. vim with no tabs, no multilple-files-handling, ...
	/sbin/.magisk/mirror/bin/busybox  vi  ##--or-as-linked:   :  /sbin/.magisk/busybox  vi  /OR direct-link:  /sbin/.magisk/busybox/vi  which is linked to  /sbin/.magisk/mirror/bin/busybox
	also installed all links in /sbin/    BUT  the are NOT persistent ! so during reboot are deleted! /sbin/ is anyway generated each time from android-OS by reboot !
