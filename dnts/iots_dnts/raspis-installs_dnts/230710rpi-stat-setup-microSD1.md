___________________ raspi1 , first raspi install on microSD, later renamed the formal-ID to  230710rpi ___________________
- hostname :  raspi1  , evv-IDs renamed later to 230710rpi !
- full-desktop-image-install on microSD-32GB ! + Home-Assistant ...


#####  ==========  users+PWs... done on ca1-raspi  /:230710 :

    - OS: u1 a...1  , (defaults-evv1-NBs)
    - homeassist:  u1  + a...1
    --- samba server installed with the share:   /g11_share/  pointing to physical: /share1/ :
        - OS-user for samba/guest-user  g11 :  useradd -c "anonym1-samba1"  g11   ##--OS-PW-g11: "ghgh11" /:230802  ##--2do: nologin!
        - smbpasswd  -a  g11  ---> PW:  "smbpw1"    ##--you need INLY the samba-PW for the share-mount, not-OS-PW  ;
        - on client eg:    smbclient  -L  192.168.43.113   --user=g11%smbpw1    ##-bzw mount/thunar :  smb://192.168.43.113/g11_share/
##________________________________________  ___________________________


#####  ==========  /:230710 :  install-Raspi-OS / DW , SD1-ca1--full-desktop-raspi--230710rpi :

	- DW: Lv13-HDD :  /up1/media/HDD11/T1_HD1/nps/Raspis_DWs
	- manually installed from arx1 to microSD:   dd bs=4M if=....  of=...microSD-card...  , OK!
	https://www.raspberrypi.com/software/operating-systems/  bzw.   http://rpf.io/downloads
	- see Ref-manual : Appendix A : Install an operating system to a microSD card  /bzw.  https://www.raspberrypi.com/software/
	--
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
    --- cmds,...:
    rpi-imager   ##--raspi-impager (to SDcard /usb/...)
##________________________________________  ___________________________


#####  ==========  /:230713 :  boot stuff
        --- eeprom /firmware uodate (was all uotodate!):
    u1@raspi1:~ $ sudo  rpi-eeprom-update  -a
    BOOTLOADER: up to date
       CURRENT: Wed 11 Jan 2023 05:40:52 PM UTC (1673458852)
        LATEST: Wed 11 Jan 2023 05:40:52 PM UTC (1673458852)
       RELEASE: default (/lib/firmware/raspberrypi/bootloader/default)
                Use raspi-config to change the release.

      VL805_FW: Dedicated VL805 EEPROM
         VL805: up to date
       CURRENT: 000138c0
        LATEST: 000138c0
    u1@raspi1:~ $ date
    Thu 13 Jul 2023 09:50:55 PM CEST
        ---
##________________________________________  ___________________________


#####  ==========  /:230712 :  zigbee in hass Integration:

    Success!
    Created configuration for TI CC2531 USB CDC, s/n: __0X00124B000E0EAA9E - Texas Instruments.
    We found the following devices:
    Zigbee Coordinator
    ZNP = Texas Instruments Z-Stack ZNP protocol: CC253x, CC26x2, CC13x2 (ZHA)
##________________________________________  ___________________________


#####  ==========  done coll on raspi1-ca1 (just coll...) /:230700 :
    --- vim :
    apt list vim*
    sudo  apt remove vim-tiny
    sudo apt install vim-runtime
    sudo apt install   vim-gtk3
    sudo apt install   vim-python-jedi
    ---
##________________________________________  ___________________________


