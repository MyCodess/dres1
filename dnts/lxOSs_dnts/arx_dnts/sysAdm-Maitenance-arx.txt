____________ system maintenance admin (also see admin extra special files as: usersMgm, kernelParams, bootProccess,... !! hier the rest!! _____________________
##________________________________________  ___________________________


#####  ==========  
https://wiki.archlinux.org/index.php/System_maintenance
https://wiki.archlinux.org/index.php/Migrate_installation_to_new_hardware (cloning-syss)
https://wiki.archlinux.org/index.php/Migrating_between_architectures (eg_1kk: on usbStick to x13 and Lv13 , xps17)
##________________________________________  ___________________________


#####  ==========  UEFI/secure-boot/BIOS/grubs/...
	-! see extra nts in .../dnts/lxSys/booties-grub-bios-uefi-HDsParts-lx .... and also here in installs-clones-DIR !
##________________________________________  ___________________________


#####  ==========  suspend /systemd-suspend , powerMgm/suspend/hibernate/acpi/....
	- for NON-systemd-approches see arx-docs (acpid, kernel direct access, ...); here mainly systemd-suspend (is higher level approch than acpid/kernel-files/...):

	_______:  
	https://wiki.archlinux.org/title/Power_management
	https://wiki.archlinux.org/title/Power_management/Suspend_and_hibernate#systemd
	man systemd-sleep , systemd-sleep.conf ,  systemd-suspend.service  systemd-logind.service

	_______:  suspend-problem of syys/2209arx/2004arx on usb-stick (obv. NO gut solution! immer wieder crash ! so disable fully !?!?):
	- disabling fully suspend !?!?:  https://wiki.archlinux.org/title/Power_management#Disabling_suspend
	- hobernate instead suspend?? for hibernate anyway a swap part/file is required! but hibernate !?!? not tried !
	- probably due to usb-strom/switched-off/... !?!? 
	- ???

	_______:  systemd-sudpend :
	https://wiki.archlinux.org/title/Power_management#Power_management_with_systemd
	systemd-logind

	_______:  cmds systemd suspends :
	-! man systemctl  ##--/suspend .... ; systemd-suspend.service  is statically loaded !
	- suspend:   systemctl  start  systemd-suspend.service ; systemctl suspend ;

	_______:  configs systemd suspends :

	_______:  disabling suspend/hibernate fully for OS:
	https://wiki.archlinux.org/title/Power_management#Disabling_suspend :
	mkdir /etc/systemd/sleep.conf.d ;  vi /etc/systemd/sleep.conf.d/uue1-sleep.conf ; ##-: set all Allow-lines to no and uncomment them!
	/OR: but not good:  vi /etc/systemd/sleep.conf  ...
	- to apply changes: either reboot /OR systemctl kill -s HUP systemd-logind ; and restart it again
##________________________________________  ___________________________


#####  ==========  chroot :
-!! https://wiki.archlinux.org/index.php/Chroot

	_______:  chroot manually (not using arch-chroot):
Using chroot
Warning: When using --rbind, some subdirectories of dev/ and sys/ will not be unmountable. Attempting to unmount with umount -l in this situation will break your session, requiring a reboot. If possible, use -o bind instead.
In the following example /location/of/new/root is the directory where the new root resides.
First, mount the temporary API filesystems:
# cd /location/of/new/root
# mount -t proc /proc proc/
# mount --rbind /sys sys/
# mount --rbind /dev dev/
And optionally:
# mount --rbind /run run/
Next, in order to use an internet connection in the chroot environment copy over the DNS details:
# cp /etc/resolv.conf etc/resolv.conf
Finally, to change root into /location/of/new/root using a bash shell:
# chroot /location/of/new/root /bin/bash
# source profiles...
Tip: Optionally, create a unique prompt to be able to differentiate your chroot environment:
# export PS1="(chroot) $PS1"
# ..... work done ...., then
When finished with the chroot, you can exit it via:
# exit
Then unmount the temporary file systems:
# cd /
# umount --recursive /location/of/new/root

	_______:  
##________________________________________  ___________________________


#####  ==========  timedate-sync/setting:

	_______:  infs:
	- VOCAB:  RTC-time==BIOS-time==hardware-clock-time==Firmware-clock-time
	-! decide first if BIOS-/RTC-time should be Local-time (MsWin) / OR UTC-time (Linux) , see below, but take UTC /Lx-defailt !
	-! man timedatectl , hwclocl , systemd-timesyncd (==systemd-simple-NTP-client-only, not NTP-server)
	-!  LPI.org-learning-dc/LPIC1-102-500/learning.lpi.org/en/learning-materials/102-500/108/108.1/index.html

	_______:  timezone setting:
	- ln -s  /usr/share/zoneinfo/Europe/Berlin  /etc/localtime ;##--if not already there!
	-/OR with systemd (does the same):  timedatectl  set-timezone Europe/Berlin  ##--or list them: timedatectl list-timezones |  grepi berlin
	-!! not-globally, but only in a shell/terminal switching: export  TZ='America/Chicago' ; ... 

	_______:  DIFF /nts:   MsWIn  <--->   Lx  timedate:
	- By default, MsWindows assumes the Firmware-time is stored in local time, while Linux assumes the Firmware-time is stored in UTC time and applies an offset.
	- MsWIn consider BIOS-time as local-time (eg Berlin, which is UTC+1)
	- Linux consider BIOS-time as UTC---time (so Greenwitch, UTC+-0 )
	- Your PC stores the time in a hardware clock on its motherboard. The clock keeps track of time, even when the computer is off. By default, Windows assumes the time is stored in local time, while Linux assumes the time is stored in UTC time and applies an offset. This leads to one of your operating systems showing the wrong time in a dual boot situation.
	- To fix this, you have two options: Disable RTC in Linux, or make Windows use UTC time. Don’t follow both steps of instructions or they still won’t be speaking the same language! We recommend you make Linux use local time, if possible.
	- Disable RTC-/BIOS-time taken as UTC-time on Linux, but read it as localtime :
	  timedatectl set-local-rtc 1 --adjust-system-clock    ; ##--so now knows Linux that BIOS-time is localtime and Not-UTC and so does NOT add the offset of +2 or so to it!! due to MsWIn--Lx-Time-confilicts !!

	_______:  SET-/Korrigieren-time-on-Lx-oneLiner/short  (for both system+bios) :
	timedatectl set-local-rtc 0      ##--bios is UTC (Lx-default)
	timedatectl   set-time  "2023-04-03 18:25:00"   ##--it sets/korrigiert  BOTH: bios + system/OS
	check all:  timedatectl  status

	_______:  SET/-timedate-more:   Bios to UTC/Linux-default and systemd-NTP-service active if wanted (can do ALL from LinuxOS):
	- timedatectl set-local-rtc 0     ##--is default in Lx, if not changed, and means BIOS is UTC ! otherwise see below!
	- /Either manually set time with date -e /or timedatectl set-time ...;
	- /OR NTP-client:  systemd-NTP-client if wanted :  systemctl enable  systemd-timesyncd  ; timedatectl set-ntp true ; 
	- can also set BIOS/RTC-time from OS:  hwclock  --systohc ;
	- check settings: timedatectl  status

	_______:  -- LONGer descp:
	- is BIOS localtime (mswin) --->  timedatectl set-local-rtc 1 --adjust-system-clock    ; 
	- is BIOS UTC--time (Linux) --->  timedatectl set-local-rtc 0 ;

	_______:  either BIOS shows  UTC-time (Linux-default) and set OS-system-time:
	- set BIOS-time manually to UTC/Greenwitch-time and,
	- either manually withOuT NTP:   hwclock --hctosys /OR  date -s ...; /OR timedatectl set-time ...
	- or per NTP-client, see below
	- if needed (but is default):   timedatectl set-local-rtc 0 --adjust-system-clock ; hwclock  --systohc /OR --hctosys ; 

	_______:  /OR BIOS-time set to Local-time (MsWin):
	- set BIOS-time manually to localtime/Berlin
	- inform OS-Linux that BIOS has local-time and NOT UTC-time :  timedatectl set-local-rtc 1 --adjust-system-clock ;
	- either set the linux-time manually or from bios/hwclock to localtime/Berlin (linux default is: BIOS shows UTC time! so you have to set localtime here manually) and do:
	- eg manually with date -s ... /OR  with timedatectl  set-time (which also updates RTC/HWclock/Bios-Time !!)

	_______:  NTP-sync-service if wanted , eg with NTP-client/SNTP of systemd :
    - quick-onlyOnceSync:  systemctl start systemd-timesyncd.service ##-done! checkit with timedatectl ; systemctl stop systemd-timesyncd.service
	- eg  systemd-NTP-client :   timedatectl set-ntp true ; systemctl  enable/start/status  systemd-timesyncd   ##-- check settings: timedatectl  status
	- more-cmds if needed:   timedatectl set-local-rtc 0 --adjust-system-clock ; hwclock  --systohc /OR --hctosys ; 
	- check-it:  timedatectl show-timesync --all ; systemctl status systemd-timesyncd ; timedatectl  status ; timedatectl   timesync-status ;
	-!nts:  If your Linux distribution uses timedatectl, then by default it implements an SNTP client rather than a full NTP implementation. This is a less complex implementation of network time and means that your machine will not serve NTP to other connected computers.
	In this case, SNTP will not work unless the timesyncd service is running. As with all systemd services, we can verify that it is running with: systemctl status systemd-timesyncd  ; ##-- LPI.org-learning-dc/LPIC1-102-500/learning.lpi.org/en/learning-materials/102-500/108/108.1/108.1_02/index.html

	_______:  MsWin force to UTC of BIOS-time (checkIt! not tried!):
	- deactivate first auto-time-update-over-internet/ntp : Settings > Time & language -->  disable “Set time automatically”. 
	- REG: in HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation\  create new key:
	Right-click the “TimeZoneInformation” key and select New > DWORD (32-bit) Value , name: RealTimeIsUniversal and set its value to 1 
##________________________________________  ___________________________


#####  ==========  cupsd printers:

	_______:  cmd-coll:
journalctl -xeu cups.service     ##--problems-tracing!
systemctl status/start/show/stop   cups.service
systemctl list-unit-files  | grepi cups

	_______:  adding u1/gu1 to cupsd-admins : 2chk!!:
to add users/gu1 to cupsd-admins:
1-  obv. is sufficient adding the gu1 group to "SystemGroup" in cups-files.conf as (checked, OK /_220205 ):
	SystemGroup sys root wheel gu1
	#- so it add obv. the gu1 group to the cupsd-admins !
2- obv. it also works in cupsd.conf replacing "Require user @SYSTEM ... " with "Require valid-user"  ##--so an valid-system-user is cupsd-admin, as:
	Require valid-user   ##--1org:   Require user @SYSTEM
###############  coll-cmds-sysAdm--All: ################################################
- timedatectl   set-time  "2022-12-19 14:23:00"  ##--I-updates both OS+RTC/BIOS !
- time-seting-status of the System/PC:		timedatectl status  ##--man  timedatectl - Control the system time and date

	_______:  SUID/SGID/...:
- find files with SUID set :  find /usr/bin -perm -4000 ; #/OR  sudo find /usr/bin -perm -u+s ; #(minus-sign in perm means mindestens...! so find files having the special permission and other permissions )
- find files with SGID set :  find /usr/bin/ -perm -2000  #/OR find /usr/bin/ -perm -g+s 
- find files with SUID or SGID set :  find /usr/bin -perm /6000
	--- nts to find -perm:
	-perm value   :  find files having the special permission exclusively
	-perm -value  :  find files having the special permission and other permissions
	-perm /value  :  find files having either of the special permission (and other permissions)

	_______:  
