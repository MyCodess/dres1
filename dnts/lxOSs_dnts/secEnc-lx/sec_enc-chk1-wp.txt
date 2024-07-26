________________ here only _CPs / nps ! for _RF-nts see  sec_enc-MEs-wp.txt  in lxdevnts !! /up1/w/docs_m/devres/devnts/lxSys/sec_enc-MEs-wp.txt _________
--########################### gpg-enc only with PW testies/wp : ###################################### 
##________________________________________  ___________________________


#####  ==========  180223 gpg with only PW testies:
u1@x13: /up1/varu/varau/wks/enc-gpg-pw1/ $date
Fr 23. Feb 12:13:07 CET 2018
u1@x13: /up1/varu/varau/wks/enc-gpg-pw1/ $tar -czv  /up1/w/docs_m/Infos/IT_Infos/ | gpg -c -o t1.tgz.gp  ##--PW:  "tt"
-- unpack-test :
pkill gpg-agent  ##--to forget the PW! otherwise is in its cache and you won't be asked for PW !!
u1@x13: /up1/varu/varau/wks/enc-gpg-pw1/unp1/ $gpg   -o t1.tgz  -d ../t1.tgz.gp1  ##---PW:  "tt"
/OR directly to tar :
gpg  -d ../t1.tgz.gp1  | tar -xzv
/OR directly to tar AND ONLY extracting certain files :
gpg  -d ../t1.tgz.gp1  | tar -xzv  up1/w/docs_m/Infos/IT_Infos/FMs.Infos/Profs.Exp.ITPeop.dw/Testmanager_Freelance.de.txt
--########################### cryptsetup/dm-crypt testies smallies : ################################# 
##________________________________________  ___________________________


#####  ==========  encfs1 stat:
- PW set : "test1" /_180221  for encfs1  , ext4, plain-type

	_______:  _CPs from :
dd   if=/dev/urandom  of=./encfs1  bs=1024  count=10240                 ##--just creating container-file  --one-time-action
sudo losetup -v  /dev/loop5  /up1/varu/varau/wks/enc-plain1/encfs1      ##--attaching the file as a block-device to the system
export enc_open_params1='--hash=ripemd160  --cipher=aes-cbc-essiv:sha256  --key-size=256  --offset=0  --skip=0'
sudo cryptsetup   $enc_open_params1 open  /dev/loop5  enc-t1  --type  plain  ##--from here commes encryting and device-Mapper! open the file as enc-device and assign it to /dev/map>
    ## PW set : "test1" /_180221
sudo mkfs.ext4 /dev/mapper/enc-t1                                       ##--format it!  --one-time-action
sudo mount /dev/mapper/enc-t1  /up1/media/cy1/                          ##--mount it! done! you can use it ! if wrong PW by "cryptsetup ..open..."  then you notice here (not there)>
    ##--chek it in another Term:  sudo chown -R  u1:gu1  /up1/media/cy1/ ;  cdlla /up1/media/cy1/  ; df. ; cp ... . ; ...
sync;sync; losetup -a ;echoline1 ; ll /dev/mapper ;echoline1 ; cryptsetup  status  /dev/mapper/enc-t1 ;  echoline1; lsblk -p ; echoline1;
-- end work, close all:
sudo cryptsetup  status  /dev/mapper/enc-t1
sudo umount /dev/mapper/enc-t1
sudo cryptsetup close  enc-t1
sudo losetup -v -d  /dev/loop5
#-to-add: all params for "plain dm-crypt" must be specified, even the defaults, in case that cryptsetup sometimes changes the defaults!
  due to having no params saved in the header, as in LUKS, you must save it with which params you had set it up !! otherwise can NOT open it !!
- nts:  with wrong PW, you could NOT mount it ! good!

	_______:  status:
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo cryptsetup  status  /dev/mapper/enc-t1
/dev/mapper/enc-t1 is active and is in use.
  type:    PLAIN
  cipher:  aes-cbc-essiv:sha256
  keysize: 256 bits
  device:  /dev/loop5
  loop:    /up1/varu/varau/wks/enc-plain1/encfs1
  offset:  0 sectors
  size:    20480 sectors
  mode:    read/write
