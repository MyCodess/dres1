_________________ win10-Allg-installs-dnts : _______________________________________
-! for 1kk-/syss-installs see extra dnts bzw. syss-DIRs ! here Allg-knowHow-installs-dnts !
- see here scripts-msRefs in extra dnts for partitioning on BIOS/UEFI systems!
- see also booties-...-dnts here for boot-dnts ! + syss_CPs here for 1kk-steps !

#####  ==========  docs:
	-! in msRef-docs the "installs/setups" are usu called there:   Manufacture , Manufacturing / Deployment
	-!! RF-doc/msRef : ManufacturingWins--Imaging-Boot-DISM--msRef bzw. https://docs.microsoft.com/en-us/windows-hardware/manufacture/?view=windows-11
	-! scripts-msRef-coll-installs (pre-partitioning, WinRE-setup, ...):  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?view=windows-11
	-! answer-files:  https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/wsim/create-or-open-an-answer-file
##________________________________________  ___________________________


##################### HDs-partitioning-for-win-installs : ########################################################################
#####  ==========  customized-partitioning of win-installs / default-parts :
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/hard-drives-and-partitions?view=windows-11  ==  manufacturing.pdf--p.391--Hard drives and partitions
	UEFI/GPT:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions
	BIOS/MBR:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/hard-drives-and-partitions?view=windows-11  ==  manufacturing.pdf--p.391--Hard drives
	!--> ready scripts there for both UEFI/BIOS customized-partitioning with diskpart :
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?view=windows-11
##________________________________________  ___________________________


#####  ==========  default-partitions-of-win10-installs:
	-! see also the scripts-msref !

	_______:  DIFFs in UEFI or BIOS ! :
	- MSR ,  ONLY in UEFI/GPT installs ! 16 MB default ! Microsoft reserved partition (MSR ); mbr-disks uses hidden-sectors for that. but hidden-sectors does not exist any more in gpt-disks !
	- Recovery-/WinRE-part : can also be contained in BCD_System-part for BIOS/MBR-setups !
	- System-part/BCD-part : is fat32 in UEFI/gpt installations, and usu. NTFS in BIOS/mbr systems !vthis part can also contain the WinRE-part for BIOS/MBR-setups ! min 100 MB bzw. 500 MB incl. WinRE. \Boot , \EFI tree !
	- For BIOS/MBR-based systems, it's still possible to combine the Windows RE tools partition with the system(BCD_System-part.

	_______:  BIOS/mbr-default-win-parts:
	-! BIOS-based device, you must format hard drives by using an MBR file system. Windows does not support the GUID partition table (GPT) file system on BIOS-based computers.
	1- system partition , min-size 100 MB, MUST be flagged as ACTIVE !! (usu. formatted ntfs, but 1kk: try fat32)
	2- Windows partition
	3- WinRE/Recovery  partition,  at least 300 MB,  partition must use the Type ID: DE94BBA4-06D1-4D40-A16A-BFD50179D6AC , We recommend that you place this partition immediately after the Windows partition (due to evtl. resizing)
	4- Data/Users-part if any. /OR in extended-part ...
	---- if more than 4 parts (so incl. extended-part), and also OEM-/Utility and user/data-parts, MS:
	1- system partition 2- OEM/Utility 3-User/Data ; Extended: 5-Win 6-WinRE

	_______:  UEFI/gpt-default-win-parts:   default partition layout for UEFI-based PCs is:   https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions?view=windows-11
	-! UEFI-based devices MUST be gpt-parted for win-parts! second/Additional drives may use either the GPT or the master boot record (MBR) file format.
	1- EFI/ESP/system partition (EFI, fat32), min-size 100 MB ! must be formatted using the FAT32 file format ! (NOT-relevant if flagged active!)
	2- MSR partition, In Windows 10, the size of the MSR is 16 MB.
	2b- OEM-part (if any; is called also utility-part) : Any other (OEM-)utility partitions not managed by Windows must be located before the Windows, data, and recovery image partitions.
	3- Windows partition
	4- WinRE/Recovery  partition,  at least 300 MB,  partition must use the Type ID: DE94BBA4-06D1-4D40-A16A-BFD50179D6AC , We recommend that you place this partition immediately after the Windows partition.
	5- Data/Users-part if any.
##________________________________________  ___________________________


