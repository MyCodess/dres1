__________ Filesystems, mount, formatting, FSChecks, swap, loop, mkfs, Disk-usage/info/check/handling, mount-image/loop, iso-files, CD-create, Memory-Disk, ... __________
##________________________________________  ___________________________


#####  ==========  Filesystems-Handling (ext2/ext3/toips/...):
- man e2fsck , tune2fs , badblocks , dumpe2fs , debugfs , e2image , mke2fs , 
- /usr/src/linux-2.6.8-1.521/Documentation/filesystems
##________________________________________  ___________________________


#####  ==========  Formatting-convertings:

	_______:  ext2-to-ext3-converting: tune2fs -j /dev/hda10
	- more, also with fstab if needed: /dev/hda10 mounted as ext3 to directory /test:
		umount /dev/hda10 ; If you can't unmount it, then remount it read only (mount -o remount,ro /dev/hda10) ; tune2fs -j /dev/hda10  ; Edit /etc/fstab, and for /dev/hda10, change ext2 to ext3  ; mount /dev/hda10  ; /sbin/shutdown -h now ; 

	_______:  ext3-to-ext2-converting: tune2fs -O ^has_journal /dev/hda10 ; see man tune2fs for "^", which means "clear"...
	- more, also with fstab if needed: /dev/hda10 mounted as ext3 to directory /test:
		umount /dev/hda10 ; tune2fs -O ^has_journal /dev/hda10 ; e2fsck /dev/hda10 ; Edit /etc/fstab to change /dev/hda10 to mount type ext2 ; mount /dev/hda10 ;
		The tune2fs command removes the journal inode, and the e2fsck command completes that
##________________________________________  ___________________________


#####  ==========  loop-FileSystems, mounting files al loop-device:

	_______:  Creating a File System in a file:
	1- Create the file: dd if=/dev/zero of=linux.ex2 bs=1024 count=131072  ; #adapt count if needed (here 128 MB)
	2- Create the filesystem:  mke2fs linux.ex2
	3- mount it: mount linux.ex2 /mnt/mnt1 -o loop=/dev/loop0     # or just -o loop ?

	_______:  with losetup with encrypting --> see exp in man losetup !?
##________________________________________  ___________________________


#####  ==========  mounting:
	- /proc/mounts , /proc/self/mountinfo : all mounted devs
	- man findmnt
	- Disk-IDs/UUIDs/...: 
		ll  /dev/disk/by-*  #-eg  /dev/disk/by-id  , by-path ...
		ll  /dev/mapper ;
		blkid  /dev/sda6
	- mounting fat32 from cmd/root : mount -o users,uid=u1,gid=users,dmask=0002,fmask=0113  /dev/sda1 /media/LacieP1/
	- iso files mounting: mount -o loop -t iso9660 <isofilename> <mountpoint>
	--- NFS-/NW-mountings:
		- mount.nfs  nas2:/volume1/    /up1/media/nas2-d1
		- NTFS-handling in Lx:   man  ntfsprogs + ntfs-3g + mswin-nts
		  eg. for ntfs/vfat from root for users: mount  -o uid=u1,gid=users,umask=002  /dev/sda2 /mnt/usb2
##________________________________________  ___________________________


#####  ==========  swaps:
- setting a partition as swap partitions:
	- mkswap -f /dev/hda5 && swapon  /dev/hda5

	_______:  adding a swap-file fot the system: (see suse-ref-10.3-CH.2.15):
    -- Procedure 2.1 Adding a Swap File Manually:
    To add a swap file in the running system, proceed as follows:
    1- Create an empty file in your system. For example, if you want to add a swap file
    with 128 MB swap at /var/lib/swap/swapfile, use the commands:
    mkdir -p /var/lib/swap
    dd if=/dev/zero of=/var/lib/swap/swapfile bs=1M count=128
    2- Initialize this swap file with the command
    mkswap /var/lib/swap/swapfile
    3- Activate the swap with the command
    swapon /var/lib/swap/swapfile
    To disable this swap file, you use the command
    swapoff /var/lib/swap/swapfile
    4- Check the current available swap spaces with the command
    cat /proc/swaps
    Note, that at this point this is only temporary swap space. After the next reboot,  i>
    (5-) To enable this swap file permanently, add the following line to /etc/fstab:
    /var/lib/swap/swapfile swap swap defaults 0 0

	_______:  short again: adding temporary swap space by creating a temporary swap file (eg 300 MB):
	- dd if=/dev/zero of=tempswap bs=1k count=300000
	- chmod 600 tempswap
	- mke2fs tempswap
	- mkswap tempswap
	- swapon tempswap
##________________________________________  ___________________________


#####  ==========  misc/cmds/....:
- what is the FS-type of a not mounted medium??:
	- file - < /dev/hdc1  /OR
	- blkid /dev/sda1
