capacity-problem:
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
C:\Users\a1>dism /online /Cleanup-Image /spsuperseded
Deployment Image Servicing and Management tool
Version: 6.1.7600.16385
Image Version: 6.1.7601.17514
Removing backup files created during service pack installation.
[==========================100.0%==========================]
Service Pack Cleanup operation completed.
The operation completed successfully.
C:\Users\a1>

	_______:  
##________________________________________  ___________________________


#####  ==========  
P1-x13-win7b--2.try
H: now source.win71-P2
C: now new.win7b-P1

	_______:  - access denied in H: later by treesize, after rebooting from new win in P1_win7B:
but both pretty small dirs:
H:\Windows\CSC\v2.0.6
H:\Windows\System32\LogFiles\WMI\RtBackup
##________________________________________  ___________________________


#####  ==========  check:
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
C:\Users\a1>t:
T:\>
T:\>
T:\>chkdsk c:
The type of the file system is NTFS.
Volume label is P1_win7b.
WARNING!  F parameter not specified.
Running CHKDSK in read-only mode.
CHKDSK is verifying files (stage 1 of 3)...
  135680 file records processed.
File verification completed.
  1 large file records processed.
  0 bad file records processed.
  2 EA records processed.
  7 reparse records processed.
CHKDSK is verifying indexes (stage 2 of 3)...
  179984 index entries processed.
Index verification completed.
  0 unindexed files scanned.
  0 unindexed files recovered.
CHKDSK is verifying security descriptors (stage 3 of 3)...
  135680 file SDs/SIDs processed.
Security descriptor verification completed.
  22153 data files processed.
CHKDSK is verifying Usn Journal...
  229056 USN bytes processed.
Usn Journal verification completed.
Windows has checked the file system and found no problems.
  21501951 KB total disk space.
  20370188 KB in 113271 files.
     61528 KB in 22154 indexes.
         0 KB in bad sectors.
    202571 KB in use by the system.
     65536 KB occupied by the log file.
    867664 KB available on disk.
      4096 bytes in each allocation unit.
   5375487 total allocation units on disk.
    216916 allocation units available on disk.
T:\>
##________________________________________  ___________________________


#####  ==========  
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
C:\Users\a1>chkdsk H:
The type of the file system is NTFS.
Volume label is win71_Di2P2_x13.
WARNING!  F parameter not specified.
Running CHKDSK in read-only mode.
CHKDSK is verifying files (stage 1 of 3)...
  207872 file records processed.
File verification completed.
  180 large file records processed.
  0 bad file records processed.
  2 EA records processed.
  187 reparse records processed.
CHKDSK is verifying indexes (stage 2 of 3)...
  252516 index entries processed.
Index verification completed.
  0 unindexed files scanned.
  0 unindexed files recovered.
CHKDSK is verifying security descriptors (stage 3 of 3)...
  207872 file SDs/SIDs processed.
Security descriptor verification completed.
  22323 data files processed.
CHKDSK is verifying Usn Journal...
  35217696 USN bytes processed.
Usn Journal verification completed.
Windows has checked the file system and found no problems.
  20991002 KB total disk space.
  16250540 KB in 91876 files.
     55596 KB in 22324 indexes.
         0 KB in bad sectors.
    311190 KB in use by the system.
     65536 KB occupied by the log file.
   4373676 KB available on disk.
      4096 bytes in each allocation unit.
   5247750 total allocation units on disk.
   1093419 allocation units available on disk.
C:\Users\a1>
##________________________________________  ___________________________


#####  ==========  
--############################ settinug-up P1 fron win7.stick: ###############
##________________________________________  ___________________________


#####  ==========  
Microsoft Windows [Version 6.1.7600]
X:\Sources>notepad
X:\Sources>dir c:
 Datenträger in Laufwerk C: ist P1_x13
 Volumeseriennummer: A6BA-BC31
 Verzeichnis von C:\
05.09.2011  23:37            38.998 00_P1_win7B_x13.txt
10.06.2009  22:42                24 autoexec.bat
10.06.2009  22:42                10 config.sys
05.09.2011  22:53    <DIR>          Program Files
05.09.2011  22:54    <DIR>          progs
02.09.2011  08:53    <DIR>          temp
05.09.2011  23:16    <DIR>          up1
05.09.2011  22:57    <DIR>          Users
05.09.2011  23:07    <DIR>          Windows
               3 Datei(en),         39.032 Bytes
               6 Verzeichnis(se),  1.189.134.336 Bytes frei
