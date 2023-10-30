_____________________ npad/tr-ad1     : ___________________________________________
--################################## olds/prev/....: ###################################################
##________________________________________  ___________________________


#####  ==========  test-dirs, where is what persistent?? after reboot are there?? :
shell@s5neolte:/ $ su -
root@s5neolte:/ # id
uid=0(root) gid=0(root) groups=0(root) context=u:r:magisk:s0
root@s5neolte:/ # pwd
/
root@s5neolte:/ # date
Mon Feb 25 09:50:26 CET 2019
root@s5neolte:/ # mount | grep -i /dev
/dev/block/platform/13540000.dwmmc0/by-name/SYSTEM    		/system    ext4    ro,seclabel,relatime,norecovery    0    0
/dev/block/platform/13540000.dwmmc0/by-name/EFS    			/efs    ext4    rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,data=ordered    0    0
/dev/block/platform/13540000.dwmmc0/by-name/CACHE    		/cache    ext4    rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,errors=panic,data=ordered    0    0
/dev/block/platform/13540000.dwmmc0/by-name/USERDATA    	/data    ext4    rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,data=ordered    0    0
/dev/block/platform/13540000.dwmmc0/by-name/PERSDATA    	/persdata/absolute    ext4    rw,seclabel,nosuid,nodev,relatime,data=ordered    0    0
/dev/block/platform/13540000.dwmmc0/by-name/CPEFS    		/cpefs    ext4    rw,seclabel,nosuid,nodev,noatime,data=ordered    0    0
/dev/block/platform/13540000.dwmmc0/by-name/SYSTEM    		/sbin/.magisk/mirror/system    ext4    ro,seclabel,relatime,norecovery    0    0
/dev/block/platform/13540000.dwmmc0/by-name/USERDATA    	/sbin/.magisk/mirror/bin    ext4    rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,data=ordered    0    0
/dev/block/vold/public:179,33    		/mnt/media_rw/3829-15F7    vfat    rw,dirsync,nosuid,nodev,noexec,noatime,nodiratime,uid=1023,gid=1023,fmask=0007,dmask=0007,allow_utime=0020,codepage=437,iocharset=iso8859-1,shortname=mixed,utf8,errors=remount-ro    0    0
/dev/block/vold/public:179,33    		/mnt/secure/asec    vfat    rw,dirsync,nosuid,nodev,noexec,noatime,nodiratime,uid=1023,gid=1023,fmask=0007,dmask=0007,allow_utime=0020,codepage=437,iocharset=iso8859-1,shortname=mixed,utf8,errors=remount-ro    0    0
root@s5neolte:/ #
root@s5neolte:/ # mkdir  /system/d11 && chmod 777 /system/d11 ;		--> error:   mkdir: '/system/d11': Read-only file system
root@s5neolte:/ # mkdir  /efs/d11 && chmod 777    /efs/d11 ;		##--OK-reboot
root@s5neolte:/ # mkdir  /cache/d11 && chmod 777  /cache/d11 ;		##--OK-reboot
root@s5neolte:/ # mkdir  /data/d11 && chmod 777   /data/d11 ;		##--OK-reboot
root@s5neolte:/ # mkdir  /persdata/absolute/d11 && chmod 777 /persdata/absolute   ##--OK-reboot
root@s5neolte:/ #
