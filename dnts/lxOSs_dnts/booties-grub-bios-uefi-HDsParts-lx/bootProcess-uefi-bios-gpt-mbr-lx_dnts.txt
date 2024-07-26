____________ Boot-Process-Lx Allg, UEFI, MBR, boot-managers, boot-loaders, SHIM, ...: __________________________
-!! for grub see extra dnts !!
##________________________________________  ___________________________


#####  ==========  docs UEFI/Secure-boot in Lx :
	-!! https://wiki.archlinux.org/index.php/Category:Boot_process
	--- boot-process-Lx-Allg:
	-!  https://en.wikipedia.org/wiki/Linux_startup_process
	-!  https://wiki.archlinux.org/title/Arch_boot_process
	-   /up1/w1/docs/CTs/CT_Articles_Topics/CT_Boots/
	--- boot-process/-params/-kernels...:
	https://wiki.archlinux.org/index.php/Arch_boot_process ,
	https://wiki.archlinux.org/index.php/Kernel_parameters , ....
	--- Disks/Partitioning for boot , MBR/GPT ....:
	https://wiki.archlinux.org/index.php/Partitioning ,
	https://wiki.archlinux.org/index.php/GPT_fdisk
	--- UEFI
	https://wiki.archlinux.org/index.php/EFI_system_partition
	https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface
	https://wiki.archlinux.org/title/GRUB#UEFI_systems  : grub installation on UEFI
	/up1/w1/docs/CTs/CT_Articles_Topics/CT_Boots/CT-UEFIs-BIOS/
	- long/comprehensive:  https://www.happyassassin.net/posts/2014/01/25/uefi-boot-how-does-that-actually-work-then/
	--- USB-/removableDisk-boot :
	https://wiki.archlinux.org/index.php/Multiboot_USB_drive
	--- Dual-Boot MsWins+Lx:
	-! https://wiki.archlinux.org/title/Dual_boot_with_Windows
	- CT !?
	--- secure boot:
	https://wiki.archlinux.org/title/Secure_Boot
	-!! ct.16.14--176-178--UEFI-Secure-Boot-Linux-Wins.pdf
##________________________________________  ___________________________


#####  ==========  Vocabs/DEFs of GUID/UEFI , basic-infs/defs/specs/... :
-!! https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface
	https://wiki.archlinux.org/index.php/EFI_system_partition
	https://uefi.org/specifications

	_______:  !! Vocabs + DEFS UEFI/GUID/...:
	- UEFI : is the FIRMWARE (so in Motherboard, pre-OS, pre-boot !! it boots/loads the OS !!)!! : 
		The Unified Extensible Firmware Interface (UEFI or EFI for short) is a new model for the interface between operating systems and firmware. It provides a standard environment for booting an operating system and running pre-boot applications.
		Unless specified as EFI 1.x, EFI and UEFI terms are used interchangeably to denote UEFI 2.x firmware.

	_______:  !!  DIFFs:
	-!!  BIOS / UEFI  <--->  MBR / GPT :
	- MBR and GPT are ONLY the type of how the disk-patition-table is defined structured ! BUT:
	- BIOS / UEFI are the firmware-software saved on motherboard to start bootin !!

	_______:  ! MsWins/Microsoft problem/deficiency :
	- ONLY microsoft wants to keep together BIOS+mbr and UEFI+gpt ! but NO-technical reason! so in linux no problem any combinations !
	- nts:  GPT-partitioning is also possible on BIOS-Legacy-Systems (eg on x13/x17) and does NOT have to be UEFI-firmware!
		but microsoft requires on UEFI-systems always GPT-partiotioning! possible is also BIOS+GPT (as my arx-stick to x13/x17))

	_______:  VOCABs-counterpart of  BIOS <---> UEFI software :
	firmware (BIOS or UEFI), software on motherboard responsible for loading the kernel  <--->  Partitioning-Table (MBR or GPT), so only parts-infos/-boundaries saved on the device
	BIOS Systems (Legacy firmware on Motherboard)  <--->  UEFI Systems (modern firmware on M.) (both are Motherboerboard-features! so pre-OS)
	BIOS Firmware (the software on Motherboard to boot the OS/Bootloader)   <--->  UEFI (== EFI , UEFI 2.x firmware , UEFI firmware )

	_______:  VOCABs-counterpart of   MBR <---> GPT partition-table-styles:
	MBR , Master Boot Record Partition Table  <--->  GPT , GUID Partition Table (GUID ca. == UUID)
	MBR-partioning-table (MBR-sector + 3 primary + Extended/logical-parts)  <--->  GPT-partioning-table (128 parts possiblem no-MBR-sector,...)
	only microfot want:  mbr/dos-Partion-Table in BIOS-/MBR-Systems  <--->   GPT-partiotion-table in UEFI-Systems !
	UUID == GUID (Microfoft intrduced GUID instead of UUID ..., ansonsten the same...; so GPT/GUID-Partition-Table is using UUIDs !)
