__________________ System_backups-nts-ad1 : ______________________________________________
##________________________________________  ___________________________


#####  ==========  ??

	_______:  full-HD-image-works??
	- dd  :  adb shell 'dd if=/dev/block/mmcblk0 2>/dev/null' > mmcblk0.img  ##/OR just login and dd ... to-sdcard ... ??
	-??adb-direct??:   adb pull /dev/block/mmcblk0 mmcblk0.img    ##--sagte-is-ok:  https://stackoverflow.com/questions/29442630/copy-full-disk-image-from-android-to-computer
