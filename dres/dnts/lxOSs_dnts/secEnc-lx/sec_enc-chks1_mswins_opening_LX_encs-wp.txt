________ opening Lx-enc-file-containers in Win7 /_180301 ___________
- FreeOTFE (-explorer) the First choice !! all others are also based on it !
- for EXT4/... formatted containers you need also the EXT-reader ...as Linux_Reader/diskinternals : https://www.diskinternals.com/linux-reader/ , Supported file systems: Ext2, Ext3, Ext4, ReiserFS, HFS, HFS+, NTFS, FAT, exFAT ! is ONLY reader! no writing!!
	/OR ext4-readers by booting as IFS/.... which usu. is not the case in uue1Env !
##________________________________________  ___________________________


#####  ==========  FreeOTFE ver. 5.21 , Treiber ver. 5.20 : OK as a1/admin  /OR use only FreeOTFE Explorer :

	_______:  here intest started as Portable-version (without installation) so in case of Peop-PCs ....:
- OK: also as potable gestartet (as a1! so must be checked if not admin!?) opened+mounted encfs1vfatluks  !! enc-fs-vfat-LUKS /_180301
- OK also encfs1vfat (NOT LUKS!) but you must set the wright params both for Schlussel-/PW-ENC AND also then for the file itself!:
	- first did NOT work due to wrong OPTs!:  mounted but could NOT read! so some enc-params were not correctly specified probably ...!
	- but then OK with OPTs (see the appropriate mesp.sh script /Or nts for the right params, but here the origin was:
		see the images/snapshots for confs! :
		export enc_open_params1='--hash=ripemd160  --cipher=aes-cbc-essiv:sha256  --key-size=256  --offset=0  --skip=0' ;##--so in FreeOTEF:
		Schluessel-Hash (Schluessel /first-TAB): RIPEMD-160 (Linux; Twice, with A) ,BUT DeActivated-checkbox of "Hash with A ..." (NOT-active!)
		File-Opts (Verschluesselung-TAB / second-TAB), von oben nach unten:
		Cypher : AES (256 bit CBC)
		IV-Generierung:
		Sector-IV:  ESSIV  with  Position-NULL "begin der Hot Datei"
		IV-Hash:  SHA-256
		IV-Cypher:  AES (256 bit CBC)
- OK: LUKS-EXT4-based-mespfs , opened-BUT to read them you need Linux_Reader/diskinternals ,..
- OK:  PlainTypeEnc+EXT4_Formatted (checked both encfs1 + new mespfsc1_RF-180225-101950 , OK!): But needs EXT4-Explorer after mounting !
	- MsWin-Explorer can NOT read it on the mounted-drive-letter!) , so it was ok with FreeOTFE + diskinternals.com/linux-reader/
	- BUT do not try to read files under mounted-drive-letter! Linux_Reader/diskinternals.com shows you the contents under its Valume-Label !!
	- sometimes some extracted files were bullshits !?!? (as rz1.txt or curr-formatted-ab.txt ...!?!?)

	_______:  see its docs in its zip-file
- can be started without installation in portable mode, just unzip and start it! but without admin then use only FreeOTFE Explorer, otherwise as admin more ...:
- open LX-files with menu "Datei --> Linux-Volume --> Datei-Mounten"  und nicht direkt "Datei --> Datei-Mounten" !
- Administrator rights are required in order to start and stop portable mode.
- Alternativly, use FreeOTFE Explorer instead - which doesn't need drivers at all
##________________________________________  ___________________________


#####  ==========  LibreCrypt-Explorer ver. 6.2 :   /_180301
- opened ONLY encfs1vfatluks  !! enc-fs-vfat-LUKS
- NOt opened: encfs1vfat (plain-type-enc + vfat-formatted) , encfs1  (plain-type-enc + ext4-formatted same as mespfsX !!)
##________________________________________  ___________________________


#####  ==========  VeraCrypt (was also installed) but NOT-OK-obv  !
- obviouly could not open even encfs1vfatluks (enc-fs-vfat-LUKS), but not tested intensively, because FreeOTFE looks fine ..!
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
--################## GPGs-on-MsWins : ################################################
- OK: C:\up1\t1\nps\wks1_CP\enc-gpg-pw1> C:\progs\GnuPG\bin\gpg  -o  unp1.tgz  -d  t1.tgz.gp1   ##--!!-do NOT forget "-o ... " otherwise PIPS....!
- OK: Gpg4win (Gui) :  "C:\progs\Gpg4win\bin\kleopatra.exe"