##________________________________________  ___________________________


#####  ==========  UEFI-start-process:
	https://wiki.archlinux.org/title/Arch_boot_process#Under_UEFI
	1- POST ( power-on self-test /HW : finding HWs by chip)
	2- After POST, UEFI initializes the hardware required for booting (disk, keyboard controllers etc.).
	3- UEFI-Firmware reads (after POST) the boot entries (A boot entry could simply be a disk) in the NVRAM to determine which EFI application to launch and from where (e.g. from which disk and partition).
	4- \EFI\BOOT\BOOTx64.EFI  :  with this boot entry/Disk, then firmware looks for an EFI system partition on that disk and tries to find an EFI application in the fallback boot path \EFI\BOOT\BOOTx64.EFI
		This is how UEFI bootable removable media work
	5- Firmware launches the EFI application! This could be a boot loader or the Arch kernel itself using EFISTUB or  UEFI shell or a boot manager like systemd-boot ...
##________________________________________  ___________________________


#####  ==========  is my-system  UEFI or Bios ?:

	_______:  -- UEFI or Bios booted?? my start-firmware ?? : -------------------
	- which mode is current system booted in :
	- Lx:  sudo  efibootmgr :   (pacman -S efibootmgr ): If your system supports UEFI, it will output different variables. If NOT you will see a message saying EFI variables are not supported.
	- Lx:  /sys/firmware/efi/... , so Check if you are using UEFI or BIOS on Linux :  look for a folder /sys/firmware/efi. The folder will be missing if your system is using BIOS ! auch CT-11.12.174: OS in UEFI-Modus gestartet, dann sollte sich im laufenden System das Verzeichnis /sys/firmware/efi/ finden.
	- MsWins:  msinfo32 : see Bios Modus  (lagacy is Bios)
	- MsWins:  or check  C:\Windows\Panther\setupact.log  and search for "Detected boot environment" 

	_______:  -- MBR  or GPT part-table has my HD ?? : ------------
	- fdisk -l :  Disklabel type:  dos == mbr , gpt == GPT 
	- check is FAT-32/16 my EFI-part??:  file -s /dev/sdb2 #/OR-mtools:  minfo -i /dev/sda2  :: ##-- https://wiki.archlinux.org/title/FAT#Detecting_FAT_type
##________________________________________  ___________________________


#####  ==========  GPT-cmds/tools (GPT-partitioning-tools for both BIOS and UEFI systems; for MBR-partionining-tools still: fdisk,... ):
	https://wiki.archlinux.org/index.php/GPT_fdisk
	https://www.rodsbooks.com/gdisk/  !!--intro to gdisk/GPT/partitioning/... !
	- cmds:  gdisk , sgdisk , cgdisk
	- arx-package:  Install the gptfdisk package.
	GPT fdisk—consisting of the gdisk, cgdisk, sgdisk, and fixparts programs—is a set of text-mode partitioning tools made by Rod Smith. They work on Globally Unique Identifier (GUID) Partition Table (GPT) disks, rather than on the older (and once more common) Master Boot Record (MBR) partition tables.
	gdisk, cgdisk and sgdisk all have the same functionality but provide different user interfaces. gdisk is text-mode interactive, sgdisk is command-line, and cgdisk has a curses-based interface. 
##________________________________________  ___________________________


#####  ==========  Convert_between_MBR_and_GPT Partioning :
	https://wiki.archlinux.org/index.php/GPT_fdisk#Convert_between_MBR_and_GPT
	- cmds to convert:  gdisk , sgdisk , cgdisk
	-!! nts converting-problem: GPT stores a backup/secondary-table at the end of disk. This data structure consumes 33 512-byte sectors (16.5 KiB) by default.  MBR does not have a similar data structure at its end, which means that the last partition on an MBR disk sometimes extends to the very end of the disk and prevents complete conversion.  If this happens to you, you must abandon the conversion and resize/shrink a bit the final partition.
