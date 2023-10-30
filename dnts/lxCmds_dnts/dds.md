__________ dd , dd-mbr/system-backups, OS-imaging/cloning with dd __________
##________________________________________  ___________________________


#####  ==========  dd : also dd-backups for partitions, disks,....
-- dd with USR1 signal for infos: 
	dd if=/dev/hdb1 of=/dev/hda1 bs=4096& pid=$! ;
	while true ; do kill -USR1 $pid; date; sleep 10; done
--! ----------- UnixToolbox.htm --> 14.5 dd : "MBR tricks":
#   The MBR contains the boot loader and the partition table and is 512 bytes small,
#   The first 446 are for the boot loader, the bytes 446 to 512 are for the partition table.
#	So with MBR-Backups with dd:
# dd if=/dev/sda of=/mbr_sda.bak bs=512 count=1       # Backup the full MBR
# dd if=/dev/zero of=/dev/sda bs=512 count=1          # Delete MBR and partition table
# dd if=/mbr_sda.bak of=/dev/sda bs=512 count=1       # Restore the full MBR
# dd if=/mbr_sda.bak of=/dev/sda bs=446 count=1       # Restore only the boot loader
# dd if=/mbr_sda.bak of=/dev/sda bs=1 count=64 skip=446 seek=446 # Restore partition table
#-------------------- end-UnixToolbox.htm (see also next part in case GRUB was on source-disk)
--!! cloning-mbr-following-sectors if grub was on source-disk (works?? is sufficient? may be only for stage1):
	http://www.2pi.info/software/copying-windows-new-hard-drive.html
- kk: the first 64 sectors on disk (0-63) are always free for bootloaders+partitiontable...; so OS/partitions alwas start after 63 !!
	The first 446 are for the boot loader, the bytes 446 to 512 are for the partition table. up to 64th sector are free for bootloaders,...
... or if you also wish to copy the sectors following the MBR (sometimes containing GRUB stage 1.5 or other bootloaders), first copy the section before the partition table, then the remainder.
   This version copies the complete first track of 63 sectors into a file, and then copies the pieces to the target disk.
dd if=/dev/sdb of=mbr.img bs=512 count=63
dd if=mbr.img of=/dev/sdc bs=446 count=1
dd if=mbr.img of=/dev/sdc bs=512 skip=1 seek=1

	_______:  loop-setup, losetup
- see man losetup:
	The following commands can be used as an example of using the loop  device.
	# dd if=/dev/zero of=/file bs=1k count=100
	# losetup -e des /dev/loop0 /file
	Password:
	Init (up to 16 hex digits):
	# mkfs -t ext2 /dev/loop0 100
	# mount -t ext2 /dev/loop0 /mnt
	 ...
	# umount /dev/loop0
	# losetup -d /dev/loop0