X:\Sources>cd ..
X:\>dir
 Datenträger in Laufwerk X: ist Boot
 Volumeseriennummer: D60A-0DC2
 Verzeichnis von X:\
14.07.2009  05:10           111.880 setup.exe
14.07.2009  03:04    <DIR>          Program Files
14.07.2009  05:15    <DIR>          sources
14.07.2009  03:03    <DIR>          Users
14.07.2009  05:05    <DIR>          Windows
               1 Datei(en),        111.880 Bytes
               4 Verzeichnis(se),     29.827.072 Bytes frei
X:\>copy c:\00_P1_win7B_x13.txt I:\
        1 Datei(en) kopiert.
X:\>dir I:\
 Datenträger in Laufwerk I: ist t1_loc
 Volumeseriennummer: 5014-0C16
 Verzeichnis von I:\
05.09.2011  23:37            38.998 00_P1_win7B_x13.txt
05.09.2011  12:33    <DIR>          clone3
05.09.2011  12:57    <DIR>          t1_loc
               1 Datei(en),         38.998 Bytes
               2 Verzeichnis(se), 62.018.052.096 Bytes frei
X:\>diskpart
Microsoft DiskPart-Version 6.1.7600
Copyright (C) 1999-2008 Microsoft Corporation.
Auf Computer: MININT-OKJ5IGT
DISKPART> lis dis
  Datenträger ###  Status         Größe    Frei     Dyn  GPT
  ---------------  -------------  -------  -------  ---  ---
  Datenträger 0    Online          465 GB  4096 KB
  Datenträger 1    Online         3817 MB      0 B
DISKPART> sel disk 0
Datenträger 0 ist jetzt der gewählte Datenträger.
DISKPART> list part
  Partition ###  Typ               Größe    Offset
  -------------  ----------------  -------  -------
  Partition 1    Primär              20 GB  1024 KB
  Partition 2    Primär              20 GB    20 GB
  Partition 3    Primär              75 GB    40 GB
  Partition 0    Erweitert          350 GB   115 GB
  Partition 4    Logisch           2050 MB   115 GB
  Partition 5    Logisch             15 GB   117 GB
  Partition 6    Logisch             60 GB   132 GB
  Partition 7    Logisch            272 GB   192 GB
DISKPART> sel part 1
Partition 1 ist jetzt die gewählte Partition.
DISKPART> deta part
Partition 1
Typ      : 07
Versteckt: Nein
Aktiv    : Ja
Offset in Byte: 1048576
  Volume ###  Bst  Bezeichnung  DS     Typ         Größe    Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
* Volume 1     C   P1_x13       NTFS   Partition     20 GB  Fehlerfre
DISKPART>
DISKPART> del part
Die gewählte Partition wurde erfolgreich gelöscht.
DISKPART> create part prim
Die angegebene Partition wurde erfolgreich erstellt.
DISKPART> list part
  Partition ###  Typ               Größe    Offset
  -------------  ----------------  -------  -------
* Partition 1    Primär              20 GB  1024 KB
  Partition 2    Primär              20 GB    20 GB
  Partition 3    Primär              75 GB    40 GB
  Partition 0    Erweitert          350 GB   115 GB
  Partition 4    Logisch           2050 MB   115 GB
  Partition 5    Logisch             15 GB   117 GB
  Partition 6    Logisch             60 GB   132 GB
  Partition 7    Logisch            272 GB   192 GB
DISKPART> sel part 1
Partition 1 ist jetzt die gewählte Partition.
DISKPART> det part
Partition 1
Typ      : 06
Versteckt: Nein
Aktiv    : Nein
Offset in Byte: 1048576
  Volume ###  Bst  Bezeichnung  DS     Typ         Größe    Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
* Volume 1                      RAW    Partition     20 GB  Fehlerfre
DISKPART> active
Die aktuelle Partition wurde als aktiv markiert.
DISKPART> format fs=ntfs quick  label=P1_win7b
  100 Prozent bearbeitet
DiskPart hat das Volume erfolgreich formatiert.
DISKPART> help assign
    Weist dem Volume mit dem Fokus einen Laufwerkbuchstaben oder
    den Pfadnamen des bereitgestellten Ordners zu.