##________________________________________  ___________________________


#####  ==========  Recover GPT header
	https://wiki.archlinux.org/index.php/GPT_fdisk#Recover_GPT_header :
	nts: GPT stores a backup/secondary table at the end of disk. This data structure consumes 33 512-byte sectors (16.5 KiB) by default.
	--
	In case main GPT header or backup GPT header gets damaged, you can recover one from the other with gdisk. /dev/sda is used in this example.
	- gdisk /dev/sda
	choose r for recovery and transformation options (experts only). From there choose either
	b: use backup GPT header (rebuilding main)
	d: use main GPT header (rebuilding backup)
	When done write the table to disk and exit via the w command.
##________________________________________  ___________________________


#####  ==========  partition-table-Backup/restore , mirroring GPT partitions:   https://wiki.archlinux.org/index.php/GPT_fdisk  :
	- backup partitiontable to a (binary) file:    # sgdisk -b=sgdisk-sda.bin /dev/sda
	- restore the backup by running:   # sgdisk -l=sgdisk-sda.bin /dev/sda
	- clone your device's partition layout (/dev/sda in this case) to another drive (/dev/sdc) run:   # sgdisk -R=/dev/sdc /dev/sda
	  If both drives will be in the same computer, you need to randomize the disk and partition GUIDs:   # sgdisk -G /dev/sdc
##________________________________________  ___________________________


#####  ==========  

	_______:  rebooting into UEFI/BIOS:
	- arx:     systemctl reboot --firmware-setup
	- mswin:  Advanced startup in Windows by the Windows PowerShell command shutdown /r /o, or via Settings > Update & Security > Recovery > Advanced startup and select Restart now. 
	- GRUB editor: Press c for command line and in GRUB command line use fwsetup to enter firmware setup.
############################# efibootmgr, UEFI-shell, efivars, UEFI-cmds for shell-edits,...: ############################################
##________________________________________  ___________________________


