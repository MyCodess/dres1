_______ andorid-rooting/boot/customRoms/Recovery/TWRP/Magisk/...-dnts : __________________________________________
- rename to rooting-boot-CRec-CRom-dnts.txt
##________________________________________  ___________________________


#####  ==========  URLs-Sys-Rooting,....:

	_______:  Rooting-URLs
https://www.heise.de/ct/ausgabe/2018-4-Root-Zugriff-und-Custom-ROMs-mit-Android-3953344.html  bzw.  https://www.heise.de/select/ct/2018/04/1518741935652659
https://www.heise.de/select/ct/2018/8/softlinks/yxuv
https://www.heise.de/ct/hotline/FAQ-Android-rooten-4109848.html?wt_mc=print.ct.2018.16.170#zsdb-article-links
https://twrp.me/
https://developer.android.com/studio/command-line/adb
https://gitlab.com/BenjaminDobell/Heimdall
https://download.lineageos.org/
https://www.droidviews.com/download-odin-tool-for-samsung-galaxy-devices-all-versions/
https://forum.xda-developers.com/
https://forum.xda-developers.com/apps/magisk/official-magisk-v7-universal-systemless-t3473445
https://forum.xda-developers.com/apps/magisk/official-magisk-v7-universal-systemless-t3473445
https://forum.xda-developers.com/android/apps-games/one-click-root-tool-android-2-x-5-0-t3107461
https://www.supersu.com/download

	_______:  Custom-Roms-URLs:
https://lineageos.org/
https://wiki.lineageos.org/devices/kltekdi/install  --> or any other device, great-guide step-to-step-installation and links .... !!
https://wiki.lineageos.org/
##________________________________________  ___________________________


#####  ==========  Dics / DIFFs /vocabs / Abbrev-uue :
- Custom-Recovery	/CRec		<-->	Stock-Recovery / Recovery / Hersteller-Recovery
- Custom-ROM (TWRP,...)	CRom	<-->	Stock-ROM / Hersteller-ROM
##________________________________________  ___________________________


#####  ==========  boot-modis:
- 3 Betriebsmodis:  ct.18.08.174-178--Root_tut_gut--Rooting-und-zurueck-zum-Stock-ROM.pdf :
	Android-Geräte laufen in einer von drei Betriebsarten.
	1- Normal-Modus  :  Die übliche startet man mit dem einfachen Druck auf die Einschalttaste.
	- Daneben gibt es die Wartungsbetriebsarten Download und Recovery. Beide aktiviert man über Tasten-kombinationen :
	2- Download-Modus/Fastboot (1kk: Partiotion-Mgm, HD-Einrichten/partitionieren, Platte-Vorbereiten, formatieren...):   dient zum Einrichten der Android-Partitionen. Zu diesen gehören zumindest System, Data, Cache, Radio/Modem und Recovery (Wiederherstellung). Man kann sie mit In- halten des Herstellers oder mit fremden befüllen, zum Beispiel einer alternativen Software für das Recovery.
	3- Recovery-Modus (1kk: boot-init-1_Lx, neues-OS-aufspielen), startet das Gerät ein minimalisiertes Android für die Wartung, etwa zum Zurücksetzen auf den Werkszustand, das Rooting oder die Einrichtung eines Custom-ROMs.
##________________________________________  ___________________________


#####  ==========  LineageOS-nts:

	_______:  versions: 
	Lineage 15.1 (Android 8.1) 	MindTheGapps (mirror), OpenGApps
	Lineage 14.1 (Android 7.1) 	OpenGApps
	Lineage 13.0 (Android 6.0) 	OpenGApps
##________________________________________  ___________________________


#####  ==========  CT-Rooting-Lx: Steps-exp on Ubuntu + Rooting-Galaxy_S5 for the whole circle/procedure of:  install-CustomRecovery-TWRP + full-Backup + Rooting + restore-Samsung-ROM :   ct.18.08.174-178--Root_tut_gut--Rooting-und-zurueck-zum-Stock-ROM.pdf :  tried/_190221 :
	-! see also parallel:
	https://wiki.lineageos.org/devices/kltekdi/install
	https://forum.xda-developers.com/galaxy-s5-neo/how-to/how-to-t3298654

	_______:  ------------------------- A- Rooting of the Stock-ROM : --------------------------------------------

	_______:  Overview:
	Das Vorgehen beim Rooten oder beim Installieren eines Custom-ROMs besteht aus drei Schritten:
	1- Bootloader entsperren (USB-Debugging in Developer-options,... ; preprations).
	2- Custom Recovery installieren (instead of Stock-Recovery)
	3- Rooten oder Custom-ROM installieren und rooten.
