________________ offline-cloning-2004arx--including-new-Partitioning-of-target-USB : _______________
src:      usb128_bigBlack--SanDisk-usb3.1  ,      /dev/sda
target:   usb128_tiny--ultraFit_SanDisk-usb3.1 ,  /dev/sdb
!! target-usb: absolutely-new-usb-stick, new-partiioning, and then rsync /OR cp -a .... !
###################### gdisk, preparing-target-usb: ################################################
date ;  ##2021-10-06T21:50:38 CEST
##________________________________________  ___________________________


#####  ==========  src_USB : ====================================================================
[root@2004arx varau]# sgdisk -p  /dev/sda
Disk /dev/sda: 240353280 sectors, 114.6 GiB
Model: Ultra           
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 53316C42-96EB-450B-8D53-E0CEAEE762EE
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         8595455   4.0 GiB     EF00  EFI system partition
   3         8595456       113453055   50.0 GiB    8300  
   4       113453056       240353246   60.5 GiB    0700  
[root@2004arx varau]# lsblk1
dev/sda                                                                                                             114.6G disk
├─/dev/sda1                                                                                                            100M part
├─/dev/sda2            vfat   FAT32 ESP1        2C89-9F52                               3.9G     2% /boot                4G part
├─/dev/sda3            ext4   1.0   2004ARX_P   80bbc6dc-623f-4ec4-aa67-d9c37e40c4a5   18.5G    57% /home               50G part
│                                                                                                   /up1/mnt/VARUfs         
│                                                                                                   /                       
└─/dev/sda4            exfat  1.0   T1FS_P      7D6F-7316                              36.3G    40% /up1/mnt/T1fs     60.5G part
##________________________________________  ___________________________


#####  ==========  target_USB : NEW-partitioning: ================================================
[root@2004arx etc]# gdisk  /dev/sdb
GPT fdisk (gdisk) version 1.0.8
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present
Found valid GPT with protective MBR; using GPT.
Command (? for help): o
This option deletes all partitions and creates a new protective MBR.
Proceed? (Y/N): y
Command (? for help): w
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!
Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/sdb.
The operation has completed successfully.
[root@2004arx etc]# 
[root@2004arx etc]# 
[root@2004arx etc]# gdisk  /dev/sdb
GPT fdisk (gdisk) version 1.0.8
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present
Found valid GPT with protective MBR; using GPT.
Command (? for help): n
Partition number (1-128, default 1): 
First sector (34-240353246, default = 2048) or {+-}size{KMGTP}: 
Last sector (2048-240353246, default = 240353246) or {+-}size{KMGTP}: +100M
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): EF02
Changed type of partition to 'BIOS boot partition'
Command (? for help): n
Partition number (2-128, default 2): 
First sector (34-240353246, default = 206848) or {+-}size{KMGTP}: 
Last sector (206848-240353246, default = 240353246) or {+-}size{KMGTP}: +3G
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): EF00
Changed type of partition to 'EFI system partition'
Command (? for help): n
Partition number (3-128, default 3): 
First sector (34-240353246, default = 6498304) or {+-}size{KMGTP}: 
Last sector (6498304-240353246, default = 240353246) or {+-}size{KMGTP}: +50G
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): 
Changed type of partition to 'Linux filesystem'
Command (? for help): n
Partition number (4-128, default 4): 
First sector (34-240353246, default = 111355904) or {+-}size{KMGTP}: 
Last sector (111355904-240353246, default = 240353246) or {+-}size{KMGTP}: 
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): 0700
Changed type of partition to 'Microsoft basic data'
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model:  SanDisk 3.2Gen1
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 0D6CD0DA-590D-4F2F-8D0C-16E42C7B47BF
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         6498303   3.0 GiB     EF00  EFI system partition
   3         6498304       111355903   50.0 GiB    8300  Linux filesystem
   4       111355904       240353246   61.5 GiB    0700  Microsoft basic data
Command (? for help): w
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!
Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/sdb.
The operation has completed successfully.
[root@2004arx etc]# 
[root@2004arx etc]# 

	_______:  ---- print again:
