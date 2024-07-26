______________ setup/installs MsWin11 : ______________________________________
- Win11-first-release ab 05.Okt.2022 !


#####  ==========  Vocabs/Gloss:
- MCT : media creation tool: creates  a bootable USB or DVD to install WIn11 (NOT-containging the whole Win11-ISO ! will download it or uses a local-win11-ISO !). it is NOT full-win11-system! only a bootable Media to install the full-win11 !
- "PC Health Check App“ (PC-Integritätsprüfungs-App) : Hawrdware-Prüfung for Win11-Install !
##________________________________________  ___________________________


#####  ==========  HW-/Systemvoraussetzungen umgehen :

    - !! see CTs-Win11s-dnts-Articles for HW-check-Umgehen + REGs-Dir here !!

	_______:  Reg-Eintrag for Upgrading/hostOS-Reg (eg Win10, which is to be upgraded to Win11): (DW: https://www.heise.de/select/ct/2021/20/softlinks/ywpz?wt_mc=pred.red.ct.ct202021.126.softlink.softlink  , bzw. ct.de/ywpz)
    Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
    "BypassTPMCheck"=dword:00000001
    "BypassSecureBootCheck"=dword:00000001
    "BypassRAMCheck"=dword:00000001
    "BypassStorageCheck"=dword:00000001
    "BypassCPUCheck"=dword:00000001

	_______:  TMP 2.0 + UEFI  win11:
    - c’t 22/2021, S.24-25  :  Windows 11: Hardwareanforderungen , TMP-2.0, UEFI-Umstellung
    - c't 16/2021--180 : TMP 2.0 /Win11-FAQ: Was ist ein TPM?
    - "Geräte-Manager" unter „Sicherheitsgeräte“: Falls ein TPM vorhanden und eingeschaltet ist, taucht es im Geräte-Manager unter „Sicherheitsgeräte“ auf. Die Systeminformationen wiederum verraten, ob UEFI Secure Boot aktiv ist (Sicherer Startzustand). Falls nicht, schauen Sie auch gleich in die Zeile „BIOS-Modus“: Steht dort „UEFI“, lässt sich Secure Boot meistens leicht im BIOS-Setup aktivieren. Falls dort jedoch „Vorgängerversion“ steht, startet das System im BIOS-kompatiblen Modus und es sind langwierigere Arbeiten nötig, siehe unten.   c’t 2021, Heft 22 ,S.24

    _______:  UEFI-Umstellung :
	Die Umstellung des PC-Bootmodus von BIOS- auf UEFI-kompatiblen Start im BIOS-Setup ist nicht schwierig, hat aber eine tückische Nebenwirkung. Letztere folgt aus der von Microsoft willkürlich festgelegten Verknüpfung des Bootmodus mit dem Verwaltungsmodus des Systemdatenträgers. Startet Windows im BIOS-Modus, muss der Bootloader auf einem Datenträger mit Master Boot Record (MBR) liegen, darf also nicht auf einem mit GUID-Partitionstabelle (GPT) gespeichert sein. Im UEFI-Startmodus ist es umgekehrt. Ändert man den Bootmodus, startet deshalb Windows nicht mehr.
	Im Prinzip lässt sich der Systemdatenträger mit dem Tool „MBR2GPT“ auf GPT umstellen [3]. Das kann aber scheitern, etwa wenn eine komplizierte Partitionierung vorliegt.  c’t 2021, Heft 22 ,S.24
##________________________________________  ___________________________


#####  ==========  Versionen/Editions/releases/... :
- Release-Info/-hist :  https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information
- MS-bordeigene-exe:   Winver.exe  ,  msinfo32.exe
-! CT-axv: Win11-Editions-installs:   c’t 2021, Heft 22 --030  !
-! CT-axv: finding-my-win-ver (incl. infos for ALL Wins-Vers), c't 14/2022 S. 172 , Was läuft?  Windows-Version und -Edition identifizieren https://www.heise.de/select/ct/2022/14/2213813360897896381
-! CT: finding-my-win-ver (incl. infos for ALL Wins-Vers), Was läuft? Windows-Version und -Edition identifizieren :  https://www.heise.de/hintergrund/Was-laeuft-Windows-Version-und-Edition-identifizieren-7138012.html
##________________________________________  ___________________________

