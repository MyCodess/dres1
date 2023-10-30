___________ clone-arx1: usb-to-usb--both-attached-to-x13-ubuntu, NO-DISK/PARTS-configs! already there ! 2021-09-01 : _________________
##________________________________________  ___________________________


#####  ==========  arx1-whole-stick-clone3--ub128_ultraBiggerBlackSandisk/
- both sticks attached to x13-usb3card, bootet from x13-arx1-sda9,
- dest/target:  /dev/sdb , ub128_ultraBiggerBlackSandisk
- source/_RF:   /dev/sdc , ub128--2004arx_sdb3--SanDisk_UltraFit_tinyHacken/
- the partitions on target-usb were already there! so hier NO-new-partitioning!
--####################### 1coll-protocoll : ###################################
[root@2004arx varau]# fdisk -l
Disk /dev/sda: 465.76 GiB, 500107862016 bytes, 976773168 sectors
Disk model: ST9500325AS     
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xa865c365
Device     Boot     Start       End   Sectors   Size Id Type
/dev/sda1  *         2048  62916607  62914560    30G  7 HPFS/NTFS/exFAT
/dev/sda2        62916608 127928319  65011712    31G  7 HPFS/NTFS/exFAT
/dev/sda3       127928320 547768319 419840000 200.2G  7 HPFS/NTFS/exFAT
/dev/sda4       547770366 976771071 429000706 204.6G  f W95 Ext'd (LBA)
/dev/sda5       547770368 611258367  63488000  30.3G 83 Linux
/dev/sda6       611260416 619657215   8396800     4G 82 Linux swap / Solaris
/dev/sda7       619659264 685195263  65536000  31.3G 83 Linux
/dev/sda8       685197312 812173311 126976000  60.5G 83 Linux
/dev/sda9       812175360 875089919  62914560    30G 83 Linux
/dev/sda10      875091968 976771071 101679104  48.5G 83 Linux
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device        Start       End   Sectors  Size Type
/dev/sdb1      2048    206847    204800  100M BIOS boot
/dev/sdb2    206848   8595455   8388608    4G EFI System
/dev/sdb3   8595456  61063167  52467712   25G Linux filesystem
/dev/sdb4  61063168  63160319   2097152    1G Linux filesystem
/dev/sdb5  63160320 240351231 177190912 84.5G Linux filesystem
*[root@2004arx varau]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.36.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device        Start       End   Sectors  Size Type
/dev/sdb1      2048    206847    204800  100M BIOS boot
/dev/sdb2    206848   8595455   8388608    4G EFI System
/dev/sdb3   8595456  61063167  52467712   25G Linux filesystem
/dev/sdb4  61063168  63160319   2097152    1G Linux filesystem
/dev/sdb5  63160320 240351231 177190912 84.5G Linux filesystem
Command (m for help): d
Partition number (1-5, default 5): 
Partition 5 has been deleted.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device        Start      End  Sectors  Size Type
/dev/sdb1      2048   206847   204800  100M BIOS boot
/dev/sdb2    206848  8595455  8388608    4G EFI System
/dev/sdb3   8595456 61063167 52467712   25G Linux filesystem
/dev/sdb4  61063168 63160319  2097152    1G Linux filesystem
Command (m for help): d
Partition number (1-4, default 4): 
Partition 4 has been deleted.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device       Start      End  Sectors  Size Type
/dev/sdb1     2048   206847   204800  100M BIOS boot
/dev/sdb2   206848  8595455  8388608    4G EFI System
/dev/sdb3  8595456 61063167 52467712   25G Linux filesystem
Command (m for help): d
Partition number (1-3, default 3): 
Partition 3 has been deleted.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device      Start     End Sectors  Size Type
/dev/sdb1    2048  206847  204800  100M BIOS boot
/dev/sdb2  206848 8595455 8388608    4G EFI System
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx varau]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.36.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device      Start     End Sectors  Size Type
/dev/sdb1    2048  206847  204800  100M BIOS boot
/dev/sdb2  206848 8595455 8388608    4G EFI System
Command (m for help): n
Partition number (3-128, default 3): 
First sector (8595456-240353246, default 8595456): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (8595456-240353246, default 240353246): +50G
Created a new partition 3 of type 'Linux filesystem' and of size 50 GiB.
Partition #3 contains a ext4 signature.
Do you want to remove the signature? [Y]es/[N]o: p
Do you want to remove the signature? [Y]es/[N]o: Y
The signature will be removed by a write command.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device       Start       End   Sectors  Size Type
/dev/sdb1     2048    206847    204800  100M BIOS boot
/dev/sdb2   206848   8595455   8388608    4G EFI System
/dev/sdb3  8595456 113453055 104857600   50G Linux filesystem
Filesystem/RAID signature on partition 3 will be wiped.
Command (m for help): n
Partition number (4-128, default 4): 
First sector (113453056-240353246, default 113453056): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (113453056-240353246, default 240353246): 
Created a new partition 4 of type 'Linux filesystem' and of size 60.5 GiB.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device         Start       End   Sectors  Size Type
/dev/sdb1       2048    206847    204800  100M BIOS boot
/dev/sdb2     206848   8595455   8388608    4G EFI System
/dev/sdb3    8595456 113453055 104857600   50G Linux filesystem
/dev/sdb4  113453056 240353246 126900191 60.5G Linux filesystem
Filesystem/RAID signature on partition 3 will be wiped.
Changed type of partition 'Linux filesystem' to 'Microsoft basic data'.
Command (m for help): p
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device         Start       End   Sectors  Size Type
/dev/sdb1       2048    206847    204800  100M BIOS boot
/dev/sdb2     206848   8595455   8388608    4G EFI System
/dev/sdb3    8595456 113453055 104857600   50G Linux filesystem
/dev/sdb4  113453056 240353246 126900191 60.5G Microsoft basic data
Filesystem/RAID signature on partition 3 will be wiped.
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
[root@2004arx varau]# mkfs.vfat -n ESP1  /dev/sdb2
mkfs.fat 4.2 (2021-01-31)
[root@2004arx varau]# mkfs.ext4 -L 2004ARX_P  /dev/sdb3
mke2fs 1.46.2 (28-Feb-2021)
Creating filesystem with 13107200 4k blocks and 3276800 inodes
Filesystem UUID: 80bbc6dc-623f-4ec4-aa67-d9c37e40c4a5
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424
Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (65536 blocks): done
Writing superblocks and filesystem accounting information: done   
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx varau]# mkfs.ex
mkfs.exfat  mkfs.ext2   mkfs.ext3   mkfs.ext4   
*[root@2004arx varau]# mkfs.exfat -L T1FS_P  /dev/sdb4
exfatprogs version : 1.1.1
Creating exFAT filesystem(/dev/sdb4, cluster size=131072)
Writing volume boot record: done
Writing backup volume boot record: done
Fat table creation: done
Allocation bitmap creation: done
Upcase table creation: done
Writing root directory entry: done
Synchronizing...
exFAT format complete!
[root@2004arx varau]# fdisk -l /dev/sdb
Disk /dev/sdb: 114.61 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra           
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 53316C42-96EB-450B-8D53-E0CEAEE762EE
Device         Start       End   Sectors  Size Type
/dev/sdb1       2048    206847    204800  100M BIOS boot
/dev/sdb2     206848   8595455   8388608    4G EFI System
/dev/sdb3    8595456 113453055 104857600   50G Linux filesystem
/dev/sdb4  113453056 240353246 126900191 60.5G Microsoft basic data
*[root@2004arx varau]# sgdisk -l /dev/sdb
*[root@2004arx varau]# gdisk -l /dev/sdb
GPT fdisk (gdisk) version 1.0.7
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present
Found valid GPT with protective MBR; using GPT.
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
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
[root@2004arx varau]# 
[root@2004arx varau]# 
[root@2004arx mnt]# mount /dev/sdb2 /mnt/t1
[root@2004arx mnt]# 
[root@2004arx mnt]# mount  -o ro /dev/sdc2   /mnt/s1
[root@2004arx mnt]# ll /mnt/s1/
amd-ucode.img                 grub/                         initramfs-linux.img           vmlinuz-linux                 
EFI/                          initramfs-linux-fallback.img  intel-ucode.img               
[root@2004arx mnt]# vi /mnt/s1/t1
[root@2004arx mnt]# date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date 
2021-09-01T14:47:18 CEST
2021-09-01T14:47:20 CEST
*[root@2004arx mnt]# date  ;  cp -a /mnt/s1/ -t  /mnt/t1/ ; date 
2021-09-01T14:48:23 CEST
2021-09-01T14:48:23 CEST
*[root@2004arx mnt]# date  ;  cp -a -t /mnt/s1/   /mnt/t1/ ; date 
2021-09-01T14:48:54 CEST
cp: cannot create directory '/mnt/s1/t1': Read-only file system
2021-09-01T14:48:54 CEST
[root@2004arx mnt]# date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date 
2021-09-01T14:49:17 CEST
2021-09-01T14:49:18 CEST
[root@2004arx mnt]# mv /mnt/t1/s1/* /mnt/t1/
[root@2004arx mnt]# rmdr /mnt/t1/s1/
bash: rmdr: command not found
*[root@2004arx mnt]# rmdir /mnt/t1/s1/
[root@2004arx mnt]# df -h /mnt/t1/
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb2       4.0G   69M  4.0G   2% /mnt/t1
[root@2004arx mnt]# 3sync 
[root@2004arx mnt]# 3sync 
[root@2004arx mnt]# 3sync 
[root@2004arx mnt]# umount /mnt/t1
*[root@2004arx mnt]# umount /mnt/s1
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# echoline1da
echoline1date     echoline1dateend  
[root@2004arx mnt]# echoline1dateend "__1END__  /dev/sdb2 , EFI1"
##________________________________________  ___________________________