root@2004arx varau]# sgdisk -p /dev/sdb
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model:  SanDisk 3.2Gen1
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 0D6CD0DA-590D-4F2F-8D0C-16E42C7B47BF
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         6498303   3.0 GiB     EF00  EFI system partition
   3         6498304       111355903   50.0 GiB    8300  Linux filesystem
   4       111355904       240353246   61.5 GiB    0700  Microsoft basic data
[root@2004arx varau]# 
[root@2004arx varau]# lsblk1 /dev/sdb
NAME        FSTYPE FSVER LABEL UUID FSAVAIL FSUSE% MOUNTPOINTS   SIZE TYPE
/dev/sdb                                                       114.6G disk
├─/dev/sdb1                                                      100M part
├─/dev/sdb2                                                        3G part
├─/dev/sdb3                                                       50G part
└─/dev/sdb4                                                     61.5G part
[root@2004arx varau]# 
###################### formattings/mkfs... : #######################################################
[root@2004arx varau]# date  ##  2021-10-07T11:53:17 CEST

	_______:  
[root@2004arx varau]# mkfs.fat  -F32  -n  ESP1   /dev/sdb2
mkfs.fat 4.2 (2021-01-31)

	_______:  
[root@2004arx varau]# mkfs.ext4  -L  2004ARX_P  /dev/sdb3
mke2fs 1.46.4 (18-Aug-2021)
Creating filesystem with 13107200 4k blocks and 3276800 inodes
Filesystem UUID: 8eadf68b-ed69-4dfe-948a-9fe297645142
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424
Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (65536 blocks): done
Writing superblocks and filesystem accounting information: done   
[root@2004arx varau]# 

	_______:  
[root@2004arx varau]# mkfs.exfat  -L  T1FS_P  /dev/sdb4
xfatprogs version : 1.1.2
Creating exFAT filesystem(/dev/sdb4, cluster size=131072)
Writing volume boot record: done
Writing backup volume boot record: done
Fat table creation: done
Allocation bitmap creation: done
Upcase table creation: done
Writing root directory entry: done
Synchronizing...
exFAT format complete!
[root@2004arx varau]# 

	_______:  
[u1@2004arx clonings_2004arx]$ lsblk1  /dev/sdb
NAME        FSTYPE FSVER LABEL     UUID                                 FSAVAIL FSUSE% MOUNTPOINTS   SIZE TYPE
/dev/sdb                                                                                           114.6G disk
├─/dev/sdb1                                                                                          100M part
├─/dev/sdb2 vfat   FAT32 ESP1      4361-3230                                                           3G part
├─/dev/sdb3 ext4   1.0   2004ARX_P 8eadf68b-ed69-4dfe-948a-9fe297645142                               50G part
└─/dev/sdb4 exfat  1.0   T1FS_P    F77F-C56E                                                        61.5G part
###################### cloning/rsync/copying of Parts ##############################################
-!!- you could try do the grub.install here, to check if it boots, before copying,... (but then need chroot for UEFI-boot,...)
  but copying does not take that long, so I do just first rsync .... :

	_______:  --
-! /boot and /T1 (sdb2 + sdb4) on src-system-attached-to-Lv13 (very fast):
	- reboot on src-sys ; login console : root :
	umount -a ;

	_______:  
	mount  -o ro /dev/sda2 /mnt/s1 ;
	mount   /dev/sdb2   /mnt/t1
	date;  rsync -a -AHXx  --delete  /mnt/s1/   /mnt/t1 ; date ;
	3sync  ; umount /mnt/s1 /mnt/t1 ; mountg sdb ; mountg sda ;

	_______:  
	mount  -o ro /dev/sda4 /mnt/s1 ;
	mount   /dev/sdb4   /mnt/t1
	date;  rsync -a -AHXx  --delete  /mnt/s1/   /mnt/t1 ; date ;
	3sync  ; umount /mnt/s1 /mnt/t1 ; mountg sdb ; mountg sda ;

	_______:  
