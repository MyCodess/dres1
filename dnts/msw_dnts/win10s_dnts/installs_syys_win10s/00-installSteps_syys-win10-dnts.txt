_____________________ for 1kk-/syss-win10-installs steps done ... __________________________________
- for more/RF see syss-nts !

#####  ==========  docs_RFs:
-! ct.15.27--070-080--Upgrade-fuer-Win10-1511.pdf  : Neuinstall oder upgrade oder VHD-Install !
##________________________________________  ___________________________


#####  ==========  prepares-/pre-install of Win10:

	_______:  ? partitioning-customized  (/OR avoiding-extra-BCD-part?? or having fat32-BCD-part??) if liked: ---> see extra-dnts in booties-....-dnts.txt !

	_______:  DWs : ISO + MCT  ---> see extra dnts!

	_______:  utils-dw:
	-! CT-Utils-Listing-Range-based:  https://www.heise.de/download/search#?page=1&sort=DOWNLOADRANK&elemcount=30
	-  https://www.heise.de/ct/ausgabe/2015-17-Welche-Funktionen-Windows-10-fehlen-und-wie-Sie-sie-ersetzen-2754086.html?wt_mc=print.ct.2015.17.90#zsdb-article-links  :  VLC , Classic Shell , ...
- ?? (if liked!?:   outlook.com/MS-Acc )!
##________________________________________  ___________________________


#####  ==========  time is UTC:
#-- OK-on-X17:  time of  BIOS/Firmware is  UTC :
    reg add  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation  /v RealTimeIsUniversal /t REG_QWORD  /d 1
	and disable Zeitgeber /TIme-Dienst:  sc config w32time start=disabled  ##--and also automatische tZeitanpassung, 
##________________________________________  ___________________________


#####  ==========  bcdedit addies-setup1:
- bcdedit  /set  {default}  bootmenupolicy  legacy  ##enabling F8 during boot to enter recovery-mode!  /_220721
- bcdedit  /set  {bootmgr}  displaybootmenu yes  ##--showing org-bootmenu
- bcdedit /set   {current}   bootlog Yes
- adding-safe-mode-with-cmd to bootmenu   /_220721 :
	bcdedit.exe   /copy {current}  /d Win10-Safe-cmd  ##The entry was successfully copied to {95eeec57-0a62-11ed-9f37-f04da26553c7}.
	bcdedit   /set   {9a8e4c86-371a-11ed-96a6-c95809b58413}  safeboot   minimal
	bcdedit   /set   {9a8e4c86-371a-11ed-96a6-c95809b58413}  safebootalternateshell  yes 
	#checkit Listin with:   bcdedit
	bcdedit > bcd2-mod.log

	_______:  !! power options: disable schnellstart !!, ...

	_______:  boot-gui-config  / msconfig?

	_______:  verbose-boot!?: works?:
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v verbosestatus /t REG_DWORD /d 1
see: https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/enable-verbose-startup-shutdown-logon-logoff-status-messages
- Note , Windows does not display status messages if the following key is present and the value is set to 1:
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\DisableStatusMessages
##________________________________________  ___________________________


#####  ==========  Utils:

	_______:  APPs-Ms uninstall !!:  --> ergaenze die Liste! :
default in powershell-PCs: no script can run! so in Powershell: 
PS C:\Windows\system32>  Get-ExecutionPolicy  #-is:  Restricted (is Default on PCs)
PS C:\Windows\system32> Set-ExecutionPolicy  ByPass 
PS C:\Windows\system32> T:\t1_Loc\w1_CPs\dc1k\dres\dnts\mswins_dnts\win10s_dnts\installs_syss_win10s\apps-uninstall-1.ps1
PS C:\Windows\system32>  Set-ExecutionPolicy  Default  ##--back to Restricted

	_______:  utils installs:
-!! see utils-Dir, here short:
- mkdir c:\Progs2 : 0-Portbl (bzw. 0-NoInstalls so portables), 0-cmdies , ...
- utils-elementary (explorer++, notepad++, 7zip, and also rest: PDF, browsers) : see utils-dir
-! notepad++ / texteditor !
- start-menu: open-shell menu
- explorer++ , explorer-alternative
- browser: iridium, vivaldi, ##weg-edge!
- NO-nvidia driver for now! NOT-really! not on x13 yet! fine with MS-default-driver !
- ?? offline-update-tools exists?? - ?? wsusu-offline-updates ?? still there? wird weiter entwickelt !?!?
##________________________________________  ___________________________


