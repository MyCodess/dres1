_____________ Win7 notes: _______________________

	_______:  !! here Allg-Win7-nts! the main-REFs are in CT-articels! only partly here in kk-nts!! also see:
	- CT-docs:		w/docs/CTs/CT_Articles_Topics/CT_Win7s/   spec. win7-dvd-Articles:  w/docs/CTs/CT_Articles_Topics/CT_Win7s/CT_Win7sDvd_Articles/
	- devnts:		w/docs_m/devres/devnts/mswins/win7s/
	- setup-l1nw:	w/docs_m/devres/l1nw_setups_res/l1nw_win7_setup/
	- w-docs:		w/docs/MSs/Win7s/
##________________________________________  ___________________________


#####  ==========  SP1-Win7-install (vo17-win71) probelm:
-!! SP1 wanted (so got problems): 110901-SP1-vo17-win71:
    1- win7-boot-part MUST be active-part!!
    2- win7-boot-part must be assigned drive letter!?!? (maybe!? or maybe the previous one was sufficient!? but this does not heart anyway!)
	--> in Lx : fdisk ... flag sda1 as active;
		then later, boot from Lx-rescue-usb and again deactivate it an keep active the extended-definition-part sda4 !!
-!! cleaning: big
	-ONLY if later on everything is OK, then cleaning with:   dism.exe  /online /cleanup-image /spsuperseded
##________________________________________  ___________________________


#####  ==========  Utils-embeded-Admin : cmdline-Controls/Guis/... aslo with runas-stuff, running as admin from cmd, ..., admin-control-panel ...;
-!! Resource-Monitoring: !!see 1022100 bzw. 1022106:
	- instead of TaskManager for finding bottlenecks:  %windir%\system32\perfmon.exe /res (as admin) ; also perfmon itself for more !!
	- Monitor/Ueberwachung: perfmon /sys  : mit Vergleichtsmoeglichkeiten, snappshots-vergleiche, logging,... see CT
	- bzw. SystemSteuerung: Control Panel\All Control Panel Items\Performance Information and Tools\Advanced Tools
- running Admin-Control-Panel from another user:
	- %systemroot%\system32\*.CPL are Control-Panel-Stuffs, so runas ...
	- Every Control Panel applet is in fact a file with a .CPL extension. If you perform a search for these files you'll see that they're all located in the %systemroot%\system32 folder.
-- runas in win7:
	- OK-cmd:  runas  /user:a1  %windir%\system32\cmd.exe   (but the same for Explorer not worked!)
	- OK-ComputerManagement: %windir%\system32\compmgmt.msc /s  (was called from an admin-cmd)
	- NOT-Ok:  explorer and control.exe
- Control-Panel-stuff (see coll-nts, hier just eg):   C:\Windows\system32\control.exe
	-eg: screen-saver:  %systemroot%\system32\control.exe desk.cpl,screensaver,@screensaver  (link copied from win-Help-source, can do for all other contorls/guis/....)
##________________________________________  ___________________________


#####  ==========  Utils-embeded-Users (Anwender-Apps/-Utils von win7-dvd; for OS/Sys/Admin-Utils see their extra nts further above):
-!! psr.exe : Recording-MouseActions-as-Fotos: C:\Windows\System32\psr.exe  : great for Docs/Anleitungen/...; generate a mht-zipped files. Also you can add comments,... to the fotos but only during recording (with add comment button)!!
- dism.exe : WIM-Abbildungen bearbeiten (aso in AIK): Deployment Image Servicing and Management (DISM.exe) installs, uninstalls, configures, and updates the features and packages in offline Windows® images and offline Windows Preinstallation Environment (Windows PE) images.: http://technet.microsoft.com/en-us/library/dd744382%28WS.10%29.aspx

	_______:  MS-dw-tools: can be added to the system from MS-dw:
	- AIK/WAIK: Windows Automated Installation Kit (AIK) : Windows-Images/deployment/Installations/unattended-Installations/Response-Files bearbeiten, generieren und ...:
	- AIK: a collection of tools and documentation that you can use to automate the deployment of Windows operating systems.
	- Also for Windows-PE creation.
##________________________________________  ___________________________