Syntax:  ASSIGN [LETTER=<D> | MOUNT=<PATH>] [NOERR]
    LETTER=<D>  Der Laufwerkbuchstabe, den Sie dem Volume zuweisen
                             möchten.
    MOUNT=<PATH>
                Der Pfadname des bereitgestellten Ordners, den Sie dem Volume
                zuweisen möchten.
    NOERR       Nur für Skripting. Bei einem Fehler wird die Verarbeitung
                von Befehlen fortgesetzt, als sei der Fehler nicht aufge-
                treten. Ohne den NOERR-Parameter wird "DiskPart" bei
                einem Fehler mit dem entsprechenden Fehlercode beendet.
    Wenn kein Laufwerkbuchstabe oder bereitgestellter Ordner angegeben ist,
    wird der nächste verfügbare Laufwerkbuchstabe zugewiesen. Ein Fehler
    wird generiert, wenn der Laufwerkbuchstabe oder Bereitstellungspunkt
    bereits verwendet wird.
    Mit dem Befehl "ASSIGN" können Sie den Laufwerkbuchstaben ändern,
    der einem Wechseldatenträger zugeordnet ist.
    Startvolumes oder Volumes, die die Auslagerungsdatei
    enthalten, können keine Laufwerkbuchstaben zugewiesen werden. Darüber
    hinaus können Laufwerkbuchstaben weder OEM-Partitionen
    (sofern kein Start in Windows PE erfolgt) noch GPT-Partitionen (GUID-
    Partitionstabelle) zugewiesen werden, die keine Basisdatenpartitionen,
    ESP-Partitionen oder Wiederherstellungspartitionen sind.
    Damit dieser Vorgang erfolgreich ausgeführt werden kann, muss ein
    Volume ausgewählt werden.
Beispiel:
    ASSIGN LETTER=D
DISKPART> assign letter=C
Der Laufwerkbuchstabe oder der Bereitstellungspunkt wurde zugewiesen.
DISKPART> exit
Datenträgerpartitionierung wird beendet...
X:\>diskpart
Microsoft DiskPart-Version 6.1.7600
Copyright (C) 1999-2008 Microsoft Corporation.
Auf Computer: MININT-OKJ5IGT
DISKPART> sel disk 0
Datenträger 0 ist jetzt der gewählte Datenträger.
DISKPART> list part
  Partition ###  Typ               Größe    Offset
  -------------  ----------------  -------  -------
  Partition 1    Primär              20 GB  1024 KB
  Partition 2    Primär              20 GB    20 GB
  Partition 3    Primär              75 GB    40 GB
  Partition 0    Erweitert          350 GB   115 GB
  Partition 4    Logisch           2050 MB   115 GB
  Partition 5    Logisch             15 GB   117 GB
  Partition 6    Logisch             60 GB   132 GB
  Partition 7    Logisch            272 GB   192 GB
DISKPART> sel part 1
Partition 1 ist jetzt die gewählte Partition.
DISKPART> det part
Partition 1
Typ      : 07
Versteckt: Nein
Aktiv    : Ja
Offset in Byte: 1048576
  Volume ###  Bst  Bezeichnung  DS     Typ         Größe    Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
* Volume 1     C   P1_win7b     NTFS   Partition     20 GB  Fehlerfre
DISKPART> exit
Datenträgerpartitionierung wird beendet...
X:\>
X:\>
X:\>dir c:
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\
Datei nicht gefunden
X:\>dir d:
Auf dem Datenträger befindet sich kein erkanntes Dateisystem.
Stellen Sie sicher, dass alle benötigten Dateisystemtreiber geladen sind und dass der Datenträger nicht beschädigt ist.
X:\>dir H:
 Datenträger in Laufwerk H: ist win71_Di2P2_x13
 Volumeseriennummer: 3464-25DD
 Verzeichnis von H:\
18.10.2010  07:51                20 00_win71_Di2P2_x13.txt
10.06.2009  22:42                24 autoexec.bat
10.06.2009  22:42                10 config.sys
01.09.2011  11:26    <DIR>          Program Files
01.09.2011  10:55    <DIR>          progs
02.09.2011  08:53    <DIR>          temp
05.09.2011  09:42    <DIR>          up1
01.09.2011  08:14    <DIR>          Users
05.09.2011  12:06    <DIR>          Windows
               3 Datei(en),             54 Bytes
               6 Verzeichnis(se),  4.803.768.320 Bytes frei