#####  ==========  efibootmgr on Lx:  see ct.12.11.174-179__Linux__Dual-Boot_mit_UEFI_und_GPT.pdf !! :

	_______:  
	-! efibootmgr is an OS-app to modify the UEFI-firmware-entries/-vars (UEFI-BootManager), like UEFI-shell but from arx/OS-terminal ! (not modifying grub/bootloader, but directly modifying UEFI-setting (basically as earlier BIOS-display)!). 
	-!!  efibootmgr is used by the GRUB installation script to write boot entries to NVRAM / efi-firmware !
	-!! ct.18.23.140-153--UEFI-Linux--und-Dual-MsWins.pdf : also, creating/recreating UEFI-boot-entried 
	- pacman -Syu  grub  efibootmgr ##-- GRUB is the bootloader while efibootmgr is used by the GRUB installation script to write boot entries to NVRAM.	- 
	- troubleshooting:  If any userspace tool is unable to modify UEFI variable data, check for existence of /sys/firmware/efi/efivars/dump-* files. If they exist, delete them, reboot and retry again.

	_______:  !!  DIFF   UUID<--->PARTUUID  :
	!! efibootmgr shows/uses PARTUUID (pre-mkfs; so pre-formatting) !! not fs UUID (pos-mkfs; so assigned UUID during formatting!) ! so:
	UUID is the UUID of the filesystem, eg relevant for grub-boot !
	PARTUUID  is the UUID of the Partition (pre-filesystem, even not-formated) , eg relevant for UEFI-bootloader !! (pre-FS !) or how UEFI finds the ESP-part ! checkit with:
	lsblk  -p  -f  -o  +SIZE,TYPE,PARTUUID  ;#-bzw.  lsblk  -o   NAME,FSTYPE,PARTUUID,LABEL,UUID,MOUNTPOINT,SIZE,TYPE,RM,MODEL,SERIAL
	CT : Verwechelungsgefahr dieser zwei UUIDs ist besonders groß, weil das BIOS die ESP über die UUID der Partition findet; Ubuntus Grub hingegen findet seine vollwertige Konfigurationsdatei nicht über die UUID von Root- oder Boot-Partition, sondern über die UUID des darin enthaltenen Dateisystems. ct.18.23.140-153--UEFI-Linux--und-Dual-MsWins.pdf s149 !

	_______:  !! syntax-nts-UEFI:   mainly MsWIn-syntx with:  \ and '  instead / and " , also  case-INsensitive :
	- UEFI-Pfadtrenner is as MsWIns  "\" , and NOT "/" !!      CT: da UEFI als Pfadtrenner nicht den Schrägstrich (/), sondern nur den Backslash (\) spezifiziert, muss man die in der Windows-Welt gewohnte Pfadnotation verwenden. Bei der Diagnose von Boot-Problemen kann der Aufruf von Efibootmgr mit dem Parameter --verbose helfen, der die UEFI- Boot-Einträge in Rohform ausgibt.
	- use single quote '  insteaad of double one " for pathes/strings/.... 
	- case-INsensitive
	- see also  ct.18.23.140-153--UEFI-Linux--und-Dual-MsWins.pdf   s.148 :

	_______:  cmds eg efibootmgr :   man  efibootmgr : /sys/firmware/efi/efivars :
	-! you see also many uefi-vars/settings in the auto mounted uefi-system: mountg efi ; eg: ll /sys/firmware/efi/efivars/ ; ...
	- listing/shoe UEFI current entries/configs:  efibootmgr
	- timeout setting of bootmanager to 5 seconds :  efibootmgr -t 5
	- on UEFI started systems:  efibootmgr  ##---> prints out the current entries and boot-orders !
	- efibootmgr  [--verbose] : shows current entries   ##   bzw. more details with  --verbose
	- mehrere DISKs, then : efibootmgr  --disk  /dev/sdX ... ##--sind mehrere Datenträger im System, sollten Sie über einen efibootmgr-Parameter wie --disk /dev/sdb jenen spezifizieren, auf dem die ESP liegt, damit der Bootloader später auch gefunden wird. /CT
	- on BIOS-started-systems (as x13-ubt): 
		u1@x13:/up1/.ee71/bin$   efibootmgr
		EFI variables are not supported on this system.
	- efibootmgr --bootorder 4,1    ##--weist die Firmware an, zuerst den Eintrag 4 (beispielsweise Fedora) zu starten, und es gegebenenfalls mit dem Eintrag 1 (eg Ubuntu) zu versuchen, wenn das nicht klappt! 
	- efibootmgr --bootnext 1       #--Soll eg Ubuntu/Eintrag-1 nur einmalig starten, greifen Sie zu einem Befehl wie diesen, der den BootNext-Wert setzt: efibootmgr --bootnext 1 /CT-11.12.174
	- delete einen BOot-Eintrag von UEFI-Menu:  efibootmgr --bootnum 1— --delete-bootnum
	- on removable-Media/USB-Stick  ./EFI/BOOT/BOOTX64.EFI on ESP-Part will be executed ! also ansonsten, if EFI-Firmware finds nothing else! (eg EFI-boot-entries are deleted/korrupt; OR nothing installed, ...) /CT
	- restoring/recreating UEFI-boot-entries:  ct.18.23.140-153--UEFI-Linux--und-Dual-MsWins.pdf  s.148 !! with  efibootmgr  --create ...

	_______:  restoring/recreating UEFI-boot-entries :   ct.18.23.140-153--UEFI-Linux--und-Dual-MsWins.pdf  s.146 :
	1- zu-fuss with  efibootmgr --create  ... (vlt. eher praktischer als grub-install-method );  eg  efibootmgr --create  --disk /dev/sda --part 2 --label 'Mein-Ubuntu' --loader '\EFI\ubuntu\shimx64.efi'  #see CT
	2- with grub-install , but for UEFI the grub-install takes NO dev-param!! so works ONLY from the target-OS aus, so using a Live-Lx + chroot + mount ... , see CT ,as:
		Dazu müssen Sie zuerst ein Rettungs- oder Live-Linux mit UEFI-Mechanismen starten. Mounten Sie damit die Root-Partition des installierten Linux (beispielsweise in /mnt/), um die Pseudo-dateisysteme /dev/, /dev/ptc/ /sys/ und /proc/ per Bind-Mount darunter einzuhängen – etwa mit Befehlen wie mount --bind /dev/ /mnt/dev/. Wechseln Sie anschließend per chroot in die so eingerichtete Dateisystemumgebung des installierten Linux, um dort noch alle in der Fstab definierten Dateisysteme per mount -a zu mounten (auch die ESP-part, which musst be in fstab). ERST dann hängt auch auch die ESP an der vorgesehenen Stelle, womit alles bereit für grub-install ist.

	_______:  
	-!! finding an ESP-part:   lsblk -f -l -o NAME,PARTTYPE | grep '.*00a0c93ec93b'  ; /CT
	- bios-update per LX-OS:  fwupdmgr /c’t 2018, Heft 23--144

	_______:  
