
	_______:  ------ notes/???/...:

	_______:  ----- prepration/partitions/HD/... + strategies:
- 3 partiotions: 1 + 2 + 5 : 1==wxp-main , 2==wxp-bup, 5=data,main-user-home,
- c.\programme + c:\progs + c:\var
-! SATA-Drivers: Intel-Drivers + CT-Reg.File: CT-0822202

	_______:  ----- a1
- Schnell install von CD-WXP-SP2,  create a1, a2 
- Menu-Properties
- Desktop
- Explorer
- Workstation-config/Arbeitsplatz-Eigenschafte
	- nodebug
	- start/stop-config
	- performance
	- virtual-mem
	- power,  Ruhe-Config, kk_lap
	- virtual-beimReboot-loeschen: Lokale-Sicherheit-Richt... ; 
	- configs: Systemwiederherstellung deaktiv (later again aktiv??) 
	- (CT-Accesrights-autostart)
- CD-Rom Buchstaben (R:\) + Partitionieren/formatieren falls notwendig. W:\ ..
- WindowsComponente-Uninstall !! + Messenger-DIR remove !! +OLExp
- Services deaktivating
- cmdcons + support tools
- boot.ini -> mehere boot-varianten -> 2DO: make ready
- Latest updates / SPx
- MS-Office-XP
- UltraEdit/Textpad + WInzip + IrfanView!!
- WXP-Small-Utils:
	- copy-unpack  utils_readyToUse.zip to c:\progs (W:\Systems\WXPs\UtilsSmallSys_wxp\0utils_NoInstallsNeeded_wxp\utils_readyToUse.zip)
	- if needed, install the rest of small-utils-xp, which need installation (W:\Systems\WXPs\UtilsSmallSys_wxp)
	- ctfmon deleting from autorun: HKEY_USERS\.DEFAULT\Software\Microsoft\Windows\CurrentVersion\Run\ ... sonstige runs
	- Tour deaktivieren
	- no autoplay for removable devices (in reg)
	- (?TWaekUI/PowerToys?); 	-  PolicyEditor/Gruppen-richtlinien (auch von TweakUI aus)
- all .reg in W:\Systems\WXPs\Reg_Notes_xp
	- cmd-window global properties (HKLM) wo??
	- drives: not indexing
- Adapting the "default user": sendto,...(where is reg?, with tweakUI?) + startmenu
- users (a1,u1,a2,u2,g1,...) + Users-Login-Style
- Mozilla , JDK14 --> change standards
- Virus + Image-tools (Ghost-Update?)
- Monitors (Filemon, Regmon,...) +  XP-smallUtils install in c:\progs  --> 2DO: a ready to copy directoy of all theses small-sys-utils + their Menu links
- Services deaktivating again.
- var/Lager-Dir-Tree in C: !
- setting defaults to NON-MS
- reboot

	_______:  -----
- Sys-Tools + Util_01
- check Network + Internet !!
- Users-Config ? je nach users (outlook, email, ...)
- Am ende: Startmenü organisierien + AllUsersRights + c:\Progs for all + Ruhezustand? + 
- Image?

	_______:  ----- End:
- Dienste: viele nicht automatisch ,+ AutoUpdate-Deaktiv + Anmelde-Art (NT-Std) + AllUsers-Rights: alles freigeben!
- small xp tools: antispy, runs, autostart-access-rights-check, ....
- path=....;C:\progs\0utils\cmds;.
- Mozilla-Configs: a1 + m1 + g1 ;
- Opera-configs
##________________________________________  ___________________________


#####  ==========  olds: ============
-! for moving the main-users-homes: !!!- it worked!! after changeing the Reg-Key ->> immediately RESTART the WXP!! (at least it worked on WXP-SP1-ku3 for a1); but only with immediate restarting the system !!
	(old: check if the Reg-Procedure works fine with standard CD install, so BEFORE any SP !!?? :	may be you have to set HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<user-sid>\NextLogonCacheable  == 1  ? test it!)
