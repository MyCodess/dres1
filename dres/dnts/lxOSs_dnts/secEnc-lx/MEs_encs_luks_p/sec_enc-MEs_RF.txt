https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions
https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption
--###################### /_230123--MEs-container-on-Lv13-2209arx : step-by-steps-done cryptsetup with "plain-dm-crypt"/dm-mapper--setup-steps for a loop-file-container : ###########
##________________________________________  ___________________________


#####  ==========  MES-new-FS-4GB-"plain dm-crypt", so NOT LUKS  /_180109 : ==============================================
- ALL cmds as m1+sudo in one Terminal (for later copy protocol), if possible ! not root ! due to ownerships/permissions,... !
- OS/2209arx on USB-stick attached to Lv13 as /dev/sda3
- now switching from 3GB to ca. 4GB for mespfsc1_RF /_230123  !
- for now the physical-files/Containers  are in  /up1/t1/mms1_P1 and upp-links/DIRs/mountpoints in /up1/mesfs  ${mespRTDP}  ##for physicals yet no VARs in evv ! ok-so! use ONLY links in ${mespRTDP} !
##________________________________________  ___________________________


#####  ==========  SHORT-summary-cmds: ------------------------------------------------------------------------

	_______:  infs: in this action are:
here NOT-using VARs ! is more überschaubar! is ok so! otherwise adapt just the pathes if needed/changed...!
/up1/mesfs/  	:  mountpoints and upp-links to mesp-files are all in:  /up1/mesfs/
/up1/t1/mms1_P1 :  physical mespfs are for now on T1Fs ,BUT NOT-using phys-pathes! for actions ONLY use the links in  /up1/mesfs/  (except for dd ...)

	_______:  
sync;sync;sync; losetup -a ;el1 ; ll /dev/mapper ; el1; lsblk -p ; el1;
mkdir -v ${newMountPoint1}   ##-if-new-mountpoint-not-there! bzw. mkdir  /up1/mesfs/mesfsc1_new

	_______:  file-container-creation + links... :
date; cd /up1/t1/mms1_P1 ; sudo  dd if=/dev/urandom  of=/up1/t1/mms1_P1/new1   bs=1M     count=3972  ; date ;   ##--ca. 4 min, ok cpu !
ln  -s  /up1/t1/mms1_P1/new1    /up1/mesfs/new1   ##--upp usese just links there!
mkdir  /up1/mesfs/new1p1    ##--mountpoint for new-transfer-container
sudo losetup -v  /dev/loop2  /up1/mesfs/new1
check:  losetup -a

	_______:  open-enc + dev-mapper --> asks PW , set enc up and opens it with dev-mapper:
export enc_open_params1='--hash=ripemd160  --cipher=aes-cbc-essiv:sha256  --key-size=256  --offset=0  --skip=0'  ##--define even default params in cmd-line for plain-dm-crypt !
sudo cryptsetup   $enc_open_params1  --verify-passphrase  open  /dev/loop2  mes1new  --type  plain    ##--from here commes encryting and device-Mapper! open the file as enc-device and assign it to /dev/mapper/enc-t1
sync;sync;sync; losetup -a ;el1 ; ll /dev/mapper ; el1; lsblk -p ; el1;

	_______:  format + mount:
sudo  mkfs.ext4  -L mespfsc1_RF   /dev/mapper/mes1new  ;  ##--!!- if here changing the fs-type (eg ext3-to-ext4), then vifstab either !!! in the plain-text-enc-style the fs-type can NOT be recongnized automatically!! then the header is also enc !!
sudo  mount -o noauto,noexec,user,nodiratime,noatime  /dev/mapper/mes1new   /up1/mesfs/new1p1
sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; sudo cryptsetup  status   /dev/mapper/mes1new  ;  el1; lsblk -p ; el1;

	_______:  cp _RF to new1-enc-part as root (easier):
chown m1:gm1  /up1/mesfs/new1p1/
echo  "/_230123  :  mespfsc1-new-setup and switch from 3GB to 4GB"  >> /up1/mesfs/new1p1/230123-mespfsc1-setup-plainEnc.flg.txt
mesp.sh   1  opena
date;  cp -a /up1/mesfs/mesp1/MEs  /up1/mesfs/new1p1/ ; date  ##--ca. 9 min !

	_______:  end work, close all:  ( either 3sync and reboot and then renaming files, /OR):