##________________________________________  ___________________________


#####  ==========  efivars:
	https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface#UEFI_variables
	/sys/firmware/efi/efivars : it is mounted in boot time by kernel to UEfI-firmware efivarfs !
	you can mount it also to anywhere, mentioning type/-t as:  mount -t efivarfs efivarfs /mnt/t1
##________________________________________  ___________________________


#####  ==========  UEFI-shell / Shell>  :
	-!! first try to do things with: efibootmgr (from arx)! it does a lot easier/better than in uefi-shell), or other arx-efi-cmds/-packs! if not possible, then use the  UEFI-shell if needed!
	  also Try bcfg only if efibootmgr fails to create working boot entries on your system.
	-! you see also many uefi-vars/settings in the auto mounted uefi-system: mountg efi ; eg: ll /sys/firmware/efi/efivars/ ; ...
	- Shell> bcfg  : modifies the UEFI NVRAM entries which allows the user to change the boot entries or driver options
	https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface#UEFI_Shell
	pacman -S edk2-shell
	- troubleshooting:  If any userspace tool is unable to modify UEFI variable data, check for existence of /sys/firmware/efi/efivars/dump-* files. If they exist, delete them, reboot and retry again.
	  If the above step does not fix the issue, try booting with efi_no_storage_paranoia kernel parameter to disable kernel UEFI variable storage space check that may prevent writing/modification of UEFI variables.
	    If the above step does not fix the issue, try booting with efi_no_storage_paranoia kernel parameter to disable kernel UEFI variable storage space check that may prevent writing/modification of UEFI variables.
	- Launching UEFI Shell:
	/either:  some UEFI-NBs have a menu-point to start the shell ! so then cp the eshell to the EFI-part-root as shellx64.efi , boot from that medium and start the shell by pressing its menu point! so:
	  cp the efi-shell into eg usb-stick--ESP-part-root as shellx64.efi  , so here: mount /dev/sdb2  /mnt/t1 ; cpt /usr/share/edk2-shell/x64/Shell_Full.efi  /mnt/t1/shellx64.efi
	/OR if no-shell-menu-point in UEFI-display, then: cpt /usr/share/edk2-shell/x64/Shell_Full.efi  <USB_drive_mointpoint-EFI-part>/EFI/BOOT/BOOTx64.EFI and boot from it !
################################ __1END__ uefi-shells,... #################################################
##________________________________________  ___________________________


#####  ==========  UEFI-partition /ESP /  EFI-System-Partition (ESP) :

	_______:  
	- https://wiki.archlinux.org/index.php/EFI_system_partition
	-!! short: an EFI-part is a fat32/fat16-formated-part with ID EF00 ! that's ALL !! (bzw. gpt-ID:  C12A7328-F81F-11D2-BA4B-00A0C93EC93B ), so:
	- The EFI system partition (also called ESP) is an OS independent partition that acts as the storage place for the EFI bootloaders, applications and drivers to be launched by the UEFI firmware. It is mandatory for UEFI boot.
	- UEFI systems require an EFI system partition.
	- The EFI system partition must be a physical partition in the main partition table of the disk, not under LVM or software RAID etc.
	- ESP ("EFI system partition") on a GUID Partition Table is identified by the partition type GUID C12A7328-F81F-11D2-BA4B-00A0C93EC93B (bzw. in BIOS mode/apps EF00 )
	-! check/verify if alread have an EFI-part?:
		in GPT-disks:  part-ID is C12A7328-F81F-11D2-BA4B-00A0C93EC93B  ##so-check:   lsblk -f -l -o NAME,PARTTYPE | grepi C12A7328-F81F-11D2-BA4B-00A0C93EC93B ;
		in MBR/dos-disks:   part-ID is: EF00
	-! When dual-booting, avoid reformatting the ESP, as it may contain files required to boot other operating systems.
	- check is FAT32 or FAT16 my EFI-part??:  file -s /dev/sdb2 #/OR-mtools:  minfo -i /dev/sda2  :: ##-- https://wiki.archlinux.org/title/FAT#Detecting_FAT_type

	_______:  crating a new EFI-part:
	-! https://wiki.archlinux.org/title/EFI_system_partition#Create_the_partition
	1- create a new part min 500 MB and set its GUiD/iD as:  EFI-partition type GUID is (GPT-disks) :  C12A7328-F81F-11D2-BA4B-00A0C93EC93B ##for mbr/dos-disks is: EF00
	2- mkfs.fat -F 32 /dev/sdxY ## -L ESP1
	3- mount it and copy: vmlinuz,... see the above archwiki-link !
