##________________________________________  ___________________________


#####  ==========  2Do: mit Dummy-WXP Testen/checken: ==================
_______________________ PCs, ... _______________________
==== KU3-Xp Akt Test:
	- Deakti. für Netzwer/Freigaben/Lan notwendig: Computerbrowser + Server
	- DHCP-Client: Deakt.
	- einfache TP-ip deaktivieret?
	- TCP/IP-NetBIOS-Hilfsprogramm deak.?
	- Terminaldienste deaktivert; notwendig für remote desktop
	- Windows Audio-dienst . manuel
____________________________________________________________
_______________________  CP--CT-Articels/Prj : WXP/Wins,... (org: see extra CTs-nts): _______________________
	-! SATA-wxp-driver-install: 0822202 , Soft-Link: 0822202 : Setup-Stick : XP auf Netbooks installieren (ohne CD-Rom)!! (several different scenarions)
	-! WXP auf Netbooks, ohne CD-Laufwerk:  0822202 , Soft-Link: 0822202 : Setup-Stick
	- RootKits, Bot-Net WP: Ihr PC als Komplize: 0702076
	- Offline-Update-Windows: Selfmade Service Pack , Windows-Updates ohne Internetverbindung installieren : c't 23/06, S. 202 (olds: CT 26/03, S. 106)
	- Knoppicillin auf Virenjagd (AntiVir-Boot-CD), Erste Hilfe CD: c't 21/2006, S. 168: Sicherheit Knoppicillin ; (in82 check with CD; not containing RootKits)
	- Email-security-config: 0408164
	-! Windows Blauscreen: 0410094 : Start,boot, rettung ...; WIndows-Debuger: 0410110
	-! Windows unkaputtbar machen (installieren, selbshilfe, updates-Katalogues,...): 0326094 + 096 +102 +106
	-!- Boot/Start process und probleme: 0326094
	-! Der Sichere PC-Windows; Windows Abschotten: 01/2003 , S. 80-94
	-! Warmlaufen : Axel Vahldiek: 0223178 : Warmlaufen Erste Handgriffe nach der XP-Installation: Praxis, Windows XP, XP, Umstieg, Explorer, Taskleiste, Startmenü, Tour
	- Windows-Exlorer-Dateitypen: in Windows/Explorer, SUffixes, Endungen, assoziations, classes: 2/2002 , S:186
	- poledit:  c't 8/02, S.106  (104, 106, 116);
	- Group Policy Editor: gpedit.msc
	- Wiederherstellungs-Console-WXP-(Dos): CT 23/02  S. 180  Am eigenen Zopf +  c't 22/01, S. 146
	-! User/Profile/Pathes: 26/2002 , S. 112 ; Nus einen User-Home verlagern, e.g. a1:
		- einfach als ein anderer admin (e.g. a2, admin1, ...) einlogen
		(- vielleicht ein HOMEROOT_MAIN_USERS global variable definieren)
		- a1-oldHome nach neuHome kopieren mit xcopy ... /v /e /x /k /o /c /h  (falls %HOMEROOT_MAIN_USERS% in FAT-partition, dann ohne /o /x ,...)
	 	- in Registry HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\"....a1-key.." verzeichnis setzen auf %HOMEROOT_MAIN_USERS%\%USERNAME% oder ...\a1 ???
	 	- opera-ini datei anpassen im neuHome; vielleicht auch checken Mozilla, ... falls installed
	- Ohne Admin-Rechte: Admin-User umwandeln in normalen user: 0415106 ; - Arbeiten ohne Admin-Rechte unter Windows: 0415118
	- IE-Suchmaschine-Icon: 12/02 S. 222 ; 	- IE ketten: 01/2003
