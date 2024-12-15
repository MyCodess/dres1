_______________________ win10s-Lx-stuff : ____________________________________________________
##________________________________________  ___________________________


#####  ==========  Dual-Boot-mswin-Lx :
	-!! https://wiki.archlinux.org/title/Dual_boot_with_Windows#Windows_before_Linux

	_______:  grub-setup in partition-bootsector instead MBR:
	-! does NOT work inter-disks ! so invoking grub-install from /dev/sdb to write boot sector into /dev/sda7 !! ONLY from same the OS on the same  Disk/HD !!
	-! so, works-only vom-target-HD aus !! so NOT from usb-stick targeting the HD with grub-install .... /dev/sda7 !
	so somehow with chroot or booting into a OS on the target-HD and then:  grub-install .... /dev/sda7 !
	so I did "cp -a arx1-stick into /dev/sda7 on mswin-HD", so is full arx-OS BUT still NOT bootable ! and then
	I booted grub from the bootOnlyStick into the arx on mswin-HD (sda7), and did: 
	grub-install  --target=i386-pc  --boot-directory=/boot/ --force  -v /dev/sdb1  ##--(for BIOS/x17 needed --target=i386-pc, ohterwise efi !)
	then: cp boot-stauff (vmlinuz,...) and vi grub.cfg !
	- check if grub is installed on a partition/HD with:  file -s /dev/sdx[x] ;/OR  dd if=/dev/sda7 bs=512 count=1 2>/dev/null | strings | grepi grub

	_______:  BCD-mswin-add:
	dd  if=/dev/sda7  of=/arx1_boot.bin  bs=512  count=1
	mount /dev/sda1 /mnt/t1 ##-- mount the mswin-boot/BCD-partiotion to copy it there:
	cp /arx1_boot.bin  /mnt/t1/
	--- reboot to mswin-OS:
	bcdedit /create /d "Linux" /application BOOTSECTOR
	bcdedit /set UUID-sda7 device partition=B: (or the drive letter on which /arx1_boot.bin is kept) 
	bcdedit /set UUID-sda7  path  \arx1_boot.bin
	bcdedit /displayorder UUID-sda7 /addlast  
	bcdedit /timeout 30
##________________________________________  ___________________________


#####  ==========  mswin-REG-files reading/handling on Lx :
    - Registry-files reading/handling on Lx: pacman -S  community/hivex ; man hivex         hivexget      hivexml       hivexregedit  hivexsh ...
    - eg, viewing BCD REG-file recursively from "Objects" key:  hivexregedit  --export   ./EFI/Microsoft/Boot/BCD   Objects
    (- Registry-files reading/handling on Lx: pacman -S  samba ; man regdiff   regpatch  regshell  regtree )
##________________________________________  ___________________________


#####  ==========  WSL / "Windows Subsystem für Linux" (WSL) :
- 
##________________________________________  ___________________________


#####  ==========  Powershell for Lx:
##________________________________________  ___________________________


#####  ==========  lx-Utils for mswins:
	pacman -Qi woeusb  : A Linux program to create Windows USB stick installer from a Windows DVD or an image
