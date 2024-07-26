_____________ win7-booties, mbr, usb-boot, ... ___________________________
- for bootings-stuff regarding imaging see the extra nts for imagings!!
##________________________________________  ___________________________


#####  ==========  DEFs, DIFFS, Vocabs, ...:

	_______:  !! DEFs: in Win7-vocabulary:
	- 1.System-Partiotion (is actually kk-booting-part, marked also as ACTIVE part): so the 100MB boot-part which contains the booting-stuff  --> must be ACTIVE!!!
	- 2.Boot-Part (is actually kk-OS-part): is the OS/System-part, so the part which contains the Windows\System32-DIR so usu. c:\Windows or so ....
##________________________________________  ___________________________


#####  ==========  cmds-boot-win7:
- see REFs in: http://technet.microsoft.com/en-us/library/hh825029.aspx  +  Windows7_TheDefinitiveGuide_Ore_0906_b.pdf--Ch.23
- bootsect /? :  MBR-/boot.sectorr-Modifications; also switch between Bootmgr (Win7/Vista) and NT Loader (NTLDR). This tool replaces FixFAT and FixNTFS.
- bcdboot /? : manage/repair system-partition files (kk-booting-part-100mb). Repairing the boot environment located on the system partition.
	If the system partition has been corrupted, you can use BCDboot to replace the system partition files with new copies of these files from the Windows partition (the boot-file there also exist as copy in c:\windows\system32\...).
	To configure the system partition, BCDboot copies a small set of boot-environment files from the installed Windows image to the system partition. Next, BCDboot creates a Boot Configuration Data (BCD) store on the system partition that instructs the computer to boot to the Windows partition.
	BCDboot uses the %WINDIR%\System32\Config\BCD-Template file to create a new BCD store and initialize the BCD boot-environment files on the system partition. 
- bcdedit /?  : boot.ini-modifications:  managing BCD stores (boot.ini in WXP). Boot Configuration Data (BCD) files provide a store that is used to describe boot applications and boot application settings. The objects and elements in the store effectively replace Boot.ini.
- mountvol /? :	Creates, deletes, or lists a volume mount point.  mountpoints/volume.letters: Creates, deletes, or lists a volume mount point. ! assignment drive.letters <--> Volume.IDs ! C:\Windows\system32\mountvol.exe
- bootrec /fixboot : NICHT benutzen auf Win7 : !!vorsicht!:  bei mir on win7 formatierete die Partition!! alles weg!
##________________________________________  ___________________________


#####  ==========  100mb-Booting-part merging-/preventing: preventing of creation by installation /OR merging it into OS-part after standard-installation:

	_______:  ! Preventing-100mb-booting-part: avoiding the creation of 100mb-booting-partition during the basic installation of win7:
	-!! just part+format the HD FULLY before stating the installation, so that ther is NO free/not-assigned segments/partitions/... at all on the HD!!
		and even if win7-install still wants to generate it (after langugae selection you see a info-window that windows creats additional part), do "cancel/abbrechen" its creation !
		see:   w/docs/MSs/Win7s/Booties_BCD_Win7s/Avoiding_BootPart_win7.html

	_______:  Merging-100mb-booting-part-: after standard win7-installatin, merging/integrating of 100mb-booting-part into OS-part (C:):
	-- eg Here:
	sda1 == booting-part (small win7-100mb-system-part, containing boot-stuff with boot-dir , bcd, ...)
	sda2 == Win7-OS-Part (win7-boot-part containing c:\windows\system32\ ...)
	(-! make backup/image from both parts : with win-imager + ntfsclone)
	--1. fdisk : make sda1 inactive (and if like delete/format it)  AND make OS-part sda2 ACTIVE!!
		either frim linux /or from current or second win-system with diskpart.
		(later the win7-system-repair-tools will be looking for bootmgr in active part, so in sda2,	but they will NOT find it and are forced to regenerate them in sda2 but, abd not in sda1 any more, because sda1 is NOT active anymore!!)
	--2. then boot several times (may be 3 times) from win7-usb/system-repair to repair the missing boot stuff! done!
		 or /AND if needed do from rescue-system: bcdboot k:\windows /s k: /l en-us
		 whereas k:\ is the drive for OS-part sda2 (containing windows\system32-dir) , but the drive-letter "k:" as it is assigned in the RESCUE-system!! not as later could be!!
##________________________________________  ___________________________


