___________________ commandline-commands of MsWins, as copy/move/md5/... : ___________________________
- for cmdUtils (as msinfo32/controlpanel/compmgm/...) see extra-dnts !! here ONLY std-cmdlineCmds (Not-Utils/Progs) for fileshandling,....
##________________________________________  ___________________________


#####  ==========  docs...:
-!! RF: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
##________________________________________  ___________________________


#####  ==========  cmdline-terminal-window-itself:
	- https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands  :
	HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor\CompletionChar
	HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor\PathCompletionChar
	HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor\CompletionChar
	HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor\PathCompletionChar
##________________________________________  ___________________________


#####  ==========  MD5, SHA Checksum Integrity Verifier (FCIV) utility to compute the MD5 or SHA-1 :
	- short:   FCIV -md5 -sha1 path\filename.ext :
	MD5 is a hashing algorithm that creates a 128-bit hash value. SHA-1 is a hashing algorithm that creates a 160-bit hash value.
	You can use the File Checksum Integrity Verifier (FCIV) utility to compute the MD5 or SHA-1 cryptographic hash values of a file. For additional information about the File Checksum Integrity Verifier (FCIV) utility, click the following article number to view the article in the Microsoft Knowledge Base:
	To compute the MD5 and the SHA-1 hash values for a file, type the following command at a command line:
	FCIV -md5 -sha1 path\filename.ext
	For example, to compute the MD5 and SHA-1 hash values for the Shdocvw.dll file in your %Systemroot%\System32 folder, type the following command:
	FCIV -md5 -sha1 c:\windows\system32\shdocvw.dll
	Last Updated: Aug 20, 2020
	https://support.microsoft.com/en-us/help/889768/how-to-compute-the-md5-or-sha-1-cryptographic-hash-values-for-a-file
	https://support.microsoft.com/en-us/help/841290/availability-and-description-of-the-file-checksum-integrity-verifier-u
