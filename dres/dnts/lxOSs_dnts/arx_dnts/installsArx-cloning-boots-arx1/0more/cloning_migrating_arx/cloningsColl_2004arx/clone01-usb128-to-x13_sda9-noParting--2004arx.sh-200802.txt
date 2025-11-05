_______________ clone1-2004arx _______________________________
- cloning arx1 from USB to x13-part , NOT-including-DISK/PARTS/GrubBoot (already there, from x13-Ubuntu)
##________________________________________  ___________________________


#####  ==========  ub128_stick-biggerBlackUltra to x13-sda9 : ===========================================
##--bootet from x13-ubuntu, and syncing  ub128-arx_RF (/mnt/src1/)  to  x13-sda9_clone1 (/mnt/tag1/) :
root@x13:~# date
Sun Aug  2 14:21:12 CEST 2020
##________________________________________  ___________________________


#####  ==========  sdb is RF-arx-stick , sda9-x13 is target-clone1 :
root@x13:~# lsblk1
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT        UUID                                 LABEL       FSTYPE
loop0     7:0    0  17.9M  1 loop /snap/pdftk/9                                                      squashfs
loop1     7:1    0  91.4M  1 loop /snap/core/8689                                                    squashfs
loop2     7:2    0  91.3M  1 loop /snap/core/8592                                                    squashfs
sda       8:0    0 465.8G  0 disk
├─sda1    8:1    0    30G  0 part                   48DD9E56472C8BAE                     Win7a-P1-RF ntfs
├─sda2    8:2    0    31G  0 part                   1672033972031D5D                     Win7b-P2    ntfs
├─sda3    8:3    0 200.2G  0 part /up1/mnt/T1fs_loc 10F4D336F4D31CB2                     T1fs_loc    ntfs
├─sda4    8:4    0     1K  0 part
├─sda5    8:5    0  30.3G  0 part /                 719f3a44-e822-4a66-aa88-b80a487faba5 OS-1503ubt  ext4
├─sda6    8:6    0     4G  0 part [SWAP]            7ffd302a-5d78-4a33-89b6-3334e6762a25             swap
├─sda7    8:7    0  31.3G  0 part /up1/mnt/UUFS1    b207ea1d-9312-4d70-898b-a918cd87e9dd UUFS1       ext4
├─sda8    8:8    0  60.6G  0 part /up1/mnt/VARUfs   1fb4a232-4ecf-4a78-999e-72f264448c08 VARUfs      ext4
├─sda9    8:9    0    30G  0 part /mnt/tag1         98788e2f-43c5-46e7-a0ec-9fd241f2d24d 2004ARX_P   ext4
└─sda10   8:10   0  48.5G  0 part                   85D4-C4AA                            T1FS_P      vfat
sdb       8:16   1 114.6G  0 disk
├─sdb1    8:17   1   100M  0 part
├─sdb2    8:18   1     4G  0 part                   59D3-23F6                            ESP1        vfat
├─sdb3    8:19   1    50G  0 part                   c09f873a-eae7-4e88-8b91-fe4d27212ae3 2004ARX_P   ext4
└─sdb4    8:20   1  60.5G  0 part                   603C-FB25                            T1FS_P      vfat
sr0      11:0    1  1024M  0 rom
##________________________________________  ___________________________


#####  ==========  rsyncs:

	_______:  sdb3 : root-arx-rf:
root@x13:~# mount -o ro  /dev/sdb3   /mnt/src1
root@x13:~# mount        /dev/sda9   /mnt/tag1
root@x13:~# rsync  -n -av -AXHx --delete   --exclude="/boot/*"   /mnt/src1/  /mnt/tag1/
root@x13:~# 3sync
root@x13:~# umount /mnt/src1/

	_______:  sdb2 : /boot-arx-rf:
root@x13:~# mount -o ro  /dev/sdb2 /mnt/src1
root@x13:~# rsync  -n -av -AXHx --delete    /mnt/src1/  /mnt/tag1/boot/
root@x13:~# 3sync
root@x13:~# umount /mnt/src1/

	_______:  
root@x13:~# umount /mnt/tag1

	_______:  T!FS_P rsync:
mount -o ro  /dev/sdb4    /mnt/src1
mount        /dev/sda10   /mnt/tag1
rsync -n  -av -AXHx --delete    /mnt/src1/t1_RF/    /mnt/tag1/t1_RF/
##________________________________________  ___________________________


#####  ==========  adaptions:
vi /etc/fstab
vi /boot/grub/grub.cfg ##--if-needed! (for now is x13 still booting from old-ubuntu-grub-configs. so nothing needed)
##________________________________________  ___________________________


#####  ==========  __1END__ 20200802-145456 ____________==========
