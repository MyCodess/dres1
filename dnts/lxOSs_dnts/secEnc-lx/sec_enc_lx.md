__________ Sec_Enc_LX, Encrypt-Partitions, Encrypt-Files, LUKS, dm-crypt, __________
-!! here mainly only ENC-sec (for emails, files,...): gpg,luks,crypts,vi-enc,....
	-! for NW-sec (firewall,..) see extra NW-nts !
	-! for sys-sec (services,boots,perms,...) see extra sys-nts!
--############################ Cryptsetup / LUKS / dm-crypt : ############################################
##________________________________________  ___________________________


#####  ==========  docs/WPs: 
man cryptsetup, cryptconfig , losetup
man cryptmount pmount  : so mounting enc-parts without root !
https://gitlab.com/cryptsetup/cryptsetup/wikis/DMCrypt
https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions
https://wiki.archlinux.org/index.php/Dm-crypt/Device_encryption
http://code.google.com/p/cryptsetup/wiki/FrequentlyAskedQuestions
https://wiki.archlinux.org/index.php/Dm-crypt/Device_encryption
https://wiki.archlinux.org/index.php/Disk_encryption#Comparison_table
https://gitlab.com/cryptsetup/cryptsetup/wikis/home
https://gitlab.com/cryptsetup/cryptsetup/wikis/DMCrypt
https://wiki.archlinux.org/index.php/EncFS
http://en.opensuse.org/Encrypted_Root_File_System
http://www.saout.de/misc/dm-crypt/
##________________________________________  ___________________________


#####  ==========  plain dm-crypt nts/wp:

	_______:  do NOT relly on default params (they will change)!! define every param manually!!  eg:
for open cmd (crypsetup  open --type plain <device> <name>):
<options> can be [--hash, --cipher, --verify-passphrase, --key-file, --keyfile-offset, --key-size, --offset, --skip, --size, --readonly, --shared, --allow-discards]  ##--man crypsetup
you MUST specify ALL, even defaults, options hier in your script! in case that dafults sometimes changes in coming releases of crypsetup !!
-
HDD1 /dev/disk/by-uuid/1234-5678-90ab-cdef /root/crypt/HDD1.key -c aes-xts-plain64 --offset 0 --skip 0 --tries 1 --noearly --loud /*I assume to syslog?*/
You still haven't specified the key size. Run "crypsetup --help" to see all of the compiled-in defaults (at the end of the output), and set values for all of them ...
see https://www.linuxquestions.org/questions/linux-software-2/luks-vs-plain-4175500534/

	_______:  -
- https://security.stackexchange.com/questions/90468/why-is-plain-dm-crypt-only-recommended-for-experts

	_______:  
Cryptsetup utility support several modes. Plain mode is just equivalent of direct configuration of dmcrypt target with passphrase hashing but without on-disk metadata.
https://gitlab.com/cryptsetup/cryptsetup/wikis/DMCrypt

	_______:  
##________________________________________  ___________________________


#####  ==========  LUKS-infs :
	LUKS is the standard for Linux hard disk encryption.
	LUKS stores all setup necessary setup information in the partition header, enabling the user to transport or migrate his data seamlessly.
##________________________________________  ___________________________


#####  ==========  DMCrypt (Kernel API for encrypting) / dm-crypt: Linux kernel device-mapper crypto target :
	-!! DIFF DMCrypt /dm-crypt (core enc-API ) <-->  "plain dm-crypt"-based encrypting with cryptsetup
	https://gitlab.com/cryptsetup/cryptsetup/wikis/DMCrypt
	http://code.google.com/p/cryptsetup/wiki/FrequentlyAskedQuestions   #see  insbesondere: 6. Backup and Data Recovery
	---
	"Device-mapper" is infrastructure in the Linux 2.6 and 3.x kernel that provides a generic way to create virtual layers of block devices.
	"Device-mapper crypt target" provides transparent encryption of block devices using the kernel crypto API.
	/proc/crypto which contains supported ciphers and modes (but note it contains only currently loaded crypto API modules).
##________________________________________  ___________________________