____________________________________________________________
############### WXP-Commands and Programm names with and without GUIs:
	============= WXP-GUI-Tools-Programm-Names  to invoke GUIs from dos:
	- charmap : unicode/encoding-charsets
	- invoking any MMCs-COntrolManagement, as admin: runas /profile  /user:a2   --> open: %SystemRoot%\system32\*.msc  ; eg. devmgm : devices-management,...
	- invoking MSCs as admin-shortcuts (MachMichAdmin.bat with GUI):
		eg. Computer-Verwaltung: C:\WINDOWS\system32\runas.exe /profile  /user:a2  "cmd /C start  %SystemRoot%\system32\compmgmt.msc /s"
	- Verwalung/Administrative-Tools Menu points:   compmgmt.msc /s
		- compmgmt.msc : Computer Management Window
		  as shortcut: C:\WINDOWS\system32\runas.exe /profile  /user:a2  "cmd /C start  %SystemRoot%\system32\compmgmt.msc /s"
	- msconfig : Ini-Dateien
	- msinfo32 : Systeminformationen, Export System-Info ;leider jetzt eingebunden in HelpCenter
	============= WXP-nonGUI-Tools-Programm-Names  to config WIN from dos without their GUIs:
	- Power Configs/Options (ACPI, Hibernate,...): powerCfg  /?  ; eg powercfg /HIBERNATE off
	- color /? ; eg for DOS-window-colors
	- Check always support-tools-Dir (support.cab and its help file Suptools.chm on WXP-CD or in installed Dir and C:\WINDOWS\Help\suptools.chm.) and WIN\system32-Dir   for *.exe ; there are a lot
	- CT 16/2003 , Windows Virtuos
	============= WXP-Std-Ref-Commands-nonGui (listen in MS-Help but not batch commands; so as tasklist,..)
	--for a complete list see entries in WXP-Help
	-! tasklist /svc  : welche services hinter welchen prozessen?
################ END-WXP-Commands-ProgNames
##________________________________________  ___________________________


#####  ==========  "cmd"-command itself: invoking and configs  ; DOS-Window-Config ; DOS-Shell: cmd /?
	- run ADMIN-Dos:  runas /profile /user:localhost\a2 "cmd /E:on /F:on /T:1F"   (/user:<UserName> should be in form USER@DOMAIN or DOMAIN\USER ; so WITHOUT \\ in hostname)
	- cmd without DOS-window for apps: cmd /C start ... (eg in MachMichAdmin/CT)
		eg:  C:\WINDOWS\system32\runas.exe /profile  /user:a2  "cmd /C start  %SystemRoot%\system32\compmgmt.msc /s"
	- TAB-Erweiterung-DOS-Shell (see cmd /?): HKCU bzw HKLM\SOFTWARE\Microsoft\Command Processor : for Tab-completetion: CompletionChar == 9 ;
##________________________________________  ___________________________


#####  ==========  Desktop, Menu, Configs, Env, Misc-kramm ...: =========================
	- Schnellstart-Leiste: C:\Dokumente und Einstellungen\a1\Anwendungsdaten\Microsoft\Internet Explorer\Quick Launch
	- Icons
		-Win-def-icons are in: %SystemRoot%\system32\SHELL32.dll
		- moz-mail-icon:  %ProgramFiles%\mozilla.org\Mozilla\chrome\icons\default\messengerWindow.ico
	- Start-menu-Adds:
		- mail-m1: C:\WINDOWS\system32\runas.exe /profile /user:m1  "C:\Programme\mozilla.org\Mozilla\mozilla.exe -mail"
	- Autoplay, Autorun: 17/2003  s180 : gpedit.msc: AdminVorlagen->System: Auto...  oder mit Powertoys/TweakUI
	----- Programzugriff und standards (standard configs MS/no-MS/user):
		- for media-plaers-selection-box: HKEY_LOCAL_MACHINE\SOFTWARE\Clients\Media
	- Autostart for Users deaktivieren (nicht schreibbar; nur lesen) schreibrecht UND Besitz wegnehmen von dem User fuer (vielleicht ein temporäres Gruppenwechsel ist notwending ; siehe: CT 0415110):
		- User-Atuostart-Menu  und
		- Registry: HKCU: windows\currentversion\run + runonce  und  windows NT\currentversion\windows
