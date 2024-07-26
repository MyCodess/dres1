___________________________ ca1-IoT-devices--testeing: ________________________


#####  ==========  ca1-Raspi Pi 4 B   /:230700 (gekauft 220700 ??) :

	Verpackung:   Raspberry Pi 4, Model B, 4GB RAM, + ioBroker :  ---> microSD defekt obv. !
	https://www.smart-home-komponente.de
	Verpackung von RPI-selber: RPI4-ARC-BL  , lieferant/shop:  sertronics.de
	?? Amazon buy ??:  https://www.amazon.de/-/en/Raspberry-Model-FHEM-Nano-Complete/dp/B07XVJR32J ,
    - serial-No: bc4515b2   ##--:  grep Serial /proc/cpuinfo  ##--->  Serial : 10000000bc4515b2
    
    --- hwinfo on raspi1:
    Platform (board):  Broadcom  "BCM2835",
    CPU:  4 core, Arch: ARM Vendor: "ARM Limited" Model: 0.3.0 ""
    Memory Size: 3 GB + 768 MB
    network: wlan0   ARM Ethernet controller ,   LAN/eth0: Broadcom BCM43430 WLAN card


    --- specs_RF from docs/manuals/descps::
    https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/
    Broadcom BCM2711, Quad core Cortex-A72 (ARM v8) 64-bit SoC @ 1.8GHz
    1GB, 2GB, 4GB or 8GB LPDDR4-3200 SDRAM (depending on model)
    2.4 GHz and 5.0 GHz IEEE 802.11ac wireless, Bluetooth 5.0, BLE
    Gigabit Ethernet
    2 USB 3.0 ports; 2 USB 2.0 ports.
    Raspberry Pi standard 40 pin GPIO header (fully backwards compatible with previous boards)
    2 × micro-HDMI® ports (up to 4kp60 supported)
    2-lane MIPI DSI display port
    2-lane MIPI CSI camera port
    4-pole stereo audio and composite video port
    H.265 (4kp60 decode), H264 (1080p60 decode, 1080p30 encode)
    OpenGL ES 3.1, Vulkan 1.0
    Micro-SD card slot for loading operating system and data storage
    5V DC via USB-C connector (minimum 3A*)
    5V DC via GPIO header (minimum 3A*)
    Power over Ethernet (PoE) enabled (requires separate PoE HAT)
    Operating temperature: 0 – 50 degrees C ambient
    * A good quality 2.5A power supply can be used if downstream USB peripherals consume less than 500mA in total.

    ---  CPU + motherboard/SoC (System-on-Chip) + Video :
    https://www.raspberrypi.com/documentation/computers/processors.html#bcm2711
    https://en.wikipedia.org/wiki/ARM_Cortex-A72
    -
    CPU:  ARM Cortex-A72 , 64-bit instruction set on a Broadcom motherboard BCM2711 , but 32-bit VideoCore !
    SoC (Chip-Satz /Motherboard ) : Raspberry Pi 4 :  BCM2711 (Broadcom 2711 chip-satz/motherboard) , quad-core-CPU: Cortex-A72 je 1.5 GHz	 , arm64 , 64 bit
    ARM cores are 64-bit, and while the VideoCore "VI 500 MHz" is 32-bit
    GPU, Pi 4 B : Broadcom VideoCore VI 500 MHz 32-bit ,
    ARM cores are capable of running at up to 1.5 GHz, making the Raspberry Pi 4 about 50% faster
    -
    Processor: Quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5 GHz.
    Memory: Accesses up to 8GB LPDDR4-2400 SDRAM (depending on model)  : ca1 : 4GB
    Caches: 32kB data + 48kB instruction L1 cache per core. 1MB L2 cache
    Multimedia: H.265 (4Kp60 decode); H.264 (1080p60 decode, 1080p30 encode); OpenGL ES, 3.0 graphics

    --- Power : 5.1 V; 3.0 A  :
    https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply :
    All models require a 5.1V supply ! ANschluss Pi4 : USB-C connector !
    1.2A is supplied to downstream USB peripherals (USB-HDD/SDD/Stick/Zigbee-Stick/...), so Max-Power on ISB-port:  1200mA total across all ports
    - ! Exactly how much current (mA) the Raspberry Pi requires is dependent on what you connect to it. typical:
        Product, 	Recommended PSU current capacity,	Maximum total USB peripheral current draw,	Typical bare-board active current consumption :
        Raspberry Pi 4 Model B , 3.0A , 1.2A , 600mA
    
    --- https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/
    Product , 	Processor	, ARM core	, Debian/Raspbian-ARP-Port,  Architecture
    Raspberry Pi 4	, BCM2711 ,	Cortex-A72	 , arm64	 , 64 bit

    --- WiPe:
    https://en.wikipedia.org/wiki/Raspberry_Pi  :
    1.5 GHz 64-bit quad core ARM Cortex-A72 processor, 
    SoC:  Broadcom BCM2711  ( ~ MotherBoard)
    CPU:  4× Cortex-A72 1.5 GHz
    GPU:  Broadcom VideoCore VI @ 500 MHz[11
    on-board 802.11ac Wi-Fi, 
    Bluetooth 5, full gigabit Ethernet (throughput not limited),
    two USB 2.0 ports, two USB 3.0 ports, 1–8 GB of RAM, and 
    dual-monitor support via a pair of micro HDMI (HDMI Type D) ports for up to 4K resolution.

    --- NW-cards:
    eth0: dc:a6:32:4a:04:6d
    wlan0: dc:a6:32:4a:04:6f
  
##________________________________________  ___________________________


#####  ==========  /:230714 :  lights--ca1-IoT :
    --- Alexa-ca1--older : ??  Amazon Echo Dot Gen-1 ?

    --- light-small, RB 248 T  ,by innr :
    https://www.innr.com/en/product/smart-candle-comfort-2pack/
    - Factory-reset: Schalten Sie die Lampe sechs Mal (6x) AUS und EIN mit Intervallen von 0,5 Sekunden. Die Lampe blinkt, um anzuzeigen, dass sie factory-reset wurde.  Es kann dann wieder mit einer Bridge verbunden werden.
    - Art number: RB 248 T-2  ,  EAN code:  8718781552299
    - Wattage 5.8W Voltage/Frequency 220-240V/50-60Hz Protocol Zigbee 3.0 Replacement wattage 40W
    - Light colour warm-to-cool tunable Colour temperature 2200K - 5000K Light quality (CRI) >80 Lumen 470 lm Beam angle 300° Rated lifespan 50.000 h Switch-on time < 0.5 sec Dimming range 5% - 100%
    - Height 110mm Diameter 38mm Weight 42gr/pc
##________________________________________  ___________________________


#####  ==========  Alexa-old-kleiner-ca1:
##________________________________________  ___________________________