#####  ==========  USB.boot.Win7.OS-setup: Win7-von-USB.Platte/Stick starten/booten:
-!! ct1013168_171_UsbInstallWin7.pdf : full Instruction!! OK! done for vo17 :

	_______:  CT-nts:
	-!! after finishing, if attaching the usb-win7 to another PC: you could get blue.screen by second booting!! to avoid it see beleow under "after finisching"!! have to check Reg-Usb-Driveres!
	- if attaching the usb-win7 to another PC, could licensing-problem with bluescreen! (was ok in l1nw-win7.ultimate!)
	- lieber usb-platte; usb-stick could be problem
	- usb-HD darf nur eine einzelne primary partition ??(for me ok mehrere)

	_______:  CT-Procedure : here eg USB-target-part f: , and win7-source-part d:
	- DISKPART: FRESH creation´+ Formatting of target-Part-in-USB.HD mit NTFS (could problems if not fresh!)
	- boote von win7-usb/win7-parallel-install/win7-dvd/win7-repair-disk, systemreperatur-media/...
	- goto Dos-window as Admin in your current parallel-win7 (eg in repair-disk with shit-F10,... or your Win7-RF,...)
	- wo/was/drive.letters??was??: dos-window --> notepad.exe --> file-open: you see a small explorer
	- note usb-target-drive + win7-source-drive (..\windows\system32,....)
	- xcopy d: f: /kreisch /Q  --> (kk: /Q) kopiert Win7, ABER noch nicht bootfähiger USB-HD!! missing bootlader!
	- bootloader into Usb-HD:  bcdboot f:\windows /s f: /l en-us ;(or de-de)  # wobei f: ist der AKTUELLE USB-win-Part!
	- USB-Treiber!! jetzt ist der Usb-part auch bootfähig, aber fehlen noch WAEHREND booeten die USB-Treiber, also:
		regeidt --> HKLM --> Load Hive (reg-datei-laden): system.reg.datei von f: (usb-win) --> see CT to load usb-drives DURING booten!
		CT: Unter  HKLM\USB\Select prüfen Sie nun, wel- chen Wert der Eintrag  Current hat. Bei einer 1 geht es unter HKLM\USB\ControlSet001 weiter, bei einer 2 unter HKLM\USB\ControlSet002 und so weiter. Hier finden Sie unter services Unterschlüssel namens  usbccgq,  usbehci,  usbhub,  usbohci,  USBSTOR und usbuhci. Die nötigen Änderungen sind bei allen gleich: Setzen Sie erstens den Wert des Eintrags Start jeweils von 3 auf 0 und zweitens den Wert des Eintrags  Group von Base auf system reserved (bei USBSTOR fehlt der Group-Eintrag, das darf so bleiben). Diese Änderungen veranlassen Windows, alle USB- Treiber gleich zu Beginn des Bootvorgangs zu laden.
	- DriveLetter correction in Reg: CT: Als Beispiel dienen hier C: und F:. Öffnen Sie den Schlüssel HKML\USB\MountedDevices. Hier tauschen Sie beim Eintrag namens \DosDevices\C: das C vorübergehend gegen irgendeinen bislang nicht vergebenen Buchstaben, beispielsweise Q. Dann ersetzen Sie beim Eintrag  \DosDevices\F: das F durch ein C. und schließlich bei  \DosDevices\Q: das Q durch das F. Das sorgt dafür, dass die Windows-Installation auf der USB-Platte diese nun für C: hält und das eingebaute Laufwerk für F:.
	- unload Hive in Reg
	-- fertig! can be bootet
	-!! BUT later strill you can get blue-screen (due to changes to loading-USB-dreivers due to updates/new.Hardware.gefunden/...!! you GOT it after attaching from x13 to vo17), so to avoid it:
		CT: Im Prinzip ist nun alles erledigt, doch bevor Sie das frisch von USB gebootete Windows 7 wieder herunterfahren, sollten Sie nochmals den Registry-Editor starten und nachprüfen, ob die vorhin vorgenommenen Änderungen erhalten geblieben sind  die Schlüssel finden Sie nun allerdings nich mehr unter HKLM\USB, sondern unter HKLM\Sys tem\CurrentControlSet. Die USB-Einträge ändern sich teilweise zurück auf die Ausgangswerte falls Windows neue Hardware erkannt hat  unwahrscheinlich, falls Windows das USB Laufwerk vor dem Umzug schon kannte aber fast unvermeidlich, falls nicht. Dieses Szenario droht auch, falls Sie von der USB Platte mal versehentlich am falschen PC boo ten. Dann sollten Sie die Nachkontrolle und gegebenenfalls die Korrekturen vor dem Herunterfahren wiederholen. (axv)
--######################## coll-booties-win7: ##################################################
##________________________________________  ___________________________


#####  ==========  boot process win7: ==================

	_______:  ------- http://forums.techarena.in/windows-software/1278282.htm :
Re: Explanation on Windows boot process   ---> kk: for wxp/NTLDR :
The list of processes which are carried out during boot process are :
1. Ntldr: load the OS.
2. Boot.ini : Built selection menu.
3. BBootsect.dos : uploaded by Ntldr to another OS.
4. Ntdetect.com : Research materials available.
5. Ntbootdd.sys : To boot from a disk whose controller has not enabled the bios.
6. Ntoskrnl.exe : NT Kernel (system32).
7. System : Configuration settings (system32 \ config).
8. Hal.dll : Makes Ntoskrnl independent of the platform on which it will work.

	_______:  ------- http://www.sevenforums.com/tutorials/2676-bcdedit-how-use.html :
Bcdedit is a really powerful tool that Windows Vista and Windows 7 uses to manage the boot loader entries.
BCDEDIT needs a boot loader file to boot your system.
A boot loader is a file that contains necessary information that instruct the system how to boot/start an operating system.
Windows 7 and Vista bootloader file is \bootmgr
Windows XP bootloader file is \ntldr
BCDEDIT can support other bootloaders too, like grub for linux. You just have to place the bootloader file on the root of the boot manager partition. e.g. \grldr and you have a grub boot loader enabled.
Bcdedit edits a file called bcd , which is located in Windows 7's hidden partition under \boot\bcd.
In Vista, its located under C:\boot\bcd.
##________________________________________  ___________________________


#####  ==========  