############# Registries/Policies/Richtlinien: (siehr auch ct-tip-datenbank datei fuer weitere eintraege!!)
	===== Registry files (eg. for backups):
		They're normally stored in the System32\Config subdirectory of your system volume;
		you can always find the correct location by examining the value of HKLM\SYSTEM\CurrentControlSet\Control\hivelist
	===== Explorer-Regs:
	- C:\WINDOWS\system32\config : reg-files
	- Explorer-Contextmenu-Neu (rechte maustaste -> neu ...):  HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Discardable\PostSetup\ShellNew
	- FehlerBerichtErstattung to MS deaktivieren: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PCHealth\ErrorReporting\DoRreport  = 0
	- Explorer: Dateitypen-User: (see CT  2/2002 , S:186 )
		- Rheinfolge/priorität: first check HKCU (siehe unten) and then HKCR ; meistens bei CU sind nur openWithList (die Liste für "öffnen mit") dabei, der rest wird von CR genommen, es sei denn die Standardwerte, shell, ... wären bei CU gesetzt.
		- HKCU\....\FileExts\.suffix_xxx  bzw. danach HKCR\.suffix_xxx	->	 HKCR\App-Type	-> shell -> open, ...
		- Die globale Assoziationen in : HKEY_CLASSES_ROOT (kurz HKCR) :	so first in .suffix -> then under its App.
		- "Öffnen Mit"-Liste im ContextMenu ist ProUser:  HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts	  -> openWithList (auch im Expl.-OrdnerOptionen sichtbar.)
		- Context menu e.g. for directories: HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\shell\...  (see Dos-Box reg-install-script)
	- Exlporer-User-Directories: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
	- Allaire-auf-Desktop-Weg: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace
	- Allaire-Scheiss-FTP-AddOn-auf-SchnellStart bzw. DrogDrop-Mouse-Action:  HKEY_CLASSES_ROOT\Directory\shellex\DragDropHandlers	(bzw. Allg. Folder\ oder Directory\ ...\shellex\ContextMenuHandlers oder DrogDrop...)
	- Verknuepfung mit / Shortcut to ...:  HKLU\Software\Microsoft\Windows\CurrentVersion\Explorer\Link  == 0 (HEX/binary 0): ohne "verkn. mit/shortcut to..", so: "link"=hex:00,00,00,00  ; nicht-Weglassen: delete-key
	==== IE-Regs:
	- Suchmaschiene-Icon: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Search\SearchAssistant
	==== System-Reg:
	-!! drive-letters are in: HKEY_LOCAL_MACHINE\SYSTEM\MountedDevices ; if wrong, delete the whole key. it will be generated again!
	-!! drive-letter-problems (D: instead C: ...): see w-Docs-Imagers-WPs/dd-cloning-and-imaging and also
		http://support.microsoft.com/default.aspx?scid=kb;EN-US;Q223188
		http://www.2pi.info/software/copying-windows-new-hard-drive.html
	- AutoRuns:
		HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
		HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
		-- RunOnce"-Einträge der Registrierung beim Start ignorieren (2000/XP/2003):
			Standardmäßig werden alle Einträge unter HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce einmalig beim Start von Windows ausgeführt.
			Nun möchten Sie dies jedoch unterbinden, sodass alle Einträge unter "RunOnce" einfach ignoriert werden. Dies ist ohne Weiteres möglich, achten Sie jedoch darauf, dass z. B. viele Setup-Routinen zur Fertigstellung der Installation einen Eintrag dort hineinsetzen.
			1.Gehen Sie zum Registrierungsschlüssel HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
			2.Erstellen Sie den DWORD-Wert "DisableLocalUserRunOnce" und weisen Sie ihm den Wert "1" zu.
			Löschen Sie einfach den Wert, um die Änderung wieder rückgängig zu machen.
	- AutoPlay for removeable medias deaktivieren (TweakUI):
		-OK:  HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoDriveAutoRun == FF FF FD 03 	: Autoplay alles dekativieren?
		-???  HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoDriveTypeAutoRun  ==  alles deaktivieren: 181/b5 ; only removable medias deaktivieren: 149/95 ; Alles Aktiviert: 145/91 ;
	- Auslagerungsdatei löschen beim runterfahren:	 Verwaltung -> Lokale SIcherheitseinstellungen: Lokale Richtlinien -> Sicherheitsoptionen -> Herunterfahren: Auslagerungsdatei...löschen: Aktivieren!
	- RUN: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
	- Tour-Deaktiv: HKEY_LOCAL_MACHINE\ SOFTWARE\Microsoft\Windows\CurrentVersion\Applets\Tour, erstelle dort einen neuen DWORD-Eintrag namens `RunCount´ und weist ihm den Wert `0´
	- Env-Varaiables-System/Allusers:  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
	- Env-Varaiables-CU/User:	 HKEY_CURRENT_USER\Environment
	=== User-Profiles see extra paper: WXPs_KB\User_profiles...txt
	==== Misc-Reg:
	- Herunterfahren: Auslagerungsdatei des virtuellen Arbeitsspeichers löschen in:
	  Computerkonfiguration\Windows-Einstellungen\Sicherheitseinstellungen\Lokale Richtlinien\Sicherheitsoptionen  :
	  /OR EN: shutdown: clear virtual memory pagefile
		Wurde diese Richtlinie aktiviert, wird die Systemauslagerungsdatei beim Herunterfahren gelöscht.
		Bei Aktivierung dieser Sicherheitsoption wird die Ruhezustanddatei (hiberfil.sys) genullt,
		sofern der Ruhezustand auf einem tragbaren Computer deaktiviert wurde.
