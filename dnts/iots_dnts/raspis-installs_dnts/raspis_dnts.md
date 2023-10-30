________________________ RaspBerryPI / RPI_dnts :_____________________________________
/:230806  :  ca1-EW1-full-install-on-usbStick_64GB--old_Med1_RF , full installs on USB + Boot-USB, OS-full-desktop (ca. 2 GB DW, 11 GB unpacked))
/:230714  :  full installs on USB + Boot-USB, OS lite, without XWin !
/:230710  :  full installs on SD + HomeAssit + lights + ... : full-check! 
/:220629  :  first short check!
##________________________________________  ___________________________

#####  ==========  docs/refs/links:
    https://www.raspberrypi.com/
    https://github.com/raspberrypi/
    https://github.com/raspberrypi/documentation
    http://raspbian.raspberrypi.org/raspbian/  ##--Repo/pkgs , /etc/apt/sources.list

    _______:  
    Power: 5 volts at 3 amps via USB Type-C  ##-manual
    -!! the default-user "pi" is obsolete now ! ab Bullseye/APr.2022 !
##________________________________________  ___________________________

#####  ==========  Headless install Raspberry (use/start your Raspberry Pi without a monitor or keyboard):
    - !! https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi
    - !! WLAN for first-boot: gleich nach imaging before first-boot put your own wpa_supplicant.conf in /boot/ (! incl. COUNTRY=DE) ! You will need to define a wpa_supplicant.conf file for your particular wireless network. Put this file onto the boot folder of the SD card. When the Raspberry Pi boots for the first time, it will copy that file into the correct location in the Linux root file system and use those settings to start up wireless networking. https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi
    - !! SSH  for first-boot: put an empty flag-file in SD /boot/ "touch /boot/ssh or ssh.txt"  : When this file is present, SSH will be enabled on boot. The contents don’t matter, it can be empty. SSH is otherwise disabled by default. https://www.raspberrypi.com/documentation/computers/configuration.html#the-boot-folder
    - ! gleich schon bei Image-Creation: also WLAN + SSH + USERs can be mit-configured !! see above link !
##________________________________________  ___________________________


#####  ==========  installs-dnts:
    - ! see here individual "syys"-instal-dnts! here just more+general infos,...
    - ! CT-Special, c't Raspi-Toolbox 2022.April, p.26 Raspi superschnell einrichten ! c't Raspi-Toolbox 2022, S. 026
    - ! https://www.raspberrypi.com/documentation/computers/getting-started.html
    - arx rpi-imager install:  AUR !
    - Auto-Install/NW-Install without imaging vorher!:  https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-over-the-network 
        - just: 1-attach raspi to KB+Monitor+NW-Kabel, 2-put an EMPTY SD-card into it, 3-[press SHIFT +]and turn raspi on /attach power !
        You can also start network install by holding SHIFT when powering on the device.
##________________________________________  ___________________________

#####  ==========  user-add ...:
    https://www.raspberrypi.com/documentation/computers/configuration.html#changing-your-username
    old-user-defaults-in-manual_RF (Pi <4) :  ‘pi’ user + ‘raspberry’  (but 1kk took u1! pi obv not setuped !)
    sudo adduser  u1
    sudo usermod -a -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi   u1
    check:   sudo su - alice
##________________________________________  ___________________________

#####  ==========  raspi-config :
    - ! https://www.raspberrypi.com/documentation/computers/configuration.html#the-raspi-config-tool
    - Navigation-Arrows:
        - right : arrow key will jump out of the Options menu and take you to the <Select> and <Finish> buttons.
        - left  : will take you back to the options.
        - TAB   : Alternatively, you can use the Tab key to switch between these.
        - ESC   : exit / goback
    - cmdline options/calls:   sudo raspi-config  nonint <options/params>   ##--!see  https://www.raspberrypi.com/documentation/computers/configuration.html#the-raspi-config-tool
    - 
##________________________________________  ___________________________

