___________________ IoT-Apps/portals/Protocols/Zigbee/,... mainly on Raspi: ____________________________


#####  ==========  ZigBees:
    https://en.wikipedia.org/wiki/Zigbee
##________________________________________  ___________________________


#####  ==========  /:230711 :  Home Assistant done on raspi1 / 230710rpi on microSD-card;
    - https://www.home-assistant.io/installation/raspberrypi
    - create user:   u1 a...1
    - port:  8123 as in  http://192.168.43.113:8123/

    --- install hass-core ,manually on raspi4  : /:230712  :
    https://www.home-assistant.io/installation/raspberrypi#install-home-assistant-core  : manually-insall-hass-on-raspi 
    - instaled manually exact steps as:  https://www.home-assistant.io/installation/raspberrypi#install-home-assistant-core  -- ohne updates and ohne homeass-version-number! all ok!
    prereq:  Python 3.10 (including the package python3-dev) or newer.  (on raspi yet still py-3.9)
    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get install -y python3 python3-dev python3-venv python3-pip bluez libffi-dev libssl-dev libjpeg-dev zlib1g-dev autoconf build-essential libopenjp2-7 libtiff5 libturbojpeg0-dev tzdata ffmpeg liblapack3 liblapack-dev libatlas-base-dev
    sudo useradd -rm homeassistant -G dialout,gpio,i2c
    sudo mkdir /srv/homeassistant
    sudo chown homeassistant:homeassistant /srv/homeassistant
    sudo -u homeassistant -H -s
    cd /srv/homeassistant
    python3 -m venv .
    source bin/activate
    python3 -m pip install wheel
    pip3 install homeassistant==2023.7.1   bzw. here done:  pip3 install homeassistant
    - starting homeassistant :
        - either manually  :  hass&   ##--!!-but better for reboots, add to systemd :
        - /OR systemd routines adding (see below): https://community.home-assistant.io/t/autostart-using-systemd/199497
    hass-portal on port 8123  :  http://X.X.X.X:8123/

    --- restart hass manually (without systemd):
    u1@raspi1:~ $ sudo -u homeassistant -H -s
    homeassistant@raspi1:/home/u1 $ cd /srv/homeassistant
    homeassistant@raspi1:/srv/homeassistant $ source bin/activate
    (homeassistant) homeassistant@raspi1:/srv/homeassistant $ hass&
    hass-portal:  http://X.X.X.X:8123/

    --- systemd add if installed manually:
    The file will be called /etc/systemd/system/home-assistant@YOUR_USER.service
    https://community.home-assistant.io/t/autostart-using-systemd/199497 :
    vi /etc/systemd/system/home-assistant@<user-name-hass>.service ,so:  /etc/systemd/system/home-assistant@homeassistant.service :
    --
    [Unit]
    Description=Home Assistant
    After=network-online.target

    [Service]
    Type=simple
    User=%i
    WorkingDirectory=/home/%i/.homeassistant
    ExecStart=/srv/homeassistant/bin/hass -c "/home/%i/.homeassistant"
    RestartForceExitStatus=100
    ##--if-liked: Automatically restarting Home Assistant on failure , then add:
    Restart=on-failure
    RestartSec=5s

    [Install]
    WantedBy=multi-user.target
    --
    sudo systemctl --system daemon-reload ; sudo systemctl enable home-assistant@homeassistant ;
    sudo systemctl start home-assistant@homeassistant ;  sudo systemctl status home-assistant@homeassistant ;

    --- ZigBee ca1:
    - ZigBee :  https://www.home-assistant.io/integrations/zha/
    - ZHA (Zigbee Home Automation) integration allows you to connect many off-the-shelf Zigbee based devices directly to Home Assistant, using one of the many available Zigbee coordinators.
    u1@raspi1:~ $ lsusb | grepi zigbee
    Bus 001 Device 003: ID 0451:16a8 Texas Instruments, Inc. CC2531 ZigBee
##________________________________________  ___________________________


#####  ==========  /:230710 :  iobroker (/OR try extra/home-assistant !?) :
    https://www.iobroker.net/#de/documentation/install/linux.md
    linux-install:    curl -sLf https://iobroker.net/install.sh | bash -
    (stand auf dem Zettel -ca1: config über:  http://<ip-raspberry>:8081  , fragen: support@/www.smart-home-komponente.de )
    --- arx1:
    https://wiki.archlinux.org/title/Home_Assistant
    pacman -Ss home-assistant
##________________________________________  ___________________________


