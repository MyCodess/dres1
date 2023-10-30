________________________ termux-on-ad1-dnts : ___________________________________________________
--termux !!        (almost a full-Lx, if you install additional packages!):

	_______:  hist:	190300	:  first-big-dnts+installs+... on GS5
##________________________________________  ___________________________


#####  ==========  misc/allg:
	- https://wiki.termux.com/wiki/FAQ
	-!!-DIFF:   diffenrent procedures/setups if   {termux-window-on-android-device-directly}  <-->  {SSH/ADB-login and using termux-env for facilities} !!
	- terminal-resizing:  eval $(resize) ;#/OR manually:  export the output-values of resize for COLUMNS and LINES ! eg:  resize ;  COLUMNS=211; LINES=50; export COLUMNS LINES; 
##________________________________________  ___________________________


#####  ==========  install/config/permissions-nts:
	-!! Important: Do not mix installations of Termux and Addons between Google Play and F-Droid ! There are compatibility issues when mixing installations from these Internet portals. This is because each download website uses a specific key for keysigning Termux ... : https://wiki.termux.com/wiki/Termux:Boot
	-!! Do not mix also pkg-install from device and from PC as another user!! _1kk
	-!! mixed-rights-problem due to partly as root/other-user installed packages:     see also https://wiki.termux.com/wiki/FAQ#I_updated_termux_packages_as_root_and_now_I.27m_getting_.27permission_denied.27_as_a_non-root_user.  :
		change directory to /data/data/com.termux/ and run restorecon -R . and chown -R <user>:<group> . to recursively apply the changes. ; termux-user-name check with "id" /OR ll ; see 
	- 
##________________________________________  ___________________________


#####  ==========  Permissions....:
	-! Both the internal shared storage ( /sdcard/ , /storage/emulated/0/ ) and external SD cards do NOT support executive permissions. 
	    You need to move your scripts to the $HOME directory of Termux and set the permissions (chmod +x <scriptname>) before you're able to run it. Alternatively you can call your script with an interpreter: python script.py, bash script.sh
	-!! sdcard/Storage-access (normal has got limited accecc to ssdcard,..):  Settings>Apps>Termux>Permissions>storage add termux, and then run termux-setup-storage in Termux. 
##________________________________________  ___________________________


