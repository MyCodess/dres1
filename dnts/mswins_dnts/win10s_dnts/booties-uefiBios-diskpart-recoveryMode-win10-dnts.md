_____________ booties-MBR-UEFI-BIOS-SHIM-win10s-devnts.txt, recovery/WinRE-mode, win10s: _____________________
-! RF-docs:  ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf
-! for BCD / bcdedit.exe see extra dnts !
- scripts-ready-msRef-for-setup/boot:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?view=windows-11
#################### Boot-Process, DEFs, basics UEFI/BIOS : #######################################
##________________________________________  ___________________________


#####  ==========  Boot-Process-Allg-WINs : (ONLY for MsWins! grub/Lx different!)
-!! https://en.wikipedia.org/wiki/Windows_NT_6_startup_process :

	_______:  bootloaders-process in Wins:
	-!! see https://en.wikipedia.org/wiki/Windows_NT_6_startup_process#Boot_loaders
	--- BIOS-mswin-bootloaders Seq. (bootmgr) :
		-! BIOS-Motherboard-firmware-sofware  -->  invokes MBR boot code (first 512 bytes) -> find active partition -> VBR code -> execute bootloader \bootmgr on active-partition ! part-2: OS-loading:  \windows\system32\[boot]\winload.exe ! (winload.exe : operating system boot loader) -->  ntoskrnl.exe and core device drivers.
		WiPe:  The BIOS invokes MBR boot code from a hard disk drive at startup. The MBR boot code and the VBR boot code are OS-specific. In Microsoft Windows, the MBR boot code tries to find an active partition (the MBR is only 512 bytes), then executes the VBR boot code of an active partition. The VBR boot code tries to find and execute the bootmgr file from an active partition.
		then The Windows Boot Manager (1kk: bootmgr) invokes winload.exe—the operating system boot loader—to load the operating system kernel executive (ntoskrnl.exe) and core device drivers. In that respect, winload.exe is functionally equivalent to the operating system loader function of NTLDR in prior versions of Windows NT. https://en.wikipedia.org/wiki/Windows_NT_6_startup_process
	--- UEFI-mswin-bootloaders Seq. :
		-! UEFI-Motherboard-firmware-sofware  -->  Windows boot manager: /EFI/Microsoft/Boot/bootmgfw.efi (grub: EFI\boot\bootx64.efi ) --> part-2:  OS-Win-Loader: C:\\windows\system32\[boot]\winload.efi :
		WiPe: The Windows boot manager is located at the \EFI\MICROSOFT\BOOT\ subfolder of the EFI system partition.
		The UEFI invokes bootmgfw.efi from an EFI system partition at startup! usu. /EFI/Microsoft/Boot/bootmgfw.efi ! 
		then The UEFI Windows Boot Manager (bootmgfw.efi) invokes the UEFI operating system boot loader. In UEFI systems, the file is called winload.efi and the file is always located at \windows\system32 or \windows\system32\boot
	--- Part-2 : OS-bootloader : is like in Lx: tranfer from initrd to linux-Kernel-OS): \windows\system32\[boot]\winload[.efi bzw. .exe] (operating system boot loader) -->  ntoskrnl.exe and core device drivers. 
		WiPe: If the computer has recently hibernated: in BIOS systems: then bootmgr will instead invoke winresume.exe.
		In UEFI systems: the file is called winresume.efi and is always located at \windows\system32 or \windows\system32\boot
##________________________________________  ___________________________


#####  ==========  DEFs: boot-part + system-part (opposite to Lx/Std-DEF) :
    -! https://en.wikipedia.org/wiki/System_partition_and_boot_partition
    - Lx-DEFs:  1-boot-part: contains bootloader(grub)+bootSW-initrd+kernel  , 2-system-part: contains OS, so "/"-part, /usr/ ,/bin/, ... !
    - MS-DEFs:  1-system-part:  contains the BCD/boot loader (bcd/efi), and keeps boot-sector , 2-boot-part: contains OS/Windows-Dir/Win10, so C:\...
##________________________________________  ___________________________