3sync;
mesp.sh   1  closea
sudo umount /dev/mapper/mes1new
sudo cryptsetup close  mes1new  ##--check:  lla /dev/mapper
sudo losetup -v -d  /dev/loop2
mvde  /up1/t1/mms1_P1/mespfsc1_RF ;
mvi /up1/t1/mms1_P1/new1  /up1/t1/mms1_P1/mespfsc1_RF ;
rm /up1/mesfs/new1  ; rmdir  /up1/mesfs/new1p1 ;

	_______:  ------- __END1__    short-summary --------------------------------------------------
--###################### 180100---step-by-steps-done cryptsetup with "plain-dm-crypt"/dm-mapper--setup-steps for a loop-file-container : ###########
##________________________________________  ___________________________


#####  ==========  MES-new-FS-3GB-"plain dm-crypt", so NOT LUKS any more /_180109 : ==============================================

	_______:  ------- short-summary-cmds: -------------------------------------------------------------
sync;sync;sync; losetup -a ;el1 ; ll /dev/mapper ; el1; lsblk -p ; el1;

	_______:  file-container:
date; dd if=/dev/urandom  of=./mesfsc1_new   bs=1M     count=2972  ; date ;  ##--> with urandom it takes time AND cpu 100% , but ok! do it! /OR do on other NB/PC ! on NB_Lv13 ca. 21 min for 5GB on usbStick ;
losetup -v  /dev/loop2  /up1/mnt/UUFS1/mesfsc1_new

	_______:  open-enc + dev-mapper :
export enc_open_params1='--hash=ripemd160  --cipher=aes-cbc-essiv:sha256  --key-size=256  --offset=0  --skip=0'  ##--define even default params in cmd-line for plain-dm-crypt !
sudo cryptsetup   $enc_open_params1  --verify-passphrase  open  /dev/loop2  mes1new  --type  plain    ##--from here commes encryting and device-Mapper! open the file as enc-device and assign it to /dev/mapper/enc-t1
sync;sync;sync; losetup -a ;el1 ; ll /dev/mapper ; el1; lsblk -p ; el1;

	_______:  format + mount:
mkfs.ext4  -L mespfsc1_RF   /dev/mapper/mes1new  ;  ##--!!- if here changing the fs-type (eg ext3-to-ext4), then vifstab either !!! in the plain-text-enc-style the fs-type can NOT be recongnized automatically!! then the header is also enc !!
mount -o noauto,noexec,user,nodiratime,noatime  /dev/mapper/mes1new  /up1/mesfs/mespx/
chown m1:gm1  /up1/mesfs/mespx/
sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; sudo cryptsetup  status   /dev/mapper/mes1new  ;  el1; lsblk -p ; el1;

	_______:  end work, close all:
sudo umount /dev/mapper/mes1new
sudo cryptsetup close  mes1new
sudo losetup -v -d  /dev/loop2

	_______:  ------- __END1__    short-summary --------------------------------------------------
############ 180109--small-test for plain dm-crypt BUT with all default params for "plain": ########################
##________________________________________  ___________________________


#####  ==========  small-test for plain dm-crypt with a small loop-file-container /_180109 : OK ===========================
see  https://wiki.archlinux.org/index.php?title=Dm-crypt/Device_encryption&printable=yes#Encryption_options_for_plain_mode

	_______:  -- kurz: ------------------------------------
--file-container and block device (no enc yet):
dd   if=/dev/urandom  of=./encfs1  bs=1024  count=10240                 ##--just creating container-file  --one-time-action
sudo losetup -v  /dev/loop5  /up1/varu/varau/wks/enc-plain1/encfs1      ##--attaching the file as a block-device to the system
-- start enc:
export enc_open_params1='--hash=ripemd160  --cipher=aes-cbc-essiv:sha256  --key-size=256  --offset=0  --skip=0'
sudo cryptsetup   $enc_open_params1 open  /dev/loop5  enc-t1  --type  plain  ##--from here commes encryting and device-Mapper! open the file as enc-device and assign it to /dev/mapper/enc-t1
	## if you input a wrong PW later by reopening the container, cryptsetup does NOT say anything, so NO error message (in case of  --type  plain )!!! you'll just NOT be able to mount it !! 
	## PW set : "test1" /_180221