#####  ==========  NWs-/WLANs-raspi:
    _______: Network Interface Names (set to eth0 / wlan0 , ... : predictable): https://www.raspberrypi.com/documentation/computers/configuration.html#the-raspi-config-tool :
    - Enable or disable predictable network interface names:   sudo raspi-config nonint do_net_names <0/1>  ##-- 0 - Enable predictable network interface names 1 - Disable predictable network interface names
    - checkit: ip link   ##--must see  eth0 / wlan0 , ... 

    _______:- WLAN config:
    https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-networking
    https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line
    - ! WLANs + SSH can also be set/configured directly by Imaging to the SD/USB ! see advanced-options of rpi-imager !!
    - steps:
    first right COuntry-COde / locale, due to frequences for wlan!! raspi-config --> locale  #/and-or-check:  vi /etc/wpa_supplicant/wpa_supplicant.conf :must contain:  country=DE  ##--reuired to choose the right Frequences !!
    sudo iwlist wlan0 scan
    wpa_passphrase "a3s-wl1"  |  sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf   ##--added your wlan1-stuff there! password-gen-with:  wpa_passphrase ...; delete the commented PW there !
    if hidden wlan, add:  scan_ssid=1  to the output of wpa_passphrase /wlan1-spec  !!
    if several NWs, can add  priority=nn to each wlan1-spec !  with the highest priority, will be the one that is connected !
    wpa_cli -i wlan0 reconfigure   ##--Reconfigure the interface 
    if needed:  sudo  systemctl   restart   dhcpcd.service  wpa_supplicant.service
    check if OK:  ifconfig wlan0  ## If the inet addr field has an address beside it, OK!  /OR:  ip r , ip addr , ...
##________________________________________  ___________________________

#####  ==========  ca1-device , __CP__-for-info-here : 
	Verpackung:   Raspberry Pi 4, Model B, 4GB RAM, + ioBroker :  ---> microSD defekt obv. !
	https://www.smart-home-komponente.de
	Verpackung von RPI-selber: RPI4-ARC-BL  , lieferant/shop:  sertronics.de
	?? Amazon buy ??:  https://www.amazon.de/-/en/Raspberry-Model-FHEM-Nano-Complete/dp/B07XVJR32J ,
##________________________________________  ___________________________

