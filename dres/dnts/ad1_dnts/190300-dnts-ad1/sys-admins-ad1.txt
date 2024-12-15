_____________________andorid-System-as-a-Linux-OS-dnts : ___________________________
##________________________________________  ___________________________


#####  ==========  cu1-cmds-qck/profile1-qcks-uue1 onn GS5-1903 :

	_______:  cuue-env-call-on-adh1  :
	adb shell;   su - ;  .   /sdcard/00rd1/up1/.cuue/etc/users/profile_adh1.sh     ##--just to be able to find/load the bash !!
	bash  ;  .  /sdcard/00rd1/up1/.cuue/etc/profile.sh    ;  promptlong

	_______:  push/pull/cp qcks:  x13-->adh1 :
	- all-kk in  /sdcard/00u/
	u1@x13$   adb  push  /up1/.cuue/etc/users/profile_adh1.sh   /sdcard/00u/up1/.cuue/etc/users/

	_______:  olds/prev--pre-cuue-setup
	.  /sdcard/0wks1/profile-ad1.sh             ##--olds:  /storage/3829-15F7/0wks/profile-ad1.sh 
	u1@x13: /up1/w/docs_m/devres/devnts/ad1-dnts/ $   adb push  profile-ad1.sh    /sdcard/0wks1/
	su - u0_a154   ;  cd  /data/data/com.termux/files/home/
##________________________________________  ___________________________


#####  ==========  SYS-infos-nts:

	_______:  SYSInfosAll-queries/infs, always check! :
	-!! cat  /proc/.... , as   /proc/mounts  /proc/cpuinfo  /proc/filesystems , .... 
	-!! lla  /sys/....  , as  /sys/dev/block/  ,   /sys/f/  ,  
	- getprop | sort  | grep -i  xxx

	_______:  SYS_DIRs-nts-ad1:
	-  main-system-root is    /system/  !
	- /bin/* stuff is in mainly  /system/bin  !
	- apps-UserData in  /data/  bzw.  /storage/3829-15F7/Android/data/

	_______:  CPU/Processor-query : - CT:  x13> adb shell --> uname -a /OR cat /proc/cpuinfo  /OR  getprop ro.product.cpu.abi  /OR getprop | grep abilist ;#/OR   per app:  AIDA64  (siehe ct.de/yxuv).

	_______:  UtilsSYS-/HWs-queries:
	- Utils-HW-Infos:  AIDA64 !!;
##________________________________________  ___________________________


#####  ==========  props:
	- getprop  , setprop
	- init will read the system properties from /default.prop , /system/build.prop , /system/default.prop , /data/local.prop (not-all-there!)  !  GS5-org-only  /default.prop , /system/build.prop !
	-  /default.prop  is overwritten on bootup, copied from the boot partition, which is not a directly accessible file system! so even with "remount rw" makes no use!! it will be overwritten by reboot from boot.img !!
	- /system/default.prop can be edited by "mount -o ro,remount  /system " !
	- To get a privileged shell you need to modify the following lines to the given values in the default.prop file:   ro.secure=0  ,  ro.debuggable=1  ,  persist.service.adb.enable=1
##________________________________________  ___________________________


#####  ==========  SYSTree-/SYSDIRs-infs, Dir-Structure + Permissions-dazu:
	-! vocab:   Device Tree Blob (DTB) - created by DT Compiler (DTC) from DT Source (DTS) : see  /proc/dev*/  bzw.  https://forum.xda-developers.com/android/general/info-boot-process-android-vs-linux-t3785254
	-!!  Apps-shared-Storage:  The root of the shared storage between all apps: /storage/emulated/0/  ,bzw. in termux    ~/storage/shared
##________________________________________  ___________________________


#####  ==========  SELinux-ad1:
	-!! checkit if your device is enforced to keep SElinux limitations/access-controls?:   getenforce
	--- SELinux :
		- https://en.wikipedia.org/wiki/Security-Enhanced_Linux
		- To put SELinux into enforcing mode: $ sudo setenforce 1  ##--no-effekt on android!
		- To query the SELinux status:     $ getenforce
