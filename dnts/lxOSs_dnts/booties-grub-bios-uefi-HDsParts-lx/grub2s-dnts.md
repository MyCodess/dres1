_________ grub2 devnts: ____________________________________
- grub.pdf is just the GUN-std-manual of grub2 /_220908 !
##________________________________________  ___________________________


#####  ==========  L1NW-NBs-PCs-extra-nts ...:
	- asus1 is somehow starange: full-EFI??? sinwdows shows Legacy! but it works only with EFI-grub-sticks !?!?
	- ok-for-X17-Bios--fuulOK-incl.-win-start BUT not for asus1! : 
		grub-install  --target=i386-pc  --boot-directory=/mnt/t1/boot1/  --efi-directory=/mnt/t1/boot1/ --removable --recheck   -v  /dev/sdb 
		without --target=i386-pc  in x17: went into grub-shell!! asus1 anyway NOT-working!
	- ok-for-asus1-BUT-not-x17:
		grub-install    --boot-directory=/mnt/t1/boot/  --efi-directory=/mnt/t1  --removable --recheck   -v  /dev/sdb
		- asus-1 could not acess hd1,msdos1 to start windows: probably because the first-win-boot-part is NTFS! and it is missing in stick/grub-boot!
		- in x17: grub/i368-pc/norme.mod missing ... (probably due to missing --target=i386-pc there !)
	- booted fine for both! (bothe commands hintereinander, once for BIOS/i386-pc-DIR , once for EFI) :
		grub-install                     --boot-directory=/mnt/t1/  --efi-directory=/mnt/t1  --removable --recheck   /dev/sdb
		grub-install --target=i386-pc    --boot-directory=/mnt/t1/  --efi-directory=/mnt/t1  --removable --recheck   /dev/sdb
		- asus1 still could not start win10, but probably because HD-win-boot-part is in NTFS ! so missing drivers here !
		- in grub.cfg you must adapt the UUID for root= of /dev/sdb2 !
##________________________________________  ___________________________


#####  ==========  dosc-WPs: grub +kernel ...:
-!  https://wiki.archlinux.org/index.php/GRUB   ,  https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks  ,  https://wiki.archlinux.org/index.php/Talk:GRUB
-!  https://wiki.archlinux.org/index.php/Kernel_parameters
-!  https://www.gnu.org/software/grub/manual/grub/grub.html
-! for BIOS+GPT-partiotioning for Grub2 see:   https://wiki.archlinux.org/index.php/GRUB#GUID_Partition_Table_(GPT)_specific_instructions
- grub.pdf is just the GUN-std-manual of grub2 /_220908 !
##________________________________________  ___________________________


#####  ==========  !!  DEFs / Vocabs / Grub-Install-Concept !!:
	-!! see grub-manual.pdf : CH-4 Installation ! /_220906 :
	-!! Vocabs:   BOOT DIRECTORY , IMAGE DIRECTORY , grub-OS-installation , grub-boot-installation :
	1- In order to install GRUB as your boot loader, you need to first install the GRUB system and utilities under your UNIX-like operating system (1kk: pacman -S grub : /usr/lib/grub/<cpu>-<platform>’)!
		GRUB comes with boot images, which are normally put in the directory ‘/usr/lib/grub/<cpu>-<platform>’ (for BIOS-based machines ‘/usr/lib/grub/i386-pc’).
		the directory where GRUB images are initially placed (normally ‘/usr/lib/grub/<cpu>-<platform>’) will be called the IMAGE DIRECTORY !
	2- After you have done OS-rpm/pacman-install, you need to install the boot loader on a drive (1kk: into MBR/EFI/... to boot) by using the utility grub-install !
		the directory where the boot loader needs to find them (usually ‘/boot’) will be called the BOOT DIRECTORY.
		this install DIFFERENT for BIOS or UEFI !! see below !
	-!!  "BOOT DIRECTORY" : default is always BIOS: /boot/ and for EFI: /boot/efi !! so calling grub-install without --boot-directory=XXX will ALWAYS copies grub-stuff into /boot/grub/ !! so evt. to the current running OS-boot-dir ! if not wanted, then specify  the target --boot-directory=... !!
	--> so usu. BOOT DIRECTORY : /boot/ (will contain then /boot/grub/ ) ,  IMAGE DIRECTORY : /usr/lib/grub/<cpu>-<platform>/ ,
		grub-OS-installation : pacman -S grub into /usr/lib/grub/.... , grub-boot-installation : copy grub-cores into MBR/EFI/... and into /boot/... by grub-install , so into /boot/grub/ !
