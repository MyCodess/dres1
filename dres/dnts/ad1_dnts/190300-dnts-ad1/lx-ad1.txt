_________________ Linux--androids : ____________________________________________
##________________________________________  ___________________________


#####  ==========  
- pacman -Syu  android-tools ; adb --help ; pacman -Ql android-tools ;
- And-Studio is in AUR !
########################## 2019pre (more on ubuntu), still-OK!: ##########################
rename it  to  lx-ubuntu-ad1-dnts.txt
##________________________________________  ___________________________


#####  ==========  URLs :
https://developer.android.com/
https://developer.android.com/studio/command-line/adb	:  Android Debug Bridge (adb) 
https://developer.android.com/studio/run/device  	:  Run apps on a hardware device 

	_______:  docs_RF :
-!!!  ubuntu + android zum rooten/TWRP/... :  ct.18.08.174-178--Root_tut_gut--Rooting-und-zurueck-zum-Stock-ROM.pdf 
##________________________________________  ___________________________


#####  ==========  CT: Steps-exp on Ubuntu+Galaxy_S5 for the whole circle/procedure of:  install-CustomRecovery-TWRP + full-Backup + Rooting + restore-Samsung-ROM :   ct.18.08.174-178--Root_tut_gut--Rooting-und-zurueck-zum-Stock-ROM.pdf :  tried/_190221 :
	!! ---> see nts in  ./rooting-boot-ROMs-recovery-parts-dnts.txt   !! all done on ubuntu 18.04 LTS , X13 with ca1-Galaxy-S5-Neo /_190200
##________________________________________  ___________________________


#####  ==========  SSH/SCP from Lx to ad1:

	_______:  ok-worked--190301 :
	- first on device install SSHDroid (SSH-server)
	- start the SSHDroid server
	- ssh from Lx-x13 :	ssh root@192.168.8.106  (default-pw admin ...)
	- scp from Lx-x13 :	scp -r root@192.168.8.106:/data/data/com.android.providers.telephony/databases/  . 
##________________________________________  ___________________________


#####  ==========  ADB-cmds-seq-ad1Lx :

	_______:  nts-ADB:
	-! When you're working inside the bootloader, adb NO longer works. You're not yet booted into Android, and the debugging tools aren't active to communicate with. You'll need to use the "fastboot" command in its place.  see man adb
	-!  if not working adb reboot xxx , or adb root,..., then try restatring the server! once worked!:  adb kill-server ; adb start-server

	_______:  adb cmds most-commons :
adb  devices ---> ONLY if device booted already in android!! so in bootloader-status ADB can NOT connect/do anything with the device !! use "fastboot"-cmds ,eg. "fastboot devices", instead !!
adb  reboot
adb  reboot  recovery
adb  reboot  bootloader
adb  install TheApp1Name.apk
adb  install -r TheApp1Name.apk  ##--update App1
adb  install -s TheApp1Name.apk  ##--install it on the SDcard
adb  kill-server
adb  start-server
adb  shell  ##--goes into the shell an waits for your commands to be executed on the device/handy !
adb  shell <cmd1>   ##--executes the cmd1 on the device and returns back to the PC !
adb  sideload .... ##--Sytem-Patch-update  , bzw. install-APK-package
adb  sideload <package1.apk>    ##--Side load (install in APK format) 
adb  logcat       view the device log in real-time  ;##  adb logcat -C to view logs in colour      ;##  adb logcat -b radio to view radio logs ;

	_______:  adb-connect DIFF : if one device only connected to your PC  <-->   if multi devices connected to the PC :
	--- checked/list connected android devices to the PC:
		u1@x13: /up1/varu/varau/tests/ $  adb devices  [-l]
			List of devices attached
			4103571f021330a3	device
	--- if only one device connected eg:
		adb -d push t1-ad1.txt  /storage/extSdCard/0wk1/   ##--> it starts also automatically the adb-server! keep handy-diplay not-locked, so that you can reply any popups there !! works also without -d !
	--- specifying the device if several devices/emulators connected to the PC::
		u1@x13: /up1/varu/varau/tests/ $  adb -s  4103571f021330a3  push t2-ad1.txt  /storage/extSdCard/0wk1/
##________________________________________  ___________________________


#####  ==========  Utils_Lx_Ad1-System/RC/Roots/...:

	_______:  heimdall  ,  (GUI:  heimdall-frontend , not-needed)  --> is Download-Modus-Util, to flash the Custom-Recovery to Device !! to connect when device in DW-Modus !!
	-works?/installed-properly??:     heimdall version
	- heimdall  --help                ##--II-no-manPages !!
	- heimdall print-pit              ##--->   If the device reboots, Heimdall is installed and working properly !!
##________________________________________  ___________________________


#####  ==========  Ubuntu-Android-Pkgs :
u1@x13: /up1/t1/syss/1503ubt/logs/ $date
Mi 13. Feb 23:25:44 CET 2019
aptssg  android
sudo apt-get install  android-tool*
sudo apt-get install  android-sdk*
sudo apt-get install  *heimdall*
u1@x13: /up1/t1/syss/1503ubt/logs/ $pkgssg android
ii  android-tools-adb                  1:7.0.0+r33-2          all                    transitional package
ii  android-tools-adbd                 5.1.1.r38-1.1          amd64                  Android Debug Bridge daemon
ii  android-tools-fastboot             1:7.0.0+r33-2          all                    transitional package
ii  android-tools-fsutils              5.1.1.r38-1.1          amd64                  Android ext4 utilities with sparse support
ii  android-tools-mkbootimg            5.1.1.r38-1.1          amd64                  Android tool to create Android boot images
ii  fastboot                           1:7.0.0+r33-2          amd64                  Android fastboot tool
--
u1@x13: /up1/t1/syss/1503ubt/logs/ $aptssg android
....
android-androresolvd
android-logtags-tools
android-platform-build-headers
android-platform-frameworks-native-headers
android-platform-libcore-headers
android-platform-system-core-headers
android-platform-tools-base
android-sdk
android-sdk-build-tools
android-sdk-build-tools-common
android-sdk-common
androidsdk-ddms
android-sdk-helper
androidsdk-hierarchyviewer
android-sdk-platform-23
android-sdk-platform-tools
android-sdk-platform-tools-common
androidsdk-traceview
androidsdk-uiautomatorviewer
android-src-vendor
android-tools-adb
android-tools-adbd
android-tools-fastboot
android-tools-fsutils
android-tools-mkbootimg
google-android-build-tools-17-installer
.....
##________________________________________  ___________________________


#####  ==========  
