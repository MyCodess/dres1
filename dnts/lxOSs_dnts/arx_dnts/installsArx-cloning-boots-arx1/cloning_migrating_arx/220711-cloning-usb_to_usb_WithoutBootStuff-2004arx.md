##________________________________________  ___________________________


#####  ==========  /_220711 :  arx-clone, USB128-to-usb128, attached to x13-arx1
new target:	/dev/sdb
source_RF:	/dev/sdc
both attached to x13-arx1--USB3_card
target was already ready partitioned and bootable! so only cp -a ...; (also OS-part was already formatted with mkfs.ext4 -cc ... !)

	_______:  
- target  /new:
/dev/sdb                                                                                                  114.6G disk
├─/dev/sdb1                                                                                                 100M part
├─/dev/sdb2  vfat   FAT32 ESP1        803D-FE47                                                               3G part
├─/dev/sdb3  ext4   1.0   2004ARX_P   4f332637-b304-4fbb-853d-68073ee4bdd9                                   50G part
└─/dev/sdb4  exfat  1.0   T1FS_P      EBFE-7889                                                            61.5G part
- source_RF /old:
/dev/sdc                                                                                                  114.6G disk
├─/dev/sdc1                                                                                                 100M part
├─/dev/sdc2  vfat   FAT32 ESP1        4361-3230                                                               3G part
├─/dev/sdc3  ext4   1.0   2004ARX_P   8eadf68b-ed69-4dfe-948a-9fe297645142                                   50G part
└─/dev/sdc4  exfat  1.0   T1FS_P      F77F-C56E                                                            61.5G part
/dev/sr0                                                                                                   1024M rom
##________________________________________  ___________________________


#####  ==========  mkfs of new target: (extra vorher gemacht! ready!)
date;  mkfs.ext4  -L  2004ARX_P   -v  -cc  /dev/sdb3  ; date  ##--ca. 5 hours with -cc !
mkfs.vfat   -v -c  -n ESP1 /dev/sdb2
mkfs.exfat  -L  T1FS_P  /dev/sdb4
##________________________________________  ___________________________


#####  ==========  cp
########## boot-part:
mount        /dev/sdb2   /mnt/t1
mount  -o ro /dev/sdc2   /mnt/s1
date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date
2022-07-11T21:37:52 CEST
2022-07-11T21:37:55 CEST
[root@2004arx varau]# mv /mnt/t1/s1/* /mnt/t1/
[root@2004arx varau]# rmdir /mnt/t1/s1/
3sync;
umount  /mnt/t1  /mnt/s1
echoline1dateend "__1END__  /dev/sdb2 , boot-part"
########## OS-part:
mount        /dev/sdb3   /mnt/t1
mount  -o ro /dev/sdc3   /mnt/s1
[root@2004arx varau]# df -h /mnt/s1
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc3        49G   23G   25G  48% /mnt/s1
[root@2004arx varau]# date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date
2022-07-11T21:46:48 CEST
2022-07-11T22:23:09 CEST
[root@2004arx varau]# mv /mnt/t1/s1/* /mnt/t1/
[root@2004arx varau]# rmdir /mnt/t1/s1/
#  rm old flag-files/thisMedia ... in  /mnt/t1/
3sync;
umount  /mnt/t1  /mnt/s1
mountg sdb; mountg sdc;
echoline1dateend "__1END__  /dev/sdb3 , OS/arx1-part"
########## T1FS-part:
mount        /dev/sdb4   /mnt/t1
mount  -o ro /dev/sdc4   /mnt/s1
[root@2004arx varau]#  df -h /mnt/s1
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc4        62G   24G   39G  38% /mnt/s1
[root@2004arx varau]# date  ;  cp -a /mnt/s1/   /mnt/t1/ ; date
2022-07-11T22:34:55 CEST
2022-07-11T23:12:43 CEST
[root@2004arx varau]# mv /mnt/t1/s1/* /mnt/t1/
[root@2004arx varau]# rmdir /mnt/t1/s1/
3sync;
umount  /mnt/t1  /mnt/s1
mountg sdb; mountg sdc;
echoline1dateend "__1END__  /dev/sdb3 , T1FS-part"
##________________________________________  ___________________________


#####  ==========  edits:  grub.cfg + fstab  /_220712 :
##---- fstab:
mount /dev/sdb3  /mnt/t1
cd   /mnt/t1/etc/ ;  cpde /mnt/t1/etc/fstab
##-  vi  /mnt/t1/etc/fstab
sed  -i  -e "s@4361-3230@803D-FE47@g"  -e "s@8eadf68b-ed69-4dfe-948a-9fe297645142@4f332637-b304-4fbb-853d-68073ee4bdd9@g"  -e "s@F77F-C56E@EBFE-7889@g"  /mnt/t1/etc/fstab
##-  gvimdiff /mnt/t1/etc/fstab  /mnt/t1/etc/fstab-$($cuds)
##---- grubs:
mount /dev/sdb2  /mnt/t2
cpde /mnt/t2/grub/grub.cfg
sed  -i  -e "s@4361-3230@803D-FE47@g"  -e "s@8eadf68b-ed69-4dfe-948a-9fe297645142@4f332637-b304-4fbb-853d-68073ee4bdd9@g"  -e "s@F77F-C56E@EBFE-7889@g"    /mnt/t2/grub/grub.cfg
##-  gvimdiff  /mnt/t2/grub/grub.cfg  /mnt/t2/grub/grub.cfg-$($cuds)
