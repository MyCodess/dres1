________ SymLinks, Hardlinks, Junctions, Links, ln,... in Win7/Win10:  mklink /d /J /H   (not old shortcuts/Verknuepfungen/.lnk): ____________
https://msdn.microsoft.com/en-us/library/windows/desktop/aa365006(v=vs.85).aspx
http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html#junctions
##________________________________________  ___________________________


#####  ==========  Summary-nts:
-! see below the try1/test-180406-win10-coll-protocl  to understand this notes!
-!! DIFF between links for FILS <--> DIRs  for mklink on WINs !! (is not the same as in Lx !)
-!! DIFF :
	symlinks	== ca. "ln -s" in Lx-SymLink (so you see the target file/dir by ls/dir ! so is NOT-tranparent for the target!)
	HardLinks	== ca. "ln " in Lx /hardlink   (so you do NOT see the target file/dir by ls/dir ! so tranparently refers to the target!)
	symlinks ONLY allowed for LOCAL Volumes/Drives/Parts !! (no Network or Ext-Media-Targets !!)
	HardLinks ONLY allowed for SAME LOCAL  Volume/Drive/Part !! (so not even to other local partitions! and anyway NOT to NW ,...!!)
-!! BE CAREFUL by deleting hardlinks/junctions!! see notes below !!
-!!! Vorsicht  by deleting/copying , AND also diff Explorer <--> cmd (xcopy...) by copying/deleting/...:

	_______:  FILES mklink :
- mklink		--> File-symlink   ==  ln -s
- mklink /H	--> File-Hardlink == ln

	_______:  DIRs mklink:
- mklink /D	--> DIR-symlink  == ln -s
- mklink /J		--> DIR-Hardlink/Junction == ln  (in WIN is called JUNCTION! only for DIRs! for files is called symlink !)

	_______:  -- Protocol-short:----------

	_______:  files-links:
T:\t1\varu\varau\wks\links1>mklink  fileLink1-ohneH.txt  d1\da.txt
symbolic link created for fileLink1-ohneH.txt <<===>> d1\da.txt
T:\t1\varu\varau\wks\links1>mklink /H  fileLink1--mitH.txt  d1\da.txt
Hardlink created for fileLink1--mitH.txt <<===>> d1\da.txt
T:\t1\varu\varau\wks\links1>dir /o
28/01/2018  11:00             8.365 fileLink1--mitH.txt
06/04/2018  17:23    <SYMLINK>      fileLink1-ohneH.txt [d1\da.txt]
...

	_______:  DIR-links:
T:\t1\varu\varau\wks\links1>mklink   dirLink1-ohneH   d1   ##--> use /D for DIRs !! not /H !! see below !
symbolic link created for dirLink1-ohneH <<===>> d1
T:\t1\varu\varau\wks\links1>mklink /J  dirLink1--mitJ   d1
Junction created for dirLink1--mitJ <<===>> d1
T:\t1\varu\varau\wks\links1>mklink /D dirLink1--mitD   d1
symbolic link created for dirLink1--mitD <<===>> d1
T:\t1\varu\varau\wks\links1>dir /o
06/04/2018  18:03    <SYMLINKD>     dirLink1--mitD [d1]
06/04/2018  17:26    <JUNCTION>     dirLink1--mitJ [T:\t1\varu\varau\wks\links1\d1]
06/04/2018  17:25    <SYMLINK>      dirLink1-ohneH [d1]
28/01/2018  11:00             8.365 fileLink1--mitH.txt
06/04/2018  17:23    <SYMLINK>      fileLink1-ohneH.txt [d1\da.txt]
....
see below the full protoco!
##________________________________________  ___________________________


#####  ==========  Creating links :
	mklink 4 variations :  FILE-symlink+hardlink and DIR-symlink+hardlink  (DIR-Hardlink is called JUNCTION in WINs !):
	1- symbolic link to a file:		mklink      Link  Target     ##--just-no-params!
	2- hard link pointing to a file:	mklink /H  Link  Target
	3- symbolic link pointing to a directory:	mklink /D Link Target
	4- hard link pointing to a directory, also known as a directory junction:  	mklink /J Link Target
