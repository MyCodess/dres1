___________________________ 230714rpi-setup-stat+coll-dnts ! install-raspiOS on USB32 and boot from usb on raspi /:230715  :  _______________________________
- raspi lite install on USB-Stick (vendor = Kingston,  model = DataTraveler 3.0) on ca-raspi(Raspberry Pi 4 Model B Rev 1.1)
    --- infs-kurz / hwinfo :
    Hardware	: BCM2835 , Platform: "BCM2835"  (?? BCM2711 , https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/ )
    Revision	: c03111
    Serial		: 10000000bc4515b2
    Model		: Raspberry Pi 4 Model B Rev 1.1
    ---


#####  ==========  users+PWs... done on ca1-raspi  /:230710 :

    - OS: u1 +  a...1  , r.. + 1a.....q2 (defaults-evv1-NBs)
##________________________________________  ___________________________


#####  ==========  raspi-image to USB-stick (230714rpi), install-raspiOS-on usb-stick, 32GB, USB3-Datatraveler,  raspi-OS lite:
    [u1@2209arx Raspis-nps1]$ unxz  2023-05-03-raspios-bullseye-armhf-lite.img.xz
    --- dd :
    [root@2209arx Raspis-nps1]# date;  dd  bs=4M   if=./2023-05-03-raspios-bullseye-armhf-lite.img   of=/dev/sdc  ; date
    2023-07-14T18:14:07 CEST
    469+0 records in
    469+0 records out
    1967128576 bytes (2,0 GB, 1,8 GiB) copied, 208,338 s, 9,4 MB/s
    2023-07-14T18:17:35 CEST
    [root@2209arx Raspis-nps1]# 
    - 
    /dev/sdc                                                                                                              28,8G disk
    ├─/dev/sdc1            vfat   FAT32 bootfs      9E81-4F92                                                              256M part
    └─/dev/sdc2            ext4   1.0   rootfs      cf2895ca-6dc2-4797-8040-f76ba1508f41                                   1,6G part

    --- on raspi, bootloader/firmware/eeprom-update :
    - if NW-actice, then first bootloader-update, otherwise then later:
        - raspi >4 bootloader is on EEPROM/firmare/HW and NOT as earlier on filesystem as “bootcode.bin” !
        sudo rpi-eeprom-update -a  ##--man   rpi-eeprom-update  / rpi-eeprom-config ...
        /OR  sudo raspi-config  #--> “Advanced Options“ -->“Bootloader Version” --> E1 Latest ...
        /OR also by:  rpi-imager ... 
    - set bootloader to USB-first-then-SD :   raspi-config  --> usb-boot  --> shutdown
    - reboot
    
    --- USB-stick attached to raspi --> boot , all-OK! did: auto-resizing of the OS-part , PARTUUID for boots, ...! --> shutdown
        maybe here the created first user NOT u1, but i1, and later manually create u1 with the right ID/evv1 !?
        but this time u1 had to be recreated with theright ID !
    
    --- back to arx for copys of evv,...:
    attached to arx1 to copy some stuff (later have to chown u1:u1 ...):
    mount  /dev/xxx   /mnt/t1/ ; mkdircd /mnt/t1/00Dir1 ; chown  -R   u1:gu1   /mnt/t1/00Dir1  ##--later must chown again anyway on raspi, due to its group ...!
    copys: evv1/up1.tgz , vi wpa_supplicant for WLan, vi /etc/profile bashrc
    cp:  u1-arx1-ssh-pubKeys to u1-rpi1
    [ not really, later on raspi have to re-create u1 with 1501 !  so ??:  vi ./etc/passwd : u1 ID:group  sett to 1501:1501 ?? but also home-dir,..! so lieber recreate u1 on raspi!)
    - for WLAN do/see raspi_dnts#wlan bzw. https://www.raspberrypi.com/documentation/computers/configuration.html#using-the-command-line ! (but here some info if ...: configure wpa for your wlan now !  cpde  /mnt/t1/etc/wpa_supplicant/wpa_supplicant.conf ; cat /etc/wpa_supplicant/1q_1kk_SHy_A3S_wpa1.conf  >>  /mnt/t1/etc/wpa_supplicant/wpa_supplicant.conf )
    vide-org  /mnt/t1/etc/bash.bashrc ##--add:   export  q_Host1full=230714rpi ; source  /up1/.cev/etc/profile.sh ;
        ##???:  vide-org   /mnt/t1/etc/profile  ##--add evv to it! ausreichend?? oder .bashrc ...??
    so:
    [u1@2209arx stat_2209arx]$ lla /mnt/t1/00Dir1/arx1/
    drwxrwxr-x 2 u1 gu1   4096 2023-07-14 19:18 u1-ssh-pubs/
    -rw-rw-r-- 1 u1 gu1  15659 2023-07-09 09:33 230709-093316_systemModifieds_2209arx.tgz
    -rw-r--r-- 1 u1 gu1 134937 2023-07-14 18:55 up1_2209arx_tz--230714-185526
    -rw-rw-r-- 1 u1 gu1  15531 2023-07-09 09:33 userss-configSubs-home--230709-093315.tgz
    - unpack up1 as u1 there and:  mvi /mnt/t1/00Dir1/arx1/up1  /mnt/t1/

    -- nts to image: no-XWin ! lite !
    Raspberry Pi OS Lite
    Release date: May 3rd 2023
    System: 32-bit
    Kernel version: 6.1
    Debian version: 11 (bullseye)
    Size: 364MB
    Show SHA256 file integrity hash:
    b5e3a1d984a7eaa402a6e078d707b506b962f6804d331dcc0daa61debae3a19a 
    [u1@2209arx Raspis-nps1]$ ll
        -rw-rw-rw- 1 u1 gu1 1,9G 2023-07-14 09:35 2023-05-03-raspios-bullseye-armhf-lite.img
        -rw-rw-rw- 1 u1 gu1 381558864 2023-07-14 09:35 2023-05-03-raspios-bullseye-armhf-lite.img.xz