- OS/System-part (/dev/sd3): booted from x13-arx1-sda9, then both USBs attached to x13 offline, and basically the same for sdb3:

	_______:  
	mount  -o ro /dev/sdb3 /mnt/s1 ;
	mount   /dev/sdc3   /mnt/t1
	date;  rsync -a -AHXx  --delete  /mnt/s1/   /mnt/t1 ; date ;
	cdlla /mnt/t1/ ; rmdir  dev proc  run sys  tmp /mnt/*  /media/*
	3sync  ; umount /mnt/s1 /mnt/t1 ; mountg sdb ; mountg sda ;

	_______:  rsync-cloning-syys, ca. 30 GB, 35 min, both attached to the USB3-Express-card !
	ArxWiki--Full system backup-rsnyc :  https://wiki.archlinux.org/title/Rsync#Full_system_backup :
	ArxWiki--Full-system-backup-rsnyc :       rsync -aAXHv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}  /src   /path/to/backup
 	ArxWiki--Full-system-backup-rsnyc-syys :  rsync -aAXHv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}  --delete  --exclude={"/VARUfs/*","/UUFS1/*","/boot/*"}  /mnt/s1/  /mnt/t1/ ;
	This approach works well for migrating an existing installation to a new hard drive or SSD.
##________________________________________  ___________________________


#####  ==========  configs-edits:

	_______:  fstab :
mount   /dev/sdc3   /mnt/t1
vide /mnt/t1/etc/fstab   ##---> UUIDs-adapts for all parts !
umount  /mnt/t1

	_______:  grub.cfg :
mount   /dev/sdc2   /mnt/t1
vide /mnt/t1/grub/grub.cfg   ##---> UUIDs-adapt !
umount  /mnt/t1
###################### grub-install , making hybrid bootable (BIOS + UEFI) #########################
-!! UEFI-booting worked WITHOUT any further works! so without following steps! just fine!! just try booting from Lv13-USB3 !
-!! MBR-booting more probelm!:
	- do NOT try on x13-USB2 ! just makes no sens! two slow and problems!
	- just try on x17 (one of its USB3-connectors boots properly). but needed just edit grub.cfg AND the following MBR-grub-install ! 
##________________________________________  ___________________________


#####  ==========  MBR /BIOS grub (bevor chroot! from real running system /OR check both from inside target-system, so after chroot !? see below nts) :
# mount /dev/sdb3  /mnt/tag1
# mount /dev/sdb2  /mnt/tag1/boot
# grub-install  --target=i386-pc  --recheck  --boot-directory=/mnt/tag1/boot    /dev/sdb  ##--!  --removable  !?!?  
# /OR just do UEFI-boot (works fine) and then there do: grub-install  --target=i386-pc  --recheck  --boot-directory=/boot    /dev/sdb  ;  ##--!  --removable  !?!?  
# /OR-after-chroot, from inside the target-system:
# grub-install  --target=i386-pc  --recheck  --boot-directory=/boot --removable   /dev/sdb  ##---> check if works !?
##________________________________________  ___________________________


#####  ==========  chroot :
# mount /dev/sdb3  /mnt/tag1
# cd   /mnt/tag1/
# mount -t proc /proc proc/
# mount --rbind /sys sys/
# mount --rbind /dev dev/
And optionally:
# mount --rbind /run run/
# if needed: vi ./etc/fstab  ##all ok?
# chroot  /mnt/tag1/  /bin/bash
# export PS1="(chroot) $PS1"
##________________________________________  ___________________________


#####  ==========  UEFI-grub (after chroot into the target-system):
grub-install  --target=x86_64-efi  --efi-directory=/boot  --boot-directory=/boot  --removable  --recheck
##________________________________________  ___________________________


#####  ==========  un-chroot /exit :
# ..... work done ...., then
When finished with the chroot, you can exit it via:
# exit
Then unmount the temporary file systems:
# cd /
# umount --recursive /location/of/new/root
##________________________________________  ___________________________


#####  ==========  verify:
- boot from Lv13-USB3
- boot from x17-usb3 /OR x13-usb for BIOS
-! also update/sync /boot/vmlinuz .... with x13: /boot_usb1/ for booting from x13-usb3.0 !
###################### __1END__ all ok! ############################################################