#####  ==========  __1END__ 20210901-145208 ============__________
[root@2004arx mnt]# 
*[root@2004arx mnt]# mount /dev/sdb3 /mnt/t1
*[root@2004arx mnt]# 
*[root@2004arx mnt]# mount  -o ro /dev/sdc3   /mnt/s1
[root@2004arx mnt]# df -h /mnt/s1
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc3        49G   26G   21G  56% /mnt/s1
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date 
2021-09-01T14:55:59 CEST
2021-09-01T15:12:41 CEST
[root@2004arx mnt]# 
[root@2004arx mnt]# 3sync 
*[root@2004arx mnt]# echoline1dateend "__1END__  /dev/sdb3 , arx1-part"
##________________________________________  ___________________________


#####  ==========  __1END__ 20210901-151716 ============__________
[root@2004arx mnt]# 
[root@2004arx mnt]# mv /mnt/t1/
lost+found/ s1/         
[root@2004arx mnt]# rmdir /mnt/t1/lost+found/
[root@2004arx mnt]# mvi /mnt/t1/s1/*  /mnt/t1/
[root@2004arx mnt]# df -h   /mnt/s1/  /mnt/t1/
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc3        49G   26G   21G  56% /mnt/s1
/dev/sdb3        49G   26G   21G  56% /mnt/t1
[root@2004arx mnt]# 
*[root@2004arx mnt]# df    /mnt/s1/  /mnt/t1/
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/sdc3       51343840 26913064  21792952  56% /mnt/s1
/dev/sdb3       51290592 26858628  21794140  56% /mnt/t1
[root@2004arx mnt]# cd
*[root@2004arx ~]# umount   /mnt/s1/  /mnt/t1/
[root@2004arx ~]# 3sync 
[root@2004arx ~]# mountg sdb
*[root@2004arx ~]# mountg sdc
*[root@2004arx ~]# echoline1dateend "__1END__  /dev/sdb3 , arx1-part--pos-works"
##________________________________________  ___________________________


