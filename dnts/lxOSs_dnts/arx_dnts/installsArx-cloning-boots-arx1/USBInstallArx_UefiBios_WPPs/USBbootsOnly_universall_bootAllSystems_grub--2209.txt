##________________________________________  ___________________________


#####  ==========  /_220906 : 1kk-manually simple-only-boot-stick to boot All systems (arx, mswins,...) on all plattforms (BIOS/UEFI):
- checked on Lv13 (UEFI), asus1-red (UEFI-old), X17 (BIOS) : OK !

	_______:  ---
-!! here done 1kk himself, but see also arx-steps:   see  https://wiki.archlinux.org/title/Multiboot_USB_drive#Hybrid_UEFI_GPT_+_BIOS_GPT/MBR_boot
-!! in Arch-Guide itself it says a bit different, says: " create a GPT partition table", here stick is dos-partTabel!

	_______:  make an EFI-partition (here /dev/sdb2 from small-USB-Stick):
- fdisk /dev/sdb  --> one EFI partiotion: so type:  EF00
- mkfs.vfat -n  BOOT_UB1   -i 04B6A1D4  /dev/sdb2

	_______:  grub-install into /dev/sdb :
- mount /dev/sdb2 /mnt/t1
- grub-install  --boot-directory=/mnt/t1/boot/  --efi-directory=/mnt/t1/boot/  --removable --recheck    /dev/sdb  ##--for UEFI-systems
- grub-install  --boot-directory=/mnt/t1/boot/  --efi-directory=/mnt/t1/boot/  --removable --recheck  --target=i386-pc      /dev/sdb  ##--for BIOS-systems
- check grub-installed?:  dd if=/dev/sdb  bs=512 count=1 2>/dev/null  | strings | grepi grub
- check: tree -d /mnt/t1

	_______:  configs:
/either:  cpt /boot/grub/grub.cfg  /mnt/t1/boot/grub/ ; cp /boot/*  /mnt/t1/boot/  ##--vmlinuz-stuff ...
/OR maybe just??  :   mv /mnt/t1/boot  /mnt/t1/boot-1 ; cp -a /boot/  /mnt/t1/ ; 
lsblk1 /dev/sdX >>  /mnt/t1/00-THisMedia-XXXX.txt
vi /mnt/t1/boot/grub/grub.cfg ...
#- ther just check/adapt/diff:  grub-boot-root-uuid-for-vmlinuz/initramm  <-->  OS-root-uuid (as param to vmlinuz ) !
#------ done !
##________________________________________  ___________________________


#####  ==========  ====================================================================
################################### 1coll: ################################################################

	_______:  --- [root@2004arx t1]# fdisk -l /dev/sdb
Disk /dev/sdb: 7.28 GiB, 7811891200 bytes, 15257600 sectors
Disk model: Alu Line
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xc583c511
Device     Boot   Start      End  Sectors  Size Id Type
/dev/sdb1          2048   206847   204800  100M  c W95 FAT32 (LBA)
/dev/sdb2  *     206848  1230847  1024000  500M ef EFI (FAT-12/16/32)
/dev/sdb3       1230848 15257599 14026752  6.7G  c W95 FAT32 (LBA)
[root@2004arx t1]#

	_______:  ---
/dev/sdb                                                                                                               7.3G disk
├─/dev/sdb1                                                                                                            100M part
├─/dev/sdb2            vfat   FAT16 BOOT_UB1    04B6-A1D4                             422.2M    16% /mnt/t1            500M part
└─/dev/sdb3                                                                                                            6.7G part

	_______:  
