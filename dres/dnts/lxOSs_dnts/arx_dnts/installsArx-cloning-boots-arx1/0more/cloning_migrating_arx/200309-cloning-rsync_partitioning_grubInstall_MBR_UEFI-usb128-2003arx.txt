NOT-copied/synced DIRs:  VARUfs  and UUFS1
--!!  Protocol of cloning + bootloaging of 2004arx to new usbStick-128GB as 2004ARX_P_T (test)
both attached to asus14,
RF-ub128 as  /dev/sda
BP-ub128 as  /dev/sdb

	_______:  more docs for infos:
wiki.archlinux.org/index.php/Multiboot_USB_drive
- for infos also about system-cloning/migration see:
https://wiki.archlinux.org/index.php/Migrate_installation_to_new_hardware
https://wiki.archlinux.org/index.php/Migrating_between_architectures
##________________________________________  ___________________________


#####  ==========  
[root@2004arx ~]# fdisk -l
Disk /dev/nvme0n1: 476.96 GiB, 512110190592 bytes, 1000215216 sectors
Disk model: HFM512GDJTNG-8310A                      
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 01B31A07-C94C-5E44-AC57-17D16F90AC0B
Device             Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048     129023    126976    62M EFI System
/dev/nvme0n1p2    129024     131071      2048     1M BIOS boot
/dev/nvme0n1p3    131072  991825919 991694848 472.9G Linux root (x86-64)
/dev/nvme0n1p4 991825920 1000214527   8388608     4G Microsoft basic data
Disk /dev/sda: 114.62 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra Fit       
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 4E2AC71A-391A-44B7-ADBB-14BADB4D651F
Device         Start       End   Sectors  Size Type
/dev/sda1       2048    206847    204800  100M BIOS boot
/dev/sda2     206848   6498303   6291456    3G EFI System
/dev/sda3    6498304 111355903 104857600   50G Linux filesystem
/dev/sda4  111355904 240353246 128997343 61.5G Microsoft basic data
Disk /dev/sdb: 114.62 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra Fit       
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000
Device     Boot Start       End   Sectors   Size Id Type
/dev/sdb1          32 240353279 240353248 114.6G  c W95 FAT32 (LBA)
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# gdisk  /dev/sdb
GPT fdisk (gdisk) version 1.0.5
Partition table scan:
  MBR: MBR only
  BSD: not present
  APM: not present
  GPT: not present
***************************************************************
Found invalid GPT and valid MBR; converting MBR to GPT format
in memory. THIS OPERATION IS POTENTIALLY DESTRUCTIVE! Exit by
typing 'q' if you don't want to convert your MBR partitions
to GPT format!
***************************************************************
Warning! Main partition table overlaps the first partition by 2 blocks!
Try reducing the partition table size by 8 entries.
(Use the 's' item on the experts' menu.)
Warning! Secondary partition table overlaps the last partition by
33 blocks!
You will need to delete this partition or resize it in another utility.
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 50B14793-BC5B-4E2A-967F-242A92E81DD0
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 32-sector boundaries
Total free space is 0 sectors (0 bytes)
Number  Start (sector)    End (sector)  Size       Code  Name
   1              32       240353279   114.6 GiB   0700  Microsoft basic data
Command (? for help): d
Using 1
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 50B14793-BC5B-4E2A-967F-242A92E81DD0
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 32-sector boundaries
Total free space is 240353213 sectors (114.6 GiB)
Number  Start (sector)    End (sector)  Size       Code  Name
Command (? for help): w
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!
Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/sdb.
The operation has completed successfully.
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# gdisk  /dev/sdb
GPT fdisk (gdisk) version 1.0.5
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present
Found valid GPT with protective MBR; using GPT.
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 50B14793-BC5B-4E2A-967F-242A92E81DD0
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 240353213 sectors (114.6 GiB)
Number  Start (sector)    End (sector)  Size       Code  Name
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
Last sector (206848-240353246, default = 240353246) or {+-}size{KMGTP}: +4G
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): EF00
Changed type of partition to 'EFI system partition'
Command (? for help): n
Partition number (3-128, default 3): 
First sector (34-240353246, default = 8595456) or {+-}size{KMGTP}: 
Last sector (8595456-240353246, default = 240353246) or {+-}size{KMGTP}: +50G
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): 
Changed type of partition to 'Linux filesystem'
Command (? for help): n
Partition number (4-128, default 4): 
First sector (34-240353246, default = 113453056) or {+-}size{KMGTP}: 
Last sector (113453056-240353246, default = 240353246) or {+-}size{KMGTP}: 
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): 8700   ##---> _1kk: wrong! changed to 0700 !! see below!
Exact type match not found for type code 8700; assigning type code for
'Linux filesystem'
Changed type of partition to 'Linux filesystem'
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 50B14793-BC5B-4E2A-967F-242A92E81DD0
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         8595455   4.0 GiB     EF00  EFI system partition
   3         8595456       113453055   50.0 GiB    8300  Linux filesystem
   4       113453056       240353246   60.5 GiB    8300  Linux filesystem  ##---> _1kk: wrong! changed to 0700 !! see below!