#####  ==========  __1END__ 20210901-152338 ============__________
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
*[root@2004arx ~]# mount /dev/sdb4 /mnt/t1
*[root@2004arx ~]# mount  -o ro /dev/sdc4   /mnt/s1
[root@2004arx ~]# date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date 
2021-09-01T15:25:32 CEST
2021-09-01T15:44:37 CEST
[root@2004arx ~]# 
[root@2004arx ~]# mvi /mnt/t1/s1/*  /mnt/t1/
renamed '/mnt/t1/s1/System Volume Information' -> '/mnt/t1/System Volume Information'
renamed '/mnt/t1/s1/t1_RF' -> '/mnt/t1/t1_RF'
[root@2004arx ~]# df    /mnt/s1/  /mnt/t1/
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/sdc4       64495488 29283456  35212032  46% /mnt/s1
/dev/sdb4       63446912 29283584  34163328  47% /mnt/t1
[root@2004arx ~]# df -h   /mnt/s1/  /mnt/t1/
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc4        62G   28G   34G  46% /mnt/s1
/dev/sdb4        61G   28G   33G  47% /mnt/t1
[root@2004arx ~]# 3sync 
[root@2004arx ~]# 3sync 
*[root@2004arx ~]# echoline1dateend "__1END__  /dev/sdb4 , T1-part"
##________________________________________  ___________________________


#####  ==========  __1END__ 20210901-172350 ============__________

	_______:  > edit /ect/fstab for UUIDs (and if needed grub.cfg), it they are UUID-based ! (if label-based, then nothing)
##________________________________________  ___________________________


#####  ==========  