X:\>
X:\>time /T
09:24
X:\>
X:\>
X:\>
X:\>xcopy  H:  c:  /kreisch /B /Q
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
Zugriff verweigert
113251 Datei(en) kopiert
X:\>
X:\>
X:\>
X:\>dir c:
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\
18.10.2010  07:51                20 00_win71_Di2P2_x13.txt
10.06.2009  22:42                24 autoexec.bat
10.06.2009  22:42                10 config.sys
06.09.2011  09:35    <DIR>          Program Files
06.09.2011  09:37    <DIR>          progs
02.09.2011  08:53    <DIR>          temp
06.09.2011  09:37    <DIR>          up1
06.09.2011  09:39    <DIR>          Users
06.09.2011  09:49    <DIR>          Windows
               3 Datei(en),             54 Bytes
               6 Verzeichnis(se),  1.438.765.056 Bytes frei
X:\>
X:\>
X:\>dir H:
 Datenträger in Laufwerk H: ist win71_Di2P2_x13
 Volumeseriennummer: 3464-25DD
 Verzeichnis von H:\
18.10.2010  07:51                20 00_win71_Di2P2_x13.txt
10.06.2009  22:42                24 autoexec.bat
10.06.2009  22:42                10 config.sys
01.09.2011  11:26    <DIR>          Program Files
01.09.2011  10:55    <DIR>          progs
02.09.2011  08:53    <DIR>          temp
05.09.2011  09:42    <DIR>          up1
01.09.2011  08:14    <DIR>          Users
05.09.2011  12:06    <DIR>          Windows
               3 Datei(en),             54 Bytes
               6 Verzeichnis(se),  4.803.768.320 Bytes frei
X:\>dir H:\up1
 Datenträger in Laufwerk H: ist win71_Di2P2_x13
 Volumeseriennummer: 3464-25DD
 Verzeichnis von H:\up1