##________________________________________  ___________________________


#####  ==========  Deleting links/Junctions:
	-!! ONLY use rmdir to delete junctions/symlind, NOT del !!:
	-!! if you delete a file in a Junction it is deleted at the original location.!!
	-!! TIP: for deleting ONLY the junction/hardlink/symlink ITSELF (not its target) from cmd use: rmdir junctionName instead del/erase!! ONLY rmdir!!
	"del junctionName/hardlinkname" will remove target.contents!!! "rmdir junction" will remove the link itself!!
	- Explorer-Deleting OK: Deleting a Junction/Symlink in Explorer, deletes only the link, so OK! BUT:
	- BUT deleting a Junction/Symlink cmd-window, deletes the Target-Dir/File-contents fully!!
##________________________________________  ___________________________


#####  ==========  Copying links DIRs/Files :
	- Explorer copies FULL target.contens of symlinkD/junction links!! (Explorer ONLY understands the old shortcuts/Verknuepfungen/.lnk, but not mklink-stuff!
	- "xcopy /B" bzw "robotcopy /..." understands <symlink/D> and copies only the link itselt, BUT it does NOT understand Junctions (mklink /J) and copies their FULL contents!!
	-!! "xcopy /b" works fine for <SYMLINKD> and <SYMLINK> so creted with "mklink /D" for folders or just "mklink" for files
		BUT NOT for junctions ("mklink /J"). by junctions it copies links.contents fully, even with /b switch!!
	-!! do not use hardlinks "mklink /H"! it is hard==physically (ln ohne -s), an you do NOT see by "dir",... the link! and xcopy also copies the target!!
	-!! so use symbolink links only: mklink for files , and "mklink /d" for dirs!!
	-!! also do NOT use Junctions, due to bad problems by copying/xcopy/robotcopy!! they all copy then the target, not the link itself!!
##________________________________________  ___________________________


#####  ==========  !!! Fazit: use only mklink [/D] and xcopy (not explorer) and rmdir (not del):
	- "linux ln -s" ca == "mklink" for files, and "mklink /D" for DIRs !! (no Junctions due to problems with copying)
	- creating links for BMs:  for BMs use ONLY normal old mouse-shortcuts ("verknuepfung mit", einfach mit Maus, .lnk-files): so NOT transparent!!
	- creating links for /up1 ,...: for Filessystems (anywhere where you want linux-ln) then use mklink, with: SymbolicLinks for files and "mklink /D" for DIRs!
	- deleting links:  ONLY use rmdir , and NOT del/erase
	- copying  links:  xcopy /B (BUT does NOT work for junctions; only OK for <SYMLINK[D]>
	- so All stuff directly in up1-dir junctions/symlinks , but all stuff in Favorites-/BMs-Dir only shortcuts/verknuepfungen!
##________________________________________  ___________________________


#####  ==========  
-!! see: "W:\docs\MSs\Win7s\WPs_Win7\LinkShellExtension_JunctionsHardlinks_p.pdf" AND nts in devres--win7s_collWPs_nts.txt !!
-!! diff: Lx-links/ln in MsWins are: Junctions + Symbolic-Links <---> as opposit to shortcuts/Verknuepfungen/soft-links, which are .lnk-files and are only texuell hints to the target (but not embedded OS-/Filesystem-Feature !!)
-!! MS differentiates between links for FOLDERs or for FILEs, so:
	1- Shortcut/Verknuepfung/old-shortcuts-in-WXP/old-.lnk-files (pre Vista; wxp had a bit): NOT-transparent as ln in Lx! just TEXTUELL links, NOT real links, not evern symbolic links!
	2- Hardlink==symlink==SymbolicLinks:  ln for files,   as ln in Lx ; only possible in the SAME-Local-NTFS-Filesystem; transparent!
	3- Junction: ln for folders, as ln in Lx ; only possible in the Whole-Local-NTFS-Filesystems (But no NW-shares!!); transparent!
	4-!! xcopy flag "/B" works ONLY for symlinks (mklink /H) BUT not for Junctions!! xcopy /B of junctions copies the WHOLE link-targets!!
	-!! Transparency: Transparency means that an application can access them just as they would any other file,
	-!!! doc-wp:
		SymbolicLinks(=Hardlinks) are to files what Junctions are to folders in that they are both transparent and Symbolic.
		Transparency means: that an application can access them just as they would any other file.
		Symbolism means: that the data objects can reside on any available volume, i.e. they are not limited to a single volume like Hardlinks.
		Symbolic Links differ from Shortcuts in that they offer a transparent pathway to the desired data object.
		with a shortcut (.lnk), something has to read and interpret the content of the shortcut file and then open the file that it references (i.e. it is a two step process).
		When an application uses a symlink it gains immediate access to the data object referenced by the symlink (i.e. it is a one step process).
    * Supported platforms are NT4/W2K/WXP/W2K3/W2K8/WXP64/Vista/Vista/Windows7 in 32bit, 64bit or Itanium.

	_______:  HardLinks: ONLY to FILES (NOT DIRs) on the same Volume (NOT other parts of the same comuter and NOT NWs,...):
	A hard link is the file system representation of a file by which more than one path references a single FILE in the same VOLUME.
	* Hardlinks can only be made on NTFS volumes, under the supported platforms.
    * Hardlinks can only be made within one NTFS volumes, and can not span across NTFS volumes.
	A hard link is the file system representation of a file by which more than one path references a single file in the same volume. 
    ... see WP

	_______:  junctions: ONLY to Directories on LOCAL-fs !
	- junction (working links) can be ONLY generated/angelegt on NTFS , ONLY for Directories, AND ONLY targeting LOCAL-fs! (no NW-shares):
	- junctions to NW-Dirs NOT possible! only to local ones, as in: C:\up1> mklink /D/J  w  w:\  ---> Local volumes are required to complete the operation.
	sysinternals: ... Notethat Windows does not support junctions to directories on remote shares.
	-! MS:  references are separate directories, and a junction can link directories located on different local volumes on the same computer (NOT in NW or Ext-Medias!)
- Link Shell Extension-wp: They can be created with the POSIX command ln included in the Windows Resource Kit, the fsutil command utility included in Windows XP or my command line ln.exe utility  Thus, using standard Windows facilities Hardlinks can only be created at the command prompt, which can be tedious, especially when Hardlinks to multiple files are required or when one only makes occasional use of Hardlinks.  Support for Junctions in standard Microsoft software offerings is even more limited than that offered for Hardlinks.
--######################### coll-WPs-Junctions/links in Wins: #############################################
##________________________________________  ___________________________


#####  ==========  Links, Hardlinks, Junctions .... in Win7: ==================
-!! diff: in MS Hardlinks are: Junctions + Symbolic-Links <---> as opposit to shortcuts/Verknuepfungen/soft-links, whichare .lnk-files and are only texuell hints to the target (but not embedded OS-/Filesystem-Feature !!)
- see:http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html#junctions :
Hardlinks are a feature common to many Unix based systems, but are not directly available with NT4/W2K/WXP. It is a feature, which must be supported by the file system of the operating system.
So what are Hardlinks? It is common to think of a file as being an association between a file name and a data object. Using Windows Explorer, the file system can be readily browsed, showing a 1:1 relationship between the file name and the data object, but this 1:1 relationship does not hold for all file systems.
Some file systems, including UFS, XFS, and NTFS have a N:1 relationship between file name and the data object, hence there can be more than one directory entry for a file.
So, how does one create multiple entries for the same data object? In Unix there is a command line utility ln, which is used to create link entries for existing files, hence there are many file names, or so called Hardlinks, for the one data object.
For each HardLink created, the file system increments a reference count stored with the data object, i.e. it stores how many file names refer to the data object, this counter is maintained (by the file system) within the data object itself. When a file name referencing a data object is deleted, the data objects reference count is decremented by one. The data object itself only gets deleted when the reference count is decremented to zero.
The reference count is the only way of determining whether there are multiple file name references to a data object, and it only informs of their number NOT there whereabouts.
Junctions are wormholes in the tree structure of a directed graph. By browsing a Junction a maybe far distant location in the file system is made available. Modifying, Creating, Renaming and Deleting files within a junction tree structure operates at the junction target, i.e. if you delete a file in a Junction it is deleted at the original location.
Symbolic Links are to files what Junctions are to folders in that they are both transparent and Symbolic. Transparency means that an application can access them just as they would any other file, Symbolism means that the data objects can reside on any available volume, i.e. they are not limited to a single volume like Hardlinks. Symbolic Links differ from Shortcuts in that they offer a transparent pathway to the desired data object, with a shortcut (.lnk), something has to read and interpret the content of the shortcut file and then open the file that it references (i.e. it is a two step process). When an application uses a symlink it gains immediate access to the data object referenced by the symlink (i.e. it is a one step process).
Limitations
    * Supported platforms are NT4/W2K/WXP/W2K3/W2K8/WXP64/Vista/Vista/Windows7 in 32bit, 64bit or Itanium.
    * Hardlinks can only be made on NTFS volumes, under the supported platforms.
    * Hardlinks can only be made within one NTFS volumes, and can not span across NTFS volumes.
    * Junctions can not be created on NTFS volumes with NT4.
    * The Pick Link Source and Drop ... choices are only visible, if its possible to create Hardlinks/Junctions/Symbolic Links. E.G.: If you select a file on a FAT drive and press the action button, you wont see the Pick Link Source in the action menu, because FAT file systems, don't support Hardlinks/Junctions/Symbolic Links. This also happens, if you select source files on a network drive, or select a file as destination, etc.
    * There is an OS limit of creating more than 1023 hardlinks per file. This is less known, but it is there.
##________________________________________  ___________________________


#####  ==========  
--######################### coll-Protocols of trys/tests/wks/... for mklink : #################################################
##________________________________________  ___________________________


#####  ==========  try1/test-180406-win10-coll-Protocol :
T:\t1\varu\varau\wks\links1>dir /o /s
 Directory of T:\t1\varu\varau\wks\links1
06/04/2018  16:35    <DIR>          .
06/04/2018  16:35    <DIR>          ..
06/04/2018  16:31    <DIR>          d1
06/04/2018  16:32    <DIR>          d2
28/01/2018  11:00            47.037 History.txt
28/01/2018  11:00             3.990 License.txt
28/01/2018  11:00             1.688 readme.txt
               3 File(s)         52.715 bytes
 Directory of T:\t1\varu\varau\wks\links1\d1
06/04/2018  16:31    <DIR>          .
06/04/2018  16:31    <DIR>          ..
28/01/2018  11:00             8.365 da.txt
28/01/2018  11:00             9.638 de.txt
               2 File(s)         18.003 bytes
 Directory of T:\t1\varu\varau\wks\links1\d2
06/04/2018  16:32    <DIR>          .
06/04/2018  16:32    <DIR>          ..
28/01/2018  11:00            18.290 hi.txt
28/01/2018  11:00             8.620 hr.txt
               2 File(s)         26.910 bytes
     Total Files Listed:
               7 File(s)         97.628 bytes
               8 Dir(s)  210.449.092.608 bytes free
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>dir /o
 Volume in drive T is T1_LOCFS
 Volume Serial Number is 5EE0-0E31
 Directory of T:\t1\varu\varau\wks\links1
06/04/2018  16:35    <DIR>          .
06/04/2018  16:35    <DIR>          ..
06/04/2018  16:31    <DIR>          d1
06/04/2018  16:32    <DIR>          d2
28/01/2018  11:00            47.037 History.txt
28/01/2018  11:00             3.990 License.txt
28/01/2018  11:00             1.688 readme.txt
               3 File(s)         52.715 bytes
               4 Dir(s)  210.449.092.608 bytes free
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>mklink  fileLink1-ohneH.txt  d1\da.txt
symbolic link created for fileLink1-ohneH.txt <<===>> d1\da.txt
T:\t1\varu\varau\wks\links1>mklink /H  fileLink1--mitH.txt  d1\da.txt
Hardlink created for fileLink1--mitH.txt <<===>> d1\da.txt
T:\t1\varu\varau\wks\links1>dir /o
 Volume in drive T is T1_LOCFS
 Volume Serial Number is 5EE0-0E31
 Directory of T:\t1\varu\varau\wks\links1
06/04/2018  17:24    <DIR>          .
06/04/2018  17:24    <DIR>          ..
06/04/2018  16:31    <DIR>          d1
06/04/2018  16:32    <DIR>          d2
28/01/2018  11:00             8.365 fileLink1--mitH.txt
06/04/2018  17:23    <SYMLINK>      fileLink1-ohneH.txt [d1\da.txt]
28/01/2018  11:00            47.037 History.txt
28/01/2018  11:00             3.990 License.txt
28/01/2018  11:00             1.688 readme.txt
               5 File(s)         61.080 bytes
               4 Dir(s)  210.449.088.512 bytes free
T:\t1\varu\varau\wks\links1>dir d1
 Volume in drive T is T1_LOCFS
 Volume Serial Number is 5EE0-0E31
 Directory of T:\t1\varu\varau\wks\links1\d1
06/04/2018  16:31    <DIR>          .
06/04/2018  16:31    <DIR>          ..
28/01/2018  11:00             8.365 da.txt
28/01/2018  11:00             9.638 de.txt
               2 File(s)         18.003 bytes
               2 Dir(s)  210.449.088.512 bytes free
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>mklink /H  dirLink1--mitH   d1
Access is denied.
T:\t1\varu\varau\wks\links1>mklink   dirLink1-ohneH   d1
symbolic link created for dirLink1-ohneH <<===>> d1
T:\t1\varu\varau\wks\links1>mklink /J  dirLink1--mitJ   d1
Junction created for dirLink1--mitJ <<===>> d1
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>dir /o
 Volume in drive T is T1_LOCFS
 Volume Serial Number is 5EE0-0E31
 Directory of T:\t1\varu\varau\wks\links1
06/04/2018  17:26    <DIR>          .
06/04/2018  17:26    <DIR>          ..
06/04/2018  16:31    <DIR>          d1
06/04/2018  16:32    <DIR>          d2
06/04/2018  17:26    <JUNCTION>     dirLink1--mitJ [T:\t1\varu\varau\wks\links1\d1]
06/04/2018  17:25    <SYMLINK>      dirLink1-ohneH [d1]
28/01/2018  11:00             8.365 fileLink1--mitH.txt
06/04/2018  17:23    <SYMLINK>      fileLink1-ohneH.txt [d1\da.txt]
28/01/2018  11:00            47.037 History.txt
28/01/2018  11:00             3.990 License.txt
28/01/2018  11:00             1.688 readme.txt
               6 File(s)         61.080 bytes
               5 Dir(s)  210.449.088.512 bytes free
T:\t1\varu\varau\wks\links1>
T:\t1\varu\varau\wks\links1>mklink /D dirLink1--mitD   d1
symbolic link created for dirLink1--mitD <<===>> d1
T:\t1\varu\varau\wks\links1>dir /o
 Volume in drive T is T1_LOCFS
 Volume Serial Number is 5EE0-0E31
 Directory of T:\t1\varu\varau\wks\links1
06/04/2018  18:03    <DIR>          .
06/04/2018  18:03    <DIR>          ..
06/04/2018  16:31    <DIR>          d1
06/04/2018  16:32    <DIR>          d2
06/04/2018  18:03    <SYMLINKD>     dirLink1--mitD [d1]
06/04/2018  17:26    <JUNCTION>     dirLink1--mitJ [T:\t1\varu\varau\wks\links1\d1]
06/04/2018  17:25    <SYMLINK>      dirLink1-ohneH [d1]
28/01/2018  11:00             8.365 fileLink1--mitH.txt
06/04/2018  17:23    <SYMLINK>      fileLink1-ohneH.txt [d1\da.txt]
28/01/2018  11:00            47.037 History.txt
28/01/2018  11:00             3.990 License.txt
28/01/2018  11:00             1.688 readme.txt
               6 File(s)         61.080 bytes
               6 Dir(s)  210.449.088.512 bytes free
##________________________________________  ___________________________


#####  ==========  __END1__Protocol-180406 ==================================================