##________________________________________  ___________________________


#####  ==========  encfs1vfat stat  (enc-fs1-vfat) /_180222 :
u1@x13: /up1/varu/varau/wks/enc-plain1/ $date
Do 22. Feb 08:56:51 CET 2018
u1@x13: /up1/varu/varau/wks/enc-plain1/ $dd   if=/dev/urandom  of=./encfs1vfat  bs=1024  count=10240
10240+0 records in
10240+0 records out
10485760 bytes (10 MB, 10 MiB) copied, 0,214767 s, 48,8 MB/s
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo losetup -v  /dev/loop5  /up1/varu/varau/wks/enc-plain1/encfs1vfat 
[sudo] password for u1: 
u1@x13: /up1/varu/varau/wks/enc-plain1/ $export enc_open_params1='--hash=ripemd160  --cipher=aes-cbc-essiv:sha256  --key-size=256  --offset=0  --skip=0'
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo cryptsetup   $enc_open_params1 open  /dev/loop5  enc-t1-vfat  --type  plain
Enter passphrase:  "test1"
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo mkfs.vfat  -n  ENC1VFAT /dev/mapper/enc-t1-vfat 
mkfs.fat 4.1 (2017-01-24)
##--check with dummy files copying ...:
sudo mount  -o utf8,noatime,noauto,noexec,users,uid=u1,gid=gu1,dmask=002,fmask=113 /dev/mapper/enc-t1-vfat  /up1/media/cy1/
cdlla /up1/media/cy1 ; vi 00-encfs1vfat.flg.txt ; cp ...

	_______:  stat :
u1@x13: /up1/media/cy1/ $lla
total 4294
-rw-rw-r-- 1 u1 gu1    1107 2018-02-22 09:07 00-encfs1vfat.flg.txt
-rw-rw-r-- 1 u1 gu1 2066622 2017-09-24 08:47 170923-MiKi-Lernen-144742.jpg
-rw-rw-r-- 1 u1 gu1 2326205 2017-12-17 17:42 171217-BiBi-WeihnachtsKorb-GB_141747.jpg
u1@x13: /up1/media/cy1/ $df.
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/enc-t1-vfat   10M  4,2M  5,8M  43% /up1/media/cy1
u1@x13: /up1/media/cy1/ $
--
u1@x13: /up1/media/cy1/ $sudo cryptsetup  status  /dev/mapper/enc-t1-vfat
/dev/mapper/enc-t1-vfat is active and is in use.
  type:    PLAIN
  cipher:  aes-cbc-essiv:sha256
  keysize: 256 bits
  device:  /dev/loop5
  loop:    /up1/varu/varau/wks/enc-plain1/encfs1vfat
  offset:  0 sectors
  size:    20480 sectors
  mode:    read/write

	_______:  close:
sync;sync; sudo umount /dev/mapper/enc-t1-vf  ; sudo cryptsetup close  enc-t1-vfat ; sudo losetup -v -d  /dev/loop5 ;
sync;sync; losetup -a ;echoline1 ; ll /dev/mapper ;echoline1 ; cryptsetup  status  /dev/mapper/enc-t1 ;  echoline1; lsblk -p ; echoline1;
##________________________________________  ___________________________


