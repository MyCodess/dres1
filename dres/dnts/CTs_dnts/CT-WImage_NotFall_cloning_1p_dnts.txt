________________ CT-WImage , cloning, ... _____________________________________________
-! NOT-worked wimage on win10-x17_1ac ! but was created with rufus instead MCT ! maybe ...!?!? win7-/win10-imagagin better/OK !
	 maybe? try again with proper pre-partitioning and with MCT ...!? (but what about UEFI + BIOS !?!? maybe NOT-trying !?)
####################   CT-Wimage /win-imaging :################################################
-! project-site and all links:	  ct.de/wimage   bzw.   https://www.heise.de/ct/artikel/c-t-WIMage-3863074.html
-! see   /up1/w1/dcs-it/CTs/CT_ProjectsDW_SpecialCTs_docs/CT-WImage-Imaging-wins/
- MCT (Media Creation Tool) nur von Win10 benutzen! noch nicht Win11 !  wegen HW-checks !

	_______:  CT-WImage  (but check always ct.de/wimage ):
	-! ct.21.11--162-167-WImage-Tipps-Tricks.pdf
	-! ct.21.10--012-023  + 178/FAQ : Windows-Backups erstellen mit c’t-WIMage  +  FAQ/178 , ct.de/yggt
	-! ct.17.02--086-099--VHD-Win10-Win2VHD--Parallel-Installation.pdf
	-! ct.15.27--070-080--Upgrade-fuer-Win10-1511.pdf ab Seite 74 : Install/Setup win10 in VHD and boot from VHD !
	-! ct.18.24--172  :  Axel Vahldiek, FAQ: Booten von USB-Laufwerken, c’t 24/2018, S. 172, auch online unter ct.de/-4209809
##________________________________________  ___________________________


#####  ==========  c't-WIMage project:  ct.de/wimage :
	-! noch KEIN win11-MCT benutzen ! nur win10-MCT benutzen !! wegen HW-checks !! see ct.de/wimage : aktuelles !
	-! Cloning-Probelm with WImage due to the cloned-licenze-key  (if both PCs run in parallel !) !! see last section of ct.21.10--178-181--FAQ-WImage.pdf !!
	  1kk:  unter PC-Einstellungen -> key-ändern !?!? /OR vor-activation create the image !?!? /OR when both PCs never run parallel !?!?
	  for product-key see:  https://support.microsoft.com/en-us/windows/activate-windows-c39005d4-95ee-b91e-b399-2820fda32227
	- ALLE Sicherungen sind in der Datei Sources\Install.wim bzw. x64\Sources in partition CT-WIMAGE ! 7-Zip kann öffnen ! ist nur zipped-file ! Details see: ct.21.11--162-167-WImage-Tipps-Tricks.pdf
	- wimage-Media/USBstick/USB-HD tauschen/erneuern (grösser nehmen...):  see: ct.21.11--162-167-WImage-Tipps-Tricks.pdf
#################### c't-Notfall-Windows :################################################################
	- https://www.heise.de/ct/artikel/c-t-Notfall-Windows-2022-6270035.html
	- ct.22.02--012-026  : c't-Notfall-Windows 2022, Bausatz für ein vom USB-Stick
	--- prev: 
	Copy & Save, Windows-Installationen als Klon übertragen oder als Image sichern, c't 22/2019, S. 20
	Die Zeit zurückdrehen, Datenrettung mit dem c't-Notfall-Windows, c't 22/2019, S. 24
	Treibsatz per ­Gießkanne, Treiber im c’t-Notfall-Windows 2021 ergänzen, c't 4/2021, S. 162
#################### parallel-win10-install / install--secondWin-mirrorong-win10: ########################
	- c’t 2/2017, S. 88 	:  Axel Vahldiek, Versuchslabor, Zweit-Windows per Drag & Drop,
	-! see wimage-nts ! do it easily with CT-WImage-USB-Stick ! on the same PC to different partitions/HDs/Medias, OK! on different PCs, due to product-key, problem, if they run parallel ! see nts there bzw. see last section of ct.21.10--178-181--FAQ-WImage.pdf !
#################### System-Wiederherstellung-Configs (-punkte): ########################################
	-!! c’t 2021, Heft 10 --S. 012-017
	- see for Imaging,... see extra dnts of CT-WImage ! obv. the win-abbild/imaging MS-app is obsolete !?!? ab win10-1803 !?
####################   VHDs, virtualizations , Hyper-V : ######################################
- ct.20.20--162 	: Mit c't-WIMage erstellte Images in Hyper-V-VMs wiederherstellen: VM-Generator, c’t-Skript erstellt Windows-VMs in Hyper-V, c't 20/2020, S. 162
- c’t 20/2020, S. 162 	: c’t-Win2Hyper-V ,  Axel Vahldiek, VM-Generator, c’t-Skript erstellt Windows-VMs in Hyper-V  :  Wiederherstellen in einer mit Hyper-V erstellten virtuellen Maschine mithilfe von c’t-Win2Hyper-V
- c’t 2/2017, S. 88 	: c’t-Win2VHD     ,  Axel Vahldiek, Versuchslabor, Zweit-Windows per Drag & Drop,
- ct.18.02--094  Virtualisierer für Windows
