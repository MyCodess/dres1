________________________ HWs-infs, udev, /dev, HW-parts ..._______________________-
-!!  see also extra-dnts   kernelModules-arx   for treiber , /dev, ... !!
##________________________________________  ___________________________


#####  ==========  docs-WPs:
- devices list: /usr/src/linux-2.6.8-1.521/Documentation/devices.txt bzw. all-list in: http://www.kernel.org/pub/linux/docs/device-list/devices.txt
https://wiki.archlinux.org/index.php/Category:Hardware_detection_and_troubleshooting
##________________________________________  ___________________________


#####  ==========  /proc/ devices-modules-infs :
- /proc for devices:
	- /proc/devices : You can see that a device driver has registered itself in the file /proc/devices.
	- /proc/devices <-> /etc/sysconfig/hwconf ; Kudzu maintains a complete profile of all your installed hardware devices in the /etc/sysconfig/hwconf
	- /proc/interrupts : You can see that the device driver is handling the device's interrupts in /proc/interrupts.
	- /proc/net/dev : currently registered network device names in /proc/net/dev
##________________________________________  ___________________________

#####  ==========  BIOS/UEFI/Firmware infs ....:
    - !!  /sys/class/dmi/id/  : all BIOS-suff all kept there by kernel !!
        - eg:  cat /sys/class/dmi/id/bios_date : update-date-of-bios-SW !
        - cat  /sys/class/dmi/id/board_name  ##--Motherboard-ID
    - BIOS-infos:   hwinfo --bios  #-/OR  sudo dmidecode -t bios
	- pacman -Ss dmidecode  ##--dmidecode  is  a  tool for dumping a computer's DMI (some say SMBIOS) table contents in a human-readable format. 
	- eg:  Lv13--serial-nr:   sudo dmidecode -t system | grep Serial  ;#-baseboard serial number:  sudo dmidecode -t baseboard | grep Serial ; https://pcsupport.lenovo.com/de/en/solutions/HT510152
##________________________________________  ___________________________

#####  ==========  cmds-utils-HWs :
	- pacman -Syu  hardinfo  hwinfo lshw  lsusb lspci
	- lspci  -k
	- my Graphic card ??:   lspci | grep -e VGA -e 3D
	- is my processor is x86_64 compatible?  grep -w lm /proc/cpuinfo   ##- long-mode:  If your processor is x86_64 compatible, you will have the lm (long mode) flag in /proc/cpuinfo    , https://wiki.archlinux.org/index.php/Frequently_asked_questions

	_______:  benchmark HDDs/USBs/SSD/..., USB-drives/sticks tempos : 
	kdiskmark (with GUI for HDD/SDD/USB) , fio , hardinfo , hwinfo, hyperfine, 
	win10-CT : Tempo von USB-Laufwerken messen:  https://www.heise.de/select/ct/2019/11/1558361239648902 , c't 11/2019 S. 160 : winsat disk -drive g: ##
##________________________________________  ___________________________


#####  ==========  SSDs / Trim :

	_______:  can my SSD do TRIM ?? verify TRIM support on your SSD : https://wiki.archlinux.org/index.php/Solid_state_drive :
	$ lsblk --discard
	And check the values of DISC-GRAN (discard granularity) and DISC-MAX (discard max bytes) columns. Non-zero values indicate TRIM support. (0B means null, so NO-TRIM-support !)
	Alternatively, install hdparm package and run:
	hdparm -I /dev/sda | grep TRIM  ##--but did not work for Lv13-SSD !?
##________________________________________  ___________________________


#####  ==========  beep ton in console / Disable_PC_Speaker (no-Sound-System!! just the simple-primitive speaker, also in Bios available):
	-!!!  https://wiki.archlinux.org/index.php/PC_speaker#Disable_PC_Speaker  ,  Disable PC Speaker  :
	- Beep is an advanced PC speaker beeping program. It is useful for situations where no sound card and/or speakers are available, and simple audio notification is desired. 
	--- Globally 	: The PC speaker can be disabled by unloading the pcspkr kernel module: # rmmod pcspkr
	- Blacklisting the pcspkr module will prevent udev from loading it at boot: # echo "blacklist pcspkr" > /etc/modprobe.d/nobeep.conf
	- Blacklisting it on the kernel command line is yet another way. Simply add modprobe.blacklist=pcspkr to your bootloader's kernel line.
	--- Console : 
	You can add this command in /etc/profile or a dedicated file like /etc/profile.d/disable-beep.sh: setterm -blength 0
	Another way is to uncomment or add this line in /etc/inputrc or ~/.inputrc: set bell-style none
	--- Less pager : 
	To disable PC speaker in less pager, you can launch it with less -q to mute PC speaker for end of line events or less -Q to mute it altogether. For man pages, launch man -P "less -Q" or set the $MANPAGER or $PAGER environment variables.
	Alternatively, you can add these lines to your ~/.bashrc:
	alias less='less -Q'
	alias man='man -P "less -Q"'
	--- Xorg :
	$ xset -b
	You can add this command to a startup file such as /etc/xprofile to make it permanent. See xprofile for more information. 
	--- GNOME:    $ gsettings set org.gnome.desktop.wm.preferences audible-bell false
##________________________________________  ___________________________


#####  ==========  
--################################ UDEVs : ######################################################--
##________________________________________  ___________________________


#####  ==========  
	https://wiki.archlinux.org/index.php/Udev
	https://wiki.archlinux.org/index.php/Udisks
	man  systemd-udevd.service(8) , udev
	man udisks 
##________________________________________  ___________________________


#####  ==========  cmds-udev: (udev is part of systemd ):
	systemctl   status  systemd-udevd.service
	- dev-info-query:    udevadm  info  /dev/video0     ##--eg: vido-camera/webcam-info  /OR:
	- dev-info-details, with devPath-query:    udevadm info --attribute-walk --path=$(udevadm info --query=path --name=/dev/video0)
	- path-query:   (udevadm info --query=path --name=/dev/video1
	- List the attributes of a device:     udevadm info --attribute-walk --name=device_name
	- Testing rules before loading/enabling:   udevadm test /sys/class/backlight/acpi_video0/    ##--/OR:   udevadm test $(udevadm info --query=path --name=device_name) 2>&1
	- monitoring udev-ENV-changes...:  devadm monitor --environment --udev
##________________________________________  ___________________________


#####  ==========  confs/pathes/....-udev :
	https://wiki.archlinux.org/index.php/Udev  :
	- If there are two files by the same name under /usr/lib and /etc, the ones in /etc take precedence.
	/usr/lib/udev/rules.d/ 	:  OS-/default-System-rules ---> most-/main-rules !!
	/usr/lib/udev/
	/etc/udev/rules.d/ 		:  Admin-/users-/locally-added-rules  -->  takes precedence !!
	/etc/udev/
	- udev rules written by the administrator go in /etc/udev/rules.d/, their file name has to end with   .rules.
	- The udev rules shipped with various packages are found in /usr/lib/udev/rules.d/.
	- If there are two files by the same name under /usr/lib and /etc, the ones in /etc take precedence.

	_______:  NEW rules : alwas LIVE !!:
- udev automatically detects changes to rules files, so changes take effect immediately WITHOUT requiring udev to be restarted.
- However, the rules are not re-triggered automatically on ALREADY existing devices. so:
- Hot-pluggable devices, such as USB devices, will probably have to be reconnected for the new rules to take effect, or at least unloading and reloading the ohci-hcd and ehci-hcd kernel modules and thereby reloading all USB drivers.
- manually force udev to trigger your rules:   udevadm trigger [devpath|file|unit]   ## see man udevadm
- 