Command (? for help): w
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!
Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/sdb.
The operation has completed successfully.
[root@2004arx ~]# 
[root@2004arx ~]# gdisk  /dev/sdb
GPT fdisk (gdisk) version 1.0.5
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present
Found valid GPT with protective MBR; using GPT.
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 50B14793-BC5B-4E2A-967F-242A92E81DD0
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         8595455   4.0 GiB     EF00  EFI system partition
   3         8595456       113453055   50.0 GiB    8300  Linux filesystem
   4       113453056       240353246   60.5 GiB    8300  Linux filesystem
Hex code or GUID (L to show codes, Enter = 8300): 0700
Changed type of partition to 'Microsoft basic data'
Command (? for help): p
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 50B14793-BC5B-4E2A-967F-242A92E81DD0
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         8595455   4.0 GiB     EF00  EFI system partition
   3         8595456       113453055   50.0 GiB    8300  Linux filesystem
   4       113453056       240353246   60.5 GiB    0700  Microsoft basic data
Command (? for help): w
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!
Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/sdb.
The operation has completed successfully.
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# mkfs.fat   -F32  -n ESP1     /dev/sdb2
mkfs.fat 4.1 (2017-01-24)
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# mkfs.ext4  -L  2004ARX_P_T     /dev/sdb3 
mke2fs 1.45.5 (07-Jan-2020)
Creating filesystem with 13107200 4k blocks and 3276800 inodes
Filesystem UUID: a0cac80d-195e-4fb8-a150-2e14eb214443
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424
Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (65536 blocks): done
Writing superblocks and filesystem accounting information: done   
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# mkfs.fat   -F32  -n T1FS_P   /dev/sdb4
mkfs.fat 4.1 (2017-01-24)
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# ll /mnt
total 8
drwxr-xr-x 2 root root 4096 2020-03-22 23:50 hd1/
drwxr-xr-x 2 root root 4096 2020-03-22 23:54 p4/
*[root@2004arx ~]# ll /mnt/*
/mnt/hd1:
total 0
/mnt/p4:
total 0
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# fdisk -l
Disk /dev/nvme0n1: 476.96 GiB, 512110190592 bytes, 1000215216 sectors
Disk model: HFM512GDJTNG-8310A                      
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 01B31A07-C94C-5E44-AC57-17D16F90AC0B
Device             Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048     129023    126976    62M EFI System
/dev/nvme0n1p2    129024     131071      2048     1M BIOS boot
/dev/nvme0n1p3    131072  991825919 991694848 472.9G Linux root (x86-64)
/dev/nvme0n1p4 991825920 1000214527   8388608     4G Microsoft basic data
Disk /dev/sda: 114.62 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra Fit       
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 4E2AC71A-391A-44B7-ADBB-14BADB4D651F
Device         Start       End   Sectors  Size Type
/dev/sda1       2048    206847    204800  100M BIOS boot
/dev/sda2     206848   6498303   6291456    3G EFI System
/dev/sda3    6498304 111355903 104857600   50G Linux filesystem
/dev/sda4  111355904 240353246 128997343 61.5G Microsoft basic data
Disk /dev/sdb: 114.62 GiB, 123060879360 bytes, 240353280 sectors
Disk model: Ultra Fit       
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 50B14793-BC5B-4E2A-967F-242A92E81DD0
Device         Start       End   Sectors  Size Type
/dev/sdb1       2048    206847    204800  100M BIOS boot
/dev/sdb2     206848   8595455   8388608    4G EFI System
/dev/sdb3    8595456 113453055 104857600   50G Linux filesystem
/dev/sdb4  113453056 240353246 126900191 60.5G Microsoft basic data
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# lla   /mnt/
hd1/ p4/  
[root@2004arx ~]# mount /dev/sdb3   /mnt/hd1
[root@2004arx ~]# lla /mnt/hd1
total 16
drwx------ 2 root root 16384 2020-03-28 20:59 lost+found/
[root@2004arx ~]# mkdir -P /mnt/hd1/boot
mkdir: invalid option -- 'P'
Try 'mkdir --help' for more information.
*[root@2004arx ~]# mkdir  /mnt/hd1/boot
[root@2004arx ~]# lla /mnt/hd1
total 20
drwxr-xr-x 2 root root  4096 2020-03-28 21:07 boot/
drwx------ 2 root root 16384 2020-03-28 20:59 lost+found/
*[root@2004arx ~]# lla /mnt/hd1/*
/mnt/hd1/boot:
total 0
/mnt/hd1/lost+found:
total 0
[root@2004arx ~]# mount   /dev/sdb2  /mnt/hd1/boot
[root@2004arx ~]# 
[root@2004arx ~]# grub-install  --target=i386-pc  --recheck  --boot-directory=/mnt/hd1/boot    /dev/sdb
Installing for i386-pc platform.
Installation finished. No error reported.
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# vi /mnt/hd1/00-BP-ub128-T2004Arx-flg-txt
[root@2004arx ~]# cpt /mnt/hd1/00-BP-ub128-T2004Arx-flg-txt  /mnt/hd1/boot/00-BP-ub128-T2004Arx-flg-txt
'/mnt/hd1/00-BP-ub128-T2004Arx-flg-txt' -> '/mnt/hd1/boot/00-BP-ub128-T2004Arx-flg-txt'
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# echo "=========== preparing chroot: =============="
##________________________________________  ___________________________