#####  ==========  encfs1-vfat-luks  /_180222 :
u1@x13: /up1/varu/varau/wks/enc-plain1/ $date
Do 22. Feb 11:26:29 CET 2018
u1@x13: /up1/varu/varau/wks/enc-plain1/ $dd   if=/dev/urandom  of=./encfs1vfatluks  bs=1024  count=10240 
10240+0 records in
10240+0 records out
10485760 bytes (10 MB, 10 MiB) copied, 0,25195 s, 41,6 MB/s
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo losetup -v  /dev/loop5  /up1/varu/varau/wks/enc-plain1/encfs1vfatluks 
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo cryptsetup -v luksFormat -c aes-cbc-essiv:sha256 --key-size 256  /dev/loop5
Enter passphrase: "test1"
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo cryptsetup -v luksDump /dev/loop5  ##--just-checked ...
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo  cryptsetup -v luksOpen /dev/loop5  enc1-vfat-luks 
Enter passphrase for /up1/varu/varau/wks/enc-plain1/encfs1vfatluks: 
Key slot 0 unlocked.
Command successful.
sync;sync; losetup -a ;echoline1 ; ll /dev/mapper ;echoline1 ; sudo cryptsetup status /dev/mapper/enc1-vfat-luks   #- just check/see
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sudo mkfs.vfat -n ENC1VFATLU  /dev/mapper/enc1-vfat-luks
mkfs.fat 4.1 (2017-01-24)
sudo mount  -o utf8,noatime,noauto,noexec,users,uid=u1,gid=gu1,dmask=002,fmask=113 /dev/mapper/enc1-vfat-luks  /up1/media/cy1/
##-- cp dummy files, flg, ...:
1@x13: /up1/t1/nps/Fotos-nps/ca1s_Ft/Zoo1/ $cpt *jpg  /up1/media/cy1/
'170923-MiKi-Lernen-144742.jpg' -> '/up1/media/cy1/170923-MiKi-Lernen-144742.jpg'
'171217-BiBi-WeihnachtsKorb-GB_141747.jpg' -> '/up1/media/cy1/171217-BiBi-WeihnachtsKorb-GB_141747.jpg'
u1@x13: /up1/t1/nps/Fotos-nps/ca1s_Ft/Zoo1/ $cdlla -
/up1/media/cy1
/up1/media/cy1
total 4316
drwxrwxr-x  2 u1 gu1   16384 2018-02-22 11:42 ./
drwxrwxr-x 26 u1 gu1    4096 2018-02-22 09:13 ../
-rw-rw-r--  1 u1 gu1     145 2018-02-22 11:40 00-encfs1-vfat-LUKS.flg.txt
-rw-rw-r--  1 u1 gu1 2066622 2017-09-24 08:47 170923-MiKi-Lernen-144742.jpg
-rw-rw-r--  1 u1 gu1 2326205 2017-12-17 17:42 171217-BiBi-WeihnachtsKorb-GB_141747.jpg
u1@x13: /up1/media/cy1/ $df.
Filesystem                  Size  Used Avail Use% Mounted on
/dev/mapper/enc1-vfat-luks  8,0M  4,2M  3,8M  53% /up1/media/cy1
u1@x13: /up1/media/cy1/ $date
Do 22. Feb 11:42:18 CET 2018
u1@x13: /up1/varu/varau/wks/enc-plain1/ $sync;sync; losetup -a ;echoline1 ; ll /dev/mapper ;echoline1 ; sudo cryptsetup status /dev/mapper/enc1-vfat-luks   #- just check/see
/dev/loop1: []: (/up1/mnt/UUFS1/mespfsc1_RF)
/dev/loop5: []: (/up1/varu/varau/wks/enc-plain1/encfs1vfatluks)
##________________________________________  ___________________________


#####  ==========  
total 0
crw------- 1 root root 10, 236 2018-02-20 12:06 control
lrwxrwxrwx 1 root root       7 2018-02-22 11:36 enc1-vfat-luks -> ../dm-1
lrwxrwxrwx 1 root root       7 2018-02-20 12:20 mespfsc1 -> ../dm-0
##________________________________________  ___________________________


#####  ==========  
/dev/mapper/enc1-vfat-luks is active and is in use.
  type:    LUKS1
  cipher:  aes-cbc-essiv:sha256
  keysize: 256 bits
  device:  /dev/loop5
  loop:    /up1/varu/varau/wks/enc-plain1/encfs1vfatluks
  offset:  4096 sectors
  size:    16384 sectors
  mode:    read/write

	_______:  close:
sync;sync; sudo umount /dev/mapper/enc1-vfat-luks  ; sudo cryptsetup luksClose  enc1-vfat-luks  ; sudo losetup -v -d  /dev/loop5 ;
sync;sync; losetup -a ;echoline1 ; ll /dev/mapper ;echoline1 ; cryptsetup  status  /dev/mapper/enc1-vfat-luks ;  echoline1; lsblk -p ; echoline1;
####################---------------############################################