05.09.2011  09:42    <DIR>          .
05.09.2011  09:42    <DIR>          ..
16.11.2010  20:52    <DIR>          0uue
16.11.2010  21:10    <VERBINDUNG>   BMs_l1nw [c:\up1\0uue\etc\BMs_l1nw]
16.11.2010  21:01    <DIR>          etcu
16.11.2010  21:14    <VERBINDUNG>   optu [c:\progs]
16.11.2010  21:16    <VERBINDUNG>   optu2 [t:\progs2a]
16.11.2010  21:16    <VERBINDUNG>   t1 [T:\t1_loc]
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <VERBINDUNG>   varu [C:\up1\t1\varu]
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  4.803.768.320 Bytes frei
X:\>dir C:\up1
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
06.09.2011  09:37    <DIR>          .
06.09.2011  09:37    <DIR>          ..
06.09.2011  09:37    <DIR>          0uue
16.11.2010  21:10    <DIR>          BMs_l1nw
06.09.2011  09:37    <DIR>          etcu
16.11.2010  21:14    <DIR>          optu
16.11.2010  21:16    <DIR>          optu2
16.11.2010  21:16    <DIR>          t1
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <DIR>          varu
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  1.438.765.056 Bytes frei
X:\>c:
C:\>del /sfq up1
Parameterformat nicht ordnungsgemäß - "sfq".
C:\>del /s /f /q up1
Datei wurde gelöscht - C:\up1\0uue\bin\bins_win7.txt
Datei wurde gelöscht - C:\up1\0uue\etc\win7_vo17_nts - Copy.tws
Datei wurde gelöscht - C:\up1\0uue\etc\win7_vo17_nts.tws
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\MPs - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\nps - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\up1 - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\varau - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\syss_win71_vo17s - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\Win7_Docs_p\CT_Win7s - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\bin - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\bins_win7.txt - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\devnts-mswins - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\l1nw_win7_setup - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\stat_win71_vo17 - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\bins_win7.txt - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\stat_win71_vo17.txt - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\stat_win71_vo17_coll_2So_p.txt - Short
cut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\vo17s_bestell_p_CP.txt - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\win7s_nts.txt - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\win7s_nts_coll_2So_p.txt - Shortcut.ln
k
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\QuickLaunch_User Pinned - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\Start Menu DefaultUser - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\Start Menu Public ProgramData - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\Start Menu User - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\Ws\2So - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\Ws\devres - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\Ws\vo17_dell_docs - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\etc\BMs_l1nw\Ws\WPad - Shortcut.lnk
Datei wurde gelöscht - C:\up1\0uue\res\00_res_nts.txt
Datei wurde gelöscht - C:\up1\0uue\res\console_a1__fullCmdConsoleHive.reg
Datei wurde gelöscht - C:\up1\0uue\res\explorer_a1_101026.reg
Datei wurde gelöscht - C:\up1\0uue\res\kk_cl3_desktop_BGImageColor_red64.themepack
Datei wurde gelöscht - C:\up1\0uue\res\kk_cl3_desktop_BGImageColor_red64_BP.themepack
Datei wurde gelöscht - C:\up1\0uue\res\QuickLaunch_a1_101101.zip
Datei wurde gelöscht - C:\up1\0uue\res\windowsCurrentversion_BigHive_a1_101026.reg
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_blackPixel_100x100.jpg
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_blackPixel_100x100.png
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkBluePixel_100x100_64blue.jpg
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkBluePixel_100x100_64blue.png
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkGreenPixel_100x100_64green.jpg
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkGreenPixel_100x100_64green.png
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkRedPixel_100x100_64red.jpg
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkRedPixel_100x100_64red.png
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_whitePixel_100x100.jpg
Datei wurde gelöscht - C:\up1\0uue\res\DesktopBG_ColorPixels\bg_whitePixel_100x100.png
Datei wurde gelöscht - C:\up1\0uue\res\more\cmd_all1__white.reg
Datei wurde gelöscht - C:\up1\0uue\res\more\cmd_mod1_black.reg
Datei wurde gelöscht - C:\up1\0uue\res\more\kk_cl2_desktop.themepack
Datei wurde gelöscht - C:\up1\0uue\res\Textpads\Helios_Textpad_a1.reg
Datei wurde gelöscht - C:\up1\0uue\res\Textpads\Textpads_nts.txt
Datei wurde gelöscht - C:\up1\0uue\res\Textpads\Helios\TextPad\5.0\config-0701.xml
Datei wurde gelöscht - C:\up1\0uue\res\Textpads\Helios\TextPad\5.0\config.xml
Datei wurde gelöscht - C:\up1\0uue\res\Textpads\Helios\TextPad\5.0\U0007.TLX
Datei wurde gelöscht - C:\up1\0uue\res\Textpads\Helios\TextPad\5.0\U1033.TLX
C:\>dir
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\
18.10.2010  07:51                20 00_win71_Di2P2_x13.txt
10.06.2009  22:42                24 autoexec.bat
10.06.2009  22:42                10 config.sys
06.09.2011  09:35    <DIR>          Program Files
06.09.2011  09:37    <DIR>          progs
02.09.2011  08:53    <DIR>          temp
06.09.2011  09:37    <DIR>          up1
06.09.2011  09:39    <DIR>          Users
06.09.2011  09:49    <DIR>          Windows
               3 Datei(en),             54 Bytes
               6 Verzeichnis(se),  1.443.250.176 Bytes frei
C:\>cddir up1
Der Befehl "cddir" ist entweder falsch geschrieben oder
konnte nicht gefunden werden.
C:\>dir up1
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
06.09.2011  09:37    <DIR>          .
06.09.2011  09:37    <DIR>          ..
06.09.2011  09:37    <DIR>          0uue
16.11.2010  21:10    <DIR>          BMs_l1nw
06.09.2011  09:37    <DIR>          etcu
16.11.2010  21:14    <DIR>          optu
16.11.2010  21:16    <DIR>          optu2
16.11.2010  21:16    <DIR>          t1
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <DIR>          varu
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  1.443.250.176 Bytes frei
C:\>del /s /f /q up1\*.*
C:\>dir up1
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
06.09.2011  09:37    <DIR>          .
06.09.2011  09:37    <DIR>          ..
06.09.2011  09:37    <DIR>          0uue
16.11.2010  21:10    <DIR>          BMs_l1nw
06.09.2011  09:37    <DIR>          etcu
16.11.2010  21:14    <DIR>          optu
16.11.2010  21:16    <DIR>          optu2
16.11.2010  21:16    <DIR>          t1
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <DIR>          varu
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  1.443.250.176 Bytes frei
C:\>cd up1
C:\up1>cd ..
C:\>mkdir up1
C:\>
C:\>
C:\>
C:\>xcopy H:\up1 ,  /BSE
Ist das Ziel , ein Dateiname
oder ein Verzeichnisname
(D = Datei, V = Verzeichnis)?
C:\>dir
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\
18.10.2010  07:51                20 00_win71_Di2P2_x13.txt
10.06.2009  22:42                24 autoexec.bat
10.06.2009  22:42                10 config.sys
06.09.2011  09:35    <DIR>          Program Files
06.09.2011  09:37    <DIR>          progs
02.09.2011  08:53    <DIR>          temp
06.09.2011  10:20    <DIR>          up1
06.09.2011  09:39    <DIR>          Users
06.09.2011  09:49    <DIR>          Windows
               3 Datei(en),             54 Bytes
               6 Verzeichnis(se),  1.443.291.136 Bytes frei