#####  ==========  preparing chroot: ==============
[root@2004arx ~]# 
[root@2004arx ~]# 
[root@2004arx ~]# cdlla 
total 68
drwxr-x---  6 root root  4096 2020-03-26 08:03 ./
drwxr-xr-x 20 root root  4096 2020-03-23 21:10 ../
drwx------  4 root root  4096 2020-03-25 21:06 .cache/
drwx------  5 root root  4096 2020-03-26 09:59 .config/
drwx------  3 root root  4096 2020-03-22 23:00 .gnupg/
drwxr-xr-x  3 root root  4096 2020-03-25 22:03 .local/
-rw-------  1 root root 17899 2020-03-28 20:39 .bash_history
-rw-------  1 root root    33 2020-03-26 08:03 .lesshst
lrwxrwxrwx  1 root root    35 2020-03-25 22:18 .profile2.sh -> /up1/.cuue/etc/users/profile2_m1.sh*
-rwxrwxrwx  1 root root    94 2020-03-25 04:58 s11.sh*
-rw-------  1 root root 11819 2020-03-24 22:53 .viminfo
/root
[root@2004arx ~]# cd -
/root
[root@2004arx ~]# cdlla /mnt/hd1/
total 32
drwxr-xr-x 4 root root  4096 2020-03-28 21:14 ./
drwxr-xr-x 4 root root  4096 2020-03-22 23:54 ../
drwxr-xr-x 3 root root  4096 1970-01-01 01:00 boot/
drwx------ 2 root root 16384 2020-03-28 20:59 lost+found/
-rw-r--r-- 1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
/mnt/hd1
[root@2004arx hd1]# mount -t proc /proc  proc/
mount: proc/: mount point does not exist.
[root@2004arx hd1]# ls /
00-arx2004-ub128_P3.flg.txt  boot  etc	 lib	lost+found  opt   root	sbin  sys  up1	UUFS1  VARUfs
bin			     dev   home  lib64	mnt	    proc  run	srv   tmp  usr	var
[root@2004arx hd1]# mkdir proc sys dev
*[root@2004arx hd1]# rmdir proc sys dev
[root@2004arx hd1]# lla
total 24
drwxr-xr-x 3 root root  4096 1970-01-01 01:00 boot/
drwx------ 2 root root 16384 2020-03-28 20:59 lost+found/
-rw-r--r-- 1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
[root@2004arx hd1]# mkdir proc sys dev
[root@2004arx hd1]# mount -t proc /proc  proc/
[root@2004arx hd1]# mount  --rbind /sys sys
*[root@2004arx hd1]# mount  --rbind /dev  dev
*[root@2004arx hd1]# mount  --rbind  /run  run
mount: run: mount point does not exist.
[root@2004arx hd1]# mkdir run
[root@2004arx hd1]# mount  --rbind  /run  run
[root@2004arx hd1]# 
[root@2004arx hd1]# 
[root@2004arx hd1]# chroot /mnt/hd1/  /bin/bash
chroot: failed to run command ‘/bin/bash’: No such file or directory
[root@2004arx hd1]# ll
total 24
drwxr-xr-x   3 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3560 2020-03-28 20:56 dev/
drwx------   2 root root 16384 2020-03-28 20:59 lost+found/
dr-xr-xr-x 291 root root     0 2020-03-28 16:38 proc/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
-rw-r--r--   1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
[root@2004arx hd1]# pwd
/mnt/hd1
[root@2004arx hd1]# ..
total 16
drwxr-xr-x  4 root root 4096 2020-03-22 23:54 ./
drwxr-xr-x 20 root root 4096 2020-03-23 21:10 ../
drwxr-xr-x  8 root root 4096 2020-03-28 21:23 hd1/
drwxr-xr-x  2 root root 4096 2020-03-22 23:54 p4/
/mnt
total 8.0K
drwxr-xr-x 8 root root 4.0K 2020-03-28 21:23 hd1/
drwxr-xr-x 2 root root 4.0K 2020-03-22 23:54 p4/
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# ll /
total 68
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 bin -> usr/bin/
drwxr-xr-x   4 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3560 2020-03-28 20:56 dev/
drwxr-xr-x  58 root root  4096 2020-03-28 12:07 etc/
drwxr-xr-x   7 root root  4096 2020-03-22 23:57 home/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib -> usr/lib/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib64 -> usr/lib/
drwx------   2 root root 16384 2020-03-22 21:53 lost+found/
drwxr-xr-x   4 root root  4096 2020-03-22 23:54 mnt/
drwxr-xr-x   3 root root  4096 2020-03-24 17:18 opt/
dr-xr-xr-x 291 root root     0 2020-03-28 16:38 proc/
drwxr-x---   6 root root  4096 2020-03-26 08:03 root/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 sbin -> usr/bin/
drwxr-xr-x   4 root root  4096 2020-03-22 23:00 srv/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
drwxrwxrwt  10 root root   300 2020-03-28 21:27 tmp/
drwxrwxr-x  12 u1   gu1   4096 2020-03-14 17:26 up1/
drwxr-xr-x   9 root root  4096 2020-03-28 12:01 usr/
drwxr-xr-x   2 m1   gm1   4096 2020-03-25 17:29 UUFS1/
drwxr-xr-x  12 root root  4096 2020-03-28 12:07 var/
drwxr-xr-x   3 u1   gu1   4096 2020-03-23 19:57 VARUfs/
[root@2004arx mnt]# rsync  -aAx   --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/up1","/VARUfs/*","/UUFS1/*"}   /   /mnt/hd1/
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# lla /mnt/hd1/
total 72
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 bin -> usr/bin/
drwxr-xr-x   3 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3560 2020-03-28 20:56 dev/
drwxr-xr-x  58 root root  4096 2020-03-28 12:07 etc/
drwxr-xr-x   7 root root  4096 2020-03-22 23:57 home/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib -> usr/lib/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib64 -> usr/lib/
drwx------   2 root root 16384 2020-03-28 20:59 lost+found/
drwxr-xr-x   2 root root  4096 2020-03-22 23:54 mnt/
drwxr-xr-x   3 root root  4096 2020-03-24 17:18 opt/
dr-xr-xr-x 289 root root     0 2020-03-28 16:38 proc/
drwxr-x---   6 root root  4096 2020-03-26 08:03 root/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 sbin -> usr/bin/
drwxr-xr-x   4 root root  4096 2020-03-22 23:00 srv/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
drwxrwxrwt   2 root root  4096 2020-03-28 21:27 tmp/
drwxr-xr-x   9 root root  4096 2020-03-28 12:01 usr/
drwxr-xr-x   2 m1   gm1   4096 2020-03-25 17:29 UUFS1/
drwxr-xr-x  12 root root  4096 2020-03-28 12:07 var/
drwxr-xr-x   2 u1   gu1   4096 2020-03-23 19:57 VARUfs/
-rw-r--r--   1 root root   136 2020-03-23 20:49 00-arx2004-ub128_P3.flg.txt
-rw-r--r--   1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# df -h
Filesystem      Size  Used Avail Use% Mounted on
dev             2.9G     0  2.9G   0% /dev
run             3.0G  1.1M  3.0G   1% /run
/dev/sda3        49G   21G   27G  44% /
tmpfs           3.0G   60M  2.9G   3% /dev/shm
tmpfs           3.0G     0  3.0G   0% /sys/fs/cgroup
tmpfs           3.0G   28K  3.0G   1% /tmp
/dev/sda4        62G  8.1G   54G  14% /up1/mnt/T1fs_loc
/dev/sda2       3.0G   60M  3.0G   2% /boot
tmpfs           595M   44K  595M   1% /run/user/1501
/dev/sdb3        49G  5.7G   41G  13% /mnt/hd1
/dev/sdb2       4.0G  7.6M  4.0G   1% /mnt/hd1/boot
*[root@2004arx mnt]# rm  /mnt/hd1/00-arx2004-ub128_P3.flg.txt
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# chroot /mnt/hd1/  /bin/bash
bash: /up1/.cuue/etc/profile.sh: No such file or directory
[root@2004arx /]# exit
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# 
[root@2004arx mnt]# chroot /mnt/hd1/  /bin/bash
##________________________________________  ___________________________


