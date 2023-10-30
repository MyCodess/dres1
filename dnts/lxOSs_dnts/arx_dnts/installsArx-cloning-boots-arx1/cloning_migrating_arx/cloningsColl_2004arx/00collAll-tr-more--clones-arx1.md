################# done-to-ub128_UltraFit_tinyHacken_SanDisk.txt #########################
##________________________________________  ___________________________


#####  ==========  
[root@2004arx clone0--ub128_01--2004arx_sdb3--SanDisk_UltraFit_tinyHacken]# date
2020-08-16T17:50:15 CEST
root@2004arx clone0--ub128_01--2004arx_sdb3--SanDisk_UltraFit_tinyHacken]# sgdisk  -p  /dev/sdb
Disk /dev/sdb: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 4E2AC71A-391A-44B7-ADBB-14BADB4D651F
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         6498303   3.0 GiB     EF00  EFI System
   3         6498304       111355903   50.0 GiB    8300  Linux filesystem
   4       111355904       240353246   61.5 GiB    0700  Microsoft basic data
[root@2004arx clone0--ub128_01--2004arx_sdb3--SanDisk_UltraFit_tinyHacken]# 
##________________________________________  ___________________________


#####  ==========  
########################################################################################################
########################################################################################################
##________________________________________  ___________________________


#####  ==========  20200731-191739 : ===============================
cloned fully neu again!! (formatted parts and rsync ....)
rsync -a -AHXx --delete /mnt/src1   /mnt/tag1 ##--..... and also /boot !! and also t1_BP on sda10 !!
- ONLY adapted /etc/fstab ! only / and T1fs_P adapted !
- grub-boot bzw. /etc/grub.cfg is still from ubuntu part! if needed, or ubuntu weg, then do it neu on arx-clone-part ! 
- still T1FS_P is noauto and from USB128-2004arx_RF-device but can be set tp sda10 !
- systg-stuff NOT-set/defined here! just manually comes to this DIR and systg is still from the source 2004arx_RF ...! basically quick but good clone1 !!
##________________________________________  ___________________________


#####  ==========  20200716-172642 : ===============================
2004arx_Cp/clone  manually copied/rsynced from 2004arx--on-usbStick-128%B  to here x13-sda9 to start it

	_______:  
##________________________________________  ___________________________


#####  ==========  
quick manuallly cloning of sourceSyss / 2004arx_usbStick_128GB  to newSyss / x13_sda9 , which workd fine an no problems !! so basically /roughly:
- mounts  sourceSyss:  /up1/media/syss4/  ,  newSyss / x13_sda9  :  /up1/media/syss5/  ; ##--was bootet from ubuntu /OR arx-iso-stick
- cp /OR-better rsync 2004arx_usbStick_128GB to x13_sda9  (--exclude "*packsvar*" ... all-big-stuff!)
	eg-ok:  date;  rsync -n  --delete -av   --exclude  "*00_1ONLY*"  --exclude  "*/packsvar/*"  --exclude  "*/.[cC]ache/*"  --exclude  "*/[cC]ache/*"   /up1/media/syss4/    /up1/media/syss5/ ; date;
- adapt /etc/fstab of newSyss / x13_sda9
- grub-mkconfig  [-o test-output-1.cfg ]non the newSyss / x13_sda9 ! /OR manually add grub-entry for the newSyss ! done!  

	_______:  
########################################################################################################