##________________________________________  ___________________________


#####  ==========  boot,system-start,Rettung, Blue-Screen
	- F8 beim booten druecken -> menu for start modus
	- sicherheits-kopien von xp-registry in "System Volume Information"\_restore......: CT 0410094
	- ! drive letter in: HKEY_LOCAL_MACHINE\SYSTEM\MountedDevices ; if wrong, delete the whole key. it will be generated again!
##________________________________________  ___________________________


#####  ==========  Platten,Disks,Partiotions,format,fdisk,Sys,...:
	--- SATA-wxp drivers: Intel-drivers + CT-registry-file , see CT-0822202
	--- FAT/FAT32 Cluster size restrictions:  (Cluster-Size == allocation-unit-size)
		- see format /?  :description to /A:size ...
		-! FAT: Number of clusters <= 65,526   ; FAT32: 65526 < Number of clusters < 4,177,918
		-! Allocations Units /Sector sizes FAT32 eg:
			- up to  15 GB : 4 KB  OK ; eg: FAT32  20 GB then must be at least 8 KB sector size
			- 30 GB partition , FAT32, 8K  :   31457280 K / 8 K = 3,932,160  ---> is smaller than 4,177,918 --->  OK  ; but eg. 4KB is too small !
	--- FAT32 Cluster Size by formating:  (WXP-SP2 auf HD-60GB von in82, Maerz.2005)
		- format W: cluster-groesse: bis 16000 MB Partitionsgroesse geht noch mit 4 KB cluster; danach mind. 8kb clustersize;
		- bei 16GB (16384 MB, also > 16000MB) ist es gescheitert mit 4kb cluster; will 8kb
		- ab 8GB partitiongroesse wollte mind. 4kb cluster.
##________________________________________  ___________________________


#####  ==========  Dos-Wiederherstellungs-Console:  CT 23/02	 S. 180	 Ameigenen Zopf
	1- Install: con WXP-CD: i386\winnt32  /cmdcons
	2- Um auch andere Verzeichnisse sehen zu können:
		a- Registryänderung : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Setup\RecoveryConsole\SetCommand	= 1
		b- von der Console: set AllowAllPath=true
	--------- Hier der CT-Artikel-Teil:
	Wiederherstellungskonsole
	Wo aus Platzmangel oder aus anderen Gründen die Installation eines zweiten Windows nicht möglich ist, bietet sich ein weiteres Werkzeug an, das bei Windows XP im Lieferumfang enthalten ist: Die Wiederherstellungskonsole ist ein textbasiertes Minimalsystem, ähnlich der Eingabeaufforderung, aber mit einem anderen Befehlsumfang.
	Um die Wiederherstellungskonsole für den Fall der Fälle parat zu haben, sollte man sie zunächst installieren. Das geschieht durch den Aufruf
	D:\i386\winnt32.exe /cmdcons
	aus einer Eingabeaufforderung heraus, wobei D: der Laufwerksbuchstabe des CD-ROM-Laufwerks ist, das zu diesem Zeitpunkt die Windows-Installations-CD enthalten sollte. Diese Installation trägt die Wiederherstellungskonsole in das Boot-Menü ein, quasi als weiteres Betriebssystem. Aber selbst ohne diese Installation lässt sich die Wiederherstellungskonsole verwenden: Dann muss man den Rechner von der Windows-CD starten und auf der Eingangsseite zum textbasierten Setup die Reparatur des installierten Systems auswählen.
	Diese Startart der Wiederherstellungskonsole ist auch die einzige, die hilft, wenn ein Virus oder eine andere Betriebssysteminstallation den Master-Boot-Record der Festplatte oder den Bootsektor der Windows-XP-Partition beschädigt hat. Innerhalb der Konsole helfen gegen diese beiden Probleme die Befehle fixmbr beziehungsweise fixboot. Ansonsten ist der Befehlsumfang der Wiederherstellungskonsole eher eingeschränkt: Alte DOS-Bekannte wie dir, copy, ren, md, rd und deltree stehen zwar zur Verfügung, aber es ist beispielsweise nicht vorgesehen, weitere Programme zu starten. So fehlt unter anderem ein Texteditor. Auskunft über alle Kommandos liefert der Befehl help; mit help <Kommando> gibt es weiter gehende Hinweise zu einzelnen Kommandos.
	Was diese Hilfe verschweigt, ist die Tatsache, dass man mit den DOS-ähnlichen Befehlen standardmäßig nur auf einige wenige Verzeichnisse zugreifen kann. Dazu gehören die Wurzelverzeichnisse sämtlicher Partitionen, das Systemverzeichnis samt Unterordnern der Windows-Installation, an die man sich angemeldet hat, alle Wechseldatenträger sowie das Installationsverzeichnis der Wiederherstellungskonsole selbst (normalerweise C:\cmdcons). Um diese Beschränkung aufzuheben, muss man den Befehl set AllowAllPaths = TRUE eingeben. Der liefert aber - genau wie die übrigen in der Hilfe dokumentierten Ausprägungen des set-Befehls - erst mal nur eine Fehlermeldung. Man muss ihn zuvor freischalten, und zwar durch einen Eingriff in die Registry, den man zweckmäßigerweise direkt nach der Installation der Wiederherstellungskonsole vornimmt. Der zuständige Wert heißt SetCommand und findet sich im Schlüssel HKEY_LOCAL_MACHINE\Software\Microsoft\WindowsNT\CurrentVersion\Setup\RecoveryConsole. Nur wenn hier eine 1 eingetragen ist, verdaut die Wiederherstellungskonsole den set-Befehl ohne Murren.
	Erwähnenswert sind noch die Befehle diskpart zum Erstellen und Löschen von Partitionen, format, um sie anschließend zu formatieren, und chkdsk zum Überprüfen der Verzeichnisstruktur. Um ein streikendes Windows wieder zum Leben zu erwecken, helfen häufig die Befehle listsvc, disable und enable: Mit ihnen lassen sich alle installierten Dienste nebst ihrem Status auflisten sowie einzelne Dienste beim Systemstart unterdrücken beziehungsweise wieder einschalten. (hos)
	----------
	- befehle: fixmbr, fixboot (for ntldr,...), bootcfg /rebuild (for boot.ini,..) , ..