#####  ==========  basic-OS-configs: erste-handgriffe ...:
- CT-CortanaGehWeg-BingSearchWeg-WebSearchWeg-1803.reg ,  Bing-weg, WebSUche-weg !
	uninstall cortana (2chk!? not-CT): PowerShell, Select 'Run as administrator':  Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage
- Einstellungen --> Datenschutz.... fast alle deaktivieren ...!
- taskbar-icons + startmenu-icons basics: icons
- explorer-configs for all
- Systemsteuerung-->System : all configs! + optimale-leistung  + no swap-files,..
- CapsLock-disable.reg  --> effects after reboot !
- MS-Progs-remove ..., Systemsteuerung --> progs ..
- MS-Apps-remove  ..., Einstellungen --> Apps ; apps die nicht "deinstall"-option haben, dann über Powershelli-Amin (CT): Get-AppxPackage  -allusers <appname> | Remove-AppxPackage  ##--CT-Win10s/ct.19.15--152-154--Win10-mit-Win7-optik.pdf
- System --> disble coredump, hibernate-files ... , no-animation/leistung ... !
- powershell-as-admin:  update-help  ##-help-docs for cmds !
- tried ??:  PS-Admin:   C:\Program Files (x86)\Microsoft\Edge\Application\103.0.1264.62\Installer> .\setup.exe   --uninstall --force-uninstall --system-level

	_______:  !!  Energie-Einstellung: Schnellstart de-aktivieren bzw. Windows 10 KOMPLETT herunterfahren : ("restart" macht immer komplett-shutdown, aber nicht Shutdown-button! es sei denn, schnellstart wurde de-aktiviert !!):
	- einmalig: gleichzeitig die Shift-Taste gedrückt halten + Klicken Sie auf "Herunterfahren"
	- immer:   "Systemsteuerung" > "Alle Systemsteuerungselemente" > "Energieoptionen" > "Systemeinstellungen". Zu den "Systemeinstellungen" gelangen Sie über "Auswählen, was beim Drücken von Netzschaltern geschehen soll". Danach erweitern Sie die Ansicht über "Einige Einstellungen sind momentan nicht sichtbar". Abschließend entfernen Sie hier den Haken neben "Schnellstart aktivieren".
	- CT:  https://www.heise.de/tipps-tricks/Windows-10-komplett-herunterfahren-so-klappt-s-4245160.html
##________________________________________  ___________________________


#####  ==========  2dos-pos--by/after-initial-setup/install of Win10:
-! myPC-nicht-P2P-updateServer-for-others (P2P-server):  Zuerst zu den Updates, genauer zu der Art, wie Windows Updates an andere weiter- verteilt. Standardmäßig passiert das nicht nur im lokalen Netz, sondern auch übers In- ternet. Diese Peer-to-Peer-Verteilung redu- ziert nicht nur Microsofts Onli.ne-Rechnung, sondern dürfte im Ernstfall auch dazu beitra- gen, dass Notfall-Patches schneller bei allen Kunden ankommen. Wer das trotzdem lieber nicht will, kann die Verteilung auf das lokale Netz begrenzen oder ganz abstellen. Die Schalter stecken in den Einstellungen unter „Update und Sicherheit/Windows Update/ Erweiterte Optionen/Übermittlung von Updates auswählen“  /ct.15.21--132-137--Windows-10-Umstieg__Tipps-Tricks.pdf
-! Hintergrund-Apps closing (not ONLY sleeping, which is default):  Die zweite Stelle sind die Hintergrund- Apps. Anders als Anwendungen, die wirklich geschlossen werden, wenn man auf das Kreuz oben rechts klickt, legt Windows Apps im Kachel-Design nur schlafen. Und manche dürfen trotz Schließens sogar im Hinter- grund weiterlaufen, etwa um Ihnen Nach- richten zu schicken oder um Mails oder Chat- Nachrichten aus dem Netz nachzuladen. Microsoft weist selbst darauf hin, dass das Energie kosten kann. In den Einstellungen unter „Datenschutz/Hintergrund-Apps“ können Sie – leider nur einzeln – auswählen, welchen Apps das erlaubt sein soll.     /ct.15.21--132-137--Windows-10-Umstieg__Tipps-Tricks.pdf

	_______:  ! disable-Online-Search (Bing) / online-suche deactivieren / disable Cortans:
	--- CT:  do REGS in win10s_dnts/REGs-Win10s/... :
	c’t 2019, Heft 15 --152-154  + REGs :  ct.de/yb8m  and
	CT_OL:  ab-win10-1803-neue-REG-Einträge:  Windows 10 Version 1803: Microsoft ändert Abschalten der Web-Suche, heise.de/-4015544 , https://www.heise.de/newsticker/meldung/Windows-10-Version-1803-Microsoft-aendert-Abschalten-der-Web-Suche-4015544.html
	REGs: ct.de/yb8m  bzw. here in win10s_dnts/REGs-Win10s/... !
	---
	- uninstall cortana (2chk!? not-CT): PowerShell, Select 'Run as administrator':  Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage  ##--??--https://www.tomsguide.com
	---
	- older: Win10-pre-1803-release:  only disable cortana , pos-1803--see-above-nts! : in gpedit.msc /Group-Policy : Computer Configuration > Administrative Templates > Windows Components > Search (or in German .... suche) : "Cortana Zulassen" auf disable ! ##-CT:  see https://www.heise.de/newsticker/meldung/Windows-10-Version-1803-Microsoft-aendert-Abschalten-der-Web-Suche-4015544.html bzw.  Suche-Einstellung-anpassen:  /ct.15.21--132-137--Windows-10-Umstieg__Tipps-Tricks.pdf , S.136/7: 
