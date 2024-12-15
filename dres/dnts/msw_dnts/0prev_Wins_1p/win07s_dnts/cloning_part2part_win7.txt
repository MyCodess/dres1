_____________ win7.part.manually.cloning:  __________
-!! see also USB-cloning-nts + CT.article there!!

	_______:  eg here:
	from part.2 (source) ---> part.1 (target) : win7.installed.on.part2

	_______:  need: win7.stick/dvd/repair + installed.win7.on.part eg here part.2
- ntfsclone did not work properly : booted still always from the source/old Partition!! so obviously boot.sector was also included in ntfsclone-image!?
	even with bcdboot /s... later applied to the new part, no use! still bootet from source.part!!
##________________________________________  ___________________________


#####  ==========  diskpart: creation + formating target.part , eg part1:
- boot from win7.stick
- (with Shift+F10 in language-selection-window you get a Dos-Fesnter...)
-! in win7.stick: call notepad from cmd and file-->open: use the small explorer, which you get there!
-!! MUST be new formatted with diskpart!!
	if possible, even re-create the partition also again fresh! ist just better:
X:\>diskpart
lis dis
sel dis 0
sel part 1
detail part
(if possible: delete part ; create part primary ; list part )
sel part 1
active
format fs=ntfs quick  label=P1_win7b
assign letter=K  ##or any letter; here eg K: for target.part
exit

	_______:  --
##________________________________________  ___________________________


#####  ==========  copying: ca. 30 Min on x13 with 16GB-source-part:
here eg C: is part.2/installed.win7 (check it with notepad/dir/....)
(problems with Junctions in up1, so remove it remporary,...?? !!Vorsicht, removing from cmd will DELETES all Link-Targets, not only the link itself!!)
xcopy  C:  K:  /kreisch /B /Q
for K: --> check sizes/free/...
cometics: rename 00_xx.txt flag,..., ; put it in autostart-dir,... :  copy  k:\00_P1_win7b.txt  "k:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"\
##________________________________________  ___________________________


#####  ==========  bcd
check: target.part/part.1 is ACTIVE !!
bcdeidt ---> check entries
bcdboot K:\Windows /s K: /l en-us  # K: is the CURRENT letter of part.1/target.part/.nem.win7
bcdeidt ---> check entries : must see new entry of "windows 7" for new installation
##________________________________________  ___________________________


#####  ==========  regedit!:
regedit --> loade hive of target.part/part.1 :
	"K:\Windows\System32\config\SYSTEM"
	--> remove mountedDevices (letters asigned! so that the new part can get C:, otherwise it is assigend to the old one!)
	(could also just chenage C: and source.target.letter, but just deleting is easier)
##________________________________________  ___________________________


#####  ==========  REBOOT ! done!=================
- assigning good drive.letters again + HD-parts-labels-renaimg,...
- easybcd : renaming, adding,...
- pagefile
- if needed (pre.SP1.dlls weg) : dism /online /Cleanup-Image /spsuperseded
