_________________ EW1-rapi1-LIVE / 230806rpi-stat-usb-ca1.md , ca1-raspi1 for caH1/home1 : ________________



#####  ==========  _1RZ + _m1  : 2del...:
    i1 + "qw....3"
    u1 + "we....4"
##________________________________________  ___________________________



#####  ==========  stats-shorts:
    ssh i1@raspi1  bzw.  ssh i1@192.168.178.48
    hass:  http://raspi1:8123/   bzw.  http://192.168.178.48:8123/
    --
    - main-user: i1
    - feste IP ueber LAN in Fritzbox:  192.168.178.48 !
    - WLAN NOT eingerichtet/ not-active !
    - ! installed on USB-stick 64GB , old-Med1_RF (!! NICHT erkannt bei allen usb3-schnittstellen !!)
    - image: full-raspi : 11GB ,  2023-07-09 21:16 2023-05-03-raspios-bullseye-armhf-full.img , Release date: May 3rd 2023 , System: 32-bit , Kernel version: 6.1 ,  Size: 2,701MB ;
    - uname -a  ##-  Linux raspi1 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:16 BST 2023 aarch64 GNU/Linux
##________________________________________  ___________________________


#####  ==========  /:230806 :  install :
    /up1/media/HDD11/T1_HD1/t1var/cpd-nps_1p/Raspis_DWs
    unxz 2023-05-03-raspios-bullseye-armhf-full.img.xz

    _______:  dd ... on arx1 : usb-stick attached to arx1/Lv13 :
    [root@2209arx Raspis_DWs]# date;  dd if=2023-05-03-raspios-bullseye-armhf-full.img   of=/dev/sdb  bs=8M ; date
    2023-08-06T18:17:30 CEST
    1310+0 records in
    1310+0 records out
    10989076480 bytes (11 GB, 10 GiB) copied, 319,106 s, 34,4 MB/s
    2023-08-06T18:22:50 CEST
    [root@2209arx Raspis_DWs]# lsblk1 /dev/sdb
    NAME        FSTYPE FSVER LABEL  UUID                                 FSAVAIL FSUSE% MOUNTPOINTS                                                        SIZE TYPE
    /dev/sdb                                                                                                                                              57,9G disk
    ├─/dev/sdb1 vfat   FAT32 bootfs 1F81-6E1F                                                                                                              256M part
    └─/dev/sdb2 ext4   1.0   rootfs 616fc5f0-b611-4063-96f4-e6fdf0317c2d

    _______:  HEADLESS-configs (without KB/Monitor !):
    #- see:  - !! https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi :
    - !! MUST  USER + SSH + NW  !! :
    - mount /dev/sdb1  /mnt/t1  ##--mount now the usb-boot-part/sdb1/part1 and put file userconf.txt there containing one line:
    1 - NW is ok (LAN-connected/cable), otherwise MUST put a wpa-file there in part1/ ...; but here with LAN-Cable , OK!
    2 - user (i1) : vi  /mnt/t1/userconf.txt  ##--contains one-line:  i1:<enc-PW/output-of: openssl passwd -6 >
    3-  sshd-start-during-boot:  touch  /mnt/t1/ssh  /mnt/t1/ssh.txt   ##put an empty flag-file in SD /boot/ "touch /boot/ssh or ssh.txt"  : When this file is present, SSH will be enabled on boot.
    -! for firts-boot WAIT a few minutes (uo to 5) !!: it resizes the part-2 and re-configure-himself (it was only dd ! but converts to running system !)

    _______:  first boot-configures:
    i1@raspberrypi:~ $ sudo  hostnamectl  set-hostname  raspi1
    -- ssh-key to  i1@raspberrypi:
    [u1@2209arx ~]$ ssh i1@192.168.178.48  ##--if needed remove the old-host-key of u1 known_hosts
    i1@raspberrypi:~ $  mkdir  ~/.ssh ; chmod 700 ~/.ssh ;
    [u1@2209arx .ssh]$ scp id_all_u1.pub  i1@192.168.178.48:.ssh/authorized_keys 
    [u1@2209arx ~]$ ssh i1@192.168.178.48  ##--if u1 ssh-agent was not running, you could start it ! easier !
    ##--if-liked-u1-on-raspi  !? i1@raspberrypi:~ $ sudo  useradd  -m -U -u 1501  u1 ; ##--leave the group empty ! it generates u1 group! OK!  #+ ssh-stuff for u1 ! but here NIT done yet !
    -- updates:
    sudo raspi-config ; ##--esp.:  hostname,  time-zone, WLAN-country (is under localizations! not onlly WLAN-configs!), ...: go through ALL-points once !
    sudo apt-get update ; sudo apt-get upgrade -y ; sudo reboot ;
    sudo rpi-eeprom-update -a ;
    vi /etc/profile  ##-- alias   ##-- alias evv1set="source /up1/.cev/etc/profile.sh"
    dpkg-query -l | grep -i vim ;     sudo  apt remove   vim-common  vim-tiny ... ; sudo apt-get install vim-gui-common vim-gtk3 ;
    sudo apt-get install  rpi-imager ;
    - add-pkgs...:
    sudo apt-get install hwinfo

    _______:  first-configs/evv1 ... :
    --- up1-stuff (nicht einbinden in profile! call manually always with an alias there! !! take python/prj-profiles OUT of evv !!)
    i1@raspberrypi:~ $ sudo mkdir /00Dir1 ;  sudo chown i1:i1 /00Dir1 ;  chmod 777 /00Dir1
    [u1@2209arx bups1_loc]$ scp up1_2209arx_tz--230714-185526  i1@192.168.178.48:/00Dir1/
    tar -xzvf ... ; mv ./up1  /up1/ ; vi /up1/.cev/etc/profile.sh  ##-: commentOut prj0prof ....  (!! python,...!) ; ##-also: hostname instead hostnamectl... !
    since no extra T1FS-part, then mkdir for all links there in /up1/mnt/... ; so physically there! but leave the links as they are, so that cdxxx/aliases/pathes still work!
    esp.  mkdir /up1/mnt/VARUfs/varu/varau  before installing anything, because all python packages will be looking for the pyc-dir there !!
    rm /up1/t1 ; mkdir /up1/t1 ; rm /up1/w1 ;  mkdir /up1/w1 ; rm /up1/varu/ ; mkdir /up1/varu/  ;
    mkdir -p /up1/t1/sy1/2307rpi  /up1/t1/sy1/2307rpi/logs /up1/t1/sy1/2307rpi/bups /up1/t1/sy1/2307rpi/stat_2307rpi  /up1/t1/sy1/2307rpi/stat_2307rpi/configs/ /up1/t1/sy1/2307rpi/stat_2307rpi/HW-Infs   
    so all links/pathes under /up1/ must "formally" work ! but they are all on root-part ! ok!

    --- pkgsListings:
    cdlla /up1/t1/sy1/2307rpi/logs ;
    i1@raspi1:/00Dir1/pkgsListings $ dpkg-query  -l   |  grep  ^i    >|  instPkgs-list-oneLiners---dpkg-query_list.log
    i1@raspi1:/00Dir1/pkgsListings $ dpkg-query  -f '${binary:Package}---Stat1::${db:Status-Status}\n'  -W  | sort | fgrep -i "Stat1::installed" | sed 's/---.*//' >|   instPkgs-list-onlyNames---dpkg-query_list.log
    i1@raspi1:/00Dir1/pkgsListings $ apt-cache  pkgnames | sort >|  allPkgs-list-namesOnly---apt-cache_pkgnames.log
    i1@raspi1:/00Dir1/pkgsListings $ apt list            | sort >|  allPkgs-list-stat---apt_list.log
    hwinfo --short >> hwinfos.log ; el1d >>  hwinfos.log ; hwinfo  >> hwinfos.log ;
    -
    el1d  >> $syysTgStats_dntsFP ;  uname -a >> $syysTgStats_dntsFP ;  el1d  >> $syysTgStats_dntsFP ;  hostnamectl   >> $syysTgStats_dntsFP ;  sudo rpi-eeprom-update -a   >> $syysTgStats_dntsFP ;

 

