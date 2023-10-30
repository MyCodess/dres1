______________________ BCDs + bcdedit-details , bootmenu from msrefs,...: __________________________


#####  ==========  docs-msRefs / helps / ...:
    /:220903 : 
    - boot-process-overview-mswins:   https://en.wikipedia.org/wiki/Windows_NT_6_startup_process
    - Concepts/Intro! older-BUT very good basic Intro ...!  :  https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc721886(v=ws.10)  : 
    - Overview-higher-cmds-params of bcdedit (bcdedit start up options) :   https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit  :  Docs / Windows / Windows Drivers / Driver Technologies / Tools for Testing Drivers  ,(WDK)
    - Overview-higher-cmds-params of bcdedit/bootsec/bcdboot (start up options) :   https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/bcdedit-command-line-options  : Docs / Windows Server / Windows Commands / Reference ,(WInServerRefs)
    - DETAILS of params/... :  https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/bcd-boot-options-reference + ... further-contents-entries:   Docs , Windows ,  Windows Drivers , Driver Technologies , Tools for Testing Drivers , BCDEdit Options Reference ,(WDK)
        https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/editing-boot-options   :  Docs / Windows / Manufacture / Desktop manufacturing   ,(Manufacturing)
##________________________________________  ___________________________


#####  ==========  Vocabs-BCDs / BCD-boot-components :
	- https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc721886(v=ws.10)
	-! see picture on https://sourcedaddy.com/windows-7/bcd-stores.html  --->BUT-shit-privacy-site!! take private-browser !
    -! Vocabs:  BCD-Store (whole-boot-stuff) --> BCD-Objects (Boot-manager, Boot-Loader per OS, Boot-Tools (as Memory-check/HW-checks...)) --> BCD-Elements (each config-entry of any of boot-objects) ! see picture in above-link!

	_______:  Seq:  BCD-System-Store (WHOLE /boot/-part, contains all) --> Boot-Manager (Menu-listing/selection of all boot-loaders) --> Boot-Loader (Loads Windows/OS/LX/...):

	_______:  BCD-Store (Reg-bin-hive!?) :
	- a BCD Store(== LagerRaum/Speicer/Inventar) contains all boot-stuff:
		One Windows Boot Manager entry (because there is only one boot manager).
		per each Windows-Entry then one Windows Boot Loader application/specification (eg {current} , {xxxx}, ....)
		one leacy entry for NTLDR /boot.ini (eg for WXP/ Win7 / ...)! (still there!??)
		and could also a few optional entries/apps (eg for memtest, linux, ...)! see below!
    - Physically, a BCD store is a binary file in the registry hive format. A computer has one system BCD store, that describes all installed Windows/iLx/OSs/systems/HW-DIag/...  and can optionally have many non-system BCD stores. 
	-- 1kk:
    - is basically the BCD-registry-file, so in BIOS: \Boot\BCD , in EFI: ./EFI/Microsoft/Boot/BCD  bzw. its backup in ./EFI/Microsoft/Recovery/BCD !
	- is a binary file in the registry hive format, contains infos/pathes of all-boot-stuff for a system (Boot-Manager, Boot-Loader, .. ). A PC has a system-BCD-store, and Optionally/theoritically a system can have many non-system BCD stores. ...

	_______:  Windows-Boot-Manager  :
	- shows the menu for selection the OS to be loaded/started. So, manages entries to display in an operating system selection menu, boot tool selection menu, and time-out for the selection menus ...
	- in BIOS: bootmgr , in EFI: bootmgfw.efi , usu. \EFI\Microsoft\Boot\Bootmgfw.efi )
	- BCD (Boot Configuration Data) contain the menu entries that are presented by the Windows Boot Manager, 

	_______:  Windows-Boot-Loader  ()  :  loads OS/Windows10 , so OS-loading !
	- for each entry in boot-manager-menu there is one extra boot-loader ! so,  Stores contain one instance of this object for each version or configuration of Windows ...
	{current}  :  When a computer is booted into Windows, the alias {current} represents the associated boot loader object (for the current-loaded-OS).
	{default}  :  When manipulating a store with BCDEdit, the default boot loader object has the alias {default}.

	_______:  optional entries in a BCD Store:
	- BCD-Legacy-boot  :  ntldr entry, for loading pre-Vista-OS, as Win7, wxp, ..., (basically like grub-chaining for ms-legacy-systems)
	- BCD-optional-apps  :  as memtest, HW-Diagnotics,... entries+apps

	_______:  BCDEdit-infs:
	- BCDEdit.exe  is a command-line tool for managing BCD stores.
	- BCDEdit.exe  replaces pre-Vista Bootcfg.exe and boot.ini , ...
	- obsol Bootcfg.exe (pre-Vista) :  You cannot use Bootcfg.exe to modify BCD. However, Bootcfg.exe will remain in the operating system in order to support older operating systems.
##________________________________________  ___________________________