1--- preparation : unlock-boot, enable USB-Debug, DW-Modus, ...: Basis-Settings-adatptions on Samsung-Org-System for later Custom-Rocevery/Rooten :
	- PC1: sudo apt-get install  heimdall-flash   heimdall-flash-frontend  android-tools-adb
	- Device1: develper-options/EntwicklerOptionen USB-Debugging aktivieren (7 mal auf Build-Nr tippen; Settings-->DeviceInfos/GeräteInfos-->SoftwareInfo/Status-->Buildnumber)
		USB-Debugging aktivieren unter EntwicklerOptionen 
	- 1kk: nicht gefunden!?:  Deaktivieren Sie auf dem Galaxy S5 in den Einstellungen im Bereich Sicher- heit die Reaktivierungssperre (Reactiva- tion Lock). Andernfalls fragt das S5 beim Zurücksetzen nach dem Passwort des Samsung-Accounts.
		- 1kk:dafü dies gemacht:
		!! worked ONly after activating of :  Settings-->Security-->install from Unknown Sources zulassen !!
		also sicherheitshalber :   OEM-Entsperrung erlauben/aktiviert   +   USB-konfig auf NRDIS umgestellt
	- Device1 power off
2--- Custom-Recovery/TWRP-installation in DW-Modus (not rooted yet!): Device1 restart in DW-mode und an PC1 anschliessen, um TWRP-/Custom-Recovery darauf zu installieren :
	- Device1 reboot in Download-mode :  Tastenkomination Leiser + Home + Power
	-!! 1kk: heimdall-calls always with option --no-reboot if reboot not wished !! see heimdall --help !	
	u1@x13: /up1/varu/varau/wks/ad1/ $   heimdall detect
	Device detected             ##--I-kk: heimdall detects devices only in download-mode !!
	- sudo heimdall download-pit --output backup_part_table.pit --no-reboot  ##--> after that must restart again in DW-mode (could try with --resume , but it does NOT work properly; so eg sudo  heimdall  print-pit --resume ; for me did not work!)
		just have it also readable, reboot-in-DW-mode and:  sudo  heimdall  print-pit  --no-reboot  > backup_part_table.pit.txt
	- dowloadin twrp:  https://eu.dl.twrp.me/s5neolte/twrp-3.2.3-0-s5neolte.img.html 
	- reboot Device1 in DW-mode
	- sudo heimdall  flash  --RECOVERY  twrp-3.2.3-0-s5neolte.img  --no-reboot  ## A blue transfer bar will appear on the device showing the recovery being transferre / fortschrit-anzeige auf dev1! hier wird Samsung-recovery-software ersetzt durch TWRP-recovery-SW !!
	-!!! AKKU+Strom einfach ruasziehen!! NOT-normal-Reboot!! but with buttons it reboots again in SAmsun-Android and Samsung will delete the TWRP-CRec !! so nach dem flashen jetzt hard-crash-down!! ohne Akku/Strom/PC-anschluss !!
	- (SD-Karten einstecken for backupsin der nächsten reboot in TWRP !)
	- Unplug the USB cable from your device.
	- MANUALLY reboot into recovery (NOT per TWRP-Menu/...! manually with device-buttons!):  With the device powered off, hold Volume Up + Home + Power. When the blue text appears, release the buttons.
	- Note: Be sure to reboot into recovery IMMEDIATELY after having installed the TWRP-custom-recovery. Otherwise the custom recovery will be overwritten/deleted and the device will reboot (appearing as though your custom recovery failed to install and stock-recovery is restored !!).
	---> stat: so, here is Custom-Recovery installed!! but NOT rooted yet !!