#####  ==========  Allg-nts-install-partitioning:

	_______:  EFI/ESP-part on mbr:    https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq?view=windows-11 :
	- EFI-part on mbr identified by ID:  0xEF  ; min size 100MBs !
	- MBR disks can also have ESP/EFI-part. UEFI specifies booting from either GPT or MBR. 
	- The ESP/EFI-part on an MBR disk is identified by partition type 0xEF. However, Windows does not support booting UEFI from MBR disks or 0xEF partitions.
	- The ESP/EFI-part should be first on the disk (after protective-MBR on BIOS/mbr systems! protective-MBR is not counted.)
	-! Only one ESP should exist on a system even if multiple operating systems are installed on that system.:w
	- The ESP partition isn't hidden, but also doesn't have an assigned drive letter. It will not appear in Explorer unless a drive letter gets assigned to it, but some tools will be able to list it.

	_______:  MSR-part (only in UEFI):
	- ONLY in UEFI-systems is required. the BIOS-systems user hidden-secotrs for that! but in GTP there is no hidden-sectors-convept any more !
	-! order/location:  Every GPT disk must contain an MSR. The order of partitions on the disk should be ESP (if any), OEM (if any) and MSR followed by primary data/users partition(s, if any) . It is particularly important that the MSR be created before other primary data partitions.  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq?view=windows-11
	- The MSR must be created when disk-partitioning information is first written to the drive. so at the very beginning!
	- min size MSR is 128 MB
##________________________________________  ___________________________


#####  ==========  avoiding-extra-BCD_System-Partiotion if liked !?!? (but OK extra! here info):
- windows extra BCD_System-part preventing , called system-partition in mswins !! : ---> BUT is ok with extra boot-part! so not needed !! here info:
	- do fdisk/parted /dev/sda and FULLY create partitions so that no free space is available any more !!
	- /OR if no linux there, then :
		Press Shift+F10 while installing Windows to open a Command Prompt window.
		Type diskpart into the Command Prompt window and press Enter.
		Create a new partition in the unallocated space using the diskpart tool. ...  Continue the setup process.
##________________________________________  ___________________________


#####  ==========  BCD_System-Part first-avoiding and then creating-as-fat32 -1ac-/_200820--on-Vo17-BIOS/MBR-Win10-setup :
	- Vo17 , BIOS , HD1 was parted with fdisk as dos /MBR-part-table  (Win10 has problems with BIOS/GPT !!)
	- this part is anyway fat32 for UEFI/gpt setups! but not for BIOS/mbr setups !
	1--prevent-extra-BCD-part: indem man die HD fully pre-formatiert, ohne nicht-zugeordnete-Sectoren :
	- fdisk /dev/sda:   part-1: 5GB, not-formatted now  ; part-2: 100GB not-fomatted ; part-3: rest-just belegt fully! ; NO-Free-spaces on HD1 !! (otherwise Win10 makes new Parts for boot,...!!))
	- install win10 (it takes part-2 and formats it) , and the setup also puts the /Boot stuf on the same part! so Part-2 is both: System (/Boot bzw. BCD) + Startpart/Bootpart (Win10-OS-files)
	- then just startup your new win10-OS from HD1
	2-- Now prepare to create new BCD-part and move the /boot stuff from HD1-part2 installation  to the  HD1-part1 as BCD-boot-part/fat32  :
		- computerVerwaltung/ compmgmt.msc : format part-1 as fat32 + mark it as ACTIVE ! (even if OS says could problems,..) and keine-laufwerkbuchstbe (just-styling)
		- reboot to Lx/arx and : mount /dev/sda1 /HD1-P1 , mount /dev/sda2 /HD1-P2 
		- rsync /OR cp -a /HD1-p2/Boot  /HD1-P1/  ; and cp /HD1-p2/bootmgr*   /HD1-P1/ ; ??:  cp /HD1-p2/BOOT*  /HD1-P1/
		# (sould do all steps also from WIn10; but the /BCD files are in-use/gesperrt and can not be copied)
	- done! reboot to Win10; if all ok , in Win10 running-OS , just rename/move the  old stuff:  rename c:\Boot Boot_1org ; move  C:\BCD*