#####  ==========  BCD  pathes / REGs-files / ... :
	- path:   %WINDIR%\System32\bcdedit.exe
	-!! Powershell usage: "{ID}" MUST be enclosed in "" !! so NOT {ID} as in cmdConsole !

	_______:  BCD-REG-FilesPathes:
	- https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc721886(v=ws.10)
	- BCD hat its OWN REG-files (which are later read into OS-REG-Editor)!
	  Where is the BCD file located in the registry? :
	- UEFI-based-systems of BCD-REG-files:  the EFI system partition contains  the BCD registry file! eg in Lv13: boot-part-/EFI/Microsoft/Boot/BCD
	- BIOS-based-systems of BCD-REG-files:  \Boot\Bcd  directory of the active partition contains the BCD registry file!
	- (?? will be copied to win-REGs-dir  \Windows\System32\config\  ??)
	- cu-REG-loaded-BCD-hive into:  [HKEY_LOCAL_MACHINE\BCD00000] 
##________________________________________  ___________________________


#####  ==========  BCD-cmds:
	- BCDBoot (as grub-install, which copies boot stuff to boot-part)	:  Initializes the boot configuration data (BCD) store and copies boot environment files to the system partition during image deployment. https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di?view=windows-11
	- BCDEdit (as vi grub.cfg, or grub-makeconfig) 	:  Manages Boot Configuration Data (BCD).
	- Bootsect  :  Updates the master boot code for hard disk partitions to switch between Windows Boot Manager (Bootmgr.exe ) and Windows NT Loader (NTLDR).
##________________________________________  ___________________________


#####  ==========  Utils-Onboard-GUIs-ms-OS for BCD-jobs:
	https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc721886(v=ws.10)
	- Startup and recovery :  OS System Properties dialog box --> Advanced tab
	- Msconfig.exe / "System Configuration utility" : advanced tool with capabilities: /debug, /safeboot, /bootlog, /noguiboot, /basevideo, and /numproc per BCD-Store-Entry !
	- 
##________________________________________  ___________________________


##############################  bcdedit cmd : ####################################################


#####  ==========  refs/docs/helps/... bcdedit :
    - ! https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
    - ! https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/bcd-boot-options-reference
    --- bcdedit helps ... :
    bcdedit /? TOPICS  ##-eg:  bcdedit.exe /? CREATESTORE
    bcdedit /?
    ! syntax/eg/...: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
##________________________________________  ___________________________

#####  ==========  /set :
    https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--set  !! Details
    - bcdedit  /set [{ID}] datatype value
    - deleting a setting:  bcdedit /deletevalue [{ID}] datatatype
##________________________________________  ___________________________

#####  ==========  eg usage bcdedit.exe  (replace {ID} with the ID of your Entry! ):
    - ! see  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
    -! F8 / boot-options-menu make available:  bcdedit /set {default} bootmenupolicy legacy  ##--see https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--set : bootmenupolicy
    -! from on offline-win/backup-boot-dir-BCD-file list the entries:  bcdedit  /store T:\bups1\boot\BCD  /enum ...
    -! backup of the contents ot the system BCD:  bcdedit /export > bups1.log ; restoring with:  bcdedit  /import ... ;
    - show ONLY the current-OS-params:   bcdedit /enum {current}
    - change default entry:  bcdedit /default {ID}   ###-eg bcdedit /default {cbd971bf-b7b8-4885-951a-fa03044f5d71}
    - ! sequence of boot-loader-entries DISPLAYED has got NOThing to do whith which OS/Loader will be as default started! this is defined by "bcdedit /default ..." cmd!!
    - change the sequence of entries DISPLAYED one-time! :  bcdedit /bootsequence {ID} {ID} {ID}   ##--Specifies a one-time display order for the next reboot! not persistent! /bootsequence command sets the one-time boot sequence to be used by the boot manager.
    - change the sequence of entries DISPLAYED permanent :  Bcdedit.exe /displayorder {ID} [/addlast|/addfirst|/remove]
    - change timeout of bootmanager:   bcdedit /timeout 5
    - set kernel debugger on or off :  bcdedit /debug [{ID}] {on|off} 
    - list entries of a particular type : bcdedit /enum [Type]  ##-- /?

        _______:  adding a new entry for a second win10-installed eg on D1P5 mounted now on x:  :
        bcdedit /copy {current} /d “NewEntryDescription” ;##--> printouts the new-GUID , take it:
        bcdedit /set {NewGuid} device partition=x:  ; bcdedit /set {NewGuid} osdevice partition=x: ; ##-if wanted:  bcdedit /displayorder {NewGuid} /addlast ;##or addfirst ... !

        _______:  boot-logging-activation  (was 1kk normal bei NT-booten anstatt GUI/Welcome sah !):
        bcdedit /set {current} bootlog [Yes , No]      ##--oder: auch per  "%windir%\System32\msconfig.exe" (Systemkonfiguration)  --> Start" aktivieren bzw. deaktivieren Sie die Option "Startprotokollierung" --> save-as-permanent-config!
        boot-log-file :  C:\Windows\ntbtlog.txt  bzw.  "%windir%\ntbtlog.txt" 
##________________________________________  ___________________________

