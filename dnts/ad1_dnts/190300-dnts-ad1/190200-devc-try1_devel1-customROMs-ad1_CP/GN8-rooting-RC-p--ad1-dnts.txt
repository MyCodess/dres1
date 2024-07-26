_______________ ANdroid-upgrade/rooting/developing TAB GN8 Samsung nts-coll , Android 4.4.2 : ______________________________
##________________________________________  ___________________________


#####  ==========  _CP-specs-GN8 :
Bestellung:  Samsung Galaxy Note 8.0 N5100 Tablet WiFi + 3G
(! Vorsicht, N5110 is nur WiFi, also ohne 3G/UMTS !! nicht verwechseln bei downloads,...!!)
Bestell: 3. November 2013  (ca /amazon)
from Device-->Setting-->About:  Model number : GT-N5100 , BaseModelVersion(baseband):  N5100XXDNH2
from-int-OL:   GALAXY Note 8.0 (GT-N5100ZWADBT) , Model number : GT-N5100  /  GT-N5100ZWADBT
Rueckseite-Aufkleber. bzw. auch das selber vom  Device-->Setting-->About:
  SerienNr, S/N:  RF1D50MHGST  , IMEI:  356564051512643 /01  bzw. 356564/05/151264/3  ; re-asking it by dialing *#06# 
? Prozessor	:  Exynos 4412 Quadcore-Prozessor 4x 1,60 GHzProzessor ??

	_______:  more codes/IDs by dialing and querying the device (but do NOT need to press "make call":  see https://www.droidviews.com/how-to-find-out-the-date-of-manufacture-on-samsung-galaxy-device-secret-codes/  (not all codes working for GN8, but some):
	-  *#1234# -- Phone info/Firmware version
	-  *#12580*369# – Software and hardware info
	-! *#9090# -- Service Mode
##________________________________________  ___________________________


#####  ==========  rootings-steps-short based on ct.18.04--100-103--Android-rooten--Was-es-bringt /p:4 :

	_______:  Bootloader-unlocking/offnen ??:
1-  "develpoder options" enabling on device/GN8  (with 7 times tapping Settings-->about device-->build-number)
2-  "USB-Debugging" enabling on  device/GN8 ( Settings-->develpoder options-->USB-Debugging)
3-  ??OEEM-Unlocking ??
4-  reboot device/GN8 in Fastboot-Mode  (for samsungs  Download-Modus):  Beide Modi dienen zum Aufspielen neuer Software.
	- reboot in Fastboot-Mode (triggering either by ADB-cmdline /OR by button-combinations, see below)
	- ct.18.04--100-103-P:4  :  Anschließend muss das Gerät im sogenannten Fastboot-Modus neu gestartet werden – entweder über ein ADB-Kommando oder eine Tastenkombination beim Einschalten. Bei Samsung wird der Download-Modus gestartet. Beide Modi dienen zum Aufspielen neuer Software. Regulär füttert das ebenfalls Fastboot genannte Kommandozeilen-Tool die Software, bei Samsung tut es Odin.
5-	Odin/Fastboot/Heimdall... :     flashing tools  to install stock ROM /OR Custom Rom as TWRP  (for samsungs is Odin/MsWIndows bzw.  heimdall/onLinux)
	- Odin tool is the official Samsung firmware flashing tool for Windows PC. If you are a Mac or Linux user, you can use Heimdall or Java Odin. https://www.droidviews.com/download-odin-tool-for-samsung-galaxy-devices-all-versions/
5b- "Custom Recovery"-install, as eg. TWRP , which contains also SU/rooting! (works also with Hersteller-Recovery, aber so leichter; es geht auch direkt booten mit Magisk ohne "Custom Recovery")...
6-  Den Bootloader sollte man nach dem Rooten NICHT abschließen ...
##________________________________________  ___________________________


#####  ==========  recovery mode rebooting Buttons for GN8 :
-!!  see    https://wiki.lineageos.org/devices/n5100

	_______:  Special boot modes buttons:   https://wiki.lineageos.org/devices/n5100  :
    Recovery mode: With the device powered off, hold Volume Up + Power until the screen flashes twice, then release both.
    Download mode: With the device powered off, hold Volume Down + Power.

	_______:  Enter custom recovery mode .droidword.com :
	Enter custom recovery mode on Galaxy Note 8 : Turn on the device by holding "Volume-up + Home + Power" buttons together until you see the recovery mode. After releasing button you see it!
	https://www.droidword.com/2017/10/03/update-samsung-galaxy-note-8-0-to-android-7-1-nougat-resurrection-remix-os/#DOWNLOADS_SECTION

	_______:  
##________________________________________  ___________________________


#####  ==========  try1 . google : installing android 8.0 on samsung galaxy note 8 GT-N5100 :
https://forum.xda-developers.com/galaxy-note-8-0
##________________________________________  ___________________________


#####  ==========  USB debugging enabling / enabaling Settings-->Developer-Option :  How to fully backup your Android smartphone or tablet without root :
https://9to5google.com/2017/11/04/how-to-backup-restore-android-device-data-android-basics/
How to enable USB debugging :
    Go to your Settings menu
    Scroll down and tap on System
    Select About phone
    Tap on the device’s Build number multiple times until it enables Developer options. Newer devices will require you to enter your PIN/password/pattern
    Hit the back button and select Developer options within the System menu
    Make sure Developer options is toggled on. Scroll down and toggle USB debugging on
How to backup your Android device’s data :
    Plug your Android device into your computer
    Using either Command Prompt or Terminal, navigate to the folder in which the ADB tools are located and type in “ADB devices“. A pop-up on the Android device will appear if you need to grant your computer permission to interact with the phone or tablet. You will know if the command worked on your computer if it returns with the connected device’s identification number
    Type in “adb backup -apk -shared -all -f <filepath>/backup.ab“
    Your Android device will now show the full backup window. Here you can encrypt your backup with a password (which is recommended)
    Tap on Back up my data
    This process can take several minutes and when completed, a new file will be placed on your computer
How to restore your Android device’s data :
    Plug your Android device into your computer
    Using either Command Prompt or Terminal, navigate to the folder in which the ADB tools are located and type in “ADB devices“. A pop-up on the Android device will appear if you need to grant your computer permission to interact with the phone or tablet. You will know if the command worked on your computer if it returns with the connected device’s identification number
    Type in “adb restore <filepath>/backup.ab“
    Your Android device will now show the full restore window. If you added a password to your backup file, enter it in the space given
    Tap on Restore my data
    This process can take several minutes and when completed, most if not all of your previously installed applications will be present on your device as well as photos and other data
You will need to download and set up the Android SDK on your computer. This will be used to initiate the backup and restore process on your Android devices.
It’s also recommended that you set your device’s display sleep timer to a time that will disable it from turning off during the process.
To do this go to Settings>Display>Sleep and choose the longest time period as possible.
##________________________________________  ___________________________


#####  ==========  "Developer options" + "USB Debugging"  enabling  :
    Go to Settings-->"About device" (or "About phone" or "About tablet") section in Settings
    Tap 7 times on "Build number" row (usually the last row). After that "Developer options" section will appear in Settings
    Go to "Developer options" section in Settings
    Tap the "USB Debugging" checkbox
##________________________________________  ___________________________


#####  ==========  