##________________________________________  ___________________________


#####  ==========  grub-install :
-! see  grub.pdf--23 Invoking grub-install
-!! DIFF ! : ABSOLUTELY different installation process if UEFI or BIOS !! see https://wiki.archlinux.org/index.php/GRUB

	_______:  Allg-nts grub-install :
	-! grub-install creates a grub dir under /boot/ as default, except with --boot-directory=XXX , then under XXX/grub/ !  and put grub-boot-loader into MBR/EFI/... !
	- copies grub-images from the OS IMAGE DIRECTORY (eg /usr/lib/grub/<cpu>-<platform>/)  into grub BOOT DIRECTORY (eg /boot/ , ...) !
	  so eg: in a BIOS-pc , mounted /dev/sda1 as /boot/ , calling "grub-install --boot-directory=/boot ... /dev/sda" :
	  it creates there /boot/grub/ , copies grub-images from eg /usr/lib/grub/i386-pc/ there AND copies its core.img into its MBR !
	- target-parameter is  "disk" eg /dev/sda and NOT partition eg /dev/sda1 !! so:
		 grub-install --target=i386-pc   /dev/sdX    ##--where /dev/sdX is the disk where GRUB is to be installed (for example, disk /dev/sda and not partition /dev/sda1).  https://wiki.archlinux.org/index.php/GRUB#Master_Boot_Record_(MBR)_specific_instructions
	- after installing grub-boot-core (core.img) by grub-install , then you need grub.cfg for boot-menu! so see nts here for "config-grub2"
	- core.img :  grub-install creats dynamically a new core.img for the current installation by running: grub-mkimage !

	_______:  params grub-install for both BIOS/UEFI :
	--boot-directory=dir1  : Install GRUB images under the directory ‘dir1/grub/’ 
		This option is useful when you want to install GRUB into USBStick, into a separate partition or a removable disk.
		If this option is not specified then it defaults to ‘/boot’, so grub-install /dev/sda is equivalent to grub-install --boot-directory=/boot/ /dev/sda
	- 

	_______:  BIOS-install-nts:
	- see:  grub.pdf--11 GRUB image files 
	-- BIOS-boot-process:  in BIOS-systems grub-install basically does:
	1- grub-install creats dynamically new boot.img + core.img whereas the block-address of core.img is hardcoded into generaed boot.img !
	2- copies boot.img into MBR   : The sole function of ‘boot.img’ is to read the first sector of the core image from a local disk and jump to it. Because of the size restriction, ‘boot.img’ cannot understand any file system structure, so grub-install hardcodes the location of the first sector of the core image into ‘boot.img’ when installing GRUB
	3- during boot, then boot.img calls the core.img, which is HARD-CODED-Address (Blocks-Counting)
	4- core.img then calls the OS-loader: kernel(vmlinuz) / chainOS(mswin, bootmgr)

	_______:  UEFI-installs:
	!! see ALL steps in:   https://wiki.archlinux.org/title/GRUB#UEFI_systems  : grub installation on UEFI !
	-!!  grub-install command (without --boot-directory param) must run from inside the system in which GRUB will be installed as the boot loader (so do:  chroot ...): Otherwise require: --boot-directory=/mnt/boot which is the path to the mounted /boot ! see above arx-url !
	--- params-UEFI of grub-install :    https://wiki.archlinux.org/title/GRUB :
		Mount the EFI system partition and in the remainder of this section, substitute esp with its mount point.
		eg:    grub-install  --target=x86_64-efi  --efi-directory=esp  --bootloader-id=GRUB  :
		UEFI:  --efi-directory and --bootloader-id are specific to GRUB UEFI, --efi-directory replaces --root-directory which is deprecated.
		-! NO target-device-param as /dev/sdX  : You might note the absence of a device_path option (e.g.: /dev/sda) in the grub-install command. In fact any device_path provided will be ignored by the GRUB UEFI install script. Indeed, UEFI bootloaders do not use a MBR bootcode or partition boot sector at all. 
	--- grub uefi application:
		- GRUB EFI application is grubx64.efi , which will be coipied to <mountpoint-boot>/EFI/BOOT/grubx64.efi (without --removable param)!
		-  If you use the option --removable then GRUB will be installed to esp/EFI/BOOT/BOOTX64.EFI (or esp/EFI/BOOT/BOOTIA32.EFI for the i386-efi target) and you will have the additional ability of being able to boot from the drive in case EFI variables are reset or you move the drive to another computer. 

	_______:  USB-/removable-installs:
	For removable installs you have to use ‘--removable’ and specify both ‘--boot-directory’ and ‘--efi-directory’:
	grub-install --efi-directory=/mnt/usb --boot-directory=/mnt/usb/boot --removable
	-! If you use the option --removable then GRUB will be installed to  <mountpoint-boot>/EFI/BOOT/BOOTX64.EFI  anstatt <mountpoint-boot>/EFI/BOOT/grubx64.efi for normal/non-removable !

	_______:  partition-installation:  installing grub into the partition-boot-sector instead the MBR/disk-boot-sector (eg dual-booting with mswins and with BCD, not with grub):
	-! MUST give alsso param "--force" ! as in: grub-install  --target=i386-pc  --boot-directory=/mnt/t1/boot/ --force  -v /dev/sdb1  ##--!-so sdb1 instead sdb ! and also --force !!
	-! worked ONLY from a OS on the same/target-HD !! NOT-inter-Disks !! see arx-multiboot-install-notes!! so need eiither chroot /OR arx1-cloning-tricks,....
	-! checking if it was done:  dd if=/dev/sdb  bs=512 count=1 2>/dev/null  | strings | grepi grub
