_______________  creating MBR+UEFI-bootable-USB-Media MANUALLY, eg. with grub-install,..., without any special OS on it (first, for now) /_190313 : ______________

	_______:  
creating a bootable USB-Media MANUALLY (zu Fuss), eg. with grub-install,..., without any special OS (first, for now), for both MBR + UEFI !
later OSs/ISOs can be added to it to boot into that OS
also ISOs , without unpacking or dd them ...; eg with "MultiBoot USB"-concept with Grub2 for both BIOS-MBR or UEFI !

	_______:  see :
-!! https://wiki.archlinux.org/index.php/Multiboot_USB_drive   --> also maybe for better alternatives, also with multiboot-ISOs,... !
	https://wiki.archlinux.org/index.php/Multiboot_USB_drive
-!! https://mbusb.aguslr.com/install.html

	_______:  for MultiBooting (One-USB-Stick and Many-Lx-ISO-files/systems-booting) see more URLs in :    https://wiki.archlinux.org/index.php/Multiboot_USB_drive   :
	There are some git projects which provide some pre-existing GRUB configuration files, and a nice generic grub.cfg which can be used to load the other boot entries on demand, showing them only if the specified ISO files - or folders containing them - are present on the drive.
	Multiboot USB: https://github.com/aguslr/multibootusb
	GLIM (GRUB2 Live ISO Multiboot): https://github.com/thias/glim
	https://mbusb.aguslr.com/install.html

	_______:  grub-short-nts:  (hdX,Y) is the partition Y on disk X, partition numbers starting at 1, disk numbers starting at 0
##________________________________________  ___________________________


#####  ==========  dd-variant :
- dd : if you do "dd   if=xx.iso   of=/dev/sdb ..." ,then be SURE to specify the of=DEVICE-name as /dev/sdb ,so NOT the Partition-name as /dev/sdb1 !! the DISK-boot-sectore must be overwritten be dd !!
- if it is hybrid-ISO, woks with dd just problomless fine! (nowadays are mostly all hybrid-ISOs !)
##________________________________________  ___________________________


#####  ==========  done-ok-try1--190313 (could be done better bzw. too comprehensive here, but hier fist just try to understand it):
	Grub2-boot-first try: manully create a bootable USB-stick, without any OS (you can add later ISOs/OS to the stick and add their boot-entry into the grub.cfg )  /_190300 ;
	https://wiki.archlinux.org/index.php/Multiboot_USB_drive
	-!! here all GRUB-cmds are from grub2 !! also grub-install,... is actually grub2-install ...!
- Partitioning and formatting the USB1-stick: made MBR-partitions and fat32 formated  :
	--> preferably with parted, and leave the first MB to Partition-Table (so called MBR-gap, so the gap between th part-table and firts-part! so "mkpart" started with sector 1 or 2, but NOT 0 !) ,
	- AND do "align-check opt 1" in parted !
	- mkfs.vfat -n UB8GP1 /dev/sdb1
	Number  Start   End     Size    Type     File system  Flags
	 1      1049kB  4000MB  3999MB  primary  fat32        boot, lba

	_______:  grub-boot-DIR on USB1
	- mount USB1 !
	- vi /media/u1/UB8GP1/00id1.txt .... ##--just a flag-file to find the part later easier in gtub-shell!
	- mkdir /media/u1/UB8GP1/boot

	_______:  grub-boot-install on USB1 for MBR-bios-systems: 
	-!! here ONLY MBR-PCs !! so UEFI-PC-with-secure-boot can not boot so ! see below for UEFI!
	- grub-install   --target=i386-pc --recheck --removable  --boot-directory=/media/u1/UB8GP1/boot/   /dev/sdb  ##-->ONLY-Bios-MBR-PC !
	Installing for i386-pc platform.
	Installation finished. No error reported.

	_______:  Keyboard-/Keymap-DE :  --> not-checked-yet!! probably a new grub.cfg must be generated !?!?---> see https://askubuntu.com/questions/751259/how-to-change-grub-command-line-grub-shell-keyboard-layout
	-! X17-nb problem!! grub-menu/-terminal freezes/no-KB !!
	- usu. you do not come into grub-shell, except your grub.cfg not working or emergency or one-time-alternative-boot-params,....
	then you NEED right keyboard-map inside the grub-shell (otherwise rather exhuasting ! default is us-kbd !!)
	so check in your running system, that your-keyboard-map exists, as for DE:   /usr/share/X11/xkb/symbols/de   ##and then eg your USB-boot-media is mounted on /media/u1/UB8GP1/ :
	mkdir /media/u1/UB8GP1/boot/grub/layouts/  &&   sudo grub-kbdcomp  -o  /media/u1/UB8GP1/boot/grub/layouts/de.gkb   de   ##--then you should see the generated keymap there !

	_______:  > now it should be bootable! done! but shows no-menu, no grub.cfg, to select the OS/Kernel,.. so :
	so to test it, if MBR-bootable, just copy any/dummy grub.cfg  to /media/u1/UB8GP1/boot/grub/grub.cfg if it will be shown at all!
	(?? or use  grub-mkconfig ) or just  https://www.gnu.org/software/grub/manual/grub/grub.html#Simple-configuration
--> should work hier for BIOS-systems / non-EFIs (also for BIOS/MBR)-PCs (not checked yet) : 	but for now it only shows the boot-menu ! the ISOs/OSs are not there yet!
##________________________________________  ___________________________


#####  ==========  UEFIs :

	_______:  for EFI-PCs : on your NB do:  apt-get     install  grub-efi  ##--needs the efi-packages if your BIOS/System is MBR-based! otherwise it is already there in UEFI-systems!
	- grub-install --target x86_64-efi --removable --boot-directory=/media/u1/UB8GP1/boot/    --efi-directory=/media/u1/UB8GP1/
	Installing for x86_64-efi platform.
	Installation finished. No error reported.
-!! on target-PC, if EFI-boots:  Disable Secure Boot on PC!

	_______:  > Wolla !! worked to boot !
##________________________________________  ___________________________


#####  ==========  
