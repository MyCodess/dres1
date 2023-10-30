____________________ HDs/Partitions/Medias/ .... ad1 ________________________
##________________________________________  ___________________________


#####  ==========  utils-HDs/parts:
	- parted  von termux oder busybox
	- gdisk is NOT available by termux-packages ! so use parted; OR fdisk partly works obv. there either!? og then  /system/bin/sgdisk from android !
	- /system/bin/sgdisk  von andorid-itself
##________________________________________  ___________________________


#####  ==========  partitions/HDs/Discs/Medias:
	https://forum.xda-developers.com/android/general/info-android-device-partitions-basic-t3586565

	_______:  - Parts-Mgm-utils:
	-!! fdisk may not fully support GPT partition table, thus in case yours is GPT, it’s recommended to use Parted instead. 
	-!! fdisk executes your commands only when changes are saved whereas Parted executes them instantly.
	- fdisk and/or parted can be installed either with busybox or better termux !
	--- parted (for GPTs better than fdisk! hier from termux) :
	-!! "-l" did NOT work with parted or fdisk !! and also not other dev-pathes! so use eg: fdisk /dev/block/mmcblk0 
	- parted ! (fdisk originally was for MBR!  internal-eMMC is GPT and not MBR !! so use parted  installed by termux , maybe also ib busybox):
		parted   /dev/block/mmcblk0
		-!!!  did NOT work for me with "-l" , or with no params !! so use as  parted   /dev/block/mmcblk0 !!
	--- fdisk: not working "-l" ! so :  /sbin/.magisk/busybox/fdisk  /dev/block/mmcblk0   ##---then print !

	_______:  parts-HDs-infs , dev-pathes-eMMC, ... :
	!!  ll /dev/block/platform/13540000.dwmmc0/by-name/     !! --> you see partion-IDs and partion-names/labels !!  13540000.dwmmc0 varies depending on the device or installation !
	!!  cat   /proc/partitions
	cat   /proc/...
	getprop | grep xxx

	_______:  HDs/Parts/Medias:
	export  PATH=$PATH:/sbin/.magisk/busybox: ;
	su - ;   blkid  ; fdisk -l ; parted ; gdisk ....
	lla  /sys/dev/block/
##________________________________________  ___________________________


#####  ==========  mounts...:

	_______:  "/" root-fs : is ONLY in RAM, so NO-physical storage/media!! as /proc/ , /sys/ or /run/ !! :
	Pseudo / Virtual / in-Memory Filesystems (Kernel space): These filesystems don't rely on a physical persistent storage but just live in RAM, to provide kernel services interfaces in user space.
- internal shared storage:  /sdcard/  bzw.  /storage/emulated/0/    ##--!!- sdcard is internal-card!!  so  sdcard <--> extSDCard  !
- stat:   cat /proc/mounts  ;  blkid  | sort ; cat   /proc/partitions ;
-!! remounting /system as rw :
	- adb shell;  su - root;   mount -o rw,remount /system   ##--!!- "adb remount" did not work! due to not working of  "adb root" !!
	"adb remount" is same as:      adb shell mount -o rw,remount  /system
	- back again tot ro after work done:     mount -o ro,remount  /system
	- /OR do it directly on the device with termux + granted-root-privalage/Magisk-Manager !
- WPs-nts: /fstab , mountable parts, ...:
	Partitions with Mountable Filesystems :Following partitions are mounted during boot process:
	system, vendor, odm, userdata (mounted at /data), cache, cust, persist (mounted at /persist or /mnt/vendor/persist), modem (mounted at /firmware or /vendor/firmware_mnt), dsp (mounted at /dsp or /vendor/dsp) Modem is formatted as vfat while all others are usually ext4 or f2fs on newer devices.
	All of these are listed in /fstab.* file which is processes by init. Starting with Android 8.0 (Treble release), fstab.* is moved to /vendor/etc/ and system, vendor and odm entries are included in dtb.
	https://forum.xda-developers.com/android/general/info-android-device-partitions-basic-t3586565
##________________________________________  ___________________________


#####  ==========  FSs/FIleSystems-ad1:
	cat /proc/filesystems		#-->  Supported filesystems by your kernel