-!? Treiber-ReInstallationen-Stoppen!?:  Eine weitere Störquelle stellen die mit Windows 10 per Update ausgeteilten Aktualisierungen für Treiber dar. Die ersetzen pe- netrant die Treiber des PC-Herstellers oder die vom Benutzer bewusst verwendeten – nicht immer zum Vorteil. Das beherzte Ein- greifen des Nutzers hilft: Er kann in der klas- sischen Systemsteuerung unter „Geräte- installationseinstellungen“ Windows 10 ver- bieten, Treiber herunterzuladen. Dann hört das Treiber-Ping-Pong auf.  /ct.15.20--098-116--Umstieg-auf-Win10.pdf--p.100
##________________________________________  ___________________________


#####  ==========  misc-during-install:
- cmd-window during install/boot:  Press Shift+F10
##________________________________________  ___________________________


#####  ==========  Schluessel/Key/license/Product Key/Aktivierung/....:
-! falls vorher war aktiviert, then einfach online gehen, mal sehen, müsste funktionieren !
-!!DIFF:   PRODUCT KEY  (which is hidden) <-->  PRODUCT ID (which is shown in System-Infos or Settings,...)

	_______:  CTs:
-! CT-KeyFInder script (win-keys rauslesen von Registry): ct.23.06.--068-078 !) bzw. DW:  ct.de/keyfinder  bzw. https://www.heise.de/hintergrund/c-t-KeyFinder-7486722.html  , FAQ:  c't 6/2023 S. 76
- ct.19.06, S. 26  :  FAQ:  Windows-Aktivierung nach PC-Wechsel
- Aktivierungs-FAQ : c't 6/2019, S. 24-26 , bzw. Starker Helfer, PC-Umzug mit c't-WIMage, c't 6/2019, S. 22-26 + Aktivierungs-FAQ !
- ct.18.04--114-115--FAQs__Aktivierung beim Gratis-Upgrade
- Installation-Key, win7-to-win10-key,... see ct.16.14--084-101--Letzte-Chance__Windows10-gratis.pdf --p.86-87
- Nachprüfen des Installations-Schluessels können Sie das unter Win- dows 10 in einer mit Administratorrechten laufenden Eingabeaufforderung mit dem Befehl slmgr -dli ##-- ct.16.14--084-101--Letzte-Chance__Windows10-gratis.pdf
- kk: upgraded systems (eg from win7-to-win10,...) have only a digital-activation registered for this NB/PC-hardware , and NOT a typical Product-key!

	_______:  MSs:
- A Windows product key is a 25-character code used to activate Windows. It looks like this:  PRODUCT KEY: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

	_______:  Int:
- 

	_______:  Utils:
- ShowKeyPlus   see ct.18.04--114-115--FAQs__Aktivierung beim Gratis-Upgrade
-