##________________________________________  ___________________________


#####  ==========  misc-allg-grub2:
	- check/verfiy is GRUB installed on the bootsector of my HD/Partition?:  dd if=/dev/sdb bs=512 count=1 2> /dev/null  | strings | grep -i GRUB  ; ##-/OR maybe: file -s /dev/sda  #see "GRUB" ??
##________________________________________  ___________________________


#####  ==========  pathes of devices/files in grub2:
	-!  grub.pdf--13.1 How to specify devices
	(disk,part)/aa/bb/cc
	- use "/" (not DOS "\" !)
	- If you omit the device name in an absolute file name, GRUB uses GRUB’s root device implicitly.
	  So, if: set root=(hd1,1), then /boot/kernel is the same as (hd1,1)/boot/kernel
	- eg: (hd0,1)/boot/grub/grub.cfg’. This means the file ‘/boot/grub/grub.cfg’ in the first partition of the first hard disk
##________________________________________  ___________________________


#####  ==========  Numbering/Naming conventions for Disks/Parts of Grub2:
	-!! see https://www.gnu.org/software/grub/manual/grub/grub.html#Naming-convention  +  grub.pdf--13.1 How to specify devices :

	_______:  Numbering :
	- partition-numbers starting at 1, disk-numbers starting at 0 ! AND all always in (Disk,Part) as:  (hdX,Y) is the partition Y on disk X, 
	- extended-parts:  partition numbers for extended partitions are counted from ‘5’, regardless of the actual number of primary partitions on your hard disk.
	- files-pathes:  (hd0,msdos1)/vmlinuz  : specifies the file named ‘vmlinuz’, found on the first partition of the first hard disk drive

	_______:  Numbering-eg :
	- (hd0,msdos2)  :  first hard disk , second partition of a dos-partitioned-HD
	- (hd0,msdos5)  :  the first extended partition of the first hard disk drive of a dos-partitioned-HD
	- (hd0,gpt3)    :  third  partition of a GPT-/GUID-partiioned-HD
	- (fd0) : first-floppy-disk

	_______:  Numbering-more...:
	- syntax ‘(hd0)’ represents using the entire disk (or the MBR when installing GRUB), while the syntax ‘(hd0,1)’ represents using the first partition of the disk (or the boot sector of the partition when installing GRUB).
##________________________________________  ___________________________


#####  ==========  grub-terminal, grub-CLI-interface for handling grub-menu or booting manually or debugging,...; so for command-line and in menu entries :
	-! see FULL-Listing-cmds:   grub.pdf--16.3 The list of command-line and menu entry commands +  14.1 The flexible command-line interface
	- entering with 'c' in boot-menu!
	-  grub> help  [cmd]  ; eg: help ; help set ; ....
	- booting manually on cmline eg: insmod xx,..., linux (hd0,gpt1)/vmlinuz ... ; initrd; boot
	- return to the grub-MENU:  grub> normal
	- boot /or reboot ;
	- search [‘--file’|‘--label’|‘--fs-uuid’] [‘--set’ [var]] [‘--no-floppy’] name
##________________________________________  ___________________________


#####  ==========  grub-Kernel-Params-Modifying:   https://wiki.archlinux.org/index.php/Kernel_parameters
- onetime-during-booting--editing-Kernel-params- /OR edit-oneTIme-menu-entries-during-booting:  Press e when the menu shows up and ....
- persistent--editing-kernel-params:  Edit /etc/default/grub and append your kernel options to the GRUB_CMDLINE_LINUX_DEFAULT and     And then automatically re-generate the grub.cfg file with: # grub-mkconfig -o /boot/grub/grub.cfg  :  https://wiki.archlinux.org/index.php/Kernel_parameters
##________________________________________  ___________________________


#####  ==========  partitioning/preparing for Grub2-setup:

	_______:  BIOS/MBR-style (std.-legacy-combination):    https://wiki.archlinux.org/index.php/GRUB#Master_Boot_Record_(MBR)_specific_instructions
	-!! free-space-up-to-first-Part-in-MBR (ArX-wiki):   Master Boot Record (MBR) specific instructions :  Usually the post-MBR gap (after the 512 byte MBR region and before the start of the first partition) in many MBR partitioned systems is 31 KiB when DOS compatibility cylinder alignment issues are satisfied in the partition table. However a post-MBR gap of about 1 to 2 MiB is recommended to provide sufficient room for embedding GRUB's core.img (FS#24103). It is advisable to use a partitioning tool that supports 1 MiB partition alignment to obtain this space as well as to satisfy other non-512-byte-sector issues (which are unrelated to embedding of core.img).  https://wiki.archlinux.org/index.php/GRUB#Master_Boot_Record_(MBR)_specific_instructions
	-!! Leave a 1 MiB free space somewhere in the first 2 TiB of the disk (e.g. by using +1M as the first sector of a partition) in case you ever need to create a BIOS boot partition.  https://wiki.archlinux.org/index.php/GPT_fdisk

	_______:  BIOS/GPT-style (eg old-NBs with newly partitioned HDs/Sticks, as now by x17 + arx-ub128):
	-!!  https://wiki.archlinux.org/index.php/GRUB :
	- On a BIOS/GPT configuration, a "BIOS boot partition" is required. GRUB embeds its core.img into this partition.
	- Before attempting this method keep in mind that not all systems will be able to support this partitioning scheme. Read more on Partitioning#GUID Partition Table.
	- The BIOS boot partition is only needed by GRUB on a BIOS/GPT setup. On a BIOS/MBR setup, GRUB uses the post-MBR gap for the embedding the core.img. On GPT, however, there is no guaranteed unused space before the first partition.
	- For UEFI systems this extra partition is not required, since no embedding of boot sectors takes place in that case. However, UEFI systems still require an EFI system partition.
	-- crating a "BIOS boot partition" :
	Create a mebibyte partition (+1M with fdisk or gdisk) on the disk with no file system and with partition type GUID 21686148-6449-6E6F-744E-656564454649.
	Select partition type BIOS boot for fdisk.
	Select partition type code ef02 for gdisk.
	For parted set/activate the flag bios_grub on the partition.
	-- install grub2:   # grub-install --target=i386-pc /dev/sdX

	_______:  EFI/GPT-style:   https://wiki.archlinux.org/index.php/GRUB#UEFI_systems  :
	- To boot from a disk using UEFI, an EFI system partition is required.
	- ... see above link for installation! 
##________________________________________  ___________________________


#####  ==========  Aufloesung/resolution of grub2-terminal / gfxterm :
- usu. grub finds the best automatically! so the default in grub.cfg is ok:   set gfxmode=auto #but if not:
- check the abilities of your NB-Display
	- in grub-terminal with:   grub>  videoinfo         ##--OR vbeinfo , ...;
	- /OR from arx1 as root:   # hwinfo --framebuffer   ##if needed: pacman -Syu  hwinfo ;
	and put them in /etc/default/grub (gfxterm=xxx,yyy,auto  #so: multiple resolutions comma separated, incl. ,auto at the end!) in preference-sequence-with-comma-separated: see  "15.1.12 gfxmod"  in grub2-manual , https://www.gnu.org/software/grub/manual/grub/html_node/gfxmode.html 
- Make sure to initialize, if not done already, GRUB graphical terminal, gfxterm, with proper video mode, gfxmode, in GRUB.
- Multiple resolutions can be specified, including the default auto, so it is recommended that you edit the line to resemble GRUB_GFXMODE=desired_resolution,fallback_such_as_1024x768,auto
-! if the following does NOT work, see other solutions/hints in https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Visual_configuration  !!
- eg in grub.cfg:   set gfxmode=1920x1200x32,1920x1200x8,1600x1200x32,1600x1200x8,1280x1024x32,1280x1024x8,1280x800x32,1280x800x8,1024x768x32,1024x768x8,auto

	_______:  
vi  /etc/default/grub  :
GRUB_GFXMODE=1600x900x32,1280x800x32,1024*786x32,auto
GRUB_GFXPAYLOAD_LINUX=keep
- grub-mkconfig .....

	_______:  
##________________________________________  ___________________________


#####  ==========  Keyboard , Keymap setting to DE-grub-keymap-file:
https://wiki.archlinux.org/index.php/Talk:GRUB#Custom_keyboard_layout
https://lists.gnu.org/archive/html/help-grub/2017-10/msg00001.html
https://fitzcarraldoblog.wordpress.com/2019/04/21/how-to-change-the-keymap-keyboard-layout-used-by-the-grub-shell-in-gentoo-linux/
- manual:  AT keyboard support allows keyboard layout remapping and support for keys not available through firmware.
-!! NOT-working in all NBs/PCs redefining KB-layout! but here the way, if possible:
	(vo17 and x13 worked fine with the following configs, BUT xps17-keyboard not worked, grub-terminal was frozen by: terminal_input at_keyboard !! /_200829  )!

	_______:  grub-std-console is US-kbd ! so changing it to DE-keymap:
1- create a custom DE-keylayout/keymap-file (grub-kbdcomp calls only ckbcomp ! if it is not there DW it from arx-AUR):
# grub-kbdcomp -o /boot/grub/de1.gkb  de   ##-same as:  ckbcomp de | grub-mklayout -o de1.gkb
2- edit The following line in /etc/default/grub: to:
GRUB_TERMINAL_INPUT="at_keyboard"  ##--so that the input is not grub-std-console, which is US-kbd
3- add Custom commands  to /etc/grub.d/40_custom load the keylayout-modules,...:
insmod   at_keyboard
insmod   keylayouts
keymap   $prefix/de1.gkb  ##--/OR   /grub/de1.gkb
4- generate new grub.cfg :
# grub-mkconfig  -o  ./grub-1.cfg ; vimdiff  ./grub-1.cfg  /boot/grub/grub.cfg ; if-ok...:mvi  ./grub-1.cfg  /boot/grub/grub.cfg ;

	_______:  /OR may be add all to the header-file (check if the sequence of entries is relevant ...??):
- vi  /etc/grub.d/00_header :
...
  insmod keylayouts
  insmod at_keyboard
  terminal_input at_keyboard   ##--->!! BUT this line crashed the grub-terminal by xps17 !! frozen!
  keymap de1
##________________________________________  ___________________________


#####  ==========  attached devices/HDs/...:
in grub-terminal (entering by "c" in boot-menu) :
grub> ls  --->!! with.no.params:  lists all found devices !!
eg:  ls (hd0,msdos5)/
- HWs-cmds to check:  lspci , lsmod
##________________________________________  ___________________________


#####  ==========  config-grub2 / grub.cfg / grub-mkconfig :
-!!  https://wiki.archlinux.org/index.php/GRUB#Configuration

	_______:  grub final conf-files:
	-! see  grub.pdf--6 Writing your own configuration file  :  6.3 Writing full configuration files directl , 6.4 Multi-boot manual config
	-! /boot/grub/grub.cfg  is now manually created/edited by 1kk !!
	- /boot/grub/custom.cfg will be invoked at the end of grub.cfg (if not out-commented !)
	-! after modifying grub.cfg always do syntax-check:  grub-script-check /boot/grub/grub.cfg
	- When booting, the Linux kernel (vmlinuz) will delegate the task of mounting the root filesystem to the initrd, usu. per vmlinuz param of root=UUID=...
	--- (ENV-)-Variables in grub.cfg and also in grub-terminal :
	- Varible-names in grub.cfg like in bash! see grub.pdf--Variable expansion
	- grub-builtin-VARs:  see grub.pdf--15.1 Special environment variables
	- $prefix : The location of the ‘/boot/grub’ directory as an absolute file name. This is normally set by GRUB at startup based on information provided by grub-install.
	- $root (DIFF with root-param for vmlinuz ! which is for the lx-kernel !):  see grub.pdf--p.73 :
		The (grub-) root device name. Any file names that do not specify an explicit device name are read from this device. The default is normally set by GRUB at startup based on the value of ‘prefix’.
		For example, if GRUB was installed to the first partition of the first hard disk, then ‘prefix’ might be set to ‘(hd0,msdos1)/boot/grub’ and ‘root’ to ‘hd0,msdos1’
	- in grub-CLI/commandline-Terminal:  list_env : prints out all env-vars!

	_______:  grub-mkconfig (for auto-creation of final config-file   /boot/grub/grub.cfg ) :
	- grub-mkconfig creates/overwrites main-final-grub-conf-file  /boot/grub/grub.cfg 
	- grub-mkconfig auto-generatess  based on /etc/default/grub  and  /etc/grub.d/* 
	-! config-DIRs as input for  grub-mkconfig :   /etc/default/grub  +  /etc/grub.d/ 
	-! grub.cfg editting will be LOST/Overwritten by recreating it with grub-mkconfig (eg by system-update, if not disabled!) based on values in /etc/default/grub  +  /etc/grub.d/*  !! so do NOT edit it directly (except for testing/quickies/...)
	-! for valid-params in /etc/default/grub  see  grub.pdf--6.1 Simple configuration handling
	-!! To make persistent the configs of grub-mkconfig generation,  edit  /etc/default/grub and then automatically re-generate the grub.cfg file with: 
		grub-mkconfig  -o  /boot/grub/grub.cfg  ##see  https://wiki.archlinux.org/index.php/Kernel_parameters
		/or to test its output:  grub-mkconfig  -o  /boot/grub/grub.cfg-1 ; vimdiff ...
	- chroot limitation:  If you are trying to run grub-mkconfig in a chroot or systemd-nspawn container, you might notice that it does not work, complaining that grub-probe cannot get the "canonical path of /dev/sdaX". In this case, try using arch-chroot as described in the BBS post !
	-  vi  -p  /etc/default/grub  /boot/grub/grub.cfg  /boot/grub/custom.cfg   /etc/grub.d/*
	- system-/user-adaptions of ENV-settings:	 	/etc/default/grub
	- system-/user-addies, insmod/keyboard/...:		/etc/grub.d/40_custom
	- system/user-Vorlagen :   /etc/grub.d/*   ##--werden uebernommen ins /boot/grub/grub.cfg  by auto-generationg with grub-mkconfig ... !
	- so do System/user-adaptions in /etc/default/grub  +  /etc/grub.d/*custom*  -->and then regenerate automatically with grub-mkconfig -o  ~/.grub-new1.cfg   ; then check if diff ... ok, then mv  ~/.grub-new1.cfg  /boot/grub/grub.cfg ;

	_______:  custom-menu-entries adding:    https://wiki.archlinux.org/index.php/GRUB#Configuration  :
	- with grub-mkconfig : You can add additional custom menu entries by editing /etc/grub.d/40_custom and re-generating /boot/grub/grub.cfg  ( with grub-mkconfig ).
	- directly:  OR you can create /boot/grub/custom.cfg and add them there. Changes to /boot/grub/custom.cfg do NOT require re-running grub-mkconfig, since /etc/grub.d/40_custom adds the necessary source statement to the generated configuration file.
- for new/modified  Kernel_parameters edit /etc/default/grub and append your kernel options to the GRUB_CMDLINE_LINUX_DEFAULT line (as GRUB_CMDLINE_LINUX_DEFAULT="quiet splash") and then do:   grub-mkconfig  -o  /boot/grub/grub.cfg
-!! main-central-editable-config-file:	/etc/default/grub and then do: sudo update-grub to auto-update /boot/grub/grub.cfg which is read by grub during booting!!:
- For full documentation of the options in this file, see:   info -f grub -n 'Simple configuration'
- Tip: users/custom boot entries can also be used when using a /boot/grub/grub.cfg generated by grub-mkconfig. Add them to /etc/grub.d/40_custom and re-generate the main configuration file or add them to /boot/grub/custom.cfg.
##________________________________________  ___________________________


#####  ==========  UUID and HD-Labels using for Parts/HDs in grub.cfg  instead old  /dev/sdX ... :
-!!  https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Persistent_block_device_naming

	_______:  they are as default enabled and is OK!  but here for info, just check that they are NOT diabled! :
	- disabling using  UUID :  GRUB_DISABLE_LINUX_UUID=true
	- 

	_______:  LABELs : It is possible to use labels, human-readable strings attached to file systems, by using:  search --label --set=root  MyLabel1
https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Using_labels  :
- First of all, label your existing partition:   tune2fs -L <LABEL>   <PARTITION>
- eg Label :
	menuentry "Arch-Linux-1" {
	  search --label --set=root  ArX1
	  linux /boot/vmlinuz-linux root=/dev/disk/by-label/ArX1
	  initrd /boot/initramfs-linux.img
	}

	_______:  UUIDs:  
-!!-DIFF:
	- UUID  :  is FileSystem-UUID, generated by mkfs.xxx, available  to grub after loading filesystem-drivers, and is Deafult by grub.cfg generation, if not disabled GRUB_DISABLE_LINUX_UUID=true !  <--->
	- PARTUUID  :  is partiotion-UUID, by defining a partition, eg fdisk, existing pre-formatting! can be disabled by GRUB_DISABLE_LINUX_PARTUUID=true !
		PARTUUID is not as reliable as using the filesystem UUID, but is more reliable than using the Linux device names. 
	- default-values:  grub default is to use (filesystem) UUID :
		GRUB_DISABLE_LINUX_UUID default is false (so do use fs UUID)  <--->  GRUB_DISABLE_LINUX_PARTUUID  default is true (not using PARTUUID, but fs UUID)
	-!! see also the comparison-table in manual, 6.2  :   Grub2-Manual-2.04--2008.htm#Root-Identifcation-Heuristics
- Whether to use UUIDs is controlled by an option in /etc/default/grub:    GRUB_DISABLE_LINUX_UUID=true  : disables using UUID! default is false and OK!
- eg UUID from x13 :
	menuentry 'Windows 7 (on /dev/sda2)' --class windows --class os $menuentry_id_option 'osprober-chain-1672033972031D5D' {
		savedefault
		insmod part_msdos
		insmod ntfs
		set root='hd0,msdos2'
		if [ x$feature_platform_search_hint = xy ]; then
		  search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos2 --hint-efi=hd0,msdos2 --hint-baremetal=ahci0,msdos2  1672033972031D5D
		else
		  search --no-floppy --fs-uuid --set=root 1672033972031D5D
		fi
		parttool ${root} hidden-
		chainloader +1
	}
##________________________________________  ___________________________


#####  ==========  Default-Menu-entry:

	_______:  setting/changing default-boot, after timeout:
	To change the default selected entry, edit /etc/default/grub and change the value of GRUB_DEFAULT=<...>   , started from ZERO, or choice-by-Menu-Title, eg:
	- Using menu titles :   GRUB_DEFAULT='Advanced options for Arch Linux>Arch Linux, with Linux linux'
	- Using numbers :    GRUB_DEFAULT="1"      ##--second-menu-entry
	- Using numbers :    GRUB_DEFAULT="0>2"    ##--second-submenu--from-first-menu-entry
	Grub identifies entries in generated menu counted from ZERO. That means 0 for the first entry which is the default value, 1 for the second and so on.
	Main and submenu entries are separated by a  ">"  .
The example above boots the third entry from the main menu 'Advanced options for Arch Linux'.

	_______:  Latest-Choice as default entry for the next boot:   https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Recall_previous_entry :
	- GRUB can remember the last entry you booted from and use this as the default entry to boot from next time.
	- To do this, edit /etc/default/grub and change the value of GRUB_DEFAULT:   GRUB_DEFAULT=saved  : This ensures that GRUB will default to the saved entry.
	- To enable saving the selected entry, add the following line to /etc/default/grub:   GRUB_SAVEDEFAULT=true
	- Note: Manually added menu items, e.g. Windows in /etc/grub.d/40_custom or /boot/grub/custom.cfg, will need savedefault added.
##________________________________________  ___________________________


#####  ==========  grub-images:
	-! see frub.pdf--11 GRUB image files
##________________________________________  ___________________________


#####  ==========  USB stick install :    https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks : 
Install to external USB stick

	_______:  BIOS :
Assume your USB stick's first partition is FAT32 and its partition is /dev/sdy1
# mkdir -p /mnt/usb
# mount /dev/sdy1 /mnt/usb
# grub-install --target=i386-pc --debug --boot-directory=/mnt/usb/boot  --removable  /dev/sdy
# grub-mkconfig -o /mnt/usb/boot/grub/grub.cfg

	_______:  Optionally backup your currents configuration files of grub.cfg:
# mkdir -p /mnt/usb/etc/default
# cp /etc/default/grub /mnt/usb/etc/default
# cp -a /etc/grub.d /mnt/usb/etc
# sync; umount /mnt/usb

	_______:  UEFI:
- EFI : To have grub write its EFI image to esp/EFI/BOOT/BOOTX64.efi, which the boot firmware will be able to find without any UEFI boot entry, use --removable when you run grub-install
##________________________________________  ___________________________


#####  ==========  MultiBoot-USB with ISOs, ... with  GRUB / Syslinux / Archiso : -!! https://wiki.archlinux.org/index.php/Multiboot_USB_drive  : see here  bootLoaders-bios-uefi-mbr-lx.txt !!
	A multiboot USB flash drive allows booting multiple ISO files from a single device. The ISO files can be copied to the device and booted directly without unpacking them first. There are multiple methods available, but they may not work for all ISO images.
##________________________________________  ___________________________


#####  ==========  grub1-->grub2 mappings...:
	- menu.lst	-->	grub.cfg
	- 
