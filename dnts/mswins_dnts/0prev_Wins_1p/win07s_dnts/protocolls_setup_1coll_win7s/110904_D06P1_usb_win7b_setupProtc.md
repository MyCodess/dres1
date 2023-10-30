!!! BlueScreen-Avoiding: !!!
before each shutdown, check the registry if the modified
USB-drivers are still loaded during booting (modified Reg-Entries by kk/CT)
Otherwise could have BlueScreen!!
-!! unter HKLM\USB\CurrentControlSet\Services\usbxxx : alle usb.kram muss start "0" und Group  system reserved sin !!
-!! backup in   C:\00_adds\bups_OK\config.02.mod1.usb\  : direct modified after setup, pre any startup!
See End of CT-Artikel!! bzw. devnts for win7!
also last modified ok-Reg-Files are in C:\Windows\System32\config.02.mod1.usb
they are ok and schould work again!!
(in case of discovering new Hardwares or attaching the Usb-HD to a new PC the
modied Reg-Entries for USB-Drivers-Boot-Loading could be overwritten by OS!!)
-!!! CT: ct1013168_171_UsbInstallWin7.pdf
Im Prinzip ist nun alles erledigt, doch bevor Sie das frisch von USB gebootete Windows 7 wieder herunterfahren,
sollten Sie nochmals den Registry-Editor starten und nachprüfen, ob die vorhin vorgenommenen Änderungen erhalten geblieben sind,
die Schlüssel finden Sie nun allerdings nich mehr unter HKLM\USB, sondern unter HKLM\System\CurrentControlSet.
Die USB-Einträge ändern sich teilweise zurück auf die Ausgangswerte falls Windows neue Hardware erkannt hat 
unwahrscheinlich, falls Windows das USB Laufwerk vor dem Umzug schon kannte aber fast unvermeidlich, falls nicht.
Dieses Szenario droht auch, falls Sie von der USB Platte mal versehentlich am falschen PC boo ten.
Dann sollten Sie die Nachkontrolle und gegebenenfalls die Korrekturen vor dem Herunterfahren wiederholen. (axv)
Lacie Part1 von vo17
110904
##________________________________________  ___________________________


#####  ==========  CP from win7-devnts : ==================================
##________________________________________  ___________________________


#####  ==========  USB.boot.Win7.OS-setup: Win7-von-USB.Platte strten/booten:
-!! ct1013168_171_UsbInstallWin7.pdf : full Instruction!! OK! done for vo17 :

	_______:  CT-nts:
	-!! after finishing, if attaching the usb-win7 to another PC: you could get blue.screen by second booting!! to avoid it see beleow under "after finisching"!! have to check Reg-Usb-Driveres!
	- if attaching the usb-win7 to another PC, could licensing-problem with bluescreen! (was ok in l1nw-win7.ultimate!)
	- lieber usb-platte; usb-stick could be problem
	- usb-HD darf nur eine einzelne primary partition ??(form me ok mehrere)

	_______:  CT-Procedure : here eg USB-target-part f: , and win7-source-part d:
	- FRISCH formatieren von USB-Part mit NTFS (could problems if not frisch!)
	- boote von win7-usb/win7-parallel-install/win7-dvd/win7-repair-disk, systemreperatur-media/...
	- goto Dos-window as Admin in your current parallel-win7 (eg in repair-disk with shit-F10,... or your Win7-RF,...)
	- wo/was/drive.letters??was??: dos-window --> notepad.exe --> file-open: you see a small explorer
	- note usb-target-drive + win7-source-drive (..\windows\system32,....)
	- xcopy d: f: /kreisch  --> kopiert Win7, ABER noch nicht bootfähiger USB-HD!! missing bootlader!
	- bootloader into Usb-HD:  bcdboot f:\windows /s f: /l de-de  # wobei f: ist der AKTUELLE USB-win-Part!
	- USB-Treiber!! jetzt ist der Usb-part auch bootfähig, aber fehlen noch WAEHREND booeten die USB-Treiber, also:
		regeidt --> HKLM --> Load Hive (reg-datei-laden): system.reg.datei von f: (usb-win) --> see CT to load usb-drives DURING booten!
		CT: Unter  HKLM\USB\Select prüfen Sie nun, wel- chen Wert der Eintrag  Current hat. Bei einer 1 geht es unter HKLM\USB\ControlSet001 weiter, bei einer 2 unter HKLM\USB\ControlSet002 und so weiter. Hier finden Sie unter services Unterschlüssel namens  usbccgq,  usbehci,  usbhub,  usbohci,  USBSTOR und usbuhci. Die nötigen Änderungen sind bei allen gleich: Setzen Sie erstens den Wert des Eintrags Start jeweils von 3 auf 0 und zweitens den Wert des Eintrags  Group von Base auf system reserved (bei USBSTOR fehlt der Group-Eintrag, das darf so bleiben). Diese Änderungen veranlassen Windows, alle USB- Treiber gleich zu Beginn des Bootvorgangs zu laden.
	- DriveLetter correction in Reg: CT: Als Beispiel dienen hier C: und F:. Öffnen Sie den Schlüssel HKML\USB\MountedDevices. Hier tauschen Sie beim Eintrag namens \DosDevices\C: das C vorübergehend gegen irgendeinen bislang nicht vergebenen Buchstaben, beispielsweise Q. Dann ersetzen Sie beim Eintrag  \DosDevices\F: das F durch ein C. und schließlich bei  \DosDevices\Q: das Q durch das F. Das sorgt dafür, dass die Windows-Installation auf der USB-Platte diese nun für C: hält und das eingebaute Laufwerk für F:.
	- unload Hive in Reg
	-- fertig! can be bootet
	-!! BUT later strill you can get blue-screen (due to changes to loading-USB-dreivers due to updates/new.Hardware.gefunden/...!! you GOT it after attaching from x13 to vo17), so to avoid it:
		CT: Im Prinzip ist nun alles erledigt, doch bevor Sie das frisch von USB gebootete Windows 7 wieder herunterfahren, sollten Sie nochmals den Registry-Editor starten und nachprüfen, ob die vorhin vorgenommenen Änderungen erhalten geblieben sind  die Schlüssel finden Sie nun allerdings nich mehr unter HKLM\USB, sondern unter HKLM\Sys tem\CurrentControlSet. Die USB-Einträge ändern sich teilweise zurück auf die Ausgangswerte falls Windows neue Hardware erkannt hat  unwahrscheinlich, falls Windows das USB Laufwerk vor dem Umzug schon kannte aber fast unvermeidlich, falls nicht. Dieses Szenario droht auch, falls Sie von der USB Platte mal versehentlich am falschen PC boo ten. Dann sollten Sie die Nachkontrolle und gegebenenfalls die Korrekturen vor dem Herunterfahren wiederholen. (axv)