sudo mkfs.ext4 /dev/mapper/enc-t1                                       ##--format it!  --one-time-action
sudo mount /dev/mapper/enc-t1  /up1/media/cy1/                          ##--mount it! done! you can use it ! if wrong PW by "cryptsetup ..open..."  then you notice here (not there) that mount does NOT work!!
##--chek it in another Term:
sudo chown -R  u1:gu1  /up1/media/cy1/ ;  cdlla /up1/media/cy1/  ; df. ; cp ... . ; ...
sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup  status  /dev/mapper/enc-t1 ;  el1; lsblk -p ; el1;
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

	_______:  check-wrong-PW: close+reopen with wrong PW:  could open with cryptsetup , BUT could NOT mount!! mount-error unknown Filesystem !!
sudo umount /dev/mapper/enc-t1
sudo cryptsetup close  enc-t1
sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ;
reopen it with the above cmds BUT enter wrong PW !
sudo cryptsetup   $enc_open_params1 open  /dev/loop5  enc-t1  --type  plain  ##--with wrong PW : NO error-msg! all looks ok! opened !!
sudo mount /dev/mapper/enc-t1  /up1/media/cy1/ 
mount: /up1/media/cy1: wrong fs type, bad option, bad superblock on /dev/mapper/enc-t1, missing codepage or helper program, or other error.

	_______:  
# check the performance (just FYI):   cryptsetup benchmark
--###################### 1500pre---step-by-steps-done cryptsetup with LUKS/dm-mapper--setup-steps for a Part OR loop-file-container : ###########
##________________________________________  ___________________________


#####  ==========  mesp-manully-direct-simple-mount-steps (done, OK, 1503ubt-x13) 150322:
-  simple direct steps to see the procedure, without using elegant /up1/mesp links,...! as rt:
-! the first loop-setup, is ONLY becasue it is a file-mounting (instead physical-dev-mounting) and has got NOThing to do with the real enc-stuff !!

	_______:  openning-steps:
1-losetup -v  /dev/loop1   /up1/mnt/UUFS1/mespfsc1_RF      ##--II- <just a free loop-dev>  , <physica-url-to-enc-file> : bind-the-flat-file as loop-dev
	check:    losetup -a       ##--> /dev/loop1: [2055]:12 (/up1/mnt/UUFS1/mespfsc1_RF)
2-cryptsetup luksOpen /dev/loop1  mespfsc1                 ##--II- <previously setup loop-dev>  <jus an arbitrary name for device-mapper. you see the name in /dev/mapper> : create dev-mapper-entry for enc-mount
	check:  ll /dev/mapper/  ##--> /dev/mapper/mespfsc1
3-mount -t ext4 -o  noauto,noexec,user,nodiratime,noatime  /dev/mapper/mespfsc1  /up1/mesfs/mesp1  ##--OR-use just entry in fstab  : mount the looped-flat-file opened by crypt indev-mapper into the mountpoint mesp1 in fstab/...
	check: ll ...

	_______:  closing steps:
sync;sync;sync;
umount /up1/mesfs/mesp1
cryptsetup luksClose mespfsc1 ;  ##--II-  <dev-mapper simple name> now the entry mespfsc1 must be gone/deleted :
	check:  ll /dev/mapper ;
losetup -d /dev/loop1             ##--II-  <dev-loop assigned dev> . now the entry mespfsc1 must be gone/deleted :
	check: losetup -a
##________________________________________  ___________________________


#####  ==========  partition/disk-encrypting in LUKS-mode of cryptsetup: done on usb-stick, ok, 080517, suse103:
	- see /proc/crypto , man cryptsetup
	physica-dev is: /dev/sdb1 , my usbSitck
	logical-dev will be generated in  /dev/mapper/
	for formatting/mounting/... ONLY  logical-dev may be used!! forget physical one; only dm-mapper-controller knows it!!
	(if needed, to delete first: dd if=/dev/urandom of=/dev/sdb1)
	dd if=/dev/urandom of=/dev/sdb1
	cryptsetup luksFormat -v --key-size 256 /dev/sdb1
		initializes a LUKS partition and sets the initial key, either via prompting or via <key file>.
		--> must generate logical mapper-device in /dev/mapper/sdb1 (shortly??)??
	-- check/view: status
	ll /dev/mapper
	cryptsetup luksDump /dev/sdb1   # just to see partition
	--
	cryptsetup luksOpen /dev/sdb1 enc1  ###-OR??:	cryptsetup luksOpen /dev/sdb1 /mnt/enc1
	ll /dev/mapper   #--> must see enc1 there!!
	mkfs.ext3 -O dir_index,resize_inode /dev/mapper/enc1  ##-OR- just: mkfs.ext3 /dev/mapper/enc1
	mount /dev/mapper/enc1 /mnt/enc1
	chown u1:users /mnt/enc1 #-- as u2 just put some dummy files there...
	umount /mnt/enc1
	cryptsetup luksClose enc1