#####  ==========  misc-boot/startups:

	_______:  verbose-boot bzw. disable wellcome-screen !?!?:
	- did NOT work : https://docs.microsoft.com/en-us/troubleshoot/windows-server/performance/enable-verbose-startup-shutdown-logon-logoff-status-messages
	- also NOT worked with : msconfig.exe , and then no GUI + ... !
	obv. not possible in Win10 ???
##________________________________________  ___________________________


#####  ==========  Bios or UEFI is my system?? query in MsWin:

	_______:  identifying if my system booted in BIOS or UEFI :
	- REG-query:   reg query HKLM\System\CurrentControlSet\Control /v PEFirmwareType   #--->   0x1 : BIOS ,  0x2 : UEFI ; see ApplyRecovery.bat in Manufacturing.pdf--p.126 :
	- msinfo32.exe ->System Information :   value of "BIOS mode" : "Legacy" is BIOS ; "UEFI" means Windows boots in UEFI/GPT mode!
	- notepad++   C:\windows\panther\setupact.log  : search for "Detected boot environment" bzw.  Callback_BootEnvironmentDetect

	_______:  Umstellen of Win10-boot von BIOS-to-UEFI /CT:
	PRAXIS c't 14/2019, Seite 162 ,  Windows 10 von klassischem Start auf UEFI-Boot umstellen :
	Wenn ein bereits installiertes Windows künftig nicht mehr im Legacy-BIOS-, sondern im UEFI-Modus booten soll, reichen zum Umstellen zwei Handgriffe – doch die haben es in sich. ...
##________________________________________  ___________________________


#####  ==========  USB-boot:
    - Axel Vahldiek, FAQ: Booten von USB-Laufwerken, c’t 24/2018, S. 172, auch online unter ct.de/-4209809
    -! see intalled-<Media>-dnts here with Rufus !
##________________________________________  ___________________________


##################### diskpart / HDs / partitions / Volumes / ... : ######################################################
#####  ==========  diskpart:
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart
https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-deployment-command-line-tools-reference?view=windows-11
##________________________________________  ___________________________


#####  ==========  HDs , parts-handling , HD-pathes, HDs in BIOS/UEFI  :
	-! https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/hard-drives-and-partitions?view=windows-11

	_______:  HDs-pathes ( Hard Disk Location Path Format)
	-!! https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/hard-disk-location-path-format?view=windows-11
	- DEF:  The location path is a string that specifies the physical location that each drive is connected to the computer, for example: PCIROOT(0)#PCI(0100)#ATA(C00T00L00). 
	- Hard disk location-path format  is based on the physical connection to the computer !
	-! identifyinf/querying HD-location-path:  diskpart -> select disk x -> detail disk  ##-- https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-multiple-hard-drives?view=windows-11
	- Select the drive by location path: diskpart -> select disk=<HD-path> as: SELECT DISK=PCIROOT(0)#PCI(0100)#ATA(C00T00L00)

	_______:  converting gpt/mbr:
	- https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc725671(v=ws.11)
	- Converted a disk from GPT to MBR, and vice versa : Microsoft offers MBR2GPT.exe which converts disks from MBR to GPT.
	- MS:  you cannot use the GPT partition style on removable media, 

	_______:  
	- duplicating of GTP-disks / dd :  Do not make a sector-by-sector copy of a GPT disk (1kk: a GUID my NOT doppelt vorhanden in a NW !). The Disk and Partition GUIDs will no longer be unique. This must never happen. You can make a sector-by-sector copy of the contents of ESP or basic data partitions. If Windows detects a duplicate Disk or Partition GUID, Windows will generate new GUIDs for any duplicate Disk GUID, MSR Partition GUID, or MSR basic data GUID upon detection. ...
##________________________________________  ___________________________


##################### cmds--disks/boots/...: #############################################################################
#####  ==========  cmds--disks/boots/...:
    https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-deployment-command-line-tools-reference  :

        _______:  disks/parts:
    - DiskPart 	:  Manages disk partitions.
    - MBR2GPT.EXE 	:   Windows 10 version 1703 and newer supports converting from BIOS/MBR to UEFI/GPT using MBR2GPT.EXE. /arx

        _______:  more:
    - Oscdimg 	:  Creates an image (.iso) file of a customized 32-bit or 64-bit version of Windows PE

        _______:  BCD cmds see extra dnts!
##________________________________________  ___________________________