3--- Backup + Rooting/Magisk-install in CRec-Modus : Device1 restart in the new/custom RC-mode (ReCovery-Mode) to do  full-backup + rooting (if you like), first PC-connestion NOT needed, but you can do it ...:
	- jetzt soll bereits the Samsung-recovery-software ersetzt worden sein durch TWRP-recovery-SW !!
	- wo soll backup gemacht werden ?  (stecke SD-karte rein oder USB,....)
	- reboot GS5 im  Recovery-Modus w,which is now TWRP-recovery: Drücken Sie dazu gleichzeitig die Tasten Lauter + Home + Power, bis oben im Display „Recovery Booting“ erscheint. Lassen Sie die Tasten los. Dann sollte das TWRP-Menü erscheinen.
	- do backup all before rooting (if needed on SD-card by mounting it !)!  --> done! backedUp all parts not-rooted on the SDcard-8GB vom ord-samsung-device-not-rooted , only TWRP/CRec-installed !
	- download latest Magisk  https://forum.xda-developers.com/apps/magisk/
		from-Install-guide-Magisk:  ... If you plan to install custom kernels, flash the zip AFTER installing Magisk ... ! : so first TWRP-recovery and then with TWRP-menu install Maisk !
		chk all nts in  https://topjohnwu.github.io/Magisk/install.html !!
	- normal-booten (leichter im normal-boot zum kopieren; geht aber auch in Rec-mode) und kopiere Magisk-v18.1.zip to sdcard (in CT meinte weiterhin in TWRP-CRec-mode with adb push Magisk-v18.1.zip   /sdcard/, but ?? somehow copy this to the device1 ) 
	- reboot in  TWRP-CRec-mode and press "Install"-button of TWRP-Menu and install it ! without signature verification !!
	--> reboot-in-normal-mode ! OHNE TWRP-App jetzt mit dem TWRP-installer in RC-mode zu installieren !! System-Defekt ! see CT! (später könnte man von dem Syystem aus machen!
	install Magisk-Manager-xxx.apk by clicking on it in FileManager (if th APK not there , dw it or copy from PC1)

	_______:  ------------------------- A:fertig. Damit ist das Stock-ROM des Galaxy-S5 gerootet ! -------------------------------

	_______:  

	_______:  ------------------------- B: Custom-ROM/LineageOS flashing : -------------------------------------------------------
-! Rooting is NOT neccessarily required for Custom-Rom-flashing!! but hier GS5 is already rooted! what is only really required, is a Custom-Recovery/TWRP !! see-great-guide-for-S5:  https://wiki.lineageos.org/devices/kltekdi/install

	_______:  CRom-instell-steps-from-LineagesOS-Guide after haveing CRec on your device, eg fo Samsung-Galxy-S5 (not neo !!):
	https://wiki.lineageos.org/devices/kltekdi/install :    Installing LineageOS from recovery
	- Download the LineageOS install package that you’d like to install or build the package yourself.
    - gApps : Optionally, download additional application packages such as Google Apps /opengapps.org (use the arm architecture).  see   https://wiki.lineageos.org/gapps.html
    - boot recovery: If your device isn’t already booted into recovery, do so:   With the device powered off, hold Volume Up + Home + Power. When the blue text appears, release the buttons.
	- backup!!:  (Optional, but recommended): Tap the Backup button to create a backup. Make sure the backup is created in the external sdcard or copy it onto your computer as the internal storage will be formatted later in this process.
	- Format-Data : Go back to return to main menu, then tap Wipe. Now tap "Format Data" and continue with the formatting process. This will remove encryption as well as delete ALL files stored on the internal storage.
    - wipe Cache and System: Return to the previous menu and tap Advanced Wipe. Select the Cache and System partitions to be wiped and then Swipe to Wipe.
	- Sideload the LineageOS .zip package:
        On the device, select “Advanced”, “ADB Sideload”, then swipe to begin sideload.
        On the host machine, sideload the package using: adb sideload filename.zip
    - (Optional): Install any additional packages using the same method.
    -gApps-if-wanted :  If you want openGApps / Google Apps on your device, you must follow this stepi NOW, before the first boot into Android! see below-nts!
	- Rooting if-wanted (Optional, not-required!): Root the device by installing the LineageOS SU Addon (use the arm package) or using any other method you prefer.
	- reboot, done! Once installation has finished, return to the main menu, tap Reboot, and then System.

	_______:  

	_______:  gApps-onLineageOS :
	LineageOS-install-guide-wiki:
	Installation-gApps: Google apps should be installed via recovery immediately after installing LineageOS. Exact steps vary, but the process is similar to that of installing LineageOS:
	warning!! Important: If you reboot into LineageOS before installing Google apps, you must factory reset and then install them, otherwise expect crashes.
    Copy the Google apps zipfile to /sdcard/ ,Using adb: adb push filename.zip /sdcard/
    After installing LineageOS, choose “install zip” or “Apply update” in recovery, and navigate to the zipfile loaded earlier.
    Reboot to system (i.e. LineageOS).

	_______:  all done!

	_______:  backup-restored from earlier steps above (no-DW-stock-Rom), all fine !!  /190226/7 ; back-to-the-start-except-installed-TWRP instead Stock-CRec !

	_______:  ---------------__1END____ B: Custom-ROM/LineageOS flashing : -------------------------------------------------------