#####  ==========  cryptsetup :
	!! see FAQ in  https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions
	Cryptsetup can do encrypting both LUKS- or "plain dm-crypt"-based and more ... ! (defined by the param "open --type plain/luks/.... " in: cryptsetup  open <device> <name> --type <device_type> )
	Cryptsetup covers Linux disk encryption with "plain dm-crypt" (one passphrase, no management, no metadata on disk) and LUKS (multiple user keys with one master key, anti-forensic features, metadata block at start of device, ...).
	Cryptsetup is utility used to conveniently setup disk encryption based on DMCrypt kernel module.
	-! DIFF: 'cryptsetup open /dev/sda10  e1' maps the raw encrypted device /dev/sda10 to the mapped (decrypted) device /dev/mapper/e1, which can then be  mounted,  fsck-ed  or have a filesystem created on it or ...
	   so /dev/mapper/xxx are decrypted/mount-able pathes to the encrypted-blockdevice /dev/loop1 or /dev/sda10 or ... !
	--- LUKS  <--> "plain dm-crypt"-based encrypting (mode) with cryptsetup? modes of cryptsetup :  diffs:
	Cryptsetup supports different encryption operating modes to use with dm-crypt.
		- The most common (and default) is " --type LUKS " 
		--type plain for using dm-crypt plain mode,
		--type loopaes for a loopaes legacy mode, and
		--type tcrypt for a TrueCrypt compatibility mode. 
	- LUKS has got the header, which is visible with "file loop-file-xxx " or with "blkid xxx/part/disk/...". by plain you do not see anything, because no header is there!!
	- An important distinction of LUKS to note at this point is that the key is used to unlock the master-key of a LUKS-encrypted device and can be changed with root access. Other encryption modes do not support changing the key after setup, because they do not employ a master-key for the encryption.
	- In dm-crypt plain mode, there is no master-key on the device, hence, there is no need to set it up. Instead the encryption options to be employed are used directly to create the mapping between an encrypted disk and a named device. The mapping can be created against a partition or a full device. In the latter case not even a partition table is needed.
	- In dm-crypt plain mode, passphrase/PW kann NOT be changed! (for new PW setup a new partition/blockdevice, set the new PW and copy alls files from old to new !  _KK1
	- In dm-crypt plain mode, No checks are performed, no metadata is used. There is no formatting operation (as luksFormat ...). KK1: because there is no Header to verify against that !!)
	- LUKS has got many more features: reencrypting, new-PW, ... 
	- LUKS  checks  for  a  valid  passphrase  when  an encrypted partition is unlocked. The behavior of plain dm-crypt is different.  It will always decrypt with the passphrase given. If the given passphrase is wrong, the device mapped by plain dm-crypt will essentially still contain encrypted data and will be unreadable.  ##--man cryptsetup
	- 
	--- LUKS-based-enc cmds:
	cryptsetup  open --type luks <device> <name>   ##--  luksOpen <device> <name> (old syntax)
	cryptsetup  luksFormat / luksOpen (old) / luks.... #see man cryptsetup
	--- "plain dm-crypt"-based-enc cmds:
	cryptsetup  open --type plain	
	--- chk: is my device LUKS/...??: (with "plain dm-crypt" there is no way to check it! no header is there !!)
	-! see FAQ  6.3 How do I test a LUKS header? :
	sudo blkid -p /dev/loop1
	sudo cryptsetup -v isLuks  /dev/loop1   ##--> no errors means: is LUKS-enc!
	--- Backup/Restore of LUKS-mode encs:
	-!! see the whole section of FAQ  6. Backup and Data Recovery :
	-- Header backup:
	-!! see FAQ 6.2 How do I backup a LUKS header? !
	cryptsetup luksHeaderBackup --header-backup-file <file> <device>   ##--backup
	cryptsetup --header <file> luksOpen <device> </dev/mapper/ -name>  ##--test/verify the header-file. If that unlocks your keys-lot, you are good. Do not forget to close the device again.
	cryptsetup luksHeaderRestore --header-backup-file <file> <device>  ##--restore
	-- Get the master key from the device mapper:
	sudo dmsetup table --target crypt --showkey  /dev/mapper/mespfsc1
	--- Header-Backup/Restor of LUKS based enc:
	losetup -v  /dev/loop5  /tmp/fsc5 
	cryptsetup luksHeaderBackup  --header-backup-file  myfile <device> ; #-eg: cryptsetup luksHeaderBackup --header-backup-file  myHeaderBup  /dev/loop5
	cryptsetup luksHeaderRestore --header-backup-file  myfile <device> ; #-eg: ryptsetup luksHeaderRestore --header-backup-file  myHeaderBup  /dev/loop5
	-- doing a test on a test-luk-file (otherwise abckup!!): (take fsc5 offline (loop is ok): cryptsetup luksClose must be done! so no dev-mapping on it!)
	dd conv=notrunc bs=1 count=1024 if=/dev/zero of=/tmp/fsc5  --> so kaputt! try cryptsetup luksOpen --> not working!
	cryptsetup luksHeaderRestore --header-backup-file  myHeaderBup  /dev/loop5  ; #--> not it should work!!
	--- FAQs:
	PW:  PASSPHRASE CHARACTER SET: Some people have had difficulties with this when upgrading distributions. It is highly advisable to only use the 95 printable characters from the first 128 characters of the ASCII table, as they will always have the same binary representation. Other characters may have different encoding depending on system configuration and your passphrase will not work with a different encoding. A table of the standardized first 128 ASCII characters can, e.g. be found on http://en.wikipedia.org/wiki/ASCII
	!! DIFF: passphrase/PW <--> master-key !!:
		passphrase/PW you use it to open the enc-device.
		master-key is derived from the passphrase/PW (as normal-user you do not see it; usu. is in the header of the enc-file/-partition) and then uses that to de-/encrypt the sectors of the device, with a direct 1:1 ma

	_______:  testing is it luks, and is ok?
	- file /tmp/fsc5
	- blkid /dev/sdb1 ; blkid /tmp/fsc5
	- cryptsetup -v isLuks <device>  ;#-eg-root: cryptsetup -v isLuks /dev/loop5

	_______:  misc:
	cryptsetup benchmark  # check the performance 
	cryptsetup status name
	cryptsetup luksAddKey /dev/[your device]  ##-I- multiple keys to unlock the device. This is helpful if it is a multi-user system and you don’t want to use a shared passphrase.
	cryptsetup luksDelKey /dev/[your device] [slot #]
##________________________________________  ___________________________


#####  ==========  Utils-lx-cryptsetup/LUKS...:
- /proc/crypto
- man cryptsetup  http://code.google.com/p/cryptsetup/
- man losetup
- dm-crypt , LUKS-site, 
- zypper se -sd LUKS/crypt/...  : cryptconfig cryptsetup ecryptfs-utils emount eMount krypt pam_mount /more: realcrypt gnu-crypto 
- realcrypt : TrueCrypt for linux:  a rebrand of TrueCrypt to allow for modifications to take place, functionality remains all the same.

	_______:  GUIs/KDEs/GNOME: (rpmslg bei suse.11.4 120300):
- krypt : KDE3 utility for controlling LUKS encrypted volumes /keeping keys, desktop.icon,...
- Seahorse /GNOME-"Passwords and Encryption Keys"  : create and  manage PGP and SSH keys.
--############################ GPGs/GunPG : ##############################################################
##________________________________________  ___________________________


#####  ==========  gpg only with PW /Passphrae (without KEY! ):

	_______:  enc:
- one file:  	gpg -o  f1.gp1  -c f1  
- a tree/DIR:	tar -czv  /up1/w/docs_m/Infos/IT_Infos/ | gpg -o t1.tgz.gp -c
-- decp:
pkill gpg-agent  ##--to forget the PW! otherwise is in its cache and you won't be asked for PW !!
gpg   -o t1.tgz  -d   ../t1.tgz.gp1
/OR directly to tar :
gpg  -d ../t1.tgz.gp1  | tar -xzv
/OR directly to tar AND ONLY extracting certain files :
gpg  -d ../t1.tgz.gp1  | tar -xzv  up1/w/docs_m/Infos/IT_Infos/FMs.Infos/Profs.Exp.ITPeop.dw/Testmanager_Freelance.de.txt
##________________________________________  ___________________________


#####  ==========  