C:\>cd up1
C:\up1>xcopy H:\up1 c:\up1\  /BSEI
H:\up1\0uue\bin\bins_win7.txt
H:\up1\0uue\etc\win7_vo17_nts - Copy.tws
H:\up1\0uue\etc\win7_vo17_nts.tws
H:\up1\0uue\etc\BMs_l1nw\MPs - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\nps - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\up1 - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\varau - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\syss_win71_vo17s - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\Win7_Docs_p\CT_Win7s - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\bin - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\bins_win7.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\devnts-mswins - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\l1nw_win7_setup - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\stat_win71_vo17 - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\bins_win7.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\stat_win71_vo17.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\stat_win71_vo17_coll_2So_p.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\vo17s_bestell_p_CP.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\win7s_nts.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_nts_BMs\0prev\win7s_nts_coll_2So_p.txt - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\QuickLaunch_User Pinned - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\Start Menu DefaultUser - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\Start Menu Public ProgramData - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\win7s_l1nw_BMs\win7_OS_BMs\Start Menu User - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\Ws\2So - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\Ws\devres - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\Ws\vo17_dell_docs - Shortcut.lnk
H:\up1\0uue\etc\BMs_l1nw\Ws\WPad - Shortcut.lnk
H:\up1\0uue\res\00_res_nts.txt
H:\up1\0uue\res\console_a1__fullCmdConsoleHive.reg
H:\up1\0uue\res\explorer_a1_101026.reg
H:\up1\0uue\res\kk_cl3_desktop_BGImageColor_red64.themepack
H:\up1\0uue\res\kk_cl3_desktop_BGImageColor_red64_BP.themepack
H:\up1\0uue\res\QuickLaunch_a1_101101.zip
H:\up1\0uue\res\windowsCurrentversion_BigHive_a1_101026.reg
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_blackPixel_100x100.jpg
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_blackPixel_100x100.png
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkBluePixel_100x100_64blue.jpg
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkBluePixel_100x100_64blue.png
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkGreenPixel_100x100_64green.jpg
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkGreenPixel_100x100_64green.png
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkRedPixel_100x100_64red.jpg
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_darkRedPixel_100x100_64red.png
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_whitePixel_100x100.jpg
H:\up1\0uue\res\DesktopBG_ColorPixels\bg_whitePixel_100x100.png
H:\up1\0uue\res\more\cmd_all1__white.reg
H:\up1\0uue\res\more\cmd_mod1_black.reg
H:\up1\0uue\res\more\kk_cl2_desktop.themepack
H:\up1\0uue\res\Textpads\Helios_Textpad_a1.reg
H:\up1\0uue\res\Textpads\Textpads_nts.txt
H:\up1\0uue\res\Textpads\Helios\TextPad\5.0\config-0701.xml
H:\up1\0uue\res\Textpads\Helios\TextPad\5.0\config.xml
H:\up1\0uue\res\Textpads\Helios\TextPad\5.0\U0007.TLX
H:\up1\0uue\res\Textpads\Helios\TextPad\5.0\U1033.TLX
54 Datei(en) kopiert
C:\up1>dir
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
06.09.2011  10:22    <DIR>          .
06.09.2011  10:22    <DIR>          ..
06.09.2011  10:22    <DIR>          0uue
16.11.2010  21:10    <DIR>          BMs_l1nw
06.09.2011  10:22    <DIR>          etcu
16.11.2010  21:14    <DIR>          optu
16.11.2010  21:16    <DIR>          optu2
16.11.2010  21:16    <DIR>          t1
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <DIR>          varu
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  1.438.765.056 Bytes frei
C:\up1>dir varau
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
Datei nicht gefunden
C:\up1>dir optu2
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1\optu2
16.11.2010  21:16    <DIR>          .
16.11.2010  21:16    <DIR>          ..
               0 Datei(en),              0 Bytes
               2 Verzeichnis(se),  1.438.765.056 Bytes frei
