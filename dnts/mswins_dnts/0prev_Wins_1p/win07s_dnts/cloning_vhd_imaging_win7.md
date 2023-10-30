_____________ win7-cloning/VHDs/USB-Install/... ______________________--
-!!! for all clonings/setups...: do FRESH  Part.Creation + Part.Formatting of the new.Target.Part ONLY with DiskPart!!! (just to be sure! Anyway NOT formatting from Lx,...)
-!! deactive all AntiVirs..., if copying/cloning from a clone/win-system and not from repair.startup.stick!!
	!! copying BEST done from win7.repair.stick/dvd and NOT from any full.windows system!
##________________________________________  ___________________________


#####  ==========  usefull.cmd.cmds for all cloning stuffs:
- see win7_nts--Booties : mountvol , bcdboot , bcdedit /?  (do NOT use bootrec! partition was gone/formated with /fixboot)
##________________________________________  ___________________________


#####  ==========  Allgemein.problems/point/.. for all cases:
-!! problems with junctions!!: bei xcopy the contetn of junctions are copied leider, not only the link!
	 so really a problem eg. in case of c:\up1 (so whole w_RF will be copied!! if there!!) no solution??!!
-!! ONLY active.parts are bootable!! so do not forget to make it active, if want to boot from it!!
##________________________________________  ___________________________


#####  ==========  HD.to.HD-/Pc.to.PC--VHD-Image-Cloning , eg vo17.chd --> x13.part OR new-HD-Di3-vo17:
-!!! HD-target-PC will be re-partiotioned/refomatted!!! a "clean parts" is doen!!:
	specially if target-HD has another parts-structure as source.HD!!
	you could be lucky, if target-HD is simillar ro source HD (specially the position of win7.source.part), then
	the win7-restore-prog maybe ask you and avoid re-partioning! but usually it repartitions...!
	specially if the checkbox is not active to avoid repartitioning, then it will repartition!!!
-!! target.part MUST be active!
- make vhd from source and take it to target.pas
- start target.pc from win7.stick and play.back from vhd to pC! reboot! done!
- (usually noot needed bcdboot ... /s ... , but if boot-problem, do it; see USB-install-nts)
- mods after reboot (not criticals): bcdedit / easybcd to adapt entries + pagefile.loc + ...
##________________________________________  ___________________________


#####  ==========  Part.2Part-Migration/Imaging, eg Part1.to.Part2-Clonong of win7:
- see extra nts!
##________________________________________  ___________________________


#####  ==========  VHD-Boot-Clone/imaging,...:
-!! see ct.10.03.086 : Eingebauter Blitzspiegel /axv :  !! great Help+Anleitung ! (bzw. der Artikel auch in CT-Spezial-Win7--cs1007112 (Windows Spiegeln) bzw. == ct1003074_088_Win7ausreizen_VHD_Imaging.pdf

	_______:  Setup of cloen2:
	- org image from smaller image  after removing WXP:  7dadfc8b-c9da-11df-a6f2-806e6f6e6963.vhd
	- adapted/modified based on CT-Anleitung:
	- reg-edits: delete MountedDevices all, so delete the whole key
		.... see CT
	--- prepare image-vhd + voraussetzungen,...:
		- Size-vhd (Image-Size only!)): Die Größe einer vom Windows-7-Imager erzeug- ten VHD-Datei entspricht unge- fähr der unkomprimierten Ge- samtgröße aller Dateien auf der gesicherten Partition mit Ausnah- me der Ruhezustandsdatei Hiber- fil.sys und der Auslagerungsdatei Pagefile.sys
		-!! Size-vhd-RunTime (nach booten von VHD): Sobald Windows aus einer VHD-Datei bootet, wächst diese jedoch und belegt vorübergehend deutlich mehr Platz – wie viel, bestimmt die Größe der Quellpartition des Images.
	--- vhd:
		- VHd-file:	you need ONLY the main vhd-file (pro part one VHD is generated. need not the boot one for this action, also no xml-files...)
		- naming:	mv and rename the mein vhd as you linke eg H:\vo17b.vhd (BUT the partition, where the VHD is located MUST be at least as big as original.source.win7.part!)
		- Laufwerkbuchstabe-Zuordnung in VHD-file aendern (ansonsten greift noch auf das ursprungliche Quellen-Part-Win7-RF)!!
			- in DatenTrägerVrwaltung: VHD attach/einbinden
			- Regedit load.Hive/Struktur.laden: VHD in Regedit einbinden und in VHD-Reg den Registry-Schlüssel "HKLM\<eingebundener-VHD>\MountedDevices"  löschen) !!:	Löschen Sie aus dem Klon in der VHD-Datei die Informationen darüber, welche Laufwerke mit welchem Lauf- werksbuchstaben eingebunden sind: --> sieh CT-Beschreibung!
			-  in DatenTrägerVrwaltung: VHD dettach/freigeben
	--- BootMenü-Eintrag hinzufügen: adding clone3 to boot-menu of the original win7-boot, in an admin-cmd:
		C:\>bcdedit /copy {current} /d clone3
		... copied to     {35491528-d692-11e0-bd1d-c522f041ff16}
		C:\>bcdedit /set  {35491528-d692-11e0-bd1d-c522f041ff16}  device    vhd=[T:]\clone3\clone3.vhd
		The operation completed successfully.
		C:\>bcdedit /set  {35491528-d692-11e0-bd1d-c522f041ff16}  osdevice  vhd=[T:]\clone3\clone3.vhd
		The operation completed successfully.
	--- reboot
	--- if you want modify/delete the above entry: delte and do it again with:  bcdedit /delete {66ceb723-c9e2-11df-a3af-892d485d7216}
