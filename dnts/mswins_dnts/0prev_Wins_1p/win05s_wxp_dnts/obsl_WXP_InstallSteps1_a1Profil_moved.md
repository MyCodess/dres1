
	_______:  --! for moving the profil of a1 somehow it did not work with WXP-SP2-rc2 on km08 --> so veraltet.

	_______:  ----- prepration/partitions/HD/... + strategies:
- 3 partiotions: 1 + 2 + 5 : 1==wxp-main , 2==wxp-bup, 5=data,main-user-home,
- c.\programme + c:\progs + c:\lager

	_______:  ----- a2 (bup-admin): 2DO: wieviel vom a2 doch beim a1?
- Schnell install von CD-SP2 or WinStd+SP2: create a1, a2
- Aber configure nur mit backup-admin-user (so NO a1,... but e.g. a2), because of their user-directory;
- login mit a2: 
	- all .reg in W:\Systems\WXPs\Reg_Notes_xp  + Global for cmd-options, wo??
	- Explorer + Desktop + Menu + Aufloesung (vorlaeufig):
		optimale leistung, Fehlerberichten abschalten , 
	- adjastments with TWaekUI
	- Global changes with Powertoys + PolicyEditor/Gruppen-richtlinien (auch von TweakUI aus)
	- ctfmon deleting from autorun: HKEY_USERS\.DEFAULT\Software\Microsoft\Windows\CurrentVersion\Run\ ... sonstige runs
	- HauptUsers und DummyUsers definieren (a1,u1,a2,u2,g1,...)
	- nur Main-User-Home/Profile-Root verlagern Nur einen User-Home verlagern, e.g. a1 (bevor jegliche software installation ;  CT:User/Profile/Pathes: 26/2002 , S. 112 ):
			(- einfach als ein anderer eingelogt sein, wie hier eingelogt als a2, aber Aenderungen fuer a1)
			(- vielleicht ein HOMEROOT_MAINUSERS global variable definieren)
			- in Registry HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\"....a1-key.." verzeichnis setzen auf %HOMEROOT_MAIN_USERS%\%USERNAME% oder ...\a1 ???
			(- falls notwendig a1-oldHome nach neuHome kopieren mit xcopy ... /v /e /x /k /o /c /h  (falls %HOMEROOT_MAIN_USERS% in FAT-partition, dann ohne /o /x ,...))
			- (nicht mehr aktuell, aber falls for alle users, dann: - home-DIR/UserProfile (CT-articleUsersprofil): 1-stop services; 2- copy DIRs to W-Home-Dir ; 3-change Registerise (see CT-file/artikel 26/2002 , S. 112 ))
	- adapting the default user (check the result beim a1-login)

	_______:  ----- a1:
- (SP2) , MS-Support-Tools + Wiederherstellungskonsole + TWaekUI/PowerToys + WXP-Small-Utils + CT-XP-Dir
- adjastments with TWaekUI
- Global changes with Powertoys + PolicyEditor/Gruppen-richtlinien (auch von TweakUI aus)
- ctfmon deleting from autorun: HKEY_USERS\.DEFAULT\Software\Microsoft\Windows\CurrentVersion\Run\ ... sonstige runs
- Filemon, Regmon,... XP-smallUtils install in c:\progs
- cmd-window global properties (HKLM)
- poledit from office-XPX-Resourcekit oder poledit.exe (dann vielleicht officeXP davor, falls ResKit)
-! Laufwerk-Eigenschaften -> nicht-indizieren !! ansonsten nachtraeglich sehr zeitaufwendig!
- WindowsComponente-Uninstall !! + Messenger-DIR remove !! +OLExp
- Arbeitsplatz-Eigenschafte -> start/stop/debug konfig! 
- boot.ini -> mehere boot-varianten
- Services deaktivating
- Partitionieren/formatieren falls notwendig. W:\ ..
- No Index on Drives + CD-Rom Buchstaben (R:\) , HD-COnfig,names,... + Index-Dienst deaktivieren/manuell
- Lager-Dir-Tree!
- w:\home
- Tour deaktivieren
- uninstall messenger, ....: Verzeichnis von Windows-Messanger löschen nach uninstall !!
- reboot
- login & test with a1
- when OK!: 
	- virtual-beimReboot-loeschen: Lokale-Sicherheit-Richt... ; 
	- System-Start-Config. no debug; 
	- VirtualMem-Config ; Ruhe-Config
- c:\progs2
- Desktop + Explorer + Menu 
- DIRs: c:\progs + w:\progs2 + w:\temp\IE+XP-tmp + Home + 
- First-Tools: +WinZip + PDF + CopySelectedPath + DosBox-Context + - Syste-Small-Utils(AntiSpy +Autoruns +Regs)
- XP-Support-tools + CMD-XOnsole-XP and its Regs + edit boot.ini for partitions....
- Dienste: viele nicht automatisch ,+ AutoUpdate-Deaktiv + Anmelde-Art (NT-Std) + AllUsers-Rights: alles freigeben!
- Temp-Dir-Tree: IE_Cach, ... -> config IE,...; IE-Optionen; XP-Temp-Dir (Env.)
- check Network + Internet !!
- office+ office-SR ; 
- xp-sp1 ; nach SP1 WIEDER software->windowsComponente-Uninstall !!  Messenger-DIR remove !!
- JDK14 + Mozilla;
- XP-Small-Utils
- Utils-01
- tools
- Virus + Image-tools + Update?
- Users-Config ? je nach users (outlook, email, ...)
- check again: Services -> deactivations
- Antispy, sysutils-chseck
- Am ende: Startmenü organisierien + AllUsersRights + c:\Progs for all + Ruhezustand? + 
- Image?
##________________________________________  ___________________________


#####  ==========  2Dos:
- Download: cmdcons wiederherstellungsconsole
##________________________________________  ___________________________


#####  ==========  notes/checks beim wxp-config:
- Tour
- Workstation-properties: Systemwiederherstellung ?, Remote deactivating, optimale leistung, 
- 