C:\up1>dir optu
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1\optu
16.11.2010  21:14    <DIR>          .
16.11.2010  21:14    <DIR>          ..
               0 Datei(en),              0 Bytes
               2 Verzeichnis(se),  1.438.765.056 Bytes frei
C:\up1>dir
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
06.09.2011  10:22    <DIR>          .
06.09.2011  10:22    <DIR>          ..
06.09.2011  10:22    <DIR>          0uue
16.11.2010  21:10    <DIR>          BMs_l1nw
06.09.2011  10:22    <DIR>          etcu
16.11.2010  21:14    <DIR>          optu
16.11.2010  21:16    <DIR>          optu2
16.11.2010  21:16    <DIR>          t1
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <DIR>          varu
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  1.438.765.056 Bytes frei
C:\up1>dir h:\up1\
 Datenträger in Laufwerk H: ist win71_Di2P2_x13
 Volumeseriennummer: 3464-25DD
 Verzeichnis von h:\up1
05.09.2011  09:42    <DIR>          .
05.09.2011  09:42    <DIR>          ..
16.11.2010  20:52    <DIR>          0uue
16.11.2010  21:10    <VERBINDUNG>   BMs_l1nw [c:\up1\0uue\etc\BMs_l1nw]
16.11.2010  21:01    <DIR>          etcu
16.11.2010  21:14    <VERBINDUNG>   optu [c:\progs]
16.11.2010  21:16    <VERBINDUNG>   optu2 [t:\progs2a]
16.11.2010  21:16    <VERBINDUNG>   t1 [T:\t1_loc]
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <VERBINDUNG>   varu [C:\up1\t1\varu]
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  4.803.768.320 Bytes frei
C:\up1>dir
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1
06.09.2011  10:22    <DIR>          .
06.09.2011  10:22    <DIR>          ..
06.09.2011  10:22    <DIR>          0uue
16.11.2010  21:10    <DIR>          BMs_l1nw
06.09.2011  10:22    <DIR>          etcu
16.11.2010  21:14    <DIR>          optu
16.11.2010  21:16    <DIR>          optu2
16.11.2010  21:16    <DIR>          t1
31.08.2011  22:21    <SYMLINKD>     t2 [U:\t2_RF]
31.08.2011  22:21    <SYMLINKD>     t3 [U:\t3_RF]
05.09.2011  09:42    <SYMLINKD>     t4 [U:\t4_RF]
16.11.2010  21:17    <DIR>          varu
31.08.2011  22:24    <SYMLINKD>     w [T:\t1_loc\w_RF]
               0 Datei(en),              0 Bytes
              13 Verzeichnis(se),  1.438.765.056 Bytes frei
C:\up1>dir BMs_l1nw
 Datenträger in Laufwerk C: ist P1_win7b
 Volumeseriennummer: AEC3-E89A
 Verzeichnis von C:\up1\BMs_l1nw
16.11.2010  21:10    <DIR>          .
16.11.2010  21:10    <DIR>          ..
               0 Datei(en),              0 Bytes
               2 Verzeichnis(se),  1.438.765.056 Bytes frei
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>bcdedit
Windows-Start-Manager

	_______:  ------------------
Bezeichner              {bootmgr}
device                  partition=H:
description             Windows Boot Manager
locale                  en-us
inherit                 {globalsettings}
default                 {default}
resumeobject            {35491525-d692-11e0-bd1d-c522f041ff16}
displayorder            {default}
                        {35491528-d692-11e0-bd1d-c522f041ff16}
                        {6cf55462-d809-11e0-99f7-002269c42fd8}
toolsdisplayorder       {memdiag}
timeout                 5
displaybootmenu         Yes
Windows-Startladeprogramm

	_______:  ----------------------
Bezeichner              {default}
device                  partition=H:
path                    \Windows\system32\winload.exe
description             Win71_x13_Di2P2
locale                  en-us
inherit                 {bootloadersettings}
osdevice                partition=H:
systemroot              \Windows
resumeobject            {35491525-d692-11e0-bd1d-c522f041ff16}
nx                      OptIn
detecthal               Yes
Windows-Startladeprogramm

	_______:  ----------------------