##________________________________________  ___________________________


#####  ==========  loop-device/file.container as crypt-device in LUKS-mode of cryptsetup:

	_______:  -- creating new enc-file-container  AND replacing current mesfsc1_RF with newly created mesfsc1_new: 120308, vo17.suse.11.4:
	-! best all cmds as ROOT, but here, more secure, mixed of user/m1 + root.
	--- generating and mounting loop-fs-dev (has got nothing to do with crypt yet): see also man losetup :
	m1@vo17:
	  date; dd if=/dev/urandom  of=/mnt/UUFS1/mesfsc1_new   bs=1048576 count=1948  ; date  ##- 100MB less than 2GB (good, fit to any 2GB-stick, and also usual size...)
	  OR     date; dd if=/dev/urandom  of=/mnt/UUFS1/mesfsc1_new   bs=1MB     count=1950  ; date  ##-II- 1MB is here 1000KB (so NOT 1024), so it is less than 2GB !
	  OR (NOT secure but fast, so all bytes with null): head -c 2G  /dev/zero > /mnt/UUFS1/mesfsc1_new
	  OR-better/longer:   badblocks -c 10240 -s -w -t random -v /dev/sdb  #: Overwrite the whole drive with random data in order to slow down attacks on the encryption.  At the same time perform a bad blocks scan to make sure the hard drive is not going to die too soon:
	- check: sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ;     #- just check/see, or with -f for next available loop device
	losetup -v  /dev/loop2  /mnt/UUFS1/mesfsc1_new
		Loop device is /dev/loop2
	- check:  losetup -a
	--- crypt-dev: (root)
	vo17: # cryptsetup -v luksFormat -c aes-cbc-essiv:sha256 --key-size 256  /dev/loop2  ##--> PW-enter and loop2-dev will be encrypted! ALL date of loop2-dev-cennected will be DELETED!! enc-formatting of device!
	- check: vo17:~ #  cryptsetup -v luksDump /dev/loop2  ; ll /dev/mapper/
	vo17:~ #   cryptsetup -v luksOpen /dev/loop2  mesfsc1_new  ##- creates also /dev/mapper/-entries
		Enter passphrase for /dev/loop2: 
		Key slot 0 unlocked.
		Command successful.
	- check: vo17:~ # sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup status mesfsc1_new
	--- dev-mount:
	vo17:~ # mkfs.ext4 /dev/mapper/mesfsc1_new  ###--> save the output
	vo17:~ # mount /dev/mapper/mesfsc1_new  /media/L1
	vo17:~ # cdlla  /up1/mesp1 ;  date; cp -a *  /media/L1/  ; date
		Thu Mar  8 23:04:22 CET 2012
		Thu Mar  8 23:06:57 CET 2012
		vo17:/mnt/UUFS1/mesp # df -h
		Filesystem            Size  Used Avail Use% Mounted on
		/dev/mapper/mesfsc1_new   1.9G  1.3G  498M  73% /media/L1
		/dev/mapper/mesfsc1       2.0G  1.3G  629M  68% /mnt/UUFS1/mesp
	--- umount + closing:
	- check:  vo17:~ # losetup -a ; ll /dev/mapper/  ;  cryptsetup status  mesfsc1_new
	   bzw. cryptsetup status /dev/mapper/mesfsc1_n
	vo17:~ # sync;sync;  umount /media/L1  ; mesp.sh 1 close ;
	- check:  vo17:~ # losetup -a ; ll /dev/mapper/  ;  cryptsetup status  mesfsc1_new
	- if want/needed:
		tune2fs  -l  /dev/mapper/mesfsc1  > logfile
		2fsck  -fD -p /dev/mapper/mesfsc1 
	vo17:~ # cryptsetup luksClose mesfsc1_new
	--- ... 
	changing mount points, replacing old one with new ones,...
		cdll /mnt/UUFS1 && mv mesfsc1_RF 110308_mesfsc1 &&  mv mesfsc1_new mesfsc1_RF ; #....

	_______:  -- first try with small filesystem /tmp/fs6 : 
	-!! see bash-scr: http://petaramesh.org/public/arc/projects/lfd/lfd  !!
	--- generating and mounting loop-dev (has got nothing to do with crypt yet): see also man losetup :
	dd if=/dev/urandom of=/tmp/fs6 bs=1024 count=10240     #-I- urandom takes long, ca. 5min/1GB
		sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ;   #- just check/see
	losetup -v  /dev/loop0 /tmp/fs6
		sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup status /dev/mapper/fs6   #- just check/see
	--- crypt-dev:
	cryptsetup -v luksFormat -c aes-cbc-essiv:sha256 --key-size 256  /dev/loop0   #- for sha256 the fs6 may NOT be too small; at least 10MB ..
	cryptsetup -v luksDump /dev/loop0         #- just check/see
	cryptsetup -v luksOpen /dev/loop0 fs6     #- hier dm-entries/dev-nodes will be generated so:  ll /dev/mapper/  /dev/dm*
		sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup status /dev/mapper/fs6   #- just check/see
	--- dev-mount:
	mkfs.ext3  /dev/mapper/fs6
	mount /dev/mapper/fs6 /mnt/enc1
	ll /mnt/enc1 ; chown u1:users /mnt/enc1 ;  #- do editting/copying...on enc1..
	--- umount + closing the enc-part:
	sync ; umount /dev/mapper/fs6  	#--I- starting closing the FS
		sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup status /dev/mapper/fs6   #- just check/see
	cryptsetup luksClose fs6         #- hier dm-entries/dev-nodes will be closed/released, but losetup not-released yet, so:  ll /dev/mapper/  /dev/dm*
		sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup status /dev/mapper/fs6   #- just check/see
	losetup -v -d /dev/loop0
		sync;sync; losetup -a ;el1 ; ll /dev/mapper ;el1 ; cryptsetup status  /dev/mapper/fs6   #- just check/see: everything must be released: dev-mappers and losetups !

	_______:  -- from faq-cryptsetup http://code.google.com/p/cryptsetup/wiki/FrequentlyAskedQuestions :
	2.3 How do I use LUKS with a loop-device? 
	  This can be very handy for experiments. Setup is just the same as with any block device. If you want, for example, to use a 100MiB file as LUKS container, do something like this: 
      head -c 100M /dev/zero > luksfile  # create empty file
      losetup /dev/loop0 luksfile        # map luksfile to /dev/loop0
      cryptsetup luksFormat /dev/loop0   # create LUKS on loop device
	  Afterwards just use /dev/loop0 as a you would use a LUKS partition. To unmap the file when done, use "losetup -d /dev/loop0".

	_______:  -- good step-by-step from: http://www.hermann-uwe.de/blog/howto-disk-encryption-with-dm-crypt-luks-and-debian
	- Make sure you run Linux 2.6.16 or better.
	- Enable the following options in your kernel: lsmod : dm-crypt dm_mod ,...
	- rpm: cryptsetup , ...
	- Overwrite the whole drive with random data in order to slow down attacks on the encryption. At the same time perform a bad blocks scan to make sure the hard drive is not going to die too soon:
		badblocks -c 10240 -s -w -t random -v /dev/sdb
		Replace /dev/sdb with whatever is correct on your system. If you're really paranoid, and are willing to wait one or two days, do this:
		dd if=/dev/urandom of=/dev/sdb 
	- Install the required packages:
		apt-get install cryptsetup
		 The current cryptsetup in Debian unstable already supports LUKS, which was not the case a while ago, if I'm not mistaken. So Debian testing or stable will most probably not work! 
	- Create one or more partitions on the drive:
		cfdisk /dev/sdb
		 I created one big 300 GB partition, /dev/sdb1. 
	- Setup LUKS:
		cryptsetup --verbose --verify-passphrase luksFormat /dev/sdb1
		 Enter a good passphrase here. Don't spoil the whole endeavour by chosing a stupid or short passphrase. 
	- Open the encrypted device and assign it to a virtual /dev/mapper/samsung300gb device:
		cryptsetup luksOpen /dev/sdb1 samsung300gb 
	- Create a filesystem on the encrypted device:
		mkfs.ext3 -j -m 1 -O dir_index,filetype,sparse_super /dev/mapper/samsung300gb
		 I used ext3 with some optimizations, see mke2fs(8). 
	- Mount the encrypted partition:
		mkdir /mnt/samsung300gb
		mount /dev/mapper/samsung300gb /mnt/samsung300gb
		 That's it. Everything you write to /mnt/samsung300gb will be encrypted transparently. 
	- For unmounting use: umount /mnt/samsung300gb
	- cryptsetup luksClose /dev/mapper/samsung300gb
#################################-E steps ##################################################################