#####  ==========  start:  profile.sh
##________________________________________  ___________________________


#####  ==========  start:  profile_2004arx.sh
=---- end--:  profile_2004arx.sh
##________________________________________  ___________________________


#####  ==========  start:  const.sh
=---- end--:  const.sh
##________________________________________  ___________________________


#####  ==========  start:  pathes.sh
=---- end--:  pathes.sh
##________________________________________  ___________________________


#####  ==========  start:  aliases.sh
=---- end--:  aliases.sh
##________________________________________  ___________________________


#####  ==========  start:  funcs1.sh
=---- end--:  funcs1.sh
##________________________________________  ___________________________


#####  ==========  start:  funcs2.sh
=---- end--:  funcs2.sh
##________________________________________  ___________________________


#####  ==========  start:  prj0Prof.sh
##________________________________________  ___________________________


#####  ==========  start:  prjArx1Prof.sh
=---- end--:  prjArx1Prof.sh
=---- end--:  prj0Prof.sh
##________________________________________  ___________________________


#####  ==========  start:  .profile2.sh
##________________________________________  ___________________________


#####  ==========  start:  .profile2.sh
=---- end--:  profile.sh
[root@2004arx /]# export PS1="chrt-- $PS1 "
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  lla /
total 72
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 bin -> usr/bin/
drwxr-xr-x   3 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3620 2020-03-28 22:06 dev/
drwxr-xr-x  58 root root  4096 2020-03-28 12:07 etc/
drwxr-xr-x   7 root root  4096 2020-03-22 23:57 home/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib -> usr/lib/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib64 -> usr/lib/
drwx------   2 root root 16384 2020-03-28 20:59 lost+found/
drwxr-xr-x   2 root root  4096 2020-03-22 23:54 mnt/
drwxr-xr-x   3 root root  4096 2020-03-24 17:18 opt/
dr-xr-xr-x 295 root root     0 2020-03-28 16:38 proc/
drwxr-x---   6 root root  4096 2020-03-26 08:03 root/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 sbin -> usr/bin/
drwxr-xr-x   4 root root  4096 2020-03-22 23:00 srv/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
drwxrwxrwt   2 root root  4096 2020-03-28 21:27 tmp/
drwxrwxr-x  12 u1   gu1   4096 2020-03-14 17:26 up1/
drwxr-xr-x   9 root root  4096 2020-03-28 12:01 usr/
drwxr-xr-x   2 m1   gm1   4096 2020-03-25 17:29 UUFS1/
drwxr-xr-x  12 root root  4096 2020-03-28 12:07 var/
drwxr-xr-x   2 u1   gu1   4096 2020-03-23 19:57 VARUfs/
-rw-r--r--   1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
chrt-- [root@2004arx /]#  lla /boot
total 8
drwxr-xr-x 5 root root 4096 2020-03-28 21:11 grub/
-rwxr-xr-x 1 root root   34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
*chrt-- [root@2004arx /]#  lla /boot/grub/
total 32
drwxr-xr-x 2 root root  4096 2020-03-28 21:11 fonts/
drwxr-xr-x 2 root root 20480 2020-03-28 21:11 i386-pc/
drwxr-xr-x 3 root root  4096 2020-03-28 21:11 themes/
-rwxr-xr-x 1 root root  1024 2020-03-28 21:11 grubenv
chrt-- [root@2004arx /]#  grub-install  --target=i386-pc     --boot-directory=/boot  /dev/sdb
Installing for i386-pc platform.
Installation finished. No error reported.
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  grub-install  --target=x86_64-efi  --efi-directory=/boot  --boot-directory=/boot  --removable  --recheck 
Installing for x86_64-efi platform.
Installation finished. No error reported.
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  
chrt-- [root@2004arx /]#  lsblk
lsblk   lsblk1  
chrt-- [root@2004arx /]#  lsblk1
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT UUID                                 LABEL
sda           8:0    1 114.6G  0 disk                                                 
├─sda1        8:1    1   100M  0 part                                                 
├─sda2        8:2    1     3G  0 part            030B-13D8                            ESP1
├─sda3        8:3    1    50G  0 part            926f6c1f-95fb-4dcf-9866-e43edfc6206a 2004ARX_P
└─sda4        8:4    1  61.5G  0 part            1663-054C                            T1FS_P
sdb           8:16   1 114.6G  0 disk                                                 
├─sdb1        8:17   1   100M  0 part                                                 
├─sdb2        8:18   1     4G  0 part /boot      C44C-7F7A                            ESP1
├─sdb3        8:19   1    50G  0 part /          a0cac80d-195e-4fb8-a150-2e14eb214443 2004ARX_P_T
└─sdb4        8:20   1  60.5G  0 part            CD39-AE7F                            T1FS_P
nvme0n1     259:0    0   477G  0 disk                                                 
├─nvme0n1p1 259:1    0    62M  0 part            51E9-7831                            
├─nvme0n1p2 259:2    0     1M  0 part                                                 
├─nvme0n1p3 259:3    0 472.9G  0 part            07da0d46-519a-4b82-9d2a-9cfd9b67d18b ostree
└─nvme0n1p4 259:4    0     4G  0 part            FA3CB0F03CB0A951                     DRIVERS
chrt-- [root@2004arx /]#  ll
total 72
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 bin -> usr/bin/
drwxr-xr-x   4 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3620 2020-03-28 22:06 dev/
drwxr-xr-x  58 root root  4096 2020-03-28 12:07 etc/
drwxr-xr-x   7 root root  4096 2020-03-22 23:57 home/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib -> usr/lib/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib64 -> usr/lib/
drwx------   2 root root 16384 2020-03-28 20:59 lost+found/
drwxr-xr-x   2 root root  4096 2020-03-22 23:54 mnt/
drwxr-xr-x   3 root root  4096 2020-03-24 17:18 opt/
dr-xr-xr-x 295 root root     0 2020-03-28 16:38 proc/
drwxr-x---   6 root root  4096 2020-03-26 08:03 root/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 sbin -> usr/bin/
drwxr-xr-x   4 root root  4096 2020-03-22 23:00 srv/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
drwxrwxrwt   2 root root  4096 2020-03-28 21:27 tmp/
drwxrwxr-x  12 u1   gu1   4096 2020-03-14 17:26 up1/
drwxr-xr-x   9 root root  4096 2020-03-28 12:01 usr/
drwxr-xr-x   2 m1   gm1   4096 2020-03-25 17:29 UUFS1/
drwxr-xr-x  12 root root  4096 2020-03-28 12:07 var/
drwxr-xr-x   2 u1   gu1   4096 2020-03-23 19:57 VARUfs/
-rw-r--r--   1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
chrt-- [root@2004arx /]#  ll /etc/fstab*
-rw-r--r-- 1 root root 3407 2020-03-23 20:41 /etc/fstab
chrt-- [root@2004arx /]#  viorg1 /etc/fstab
-rw-r--r-- 1 root root 3407 Mar 23 20:41 /etc/fstab
==== backup-to:  /etc/fstab-200328_1org , continue editing /etc/fstab ? Enter or Ctrl-C  ?
-rw-r--r-- 1 root root 4040 Mar 28 22:25 /etc/fstab
-rw-r--r-- 1 root root 3407 Mar 23 20:41 /etc/fstab-200328_1org
chrt-- [root@2004arx /]#  ll
total 72
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 bin -> usr/bin/
drwxr-xr-x   4 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3620 2020-03-28 22:06 dev/
drwxr-xr-x  58 root root  4096 2020-03-28 22:25 etc/
drwxr-xr-x   7 root root  4096 2020-03-22 23:57 home/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib -> usr/lib/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib64 -> usr/lib/
drwx------   2 root root 16384 2020-03-28 20:59 lost+found/
drwxr-xr-x   2 root root  4096 2020-03-22 23:54 mnt/
drwxr-xr-x   3 root root  4096 2020-03-24 17:18 opt/
dr-xr-xr-x 295 root root     0 2020-03-28 16:38 proc/
drwxr-x---   6 root root  4096 2020-03-26 08:03 root/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 sbin -> usr/bin/
drwxr-xr-x   4 root root  4096 2020-03-22 23:00 srv/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
drwxrwxrwt   2 root root  4096 2020-03-28 22:25 tmp/
drwxrwxr-x  12 u1   gu1   4096 2020-03-14 17:26 up1/
drwxr-xr-x   9 root root  4096 2020-03-28 12:01 usr/
drwxr-xr-x   2 m1   gm1   4096 2020-03-25 17:29 UUFS1/
drwxr-xr-x  12 root root  4096 2020-03-28 12:07 var/
drwxr-xr-x   2 u1   gu1   4096 2020-03-23 19:57 VARUfs/
-rw-r--r--   1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
chrt-- [root@2004arx /]#  ll /
total 72
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 bin -> usr/bin/
drwxr-xr-x   4 root root  4096 1970-01-01 01:00 boot/
drwxr-xr-x  20 root root  3620 2020-03-28 22:06 dev/
drwxr-xr-x  58 root root  4096 2020-03-28 22:25 etc/
drwxr-xr-x   7 root root  4096 2020-03-22 23:57 home/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib -> usr/lib/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 lib64 -> usr/lib/
drwx------   2 root root 16384 2020-03-28 20:59 lost+found/
drwxr-xr-x   2 root root  4096 2020-03-22 23:54 mnt/
drwxr-xr-x   3 root root  4096 2020-03-24 17:18 opt/
dr-xr-xr-x 295 root root     0 2020-03-28 16:38 proc/
drwxr-x---   6 root root  4096 2020-03-26 08:03 root/
drwxr-xr-x  21 root root   600 2020-03-28 20:27 run/
lrwxrwxrwx   1 root root     7 2019-11-13 17:23 sbin -> usr/bin/
drwxr-xr-x   4 root root  4096 2020-03-22 23:00 srv/
dr-xr-xr-x  13 root root     0 2020-03-28 16:38 sys/
drwxrwxrwt   2 root root  4096 2020-03-28 22:25 tmp/
drwxrwxr-x  12 u1   gu1   4096 2020-03-14 17:26 up1/
drwxr-xr-x   9 root root  4096 2020-03-28 12:01 usr/
drwxr-xr-x   2 m1   gm1   4096 2020-03-25 17:29 UUFS1/
drwxr-xr-x  12 root root  4096 2020-03-28 12:07 var/
drwxr-xr-x   2 u1   gu1   4096 2020-03-23 19:57 VARUfs/
-rw-r--r--   1 root root    34 2020-03-28 21:14 00-BP-ub128-T2004Arx-flg-txt
chrt-- [root@2004arx /]#  vi 00-BP-ub128-T2004Arx-flg-txt 
chrt-- [root@2004arx /]#  