##________________________________________  ___________________________


#####  ==========  Secureboot-lx:
	-! https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot
	-! status-secureboot, from arx1-OS aus?:   bootctl status

	_______:  mokutil : managing UEFFI-secure-boot and its Keys enabling/disabling/setting/.... ;  man mokutil
	- man mokutil   ##--if not there :  apt-get install mokutil
	- apt-get install mokutil
	- sudo mokutil --disable-validation  ##--disables secure-boot ! But im BIOS/Systemstart ist Secure Boot aber noch aktiv, denn komplett lässt sich die Technik nur im BIOS-Setup ausschalten !! aber ist jetzt deaktiviert bei diesem LX-Hochfahren nur !!
	- sudo mokutil --sb-state
##________________________________________  ___________________________


#####  ==========  LX-system/kernel and UEFI (if the system is using UEFI !):
	https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface#Linux_kernel_config_options_for_UEFI
	-!! all runtime-infs for UEFI:    /sys/firmware/efi/....  #if not there, is BIOS-Syystem! no UEFI-system !
	- Kernel-params for UEFI : see link above!
	-  efivar --list  ##--efivarfs (EFI VARiable FileSystem) interface  kernel module mounted at /sys/firmware/efi/efivars
	-!!   UEFI-Shell :  https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface#UEFI_Shell
##________________________________________  ___________________________


#####  ==========  MultiBoot-USB with ISOs, ... with  GRUB / Syslinux / Archiso :
	-!! https://wiki.archlinux.org/index.php/Multiboot_USB_drive  :
	-! UEFI-Multibooting is simple: Since each OS or vendor can maintain its own files within the EFI system partition without affecting the other, multi-booting using UEFI is just a matter of launching a different EFI application corresponding to the particular operating system's boot loader. This removes the need for relying on the chain loading mechanisms of one boot loader to load another OS.  https://wiki.archlinux.org/title/Arch_boot_process#Multibooting_in_UEFI
	A multiboot USB flash drive allows booting multiple ISO files from a single device. The ISO files can be copied to the device and booted directly without unpacking them first. There are multiple methods available, but they may not work for all ISO images.
	There are some git projects which provide some pre-existing GRUB configuration files, and a nice generic grub.cfg which can be used to load the other boot entries on demand, showing them only if the specified ISO files - or folders containing them - are present on the drive.
	Multiboot USB: https://github.com/aguslr/multibootusb
	GLIM (GRUB2 Live ISO Multiboot): https://github.com/thias/glim
	https://mbusb.aguslr.com/install.html

	_______:  utils-usb-boot:
	- ventoy : c't 24/2021, S. 142 ; www.ventoy.net ,  Multiboot-Stick, Ventoy is an open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files. , https://www.heise.de/select/ct/2021/24/softlinks/y1ua ;
--###################### BIOS+MBR (lagacy)  : #####################################################
##________________________________________  ___________________________