##________________________________________  ___________________________


#####  ==========  WXP-SP2-CD erstellen: CT-0416092
		1- Als Erstes kopieren Sie den kompletten Inhalt der Windows-CD in ein Verzeichnis auf der Festplatte, etwa nach D:\xpcd
		2- XPSP2.exe /integrate:d:\xpcd  ; oder von unpackten Version (mit XPSP2.exe /x ):  Update.exe im Ordner update mit dem Schalter /integrate aufrufen. Update.exe nimmt dieselben Kommandozeilenparameter entgegen wie das SP2-Paket selbst.
		3- boot-sector-image con XP-Original-CD extrahieren z.B. mit bbie:  bbie R:\
		4- booable CD brennen von XP-updaed-Dir + image1.bin von bbie als boot sector:
			-In den Experteneinstellungen muss "keine Emulation" ausgewählt sein, denn beim Boot-Code handelt sich nicht um ein Disketten-Image. Ins Feld "Ladesegment" gehört der normalerweise voreingestellte hexadezimale Wert 07C0, die Anzahl der zu ladenden 512 Byte großen Sektoren beträgt 4, denn das Image hat eine Größe von 2 KByte. Die Optionen auf dem Reiter ISO sind bereits sinnvoll vorbelegt, wichtig ist der Schalter "ISO ';1' Dateiversion nicht schreiben", sonst erscheint beim Start die Meldung "CDBOOT: Couldn't find NTLDR".

	_______:  -- notwenfige Dienste fuer updates after SP2:
	Windows Update kann nicht fortgesetzt werden, da eine erforderliche Dienstanwendung deaktiviert ist. Für Windows Update sind die folgenden Dienste erforderlich:
	- Automatische Updates - ermöglicht die Erkennung, den Download und die Installation wichtiger Updates für den Computer.
	- Intelligenter Hintergrundübertragungsdienst (BITS) - ermöglicht einen schnelleren Download von Updates und die Fortsetzung unterbrochener Downloads.
	- Ereignisprotokoll - protokolliert die Windows Update-Ereignisse zur Problembehandlung. So stellen Sie sicher, dass diese Dienste aktiviert sind
##________________________________________  ___________________________


#####  ==========  Remote-Login, VNC, Remote-Help, Remote-Desktop:
-! CT: http://www.heise.de/ct/08/05/links/124.shtml + links
- 
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
