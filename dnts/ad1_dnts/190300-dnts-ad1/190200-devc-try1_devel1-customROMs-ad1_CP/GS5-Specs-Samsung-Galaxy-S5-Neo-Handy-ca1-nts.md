_______ gebrochenes-Display-Test-Handy1-for-Android-von-ca1--180900 : __________________
##________________________________________  ___________________________


#####  ==========  Rueckseite-Device (manl):
Samsung Galaxy S5 neo /Marshmallow  (Android 6.0.1  Marshmallow )
Modell	:  SM-G903F
FCC ID	:  A3LSMG903F
SSN		:  -G903FGfMH
-- codecs-tel:
IMEI	:  353008071649103 /01  bzw.  353008/07/164910/3    :  *#06#  Shows IMEI Number , OR also in Settings--DeviceInfo--....
AP:  G903FXXU1BQC1  , CP: G903FXXU1BQC1   , CSC: G903FOXA1BQC1   :   *#1234# -- shows Phone info/Firmware version
S/N		:  RF8G82FTAFD

	_______:  vom system--settings :
IMEISV		:  01
wlan-mac	:  54:40:AD:C4:D6:DB	(manl)

	_______:  infos-nts:
- SIM/SD-KarteN:
	-!! SIM-Karte unten, SD-Karte oben darauf! (mit Akkuseite/Ruckseite zu Dir) ! nicht verjehrt rum einstecken !! goldfarbenen Kontakten nach unten /zu-dem-Display!
	- Micro-SIM-Karten , SIM- oder USIM-Karte mit den goldfarbenen Kontakten nach unten/zu-dem-display !
	- SD-Karte : goldfarbenen Kontakten nach unten , maximal 128 GB , FAT- und exFAT-Dateistruktur ! see manual

	_______:  From AIDA64-SystemInofs after rooting:
	<<< CPU >>>
	SoC Model: Samsung Exynos 7 Octa (7580)
	Core Architecture: 8x ARM Cortex-A53 @ 1600 MHz
	Manufacturing Process: 28 nm
	Instruction Set: 64-bit ARMv8-A (32-bit Mode)
	--
	Hardware    : SAMSUNG Exynos7580   <-- from ADB-shell also !
	---
	[shell@s5neolte:/ $ getprop | grep -i exy                                     
	[ro.arch]: [exynos7580]
	[ro.board.platform]: [exynos5]
	[ro.boot.hardware]: [samsungexynos7580]
	[ro.chipname]: [exynos7580]
	[ro.hardware]: [samsungexynos7580]

	_______:  codecs-queries : from-Device by code-queries (tel-bottun/ok NICHT drücken nach der code-Eingabe! zeigen von alleine die infos falls be dem Device sie funktionieren ! nicht alle code im INT funktionieren!): 
*#06#  Show IMEI Number
*#1234# -- Phone info/Firmware version
*#9900# -- Sysdump (Logfiles etc.)
*#9090# -- Service Mode
see full-listing in:  https://www.droidviews.com/how-to-find-out-the-date-of-manufacture-on-samsung-galaxy-device-secret-codes/
##________________________________________  ___________________________


#####  ==========  Rooting-nts :
-!! see  lx-ad1-dnts.txt   for done-actions-Galaxy-S5-from-x13-ubuntu--190221 !! and CT-artikel there !!
-!! see ct.18.08.174-178--Root_tut_gut--Rooting-und-zurueck-zum-Stock-ROM.pdf   :  Samsung Galaxy S5: LineageOS, Rooting und zurück zum Stock-ROM 
##________________________________________  ___________________________


#####  ==========  syste-infos-adb_shell-after rooting1 :
u1@x13: ... $    adb shell
shell@s5neolte:/ $ date
Sat Feb 23 20:18:29 CET 2019
shell@s5neolte:/ $ uname -a
Linux localhost 3.10.61-10798689 #1 SMP PREEMPT Tue Feb 28 21:14:13 KST 2017 armv8l
shell@s5neolte:/ $ cat  /proc/cpuinfo                                          
Processor	: AArch64 Processor rev 3 (aarch64)
processor	: 0
Features	: fp asimd aes pmull sha1 sha2 crc32 wp half thumb fastmult vfp edsp neon vfpv3 tlsi vfpv4 idiva idivt 
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 3
Hardware	: SAMSUNG Exynos7580
##________________________________________  ___________________________


#####  ==========  Specs-OL--samsung.com :
	https://www.samsung.com/de/smartphones/galaxy-s5-neo-g903f/SM-G903FZDADBT/

	_______:  specs-samsung-OL-short :
    12,94 cm / 5,1" Displaygröße (Hauptdisplay)	
    CMOS 16,0 MP Auflösung Hauptkamera	
    145 Gewicht (in g)	
    2800 Akku-Kapazität (mAh)	
    Bis zu 73 Musikwiedergabe (in Stunden)	
    1,6 GHz Prozessorgeschwindigkeit	
	amazon:  Smartphone (5,1 Zoll (12,9 cm) Touch-Display, 16 GB Speicher, Android 5.1) schwarz von Samsung

	_______:  specs-samsung-OL-long  :
    Prozessor
        Prozessortaktung
        1,6 GHz
        Prozessortyp
        Octa-Core
    Artikelinformationen
        Artikelname
        Galaxy S5 neo
        Artikelnummer
        SM-G903FZDADBT
        EAN
        8806088055138
        Farbe
        Gold
    Display
        Displaygröße (Hauptdisplay)
        12,94 cm / 5,1"
        Displayauflösung in Pixel (Hauptdisplay)
        1920 x 1080 (Full HD)
        Displaytechnologie (Hauptdisplay)
        Super AMOLED
        Anzahl Farben (Hauptdisplay)
        16 Mio.
        S Pen-Unterstützung
        Nein
    Kamera
        Auflösung Hauptkamera
        CMOS 16,0 MP
        Autofokus Hauptkamera
        Ja
        Auflösung Frontkamera
        5 Megapixel (CMOS)
        Blitz Hauptkamera
        Ja
        Auflösung Videoaufnahme
        Full HD (1.920 x 1.080 Pixel) @30fps
    Speicher
        Arbeitsspeicher in GB
        2 GB
        Interner Gerätespeicher in GB
        16 GB
        Frei verfügbarer interner Gerätespeicher in GB*
        ca. 9,5 GB
        Speichererweiterung
        microSD (bis zu 128 GB)
    Netzwerkspezifikation
        Multi-SIM
        Single-SIM
        Größe SIM-Karte
        Micro-SIM (3FF)
        Infrastruktur
        GSM (2G), W-CDMA (3G), FDD-LTE (4G)
        GSM-Band
        GSM 850 MHz, GSM 900 MHz, DCS 1.800 MHz, PCS 1.900 MHz
        UMTS-Band
        B1 (2100), B2 (1900), B5 (850), B8 (900)
        LTE-Band
        B1(2100), B3(1800), B5(850), B7(2600), B8(900), B20(800)
    Konnektivität
        ANT+
        Ja
        USB-Version
        USB 2.0
        Standortbestimmung
        GPS, Glonass
        Headset/Kopfhöreranschluss
        3,5mm Klinkenanschluss
        MHL-Schnittstelle
        Nein
        WLAN
        802.11 a/b/g/n/ac 2,4 + 5 GHz, VHT80
        Wi-Fi Direct
        Ja
        Bluetooth-Version
        Bluetooth® v4.1
        NFC
        Ja
        Bluetooth-Profile
        A2DP, AVRCP, DI, HFP, HID, HOGP, HSP, MAP, OPP, PAN, PBAP, SAP
        Synchronisation
        Smart Switch (PC Version)
    Artikelinformationen
        Formfaktor
        Touch
    Abmessung und Gewicht
        Abmessungen (HxBxT in mm)
        142 x 72,5 x 8,1
        Gewicht (in g)
        145
    Akku
        Internet-Nutzungsdauer (3G) (in Stunden)
        Bis zu 10
        Internet-Nutzungsdauer (LTE) (in Stunden)
        Bis zu 11
        Internet-Nutzungsdauer (WLAN) (in Stunden)
        Bis zu 13
        Videowiedergabe (in Stunden)
        Bis zu 13
        Akku-Kapazität (mAh)
        2800
        Austauschbar
        Ja
        Musikwiedergabe (in Stunden)
        Bis zu 73
        Gesprächszeit (3G WCDMA) (in Stunden)
        Bis zu 15
    Audio und Video
        Videoformate (Wiedergabe)
        MP4, M4V, 3GP, 3G2, WMV, ASF, AVI, FLV, MKV, WEBM
        Videoauflösung (Wiedergabe)
        Full HD (1.920 x 1.080 Pixel) @30fps
        Audioformate (Wiedergabe)
        MP3, M4A, 3GA, AAC, OGG, OGA, WAV, WMA, AMR, AWB, FLAC, MID, MIDI, XMF, MXMF, IMY, RTTTL, RTX, OTA
    Services und Apps
        Wearable Unterstützung
        Gear Circle (Gear Manager Support), Gear Fit, Gear S
        S Voice
        Ja
        Mobile TV
        Nein
##________________________________________  ___________________________


#####  ==========  cAp-from-INT-sites....-coll ??:
- https://samdb.org/download/Galaxy__S5__neo__/1m60/DBT/G903FXXU1BQC1/G903FOXA1BQC1/ :
    PDA/AP Version G903FXXU1BQC1
    CSC Version G903FOXA1BQC1
    Region  DE
    Build Date 2017-02-28
    Changelist 10798689
    OS Marshmallow
    OS Version 6.0.1
    Size 1.429 GiB
- https://samfrew.com/download/Galaxy__S5__neo__/9bp3/BTU/G903FXXU1BQC1/G903FOXA1BQC1/  :
	PDA/AP Version G903FXXU1BQC1
	CSC Version G903FOXA1BQC1
	MODEM/CP Version G903FXXU1BQC1
	Region BTU — United Kingdom
	Build Date 2017-02-28
	Changelist 10798689
	OS Marshmallow
	OS Version 6.0.1
##________________________________________  ___________________________


#####  ==========  