#####  ==========  bootLoader/boot-process-1: bootloader/firmware/BIOS/eeprom/usb-boot/bootloader-config/... (sprich ca. BIOS / UEFI of Raspis ):
    _______:
    - !! https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-boot-eeprom
         https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-bootloader-configuration
    - man   rpi-eeprom-update  / rpi-eeprom-config  / rpi-imager

    _______: nts:
    - !! raspi bootloader is in eeprom/firmware  AND  "BIOS-configs"/Video-Audio-firmware-configs are in a file /boot/config.txt :
    - !! Raspberry Pi 4, 400, Compute Module 4, and Compute Module 4S computers use an EEPROM to boot the system. All other models of Raspberry Pi computer use the bootcode.bin file located in the boot filesystem.
    - raspi >4 bootloader is on EEPROM/firmare/HW and NOT as earlier on filesystem as “bootcode.bin” !
    - Raspberry Pi uses a configuration file (/boot/config.txt) instead of the BIOS you would expect to find on a conventional PC.  https://www.raspberrypi.com/documentation/computers/config_txt.html#what-is-config-txt
    - ! firmware loader (start.elf and its variants) is responsible for loading the DTB (Device Tree Blob - a machine readable DT file) + config.txt is scanned for user-provided parameters, ... , Finally it launches the kernel, passing a pointer to the merged DTB. https://www.raspberrypi.com/documentation/computers/configuration.html#device-trees-overlays-and-parameters
    - ! The kernel and firmware are installed as a Debian package, and so will also get updates by apt update/upgrade !
    - ! If moving an existing SD card to a new Raspberry Pi model (for example the Raspberry Pi Zero 2 W), you may also need to update the kernel and the firmware first using the aapt update/upgrade !

    _______: boot-load-process Pi4 :
    - ! https://www.raspberrypi.com/documentation/computers/configuration.html#the-boot-folder , https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-boot-eeprom
    - onboard EEPROM (Firmware/BIOS)  --> /boot/start*A  (configurable by config.txt)  --> kernel7l.img (kernel image for Pi4)
        - Pi < 4 : instead EEPROM : /boot/bootcode.bin :
        Raspberry Pi 4, 400, Compute Module 4, and Compute Module 4S computers use an EEPROM to boot the system. All other models of Raspberry Pi computer use the bootcode.bin file located in the boot filesystem.
    - cmds:  rpi-eeprom , llinpath eeprom

    _______: firmware-update / bootloader-/eeprom-update:
    - ! https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-4-boot-eeprom
    - before updating bootloader/eprom full updates : sudo apt update ; sudo apt full-upgrade ;  reboot
    - sudo rpi-eeprom-update -a  ;  reboot   ##-- can do it also by  raspi-config  /OR  rpi-imager !see above limk !
    - /OR Using Raspberry Pi Imager to update the bootloader !
    - /OR pre-any-raspi-installs:
        neuste firmware-zip for SD-card/*.sd.* downloaden unter https://downloads.raspberrypi.org/net_install/beta/ ,
        unzip it , dd to sd-card , boot raspi with it, it auto-updates the firmware ! (grünes Lämpchen schnel blinken!); take it out and do your normal install raspi ...! see CT-Special-2204-p.36 !
        links for firmware-DW: https://www.heise.de/select/ct-wissen/2022/4/softlinks/wrkm?wt_mc=pred.red.ct.sh_wissen042022.034.softlink.softlink
    
    _______: eeprom/BIOS--show/config/edit/... : 
    https://www.raspberrypi.com/documentation//computers/raspberry-pi.html#updating-the-eeprom-configuration  :
    - show cu BIOS/eeprom/bootloader-configs:   sudo rpi-eeprom-config  /OR   sudo  vcgencmd bootloader_config 
    - backup BIOS : rpi-eeprom-config  --out  boot1.conf
    - edit eeprom configs:   sudo -E rpi-eeprom-config --edit  ##-!! any exits still puts new eeprom-updates in /boot/ for next reboot to update it! to cancel this:  sudo rpi-eeprom-update -r
        but also, If the updated configuration is identical or empty then no changes are made ! so fine !
    - Auto-updates of firmware/BIOS/Bootloader:
        sudo  systemctl  status rpi-eeprom-update.service
        disable auto-firmware-update  :  sudo systemctl mask   rpi-eeprom-update
        enable  auto-firmware-update  :  sudo systemctl unmask rpi-eeprom-update
    
    _______: boot-order /  USB-boot (stick/HDD/SDD/Mass-Media/...):
    - ! https://www.raspberrypi.com/documentation//computers/raspberry-pi.html#BOOT_ORDER
    - ! https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot
    - !! default is: first-SD-then-USB ! so, NOT needed do anything ! since: if wanted USB-boot, then just leave microSD-slot empty ! done ! but here infos to re-order:
    - ! Pi 4B : support USB boot by default !! (although the BOOT_ORDER bootloader configuration can be modified, but default is anyway first-SD-second-USB !).
    - sudo raspi-config nonint do_boot_order <B1/B2/B3>  ##--:
        B1 - SD Card Boot - Boot from SD Card if available, otherwise boot from USB
        B2 - USB Boot - Boot from USB if available, otherwise boot from SD Card
        B3 - Network Boot - Boot from network if SD card boot fails
    - /OR GUI:  sudo raspi-config  ##--> Then choose Advanced Options -> Boot Order -> USB Boot ; Restart to apply the changes. --> reboot
    - check it : rpi-eeprom-config   ##--> must see BOOT_ORDER=0xf14  :which is USB-first ! see above link for boot order codes !
        BOOT_ORDER = 0xf14 : Try USB first, followed by SD then repeat ; 0xf41  :  Try SD first, followed by USB-MSD then repeat (default if BOOT_ORDER is empty)
##________________________________________  ___________________________

#####  ==========  boot / kernels , ... :
    _______: boot-options/boot-files / boot-folder:  /boot/config.txt , /boot/cmdline.txt , ... :
        - !!  https://www.raspberrypi.com/documentation/computers/config_txt.html#boot-options  :
        - /boot/config.txt   :  MAIN-boot-options
        - /boot/cmdline.txt  :  Kernel-Params ; this filename can be changed/set in config.txt with cmdline="..." option !
        - /boot/kernel8.img  :  Kernel itself for raspi-4
        - /boot/ folder      :  https://www.raspberrypi.com/documentation/computers/configuration.html#the-boot-folder
        - boot files are stored on the first partition of the boot-media (SD card /USB-Stick) , which is formatted with the FAT file system.

    _______: Kernel-Params:
        - https://www.raspberrypi.com/documentation/computers/config_txt.html#boot-options  :
        - kernel-params in /boot/cmdline.txt OR/AND the rest in /boot/config.txt); this filename can be reset/renamed with "cmdline=..." entry in /boot/config.txt !

    _______: Tools-configs :   raspi-config , vcgencmd get_config ...
    _______: /boot/config.txt :
        - ! reboot required for changes to take effekt !! config.txt is proccessed ONLY during boot !
    _______: Kernel-Compiling:  https://www.raspberrypi.com/documentation/computers/linux_kernel.html
##________________________________________  ___________________________

#####  ==========  OSs/Sys/Admins/...:
    -! https://www.raspberrypi.com/documentation/computers/os.html
    _______: pkgs/...:
    - update all pkgs:  sudo apt update ;  sudo apt full-upgrade ;
    - ! auto-update-service (fo all pkgs): see CT-Special-RAspi-2204-S.102-106 : Auto-update anpassen !
##________________________________________  ___________________________


#####  ==========  troubleshooting/Admin-Maintains/justierens/....:
    - !! strom-versorgungs-probleme !?!?:  dmesg | grepi "Under-Voltage"   
##________________________________________  ___________________________

#####  ==========  HWs :
    - DEF: A Device Tree (DT) is a description of the hardware in a system ...; A Device Tree represents the hardware configuration as a hierarchy of nodes. 
    - https://www.raspberrypi.com/documentation/computers/configuration.html#device-trees-overlays-and-parameters

    _______: cmds-HWs:
    - my aarchitecture/processor/CPD:  lscpu   ##--he architecture reported by lscpu is armv7l for systems running a 32-bit kernel (i.e. everything except kernel8.img), and aarch64 for systems running a 64-bit kernel.
    - vcgencmd - query the VideoCore for information ##-- https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd , vcgencmd commands , man vcgencmd
##________________________________________  ___________________________

#####  ==========  NAS / Ext-HDD :
    _______: Ext-HDD :
    - ! https://www.raspberrypi.com/documentation/computers/configuration.html#external-storage-configuration
    - ! Raspberry Pi OS Lite does NOT implement automounting.
    - ! 90 seconds could take long to list a newly attached HDD to raspi! see link above to change it ! (systemd)
    - sudo apt install ntfs-3g
    - ! fstab FAT / NTFS :  If the filesystem type is FAT or NTFS, add ,umask=000 immediately after nofail - this will allow all users full read/write access to every file on the storage device.
##________________________________________  ___________________________

#####  ==========  ssh-connecting-raspi:
    - ! https://www.raspberrypi.com/documentation/computers/remote-access.html  : ssh + scp + rsync + NFS + samba + ...

    _______: enable/activate sshd on raspi :
        - !! for headless-raspi /first-boot :  touch  /boot/ssh or ssh.txt : When this file is present, SSH will be enabled on boot. The contents don’t matter, it can be empty. SSH is otherwise disabled by default. https://www.raspberrypi.com/documentation/computers/configuration.html#the-boot-folder
        - /OR systemd /systemctl enable/start sshd ... /OR
        - /OR sudo raspi-config nonint do_ssh  1   ##--0 - Enable SSH 1 - Disable SSH   ##--see https://www.raspberrypi.com/documentation/computers/configuration.html#the-raspi-config-tool
        - /OR raspi-config --> GUI, sshd
        (GUI: Preferences --> raspi-config ...)
	- on arx1:  IP query of raspi1-host:  nmap -sn 192.168.43.0/24
	- ssh -X u1@192.168.43.113 ; sapi]  mkdir ~/00Dir1 ;
	- scp ./up1__tz--221004-210906  u1@192.168.43.113:./00Dir1/

    _______: for key-login-ssh :
    - on raspi1:  mkdir ~/.ssh ; chmod 700 .ssh ;
    - on arx: scp    ~/.ssh/id_rsa.pub  ~/.ssh/id_ed25519.pub   u1@192.168.43.113:./.ssh/
    - on raspi:  cd  ~/.ssh/ ; cat *pub >>  authorized_keys ; chmod 600 authorized_keys ;

    _______: cpd-from-ssh_dnts:   X-forwarding (eg openning a terminal on the server/raspi1 and get its window on the clien/arx1 opened):
    - X-forwarding MUST be activated on both sides, client/ssh + server/sshd:
    - server/sshd/raspi1:  On the server side, X11Forwarding yes must be specified in /etc/ssh/sshd_config
    - server:   the xauth program must be installed on the server side.
    - client/arx1:  call ssh -X ...  /OR configure it as your ssh-client-default:  ForwardX11 yes in ~/.ssh/config
    - client, if needed:   xhost +   ##--/OR xhost <only your-server...>...
    - !! NO DISPLAY setting required!:  Note that you do not need to set any environment variables on the server. DISPLAY and XAUTHORITY will automatically be set to their proper values. If you run ssh and DISPLAY is not set, it means ssh is not forwarding the X11 connection.
    - checkit eg open terminal:  /etc/alternatives/x-terminal-emulator
    - check it with -v if problems ...:  ssh  -X  -v   u1@192.168.43.113

    _______: so: To get X11 forwarding working over SSH, you'll need three things in place:
        Your client must be set up to forward X11.
        Your server must be set up to allow X11 forwarding.
        Your server must be able to set up X11 authentication.

    _______: manual :
    https://www.raspberrypi.com/documentation/computers/remote-access.html
    hostname:  raspberrypi bzw.  raspberrypi.local  (mDNS/Multi-DNS)
##________________________________________  ___________________________

#####  ==========  NW-Shares /NFS /Samba /VNC /remote-connections ... :
    -! https://www.raspberrypi.com/documentation/computers/remote-access.html
##________________________________________  ___________________________

#####  ==========  security / ... :
    - !  https://www.raspberrypi.com/documentation/computers/configuration.html#securing-your-raspberry-pi
##________________________________________  ___________________________

#####  ==========  CTs-RaspberryPI:
    CT-Special-Raspi-2204 : c’t Raspi-Toolbox 2022.April , c't Special
    CT-OL-27.06.2022---RaspberryPi-Windows10-2206.pdf  : Raspberry Pi: Windows 10 installieren - so klappt's Von Anna Kalinowsky am 27. Juni 2022
    CT-OL-27.06.2022 : https://www.heise.de/tipps-tricks/Raspberry-Pi-Windows-10-installieren-so-klappt-s-4456283.html
    c't 2021/22 Seite 170  : ioBroker  :   Steuerungssoftware ioBroker als Docker-Container in Betrieb nehmen
    c't 2021/20 Seite 162  : ioBroker  :  Smart-Home-Steuerungssoftware ioBroker: modernere Oberfläche, breitere Geräteunterstützung, leichtere Fehlersuche
    c't 2021/17	:  Upcycling mit dem Raspi,
    c't 2021/16-032 	:  Raspi mit Windows 11 Ja, das geht !
    c't 2021/09	:  Raspi als Profi-Werkzeug
    c’t 2019/15--014 :  Raspberry Pi 4: Test & Praxis
    CT-OL-02.03.2019  :  Windows 10 auf dem Raspberry Pi (+ Video, sehr lang! 2 Std, unter: ct.de/y8ka ):  https://www.heise.de/ct/artikel/Windows-10-auf-dem-Raspberry-Pi-4321822.html
##________________________________________  ___________________________

#####  ==========  MsWin-on-RPI :
    c't 16/2021--32     :  Raspi mit Windows 11 Ja, das geht ! :
    https://www.worproject.com
    https://uupdump.net  :  Downloadpaket für Windows 11 für die ARM64-Plattform inklusive Updates
##________________________________________  ___________________________

#####  ==========  GPIOs:
    - https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header
##________________________________________  ___________________________

############################ trys1/done/... : ########################################################

############################ 1coll/....: #############################################################
#####  ==========  cmds-coll-all:
    terminal  :  lxterminal  ##-bzw.  /etc/alternatives/x-terminal-emulator -> /usr/bin/lxterminal
    _______: poweroff-schalter mit BüroKlammer/schalter/paperclip :
        - !!  mit einer Büroklammer ausschalten : https://maker-tutorials.com/raspberry-pi-mit-einer-bueroklammer-ausschalten-bzw-herunterfahren/
        - bzw. weitere links dazu:
        - Py:  https://github.com/TonyLHansen/raspberry-pi-safe-off-switch/
        - systemd activation: https://github.com/adafruit/Adafruit-GPIO-Halt ! 
        - https://magpi.raspberrypi.com/articles/off-switch-raspberry-pi  ;
    #!/usr/bin/env python3 , from gpiozero import Button , import os , Button(21).wait_for_press() , os.system("sudo poweroff") , 


#####  ==========  apt/dpkg-cmds_1coll : 
    apt  list  vim*  ##--lists AllPkgs, installed + not-Installed,  vim* pkgs !
##________________________________________  ___________________________