##________________________________________  ___________________________


#####  ==========  boot usb-stick on raspi-device and basic updates/configs  /:230715 :
    --- boot, ok! must reconfigure wlan/wpa-configs in /etc/...  and restart it with :  sudo  systemctl   restart   dhcpcd.service  wpa_supplicant.service
        check with journalctl if problems! also ip link (wlan0 must be up),....
    --- login as root (/OR it not possible  login as u1 or pi, then sudo -i, then set root pw, then relogin as root) and: re-create user u1 (due to its ID ...)
    userdel -r u1 ; useradd  -m -U -u 1501  u1 ; ##--I left the group as u1 ! ok for raspi! there are no other evv-users !
    --- ! /up1 :
    since no extra T1FS-part, then mkdir for all links there in /up1/mnt/... ; so physically there! but leave the links as they are, so that cdxxx/aliases/pathes still work!
    esp.  mkdir /up1/mnt/VARUfs/varu/varau  before installing anything, because all python packages will be looking for the pyc-dir there !!
    so all links/pathes under /up1/ must "formally" work ! but they are all on root-part ! ok!
    check that all major cdxxx work !
    mkdir also syystg-tree !!
    !! chown u1:u1 -R /up1/
    -- raspi-config  ##--if needed ... 
    --- generate pkgs-logs in /up1/t1/sy1/230714rpi/logs  of installed-/all-pkgs !
    ---pkgs 1:
    apt purge vim-tiny
    apt install vim-runtime
    apt autoremove
    apt update
    apt full-upgrade
    - more pkgs??: if OS-Media-creation required:  apt install rpi-imager
##________________________________________  ___________________________


#####  ==========  pkgs more added ..1coll some ...:
    sudo apt-get install  rpi-imager
##________________________________________  ___________________________



############################## 1coll/logs/protocs/...: ###########################################


#####  ==========  /:230718 :  
    ---
    Tue 18 Jul 13:50:26 CEST 2023
    u1@230714rpi:/up1/t1/sy1/230714rpi/stat_230714rpi/HWs-infs $     uname -a
    Linux 230714rpi 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:16 BST 2023 aarch64 GNU/Linux
    ---
##________________________________________  ___________________________

#####  ==========  /:230715 :  BootLoader-/EEPROM-/Firmware-update:
Sat 15 Jul 13:49:06 CEST 2023

u1@230714rpi:~ $ sudo   rpi-eeprom-update  -a
*** INSTALLING EEPROM UPDATES ***

BOOTLOADER: update available
   CURRENT: Wed 11 Jan 17:40:52 UTC 2023 (1673458852)
    LATEST: Thu 11 May 06:26:03 UTC 2023 (1683786363)
   RELEASE: stable (/lib/firmware/raspberrypi/bootloader/stable)
            Use raspi-config to change the release.

  VL805_FW: Dedicated VL805 EEPROM
     VL805: up to date
   CURRENT: 000138c0
    LATEST: 000138c0
   CURRENT: Wed 11 Jan 17:40:52 UTC 2023 (1673458852)
    UPDATE: Thu 11 May 06:26:03 UTC 2023 (1683786363)
    BOOTFS: /boot
Using recovery.bin for EEPROM update

EEPROM updates pending. Please reboot to apply the update.
To cancel a pending update run "sudo rpi-eeprom-update -r".
u1@230714rpi:~ $ 

u1@230714rpi:~ $ sudo   rpi-eeprom-update  
BOOTLOADER: up to date
   CURRENT: Thu 11 May 06:26:03 UTC 2023 (1683786363)
    LATEST: Thu 11 May 06:26:03 UTC 2023 (1683786363)
   RELEASE: stable (/lib/firmware/raspberrypi/bootloader/stable)
            Use raspi-config to change the release.

  VL805_FW: Dedicated VL805 EEPROM
     VL805: up to date
   CURRENT: 000138c0
    LATEST: 000138c0
u1@230714rpi:~ $ date
Sat 15 Jul 14:39:35 CEST 2023

##________________________________________  ___________________________