#####  ==========  BIOS-MBR-specs, BIOS-MBR-backup/restore , BIOS-MBR-bootsector , MBR-partition-table:
	-  https://wiki.archlinux.org/index.php/Partitioning
	-!!  https://wiki.archlinux.org/index.php/Dd#Backup_and_restore_MBR  :
	-!! The MBR/"Master Boot Record" is stored in the the first 512 bytes of the disk. It consists of 4 parts:
		1-The first 440 bytes contain the bootstrap code (boot loader,first-stage / Master Boot Record / bootstrap code).
		2-The next 6 bytes contain the disk signature.
		3-The next 64 bytes contain the partition table (4 entries of 16 bytes each, one entry for each primary partition).
		4-The last 2 bytes contain a boot signature.
	- Master Boot Record (bootstrap code ):  The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.
	- Master Boot Record (partition table):  In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions: Primary, Extended, Logical
	- backup/save the whole MBR as mbr_file.img:    dd if=/dev/sdX of=/path/to/mbr_file.img bs=512 count=1
		You can also extract the MBR from a full dd disk image:    dd if=/path/to/disk.img of=/path/to/mbr_file.img bs=512 count=1
	- restore the whole MBR (be careful, this destroys the existing partition table and with it access to all data on the disk):  
	dd if=/path/to/mbr_file.img of=/dev/sdX bs=512 count=1
	Warning: Restoring the MBR with a mismatching partition table will make your data unreadable and nearly impossible to recover. If you simply need to reinstall the bootloader see their respective pages as they also employ the DOS compatibility region: GRUB or Syslinux.
	- restore ONLY the boot loader, but NOT the primary partition table entries, just restore the first 440 bytes of the MBR:
	dd if=/path/to/mbr_file.img of=/dev/sdX bs=440 count=1
	- restore ONLY the partition table:   dd if=/path/to/mbr_file.img of=/dev/sdX bs=1 skip=446 count=64
	- erase ONLY the MBR bootstrap code, but NOT the parttable (may be useful if you have to do a full reinstall of another operating system) only the first 440 bytes need to be zeroed:
	dd if=/dev/zero of=/dev/sdX bs=440 count=1
##________________________________________  ___________________________


#####  ==========  MBR <--> GPT:
	-!! Tip:  Leave a 1 MiB free space somewhere in the first 2 TiB of the disk (e.g. by using +1M as the first sector of a partition) in case you ever need to create a BIOS boot partition.  https://wiki.archlinux.org/index.php/GPT_fdisk
	-!! Tip: When partitioning a MBR disk consider leaving at least 33 512-byte sectors (16.5 KiB) of free unpartitioned space at the end of the disk in case you ever decide to convert it to GPT. The space will be required for the backup GPT header.  https://wiki.archlinux.org/index.php/Partitioning
#############################################################################################
##________________________________________  ___________________________


#####  ==========  gdisk nts:
	-!! gdisk-intro:   https://www.rodsbooks.com/gdisk/
	----- Common partition types : ----------------------------------
	https://wiki.archlinux.org/index.php/GPT_fdisk :
	-- Partition type,	Mountpoint,	gdisk-code,	Partition-type-GUID : --
	BIOS boot partition	None	ef02		21686148-6449-6E6F-744E-656564454649
	Linux filesystem	Any		8300		0FC63DAF-8483-4772-8E79-3D69D8477DE4
	EFI system partition	Any	ef00		C12A7328-F81F-11D2-BA4B-00A0C93EC93B
	Linux x86-64 root (/)	/	8304		4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709
	Linux swap		[SWAP]		8200		0657FD6D-A4AB-43C4-84E5-0933C84B4F4F
	Linux /home		/home		8302		933AC7E1-2EB4-4F13-B844-0E14E2AEF915
	Linux /srv		/srv		8306		3B8F8425-20E0-4F3B-907F-1A25A76F98E8
	Linux /var		/var1		8310		4D21B016-B534-45C2-A9FB-5C16E091FD2D
	Linux LVM		Any		8e00		E6D6D379-F507-44C2-A23C-238F2A3DF928
	Linux RAID		Any		fd00		A19D880F-05FC-4D3B-A006-743F0F84911E
	Linux LUKS		Any		8309		CA7D7CCB-63ED-4C53-861C-1742536059CC
	Linux dm-crypt	Any		8308		7FFEC5C9-2D00-49B7-8941-3EA10A5586B7
	Linux /var/tmp		/var/tmp1		8311		7EC6F557-3BC5-4ACA-B293-16EF5DF639D1
	systemd-gpt-auto-generator(8) will only automount the partition if specific conditions are met. See systemd#GPT partition automounting for details.
	------------
