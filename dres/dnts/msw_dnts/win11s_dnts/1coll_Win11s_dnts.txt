_________________________ 1coll WIN11s Installs/... : ______________________________


#####  ==========  HW-Prüfung-/TMP-Emgehen integriert in USB-install-Media :

    _______:  CT : see here dnts + REG-dir ! CT-2201-152--Win11_HWCheck_bypass_in_USBInstallMedia--befehle.txt

    _______:  Alternative-Kommentar zu dem Artikel in CT-2201-152  (aber OK??): renaming systemfiles (CT-comment):
    Es geht auch einfacher....  , 21.12.2021  :
    Es gibt da auch die Möglichkeit, bei einem Windows10 USB-Installationsstick die "install.esd" im Verzeichnis \sources zu tauschen. Youtube ist voll mit solchen Tipps.
    Mit dem Original Stick, welcher mit dem MediaCreationTool erstellt wird, kann kurz vor dem eigentlichen Installationsprozess die Hardwareerkennung auch dadurch ausgeheblt werden, dass im Verzeichnis (meistens "C:\$WINDOWS.-BT\Sources") die beiden Dateien "appriser.dll" und "appriser.sdb" umbenannt oder gelöscht werden. Funktioniert sogar beim InplaceUpgrade
    - see CTs entries in win11-dnts , but here also ein Kommentat (aler leiterer Wef) zu:
     c't 1/2022, Seite 152 , Hardwareprüfung aus Windows-11-Setup-Medium entfernen (also, integriert in USB-install-Media):
     https://www.heise.de/forum/c-t/Kommentare-zu-c-t-Artikeln/Hardwarepruefung-aus-Windows-11-Setup-Medium-entfernen/Es-geht-auch-einfacher/posting-40182224/show/

    _______: Alternative RegEdit during Installation (but persistent!?!?) : Regedit-of-usb-stick:
    https://pureinfotech.com/install-windows-11-unsupported-pc/
    - edit the registry os USB-install-stick (in advance, from other windows, or with shift-F10 during installation as:):
    Press any key to continue.
    Use the “Shift + F10” keyboard shortcut to open Command Prompt.
    Type the following command and press Enter:
    regedit
    Navigate the following path:
    HKEY_LOCAL_MACHINE\SYSTEM\Setup
    Right-click the Setup (folder) key, select New, and then the Key
    Name the key LabConfig and press Enter.
    Right-click the LabConfig (folder) key, select New, and then the DWORD (32-bit) Value option.
    Name the key BypassTPMCheck and press Enter.
    Double-click the newly created key and set its value from 0 to 1.
    Click the OK button.
    Right-click the LabConfig (folder) key, select New, and then the DWORD (32-bit) Value option.
    Name the DWORD BypassSecureBootCheck and press Enter.
    Double-click the newly created key and set its value from 0 to 1.
    Click the OK button.
    Click the Next button.
    Click the Install now button.
    Click the “I don’t have a product key” option if you are reinstalling. If Windows 11 has been previously activated after the installation, reactivation will happen automatically.
##________________________________________  ___________________________