#################### WinRE / recovery-mode-boot (during booting go to WinRE/WInPE):  #############################
- !!DIFF : recovery-mode (bei reboot in WinRE-mode)   <-->  Wiederherstellung/restore/backup: zu einem Punkt zurück (in extra dnts)!
##________________________________________  ___________________________


#####  ==========  nachträglich (re-)creating the Recovery-Partition:
	-! use/see ApplyRecovery.bat in Manufacturing.pdf--p.126 ! bzw. https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?view=windows-11
	-! in UEFI the WinRE on seperate partition. in BIOS usu. on the BCD-system-partition !
##________________________________________  ___________________________


#####  ==========  entering into boot-recovery-mode (WInRE / Windows-Recovery)
- see also https://en.wikipedia.org/wiki/Windows_NT_6_startup_process#Advanced_Boot_Options

	_______:  - F8+shift  problem!
	-!! F8 does NOT work anymore ab Win10 for entering boot-recovery WInRE !
	- if want it, admin do:   bcdedit /set {default} bootmenupolicy legacy   ##back-to-default:   bcdedit /set {default} bootmenupolicy standard
	-! see  https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--set  -> bootmenupolicy

	_______:  cmdline restart into recovery mode:
	shutdown /r /o /f /t 00 
	shutdown  /?  ##arguments-listing

	_______:  from Desktop restart into recovery:
	https://www.dell.com/support/kbdoc/de-de/000124344/how-to-boot-to-safe-mode-in-windows-10?lang=en  :
	- if logged-in /OR login-screen:  then: hold-SHIFT+restart ! or even from the Login-Screen also !
	- if logged-in: System-->Recovery ....
	- if logged-in: msconfig --> boot ...
	- if logged:  Settings -> Update & Security -> Recovery ->  Under Advanced Startup, click Restart Now.

	_______:  hard-core-forcong:  so PC-NOT-up/not-logged-in : three times start-win and crash-it with turnoff-button ! After the third attempt to boot has failed, Windows 11 and Windows 10 will automatically boot into the Windows Recovery Environment (WinRE).
##________________________________________  ___________________________


#####  ==========  
############### DW-ISO, Create MCT, preparing insalls win10: ##########################################
##________________________________________  ___________________________


#####  ==========  MCT , Media Creation Tool :

	_______:  -- MCT cmdline arguments ??:
-! NOT found the listing in int !! here a few:
- MediaCreationTool20H2.exe  /Eula Accept  /Retail  /MediaLangCode en-US  /MediaArch x64  /MediaEdition Enterprise

	_______:  -- Download Any Windows 10 Version ISO with MCT :
https://winaero.com/how-to-use-media-creation-tool-to-download-any-windows-10-version/
https://gist.githubusercontent.com/AveYo/c74dc774a8fb81a332b5d65613187b15/raw/c67083ebc8cac4ae74e6cd680fc32aa6e2aeb91d/MediaCreationTool.bat  ##-batch-file for that !
MediaCreationTool20H2.exe /Eula Accept /Retail /MediaLangCode en-US /MediaArch x64 /MediaEdition <your-edition>

	_______:  -- ISO-Enterprise-DW with MCT (needed??):       : 2chk/not-done:   Enterprise-DW  with MCT :
https://kevinstreet.co.uk/tag/media-creation-tool/  :
- MediaCreationTool20H2.exe /Eula Accept /Retail /MediaLangCode en-US /MediaArch x64 /MediaEdition Enterprise
- product-Key check:  https://docs.microsoft.com/sl-si/windows-server/get-started/kms-client-activation-keys

	_______:  if wanted: convert ...\sources\install.esd in ISO-file  to  ...\sources\install.wim  :
dism.exe /Get-WimInfo /WimFile:C:\Temp\Windows10_20H2\sources\install.esd
dism.exe /Export-Image /SourceImageFile:C:\Temp\Windows10_20H2\sources\install.esd /SourceIndex:XX /DestinationImageFile:C:\Temp\Windows10_20H2\sources\install.wim /Compress:max /CheckIntegrity  ##--replace index:XX with the index-number you want from the lisint of previous cmd !
##________________________________________  ___________________________


#####  ==========  ISO-setup-Media: (eg Win10-ISO-DW ....)
- setup.exe cmdline arguments ?:   try:  setup.exe  /? ##-or see:
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-command-line-options?view=windows-11
################################################################################################################