Bezeichner              {35491528-d692-11e0-bd1d-c522f041ff16}
device                  vhd=[I:]\clone3\clone3.vhd
path                    \Windows\system32\winload.exe
description             clone3
locale                  en-us
inherit                 {bootloadersettings}
osdevice                vhd=[I:]\clone3\clone3.vhd
systemroot              \Windows
resumeobject            {35491525-d692-11e0-bd1d-c522f041ff16}
nx                      OptIn
detecthal               Yes
Windows-Startladeprogramm

	_______:  ----------------------
Bezeichner              {6cf55462-d809-11e0-99f7-002269c42fd8}
device                  partition=C:
path                    \Windows\system32\winload.exe
description             P1_win7B
locale                  en-US
osdevice                partition=C:
systemroot              \Windows
C:\up1>bcdboot
Bcdboot - Tool zum Erstellen und Reparieren von Startdateien.
Das Befehlszeilentool "bcdboot.exe" wird zum Kopieren wichtiger
Startdateien auf die Systempartition und zum Erstellen eines neuen
BCD-Systemspeichers verwendet.
bcdboot <Quelle> [/l <Gebietsschema] [/s <Volumebuchstabe>] [/v]
                 [/m [{ID des Betriebssystem-Ladeprogramms}]]
  source            Gibt den Speicherort des Windows-Systemstamms an.
  /l                Gibt einen optionalen Gebietsschemaparameter an, der
                    beim Initialisieren des BCD-Speichers verwendet wird.
                    Der Standardwert ist US-Englisch.
  /s                Gibt einen optionalen Volumebuchstabenparameter an, um
                    Die Zielsystempartition zu bestimmen, auf die die
                    Startumgebungsdateien kopiert werden. Der Standardwert
                    ist die von der Firmware identifizierte Systempartition.
  /v                Aktiviert den ausführlichen Modus.
  /m                Wird eine GUID für das Betriebssystem-Ladeprogramm
                    angegeben, führt diese Option das angegebene
                    Ladeprogrammobjekt mit der Systemvorlage zusammen, um einen
                    startfähigen Eintrag zu erstellen. Andernfalls werden
                    lediglich globale Objekte zusammengeführt.
Beispiele: bcdboot c:\windows /l en-us
           bcdboot c:\windows /s h:
          bcdboot c:\windows /m {d58d10c6-df53-11dc-878f-00064f4f4e08}
C:\up1>
C:\up1>
C:\up1>
C:\up1>bcdboot c:\Windows /s c: /l en-us
Die Startdateien wurden erfolgreich erstellt.
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>
C:\up1>bcdedit
Windows-Start-Manager

	_______:  ------------------
Bezeichner              {bootmgr}
device                  partition=C:
description             Windows Boot Manager
locale                  en-us
inherit                 {globalsettings}
default                 {default}
resumeobject            {b4f931b1-d86a-11e0-92f0-fb9437bfa317}
displayorder            {default}
                        {35491526-d692-11e0-bd1d-c522f041ff16}
                        {35491528-d692-11e0-bd1d-c522f041ff16}
toolsdisplayorder       {memdiag}
timeout                 30
Windows-Startladeprogramm

	_______:  ----------------------
Bezeichner              {default}
device                  partition=C:
path                    \Windows\system32\winload.exe
description             Windows 7
locale                  en-us
inherit                 {bootloadersettings}
osdevice                partition=C:
systemroot              \Windows
resumeobject            {b4f931b1-d86a-11e0-92f0-fb9437bfa317}
nx                      OptIn
detecthal               Yes
Windows-Startladeprogramm

	_______:  ----------------------
Bezeichner              {35491526-d692-11e0-bd1d-c522f041ff16}
device                  partition=H:
path                    \Windows\system32\winload.exe
description             Win71_x13_Di2P2
locale                  en-us
inherit                 {bootloadersettings}
osdevice                partition=H:
systemroot              \Windows
resumeobject            {35491525-d692-11e0-bd1d-c522f041ff16}
nx                      OptIn
detecthal               Yes
Windows-Startladeprogramm

	_______:  ----------------------
Bezeichner              {35491528-d692-11e0-bd1d-c522f041ff16}
device                  vhd=[I:]\clone3\clone3.vhd
path                    \Windows\system32\winload.exe
description             clone3
locale                  en-us
inherit                 {bootloadersettings}
osdevice                vhd=[I:]\clone3\clone3.vhd
systemroot              \Windows
resumeobject            {35491525-d692-11e0-bd1d-c522f041ff16}
nx                      OptIn
detecthal               Yes
C:\up1>regedit
C:\up1>