#####  ==========  Home-Assistant-install /:230807  :
    i1@raspi1:~ $ python -V ; ## Python 3.9.2 ; wa py-3.10 angefordert, aber so OK!
    root@raspi1:~# apt-get  python3-dev ; sudo apt-get update ; sudo apt-get upgrade -y ; 
    sudo apt-get install -y python3 python3-dev python3-venv python3-pip bluez libffi-dev libssl-dev libjpeg-dev zlib1g-dev autoconf build-essential libopenjp2-7 libtiff5 libturbojpeg0-dev tzdata ffmpeg liblapack3 liblapack-dev libatlas-base-dev
    sudo useradd -rm homeassistant -G dialout,gpio,i2c
    sudo mkdir /srv/homeassistant ;  sudo chown homeassistant:homeassistant /srv/homeassistant ;
    sudo -u homeassistant -H -s ;
    cd /srv/homeassistant ; python3 -m venv . ; source bin/activate ;
    python3 -m pip install wheel ;
    pip3 install  homeassistant  ##--org-Anleitung was :   homeassistant==2023.8.1 ;
    had to also as homeassistant :  mkdir /home/homeassistant/.homeassistant  ##--not in Anleitung!
    --- done ! manaulay call: hass& ##--but prefere with systemd , dur to reboots-autostarts ! : see  iot-apps.md  dnts here, short:
    vi  /etc/systemd/system/home-assistant@homeassistant.service ##.. seet entries there ...!
    sudo systemctl --system daemon-reload ; sudo systemctl enable home-assistant@homeassistant ;
    sudo systemctl start home-assistant@homeassistant ;  sudo systemctl status home-assistant@homeassistant ;  ---> CHECK status !!
    http://raspi1:8123/  bzw.  http://192.168.178.48:8123/
##________________________________________  ___________________________


################################## coll-stats,...: #################################
#####  ==========  DW-image-raspi
    --
    image: full-raspi : 11GB ,  2023-07-09 21:16 2023-05-03-raspios-bullseye-armhf-full.img :
    Raspberry Pi OS with desktop and recommended software
    Release date: May 3rd 2023
    System: 32-bit
    Kernel version: 6.1
    Debian version: 11 (bullseye)
    Size: 2,701MB
    Show SHA256 file integrity hash:
    67abd3bc034faf85b59b8e4a28982cb0ab1bc0504877ec3d426e05f6402ed225
    Release notes
    --
##________________________________________  ___________________________


#####  ==========  stats-logs-shorts...:
    ---
    i1@raspi1:~ $ sudo rpi-eeprom-update -a   
    BOOTLOADER: up to date
       CURRENT: Wed 11 Jan 17:40:52 UTC 2023 (1673458852)
        LATEST: Wed 11 Jan 17:40:52 UTC 2023 (1673458852)
       RELEASE: default (/lib/firmware/raspberrypi/bootloader/default)
                Use raspi-config to change the release.

      VL805_FW: Dedicated VL805 EEPROM
         VL805: up to date
       CURRENT: 000138c0
        LATEST: 000138c0
    ---

##________________________________________  ___________________________