#####  ==========  PKGs /add-more-pkg:     see  https://wiki.termux.com/wiki/Package_Management  :
	-!! invoke "pkg/apt install ..." ONLY from device!  from PC/SSH/ADB the cache was then corrupted !! then had to do:  su - ; rm -rf /data/data/com.termux/files/usr/var/cache/* ;
	- dpkg -l  ##-installed    ;    pkg  list-all  ##-all-in-repo ;
	- add/Install package:   pkg install [package name]  ;  Remove package:   pkg uninstall [package name] ; List all packages:  pkg list-all ; pkg help ; Listing all installed packages: dpkg -l  ;(pkg == apt-get)
	- uue-added-pkgs:
	  pkg  install  man  openssh vim  mlocate  apt zip  rsync  tree  file  htop  binutils  coreutils  findutils ; ##--!!add-them!!
	  pkg  install  diffutils  dos2unix  fsmon  gawk  gzip  lynx  mtools net-tools  nmap  p7zip  readline sed  strace  tar  tracepath  unzip  unrar  util-linux  w3m  ;
##________________________________________  ___________________________


#####  ==========  users /username in termux or ssh/adb:
	-! username-of-main-cu-termux-install (for pkg,..; in GS5-install is u0_a154 ): in device enter "id" /OR see the user in ls -la /data/data/com.termux/files/home/ ;  then in ssh/adb:  su - u0_a154 ; ....
	- in profile-ad1.sh:   decide if you use termux (incldes also busybox) /OR eg busybox-direct-setuo (under magisk) /OR any other UX-setups,... and set the pathes appropriately! but try NOT to mix !
	- do 'su - <termux-user>' eg su - u0_a154  ; and then this profile! if needed later on you can also be root "su -" ; BUT other users as shell/... do NOT have access-rights to termux-dirs!
##________________________________________  ___________________________


#####  ==========  pathes on device1:
	- Install-Root:		/data/data/com.termux/    ##--uue:  termux_RDP
	- HOME=/data/data/com.termux/files/home/
	- PREFIX=/data/data/com.termux/files/usr/   ##--is set in temux-term!  -uue:  termux_pre_RDP
	- bin:   /data/data/com.termux/files/usr/bin/    bzw.   ${PREFIX}/bin   and  /data/data/com.termux/files/usr/bin/applets
	- etc:   /data/data/com.termux/files/usr/etc/    bzw.   ${PREFIX}/etc
	- man:   /data/data/com.termux/files/usr/share/man/
	- profiles:  /data/data/com.termux/files/usr/etc/profile  ,  /data/data/com.termux/files/usr/etc/profile.d/*  ,  /data/data/com.termux/files/usr/bin/login ;
	- installation-path:  Termux-bin is in  $PREFIX/bin where PREFIX=/data/data/com.termux/files/usr  ;##--1kk:  the "PREFIX"-envVar is already set in termux, when you start it!
	- apt-repos in :   $PREFIX/etc/apt/sources.list
##________________________________________  ___________________________


#####  ==========  VARs needed if you use its tools in eg adb-/ssh-shell and dot directly in termux-window! (they are set already in termux-window! for verifications/updates see their values in termux-window!
	- see   ${PREFIX}/bin/login  ##--mayebe some mods needed for you profile-ad1.sh
##________________________________________  ___________________________


#####  ==========  backup-termux-installation /tranfer it:
	see https://wiki.termux.com/wiki/Package_Management#Backup_and_restore_Termux_installatio
	obviously needs only a tar of $PREFIX/  !?
##________________________________________  ___________________________


#####  ==========  SSH / SCP termux (works with both passwd /OR  ssh-keys! )
	- see also:     https://wiki.termux.com/wiki/FAQ#How_do_I_ssh_in_Termux.3F   ,    https://wiki.termux.com/wiki/Remote_Access#Setting_up_password_authentication  ,  https://wiki.termux.com/wiki/Remote_Access#SSH ,  https://glow.li/technology/2015/11/06/run-an-ssh-server-on-your-android-with-termux/
	- server/SSHD on device:
		- install-sshd/openSSH:  on device call termux and :  pkg  install  openssh ;
		- starting-server:  sshd ; check-sshd-log:  logcat -s 'syslog:*' ;
		- see-device-IP for the client:  ifconfig ;
	--- client-ssh on PC/Host/remote:   password- /OR Key-login:
		- passwd-connection:
			- username-termux ??:  on device-termux:  id  /OR ls -l /data/data/com.termux/files  (on GS5, he is called u0_a154 )
			- password setting  (ssh-client did NOT work with empty passwd!):   passwd  
			- connection from PC-to-device:    ssh -p 8022  {u0_a154}@{ip_address}     ##--> enter pw  /OR for key  then nothing! done! ; 
		- key connection: 
			- if the PC-user has no sshkeys yet, generate them on the PC:   ssh-keygen -t rsa -b 2048 -f id_rsa ;  ##--generates-key-files:  id_rsa  (private)  , and  id_rsa.pub (public)
			- put your keys on PC in :  ~/.ssh/ ; check permissions:  chmod 700 ~/.ssh  ;  chmod 600 ~/.ssh/authorized_keys ;
			- on android-device (as NOT-root!):  check the permissions of ~/.ssh set properly as above! ; cd  ~/.ssh ; (somehow push/copy your id_rsa.pub to the device);  cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys ; chmod 600 ~/.ssh/authorized_keys ;
	- then if you like/need, do also "su - " there in ssh-window and become root also, if rooted !
	- If you have installed OpenSSH daemon, you can start it with command sshd. Also, the "standard" SSH port in Termux is 8022. So, to connect to the Termux via SSH, you have to use command ssh -p 8022 {ip_address}, with substituting {ip_address} with actual remote device IP. Note that Termux supports both password and public key authentication. All information can be found on Remote Access#SSH page. 
##________________________________________  ___________________________


#####  ==========  rsync over WLAN/SHH (with USB-plugged is jsut as normal easy, as long as the permissions are fine!):
	-! see  https://wiki.termux.com/wiki/Remote_Access#Rsync
	- Sync your photos with PC:      $ rsync -av /sdcard/DCIM/ user@192.168.1.20:~/Pictures/Android/
	- Get photos from remote Android device:     $ rsync -av -e 'ssh -p 8022' 192.168.1.3:/sdcard/DCIM/ /sdcard/DCIM/
	- Sync local directories (e.g. from external sdcard to Termux home):  $ rsync -av /storage/0123-4567/myfiles ~/files
##________________________________________  ___________________________


#####  ==========  TOR / accessing termux from internet :
	https://wiki.termux.com/wiki/Remote_Access#Accessing_Termux_from_the_Internet  !!
##________________________________________  ___________________________


#####  ==========  addons-2chk/-ifNeeded:
	- boot-scripting-addon:   https://wiki.termux.com/wiki/Termux:Boot
##________________________________________  ___________________________


#####  ==========  Lx-and-termux:
	https://wiki.termux.com/wiki/FAQ#Is_Termux_a_complete_Linux_Environment.3F
	https://wiki.termux.com/wiki/Differences_from_Linux
