__________ arx1-usb128-to-x13-cloning, ohne boot/grub/parting/....; booted from ubuntu, all parts/grub... were done! only new copys/syncs: _____
source1:  usb128  /dev/sdb
target1:  x13     /dev/sda9
boot/grub/... all already in ubuntu-x13 ! so not done here !
##________________________________________  ___________________________


#####  ==========  
Tue Apr 12 22:06:02 CEST 2022
mkfs.ext4  -L  2004ARX_P  -U dac2d4ce-28e3-4a5c-93de-1f7f227155d9  /dev/sda9  ##--!? -c , ...? ; here just the prev UUID uebernommen.
mount /dev/sda9  /mnt/t1
#- attache now _RF/source1 usb128 to x13
--OS-part sdb3 :
mount -o ro /dev/sdb3  /mnt/s1
date; cp -a /mnt/s1/   /mnt/t1/ ;date   ##--ca. 10-min/18-GB
mv /mnt/t1/s1/* /mnt/t1/ ; rmdir  /mnt/t1/s1/ ;
--boot-part sdb2 : (copy to  /mnt/t1/boot/ in x13-OS-Part!):
3sync  ; umount /mnt/s1 ;
mount   -o ro /dev/sdb2  /mnt/s1 ;
cp -a  /mnt/s1/*   /mnt/t1/boot/ ;
3sync  ; umount /mnt/s1 ; umount /mnt/t1 ;
--t1-part: 
mkfs.exfat  -n T1FS_P  -i  F1B6-F574  /dev/sda10
mount /dev/sda10  /mnt/t1
mount -o ro /dev/sdb4  /mnt/s1
date; cp -a /mnt/s1/t1_RF   /mnt/t1/ ;date  ##--ca. 12-min/23-GB
3sync ;  umount -v /mnt/t1 /mnt/s1 ;
-- edits/modifs :
mount -v /dev/sda9  /mnt/t1 ;
vi /mnt/t1/etc/fstab   ##--adapt UUIDs , and comment-OUT boot-part-mount ! by intHD-x13 boot-part now not needed (is copied to OS-part and is bootet from ubuntu for now!)
check in ubuntu /boot/grub/grub.cfg  all ok for sda9 ! (basically no edit needed; all without UUID but directly with /dev/sda9)
-- just check the source-filesystems:
fsck.ext4  -p -D -c -k -f -E optimize_extents  /dev/sdb3
...
######################## infos1-coll: ########################################
-- OS-System-Part  , /dev/sdb3 :
/dev/sda9        30G   18G   11G  62% /mnt/t1
/dev/sdb3        49G   18G   30G  37% /mnt/s1
-- T1Fs:
/dev/sda10       49G   23G   26G  47% /mnt/t1
/dev/sdb4        62G   23G   39G  37% /mnt/s1