#####  ==========  Misc-Tips (Misc, smallies, helpies...):
-!! instead right-mouse for context-menu use always shift+right-mounse, a muchbetter context menu! see CT cs1007-p.103 !!
- Login-Gui--Backgroung-Changing:  : CT-cs1007-p.118--Anmeldeschirm :
	HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background set to 1
	- AND in explorer mkdir C:\Windows\System32\oobe\info\backgrounds
	- put image there, must be: backgroundDefault.jpg , and must be max 250 KB !
- powercfg -h off  --> deactivating hibernate  ; also Energy-/Power-Options and configs is done with powercfg !
##________________________________________  ___________________________


#####  ==========  NW-win7:

	_______:  -- cmdline-networking:
-!! netsh : all NW-stuff from cmdline!!: Network Shell (Netsh) commands offer an alternative to configuring network technologies using the Windows interface. C:\Windows\system32\netsh.exe
	http://technet.microsoft.com/en-us/library/cc725935%28WS.10%29.aspx	: doc-ref
	http://www.microsoft.com/downloads/en/details.aspx?FamilyId=F41878DE-2EE7-4718-8499-2EF336DB3DF5&displaylang=en
##________________________________________  ___________________________


#####  ==========  Profile, BenutzerDaten, AppDataDirs,....:
-!! see ct1005168_171_PeroenlicheDatenTrennenVomSysWin7_WIn7WartungsFreundlich.pd
-! verschieben der Kompletten Profile bzw. whole c:\users oder AppData,.. see ct1005168_171
##________________________________________  ___________________________


#####  ==========  Dirs-Sys-Conf-Win7 : ==================================
-!! see in cmd set outputs!!, as set app for APPDATA=C:\Users\a1\AppData\Roaming
- new DIRs in win7/vista: For example, the location of the Send To shell folder in Windows XP is Documents and Settings\username\SendTo. The location of the Send To shell folder in Windows Vista is Users\username\AppData\Roaming\Microsoft\Windows\SendTo.

	_______:  StartMenu/DesktopCOnfigs/....-Dirs:
	-!! APPDATA=C:\Users\a1\AppData\Roaming
	-!! finding out links-targets: cmd> dir /A:H  --> so you can find out all real-dirs as:
	- startmenu-allusers:	C:\ProgramData\Microsoft\Windows\Start Menu
	- startmenu-User:	C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu
	- startMenu, sendto, ...: %USERPROFILE%\AppData\Roaming\Microsoft\Windows	eg: C:\Users\a1\AppData\Roaming\Microsoft\Windows
	- sendto-user: C:\Users\a1\AppData\Roaming\Microsoft\Windows\SendTo
	- Pin-menus/Quick-Lunch: %USERPROFILE%\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch

	_______:  Libraries:
	- see CT-ct1005168_171_PeroenlicheDatenTrennenVomSysWin7_WIn7WartungsFreundlich.pd
	%HomeDrive%%HomePath%\AppData\Roaming\Microsoft\Windows\Libraries
	 %Public%\Libraries
	so see there per Lib the xxxx.library-ms , not with Explorer but with dir ...

	_______:  Favorites in Left-Explorer:  C:\Users\%USERNAME%\Links

	_______:  REGs-user:
	env-variables:  HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Session Manager\Environment

	_______:  Utils/Apps-Dirs+Configs:
	Firefox:   C:\Users\u1\AppData\Roaming\Mozilla\Firefox\Profiles\ljl7u75u.default
##________________________________________  ___________________________


#####  ==========  Updates-win7:
	- download-DIR of win-update-function: C:\Windows\SoftwareDistribution\Download\Install  , !! aber sie werden nach dem Dialog-Fenste-Anfrage schnell geloescht! see: ct1010168-173
##________________________________________  ___________________________


#####  ==========  Licensing/Versions/.... :
	- which Win7-version from DVD will be installed? : "R:\sources\ei.cfg" : if deleted, user will be asked, what should be installed (see CT: unverselle DVD: ct1010168-173)
##________________________________________  ___________________________


#####  ==========  WXP and Win7:
	-! WXP-Installtion-AFTER-Win7.Installtion (and win7.boot.restore): installing eg WXP after having installed Win7 on the same HD:
	see Windows7_TheDefinitiveGuide_Ore_0906_b.pdf--Ch.23--p.908 : Installing a Previous Version of Windows on a Computer Running Windows 7
##________________________________________  ___________________________


#####  ==========  
