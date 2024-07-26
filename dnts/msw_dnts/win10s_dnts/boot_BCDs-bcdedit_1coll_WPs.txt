_____________________ bcd-cmds 1coll ...: ___________________________________________________

##############################  bcdedit MS-Articles for offline-usage (but check online!) : ####################
#####  ==========  !! MS-Article : Boot Configuration Data Editor Frequently Asked Questions :
	- !! a bit older article, but very good for concepts/DEFs ! was by introducing Vista, but still all relevant:
	Article 07/02/2012 14 minutes to read Applies To: Windows Server 2008, Windows Vista
	https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc721886(v=ws.10)

		_______:  ----- Boot Configuration Data
	What is the BCD store?
	The Boot Configuration Data (BCD) store contains boot configuration parameters and controls how the operating system is started in Microsoft® Windows Vista® and Microsoft® Windows Server® 2008 operating systems. These parameters were previously in the Boot.ini file (in BIOS-based operating systems) or in the nonvolatile RAM (NVRAM) entries (in Extensible Firmware Interface–based operating systems). You can use the Bcdedit.exe command-line tool to affect the Windows® code which runs in the pre-operating system environment by adding, deleting, editing, and appending entries in the BCD store. Bcdedit.exe is located in the \Windows\System32 directory of the Windows Vista partition.
	 Note : Even though this document focuses primarily on Windows Vista, this information applies to both Windows Vista and Windows Server 2008.
	 Note: For detailed command and option information at the command prompt, type bcdedit.exe /? command. For example, type bcdedit.exe /? CREATESTORE.
	Why was there a change to BCD from Boot.ini?
	BCD was created to provide an improved mechanism for describing boot configuration data. With the development of new firmware models (for example, the Extensible Firmware Interface (EFI)), an extensible and interoperable interface was required to abstract the underlying firmware. This new design provides the foundation for a variety of new features in Windows Vista (for example, the Startup Repair tool and Multi-User Install shortcuts).
	Where is the BCD file located in the registry?
	BIOS-based operating systems. The BCD registry file is located in the \Boot\Bcd directory of the active partition.
	EFI–based operating systems. The BCD registry file is located on the EFI system partition.
	Can any user modify BCD?
	No. You need administrative credentials to modify BCD.
	What are the ways that I can modify BCD?
	Depending on what you want to change, you can use the following tools to modify BCD:
	Startup and recovery. The Startup and recovery dialog box enables you to select the default operating system to start if you have multiple operating systems installed on your computer. You can also change the time-out value. These settings are located on the Advanced tab in the System Properties dialog box.
	System Configuration utility (Msconfig.exe). Msconfig.exe is a more advanced tool with capabilities that include the following options: /debug, /safeboot, /bootlog, /noguiboot, /basevideo, and /numproc.
	BCD WMI provider. The BCD Windows Management Instrumentation (WMI) provider is a management interface that you can use to script utilities that modify BCD. This is the only programmatic interface available for BCD. For more information, see Boot Configuration Data (BCD) at the Microsoft Web site (https://go.microsoft.com/fwlink/?LinkId=56792).
	BCDEdit.exe. BCDEdit.exe is a command-line utility that replaces Bootcfg.exe in Windows Vista. For more information, see What can I do with Bcdedit.exe?.
	 Note
	You cannot use Bootcfg.exe to modify BCD. However, Bootcfg.exe will remain in the operating system in order to support older operating systems.
	Why don’t I see any Windows entries in the EFI boot manager? And why are there two boot managers?
	All Windows entries are stored in the BCD store. On an EFI-based operating system, there is a single entry in the EFI firmware boot manager called “Windows Boot Manager”. This file is located in \EFI\Microsoft\Boot\Bootmgfw.efi. If you start Windows Boot Manager using the EFI boot manager, you should get a common look and feel on both your EFI-based and PC/AT-based operating systems. For example, the advanced boot options menu should work. The default timeout for the EFI boot manager is 2 seconds to make it easier to boot back and forth between Windows Server 2003 with Service Pack 1 and Windows Vista.

		_______:  ----- Multiboot Environments
	Can I install Windows Vista on a computer that already contains an operating system?
	Yes. You can install Windows Vista on a different partition. It is best to install Windows Vista after you install the older operating systems. Older operating systems will continue to use Boot.ini for boot configuration.
	Should I replace the code that used to work with Boot.ini to now use BCD on Windows Vista?
	No. You will need to alter your code so that it uses Boot.ini for the older operating systems, and so that it uses BCD on Windows Vista.
	In a multiboot environment, does modifying BCD on the pre-Windows Vista operating system modify the boot configuration?
	No. You need to modify BCD to alter the boot configuration for Windows Vista. You also need to modify Boot.ini (for BIOS-based operating systems) or NVRAM (for EFI-based operating systems) to alter boot configuration for the older operating systems.
	Can I disable BCD entirely when I am not booting to Windows Vista?
	No. The boot manager for Windows Vista runs first to determine which operating system to start. Therefore, if you want to boot to the older operating system, you must set the default order to the older operating system in the BCD store. For more information, see How to change the default operating system entry.

		_______:  ----- BCDedit.exe
	What is Bcdedit.exe?
	You can use Bcdedit.exe to modify the Windows code which runs in the pre- operating system environment by adding, deleting, editing, and appending entries in the BCD store. Bcdedit.exe is located in the \Windows\System32 directory of the Windows Vista partition.
	What can I do with Bcdedit.exe?
	Bcdedit.exe currently enables you to do the following:
	•Create a BCD store for a later installation of Windows Server 2008.
	•Add entries to a existing BCD store
	•Modify existing entries in a BCD store.
	•Delete entries from a BCD store.
	•Export entries to a BCD store.
	•Import entries from a BCD store.
	•List currently active settings.
	•Query entries of a particular type.
	•Apply a global change (to all the entries).
	•Change the default time-out value.
	When I run bcdedit /enum, why do I get a Windows Boot Manager entry, a few Windows Boot Loader entries, and a legacy entry?
	The boot environment has been split into two categories: Windows Boot Manager and various boot applications that run in the boot environment. Windows Boot Manager is basically a mini-operating system that controls your boot experience and enables you to choose which boot application to run. There are various boot applications (for example, Windows Boot Loader) and each one does something different. For example, a Windows Boot Loader application loads Windows.
	When you specify /enum, you will get the following:
	One Windows Boot Manager entry (because there is only one boot manager).
	A Windows Boot Loader application for each Windows Vista operating system you have installed on the computer. For example, if you have two different versions of Windows Vista installed on different partitions, you will see two Windows Boot Loader entries.
	One legacy entry. This entry is not a boot application, but instead uses NTLDR and Boot.ini to boot into an operating system that is older than Windows Vista. You will use this entry to boot into Windows Server 2003, Windows XP, and earlier operating systems (if installed on the computer).
	Is there command-line Help for Bcdedit.exe?
	Yes. For detailed command and option information at the command prompt, type bcdedit.exe /? and bcdedit.exe /? Command. For example, type bcdedit.exe /? CREATESTORE.

		_______:  ------ New Ways To Do Familiar Tasks
	How to change the global debugger settings
	At the command prompt type:
	bcdedit /dbgsettings DebugType [debugport Port**] [baudrate** Baud**]**
	[channel Channel] [targetname TargetName]
	Option	Explanation
	DebugType Specifies the type of debugger. DebugType can be one of SERIAL, 1394 or USB. The remaining options
	depend on the debugger type selected.
	Port For SERIAL debugging, specifies the serial port to use as the debugging port.
	Baud For SERIAL debugging, specifies the baud rate to be used for debugging.
	Channel For 1394 debugging, specifies the 1394 channel to be used for debugging.
	TargetName For Universal Serial Bus (USB) debugging, specifies the USB target name to be used for debugging.

		_______:  ---- Examples
	The following command sets the global debugger settings to serial debugging
	over com1 at 115,200 baud:
	bcdedit /dbgsettings serial debugport 1 baudrate 115200
	The following command sets the global debugger settings to 1394 debugging
	using channel 23:
	bcdedit /dbgsettings 1394 CHANNEL 32
	The following command sets the global debugger settings to USB debugging
	using target name "debugging":
	bcdedit /dbgsettings USB targetname debugging
	How to check the debugger settings
	At the command prompt, type:
	bcdedit /enum Type /v
	Option	Explanation
	Type
	Specifies the type of entries to be listed. Type can be one of the following:
	ACTIVE
	FIRMWARE
	BOOTAPP
	BOOTMGR
	OSLOADER
	INHERIT
	ALL
	For example, the following command lists all entries:
	bcdedit /enum all /v
	How to change the default operating system entry
	At the command prompt, type:
	bcdedit /default ID
	Option	Explanation
	ID
	Specifies the default GUID to be used when the time-out expires.
	{466f5a88-0af2-4f76-9038-095b170dc21c} is the predefined GUID for NTLDR.
	You can find the ID for a particular object by specifying bcdedit /enum all.
	Examples
	The following command sets the specified entry as the default boot manager
	entry:
	bcdedit /default {cbd971bf-b7b8-4885-951a-fa03044f5d71}
	The following command sets the legacy Windows loader (Ntldr) as the default
	entry: {466f5a88-0af2-4f76-9038-095b170dc21c} is the predefined GUID for Ntldr.
	bcdedit /default {466f5a88-0af2-4f76-9038-095b170dc21c}
	How to change the boot sequence for the next reboot
	At the command prompt, type:
	bcdedit /bootsequence {ID} {ID} {ID} …
	Option	Explanation
	ID
	Specifies the GUID(s) that make up the boot sequence for the next restart. After this one-time boot it will revert back to the default boot order.
	Examples
	The following command sets the specified operating system as the default for the next restart. After that restart, it will be reset to DISPLAYORDER.
	bcdedit /bootsequence {cbd971bf-b7b8-4885-951a-fa03044f5d71}
	The following command sets two operating system entries and the
	legacy Windows loader (Ntldr) in the boot manager one-time boot sequence:
	bcdedit /bootsequnce {802d5e32-0784-11da-bd33-000476eba25f}
	{cbd971bf-b7b8-4885-951a-fa03044f5d71} {legacy}
	How to change boot manager time-out
	To change the length of time the computer waits until the default operating system is selected, type the following:
	bcdedit /timeout TimeOut
	Option	Explanation
	TimeOut
	Specifies the time to wait, in seconds, before the boot manager selects a default entry.
	For example, the following command sets the boot manager TimeOut to 15 seconds:
	bcdedit /timeout 15
	How to set the boot manager display order
	At the command prompt, type:
	Bcdedit.exe /display {ID} {ID1} {ID2} …
	or
	Bcdedit.exe /displayorder {ID} [/addlast|/addfirst|/remove]
	Option	Explanation
	ID
	Specifies one GUID or a list of GUIDs that make up the display order. You must specify at least one ID.
	For more information about identifiers, type bcdedit /? ID.
	Examples
	The following command sets three operating system entries in the boot manager display order:
	Bcdedit.exe /displayorder {c84b751a-ff09-11d9-9e6e-0030482375e6} {c74b751a-ff09-11d9-9e6e-0030482375e4} {c34b751a-ff09-11d9-9e6e-0030482375e7}
	The following command sets two operating system entries and the legacy Windows loader in the boot manager display order:
	bcdedit /displayorder {802d5e32-0784-11da-bd33-000476eba25f}
	{cbd971bf-b7b8-4885-951a-fa03044f5d71} {legacy}
	The following command adds the entry represented by the GUID to end of the boot menu display order.
	bcdedit.exe /displayorder {c84b751a-ff09-11d9-9e6e-0030482375e6}-addlast
	How to delete a boot entry
	At the command prompt, type:
	bcdedit /delete ID [/f]
	Option	Explanation
	ID
	Specifies the GUID of the boot entry you want to delete. If ID is not specified, the current boot entry ID will be deleted.
	If you specify a well-known GUID, you will have to force the deletion by specifying /f. For example:
	bcdedit /delete {default} /f
	For example, the following command deletes the entry with id {802d5e32-0784-11da-bd33-000476eba25f}.
	bcdedit /delete {802d5e32-0784-11da-bd33-000476eba25f}
	How to turn the kernel debugger on or off
	At the command prompt, type:
	bcdedit /debug [{ID}] {on|off}
	Option	Explanation
	ID
	Specifies the GUID of the boot entry you want to modify. If ID is not specified, it modifies the current boot entry ID.
	For example, the following command enables boot debugging for the specified operating system boot entry:
	bcdedit /debug {cbd971bf-b7b8-4885-951a-fa03044f5d71} on
	 Note
	For more information about IDs, run bcdedit /? ID.
	How to set Physical Address Extension (PAE)
	At the command prompt, type:
	bcdedit /set {ID} pae [Default|ForceEnable|ForceDisable]
	Option	Explanation
	ID
	Specifies the ID of the operating system entry you want to change. If you do not specify ID, the current operating system settings will be modified.
	For example:
	bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f} pae forceenable
	How to set REMOVEMEMORY
	At the command prompt, type the following. Removememory removes memory from the total available memory that the operating system can use.
	bcdedit /set {GUID} removememory bytes
	Option	Explanation
	ID
	Specifies the ID of the operating system entry you want to change. If you do not specify ID, the current operating system settings will be modified.
	bytes
	The number of bytes to remove.
	Example
	This example removes 256 MB of memory from the total available:
	bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f } removememory 256
	How to set MAXMEM/TRUNCATEMEMORY
	At the command prompt, type the following. Truncatememory disregards all memory at or above the specified physical address.
	bcdedit /set {ID} truncatememory bytes
	 Note
	We recommend that you use removememory instead. It does a better job of restricting the operating system to use the specified memory while accounting for memory holes.
	Option	Explanation
	ID
	The ID of the operating system entry you want to change. If you don't specify ID, the current operating system settings will be modified.
	bytes
	Specifies the number of bytes to truncate.
	Example
	This example sets the truncate memory to 1024 MB:
	bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f} truncatememory 1073741824
	How to add a private kernel
	At the command prompt, type:
	bcdedit /set {ID} kernel "Path"
	Option	Explanation
	ID
	Specifies the identifier of the operating system entry you want to change. If you do not specify ID, then the current operating system settings will be modified.
	For example:
	bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f} kernel "mykrnl.dll"
	How to create a new Windows Vista operating system entry
	To create a new Windows Vista operating system entry, use the following procedure:
	To create a new Windows Vista operating system entry
	First, copy the operating system entry you want to replicate and name it NewEntryDescription.
	bcdedit /copy {GuidToCopy} /d “NewEntryDescription”
	This command will split the new GUID. Use the new GUID to modify the partition information by specifying:
	bcdedit /set {NewGuid} device partition=x:
	bcdedit /set {NewGuid} osdevice partition=x:
	Add the new operating system entry created to the display by specifying:
	bcdedit /displayorder {NewGuid} /addlast
	How to list entries of a particular type
	The /enum command lists entries in the BCD store. To list entries, type:
	bcdedit /enum [Type]
	Option	Explanation
	Type
	Specifies the type of entries to list. Type can be one of the following:
	active (default). Lists all entries in the boot manager display order.
	Firmware. Lists all firmware applications entries.
	Bootapp. Lists all boot environment applications entries.
	Bootmgr. Lists all Boot manager entries.
	Osloader. Lists all operating system entries.
	Inherit. Lists all inherit type entries.
	All. Lists all entries.
	Examples
	The following command lists all operating system loader boot entries:
	bcdedit /enum osloader
	The following command lists all boot manager entries:
	bcdedit /enum bootmgr
	How to modify BCD when installing a previous version of Windows onto a computer running Windows Vista
	To install an older Windows operating system on a computer running Windows Vista, use the following procedure.
	To install a previous version of Windows onto a computer running Windows Vista
	Install the previous version of Windows.
	Log on to the older operating system and restore the latest boot manager by running the following. Fixntfs.exe will be in the \boot directory of the active partition.
	fixntfs /lh
	Create a BCD entry for the older operating system by specifying the following. Bcdedit.exe is located in the \Windows\System32 directory of the Windows Vista partition. Description is the description of the new entry for the older operating system.
	Bcdedit /create {legacy} /d “Description”
	Bcdedit /set {legacy} device boot
	Bcdedit /set {legacy} path \ntldr
	Bcdedit /displayorder {legacy} /addlast
	Restart the computer in order for the changes to take effect.
	How to create an entry to boot a WIM image from a hard disk
	To create an entry to boot a Windows Imaging Format (WIM) image, you will need to create an OSloader type entry with RAMDISK options pointing to the boot partition. To do this, use the following procedure. In this procedure, the arcpath multi(0)disk(0)rdisk(0)partition(1) refers to the C: drive on the computer, and Boot.wim is a regular Boot.wim with Winload.exe in the System32 folder inside the WIM image.
	To create an entry to boot a WIM image from hard disk
	Create the {ramdisktoptions} object in your BCD store by specifying the following. Drive should be the drive that contains the image.
	bcdedit /create {ramdiskoptions} /d "Ramdisk options"
	**bcdedit /set {ramdiskoptions} ramdisksdidevice partition=**Drive
	bcdedit /set {ramdiskoptions} ramdisksdipath \boot\boot.sdi
	Create a new boot application entry by specifying:
	bcdedit /create /d "Boot from WIM" /application OSLOADER
	This will return an identifier (GUID) for the newly created entry. This new entry will be referred to as {GUID} in the rest of this procedure. Next specify the following:
	bcdedit /set {GUID} device ramdisk=[c:]\sources\boot.wim,{ramdiskoptions}
	bcdedit /set {GUID} path \windows\system32\winload.exe
	bcdedit /set {GUID} osdevice ramdisk=[c:]\sources\boot.wim,{ramdiskoptions}
	bcdedit /set {GUID} systemroot \windows
	If you are booting into Windows Preinstallation Environment (Windows PE), then you will also need to specify:
	bcdedit /set {GUID} winpe yes
	bcdedit /set {GUID} detecthal yes
	Next specify the following to add your new entry to the display order:
	bcdedit /displayorder {GUID} /addlast
	How to change the debugger settings of a specific entry
	To override the global entry for a specific debugger setting, type one of the following.
	 Note
	This command does not enable or disable the debugger for the specific boot entry.
	To set serial debugging, type:
	bcdedit /set {GUID} debugtype:serial
	bcdedit /set {GUID} baudrate:Baudrate
	bcdedit /set {GUID} debugport:Port
	To set USB debugging, type:
	bcdedit /set {GUID} debugtype:usb bcdedit /set {GUID} targetname:debugging
	To set 1394 debugging, type:
	bcdedit /set {GUID} debugtype:1394 bcdedit /set {GUID} targetname:32
	Example
	The following command sets the debugger setting for c74b751a-ff09-11d9-9e6e-0030482375e4 to serial debugging over com1 at 115,200 baud:
	Bcdedit /set {c74b751a-ff09-11d9-9e6e-0030482375e4} debugtype:serial
	Bcdedit /set {c74b751a-ff09-11d9-9e6e-0030482375e4} baudrate:115200
	Bcdedit /set {c74b751a-ff09-11d9-9e6e-0030482375e4} debugport:1
##________________________________________  ___________________________


#####  ==========  MS-Article:  bcdedit : syntax-overview, highest-cmds-level-intro:
	msCmdsRefs : https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
	bcdedit , 	Article 02/03/2023 ￼8 contributors ￼
	---

	Boot Configuration Data (BCD) files provide a store that is used to describe boot applications and boot application settings. The objects and elements in the store effectively replace Boot.ini.

	BCDEdit is a command-line tool for managing BCD stores. It can be used for a variety of purposes, including creating new stores, modifying existing stores, adding boot menu parameters, and so on. BCDEdit serves essentially the same purpose as Bootcfg.exe on earlier versions of Windows, but with two major improvements:

	Exposes a wider range of boot parameters than Bootcfg.exe.

	Has improved scripting support.

	 Note

	Administrative privileges are required to use BCDEdit to modify BCD.

	BCDEdit is the primary tool for editing the boot configuration of Windows Vista and later versions of Windows. It is included with the Windows Vista distribution in the %WINDIR%\System32 folder.

	BCDEdit is limited to the standard data types and is designed primarily to perform single common changes to BCD. For more complex operations or nonstandard data types, consider using the BCD Windows Management Instrumentation (WMI) application programming interface (API) to create more powerful and flexible custom tools.

	Syntax
	￼
	Copy
	bcdedit /command [<argument1>] [<argument2>] ...
	Parameters
	General BCDEdit Command-Line Options
	Option	Description
	/?	Displays a list of BCDEdit commands. Running this command without an argument displays a summary of the available commands. To display detailed help for a particular command, run bcdedit /? <command>, where <command> is the name of the command you are searching for more information about. For example, bcdedit /? createstore displays detailed help for the Createstore command.
	Parameters that Operate on a Store
	Option	Description
	/createstore	Creates a new empty boot configuration data store. The created store is not a system store.
	/export	Exports the contents of the system store into a file. This file can be used later to restore the state of the system store. This command is valid only for the system store.
	/import	Restores the state of the system store by using a backup data file previously generated by using the /export option. This command deletes any existing entries in the system store before the import takes place. This command is valid only for the system store.
	/store	This option can be used with most BCDedit commands to specify the store to be used. If this option is not specified, then BCDEdit operates on the system store. Running the bcdedit /store command by itself is equivalent to running the bcdedit /enum active command.
	Parameters that Operate on Entries in a Store
	Parameter	Description
	/copy	Makes a copy of a specified boot entry in the same system store.
	/create	Creates a new entry in the boot configuration data store. If a well-known identifier is specified, then the /application, /inherit, and /device parameters cannot be specified. If an identifier is not specified or not well known, an /application, /inherit, or /device option must be specified.
	/delete	Deletes an element from a specified entry.
	Parameters that Operate on Entry Options
	Parameter	Description
	/deletevalue	Deletes a specified element from a boot entry.
	/set	Sets an entry option value.
	Parameters that Control Output
	Parameter	Description
	/enum	Lists entries in a store. The /enum option is the default value for BCEdit, so running the bcdedit command without parameters is equivalent to running the bcdedit /enum active command.
	/v	Verbose mode. Usually, any well-known entry identifiers are represented by their friendly shorthand form. Specifying /v as a command-line option displays all identifiers in full. Running the bcdedit /v command by itself is equivalent to running the bcdedit /enum active /v command.
	Parameters that Control the Boot Manager
	Parameter	Description
	/bootsequence	Specifies a one-time display order to be used for the next boot. This command is similar to the /displayorder option, except that it is used only the next time the computer starts. Afterwards, the computer reverts to the original display order.
	/default	Specifies the default entry that the boot manager selects when the timeout expires.
	/displayorder	Specifies the display order that the boot manager uses when displaying boot parameters to a user.
	/timeout	Specifies the time to wait, in seconds, before the boot manager selects the default entry.
	/toolsdisplayorder	Specifies the display order for the boot manager to use when displaying the Tools menu.
	Parameters that Control Emergency Management Services
	Parameter	Description
	/bootems	Enables or disables Emergency Management Services (EMS) for the specified entry.
	/ems	Enables or disables EMS for the specified operating system boot entry.
	/emssettings	Sets the global EMS settings for the computer. /emssettings does not enable or disable EMS for any particular boot entry.
	Parameters that Control Debugging
	Parameter	Description
	/bootdebug	Enables or disables the boot debugger for a specified boot entry. Although this command works for any boot entry, it is effective only for boot applications.
	/dbgsettings	Specifies or displays the global debugger settings for the system. This command does not enable or disable the kernel debugger; use the /debug option for that purpose. To set an individual global debugger setting, use the bcdedit /set <dbgsettings> <type> <value> command.
	/debug	Enables or disables the kernel debugger for a specified boot entry.
	Related links
	For examples of how to use BCDEdit, see the BCDEdit Options Reference article.

	To see the notation used to indicate command-line syntax, see Command-Line Syntax Key.
##________________________________________  ___________________________


#####  ==========  MS-Article:  BCDEdit Options Reference, Article 12/15/2021
    https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/bcd-boot-options-reference
    --
    Topic	Description
    BCDEdit /bootdebug	The /bootdebug boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.
    BCDEdit /bootsequence	Sets the one-time boot sequence for the boot manager.
    BCDEdit /dbgsettings	The /dbgsettings option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the BCDEdit /debug option.
    BCDEdit /debug	The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.
    BCDEdit /default	Sets the default entry that the boot manager will use.
    BCDEdit /deletevalue	The /deletevalue option deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the BCDEdit /deletevalue command to remove options that were added using BCDEdit /set command. You might need to remove boot entry options when you are testing and debugging your driver.
    BCDEdit /displayorder	Sets the order in which the boot manager displays the multiboot menu.
    BCDEdit /ems	The /ems option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.
    BCDEdit /emssettings	The /emssettings option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the /ems option. The /emssettings option does not enable or disable EMS for any boot entry.
    BCDEdit /enum	The /enum command lists entries in boot configuration data (BCD) store.
    BCDEdit /event	The /event command enables or disables the remote event logging for the specified boot entry.
    BCDEdit /hypervisorsettings	The /hypervisorsettings option sets or displays the hypervisor debugger settings for the system.
    BCDEdit /set	The BCDEdit /set command sets a boot entry option value in the Windows boot configuration data store (BCD). Use the BCDEdit /set command to configure specific boot entry elements, such as kernel debugger settings, memory options, or options that enable test-signed kernel-mode code or load alternate hardware abstraction layer (HAL) and kernel files. To remove a boot entry option, use the BCDEdit /deletevalue command.
    BCDEdit /timeout	Sets the boot manager time-out value.
    BCDEdit /tooldisplayorder	Sets the order in which the boot manager displays the tools menu.
    !! ---> further there links to each param-details !!
##________________________________________  ___________________________


#####  ==========  MS-Article: /set params:
    https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--set
    --
    Overview of Boot Options in Windows
    Boot Options Identifiers
    BCDEdit Options Reference
    BCDEdit /bootsequence
    BCDEdit /bootdebug
    BCDEdit /dbgsettings
    BCDEdit /debug
    BCDEdit /deletevalue
    BCDEdit /displayorder
    BCDEdit /ems
    BCDEdit /emssettings
    BCDEdit /enum
    BCDEdit /event
    BCDEdit /hypervisorsettings
    BCDEdit /set
    BCDEdit /timeout
    BCDEdit /toolsdisplayorder
    Docs  Windows  Windows Drivers  Driver Technologies  Tools for Testing Drivers 
    BCDEdit /set
    Article 03/18/2022 19 minutes to read

        _______:  
    The BCDEdit /set command sets a boot entry option value in the Windows boot configuration data store (BCD). Use the BCDEdit /set command to configure specific boot entry elements, such as kernel debugger settings, memory options, or options that enable test-signed kernel-mode code or load alternate hardware abstraction layer (HAL) and kernel files. To remove a boot entry option, use the BCDEdit /deletevalue command.
    Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the BCDEdit /set command could render your computer inoperable. As an alternative, use the Startup settings or the System Configuration utility (MSConfig.exe) to change boot settings.
     Note Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
    Alternatives to BCDEdit
    Settings startup options
     Tip To avoid the risk associated with using BCDEdit, consider using an alternative method to perform boot configuration discussed in this section.
    Startup Settings
    Some common boot options such as enabling debugging mode are available in the start up options. In Windows 10, the settings can be accessed in Settings, Update and Security, select Recovery. Under Advanced startup, select Restart Now. When the PC reboots, select Startup options. Then select Troubleshoot > Advanced options > Startup Settings , then select Restart button. When the PC restarts, you will be able to set the available startup options.
    System Configuration Utility
    Use the System Configuration Utility (MSConfig.exe) instead of BCDEdit when possible. For more information, see How to open MSConfig in Windows 10.
    Syntax
    bcdedit  /set [{ID}] datatype value
    Parameters [{ID}] The {ID} is the GUID that is associated with the boot entry. If you do not specify an {ID}, the command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces { }. To view the GUID identifiers for all of the active boot entries, use the bcdedit /enum command. The identifier for the current boot entry is {current}. For more information about this option, use the following command: bcdedit /? ID
    Note If you are using Windows PowerShell, you must use quotes around the boot entry identifier, for example: "{49916baf-0e08-11db-9af4-000bdbd316a0}" or "{current}".
    datatype value
    Use the command line help to view options
    Use the command line help for BCDEdit to display information available for a specific version of Windows.
    C:\> BCDEdit /?
    BCDEDIT - Boot Configuration Data Store Editor
    The Bcdedit.exe command-line tool modifies the boot configuration data store.
    The boot configuration data store contains boot configuration parameters and
    controls how the operating system is booted. These parameters were previously
    in the Boot.ini file (in BIOS-based operating systems) or in the nonvolatile
    RAM entries (in Extensible Firmware Interface-based operating systems). You can
    use Bcdedit.exe to add, delete, edit, and append entries in the boot
    configuration data store.
    For detailed command and option information, type bcdedit.exe /? <command>. For
    example, to display detailed information about the /createstore command, type:
     bcdedit.exe /? /createstore
    For an alphabetical list of topics in this help file, run "bcdedit /? TOPICS".
    The following sections describe some common datatypes and their associated values.
    Boot Settings
    bootlog [ yes | no ]
    Enables the system initialization log. This log is stored in the Ntbtlog.txt file in the %WINDIR% directory. It includes a list of loaded and unloaded drivers in text format.
    bootmenupolicy [ Legacy | Standard ]
    Defines the type of boot menu the system will use. ForWindows 10, Windows 8.1, Windows 8 and Windows RT the default is Standard. For Windows Server 2012 R2, Windows Server 2012, the default is Legacy. When Legacy is selected, the Advanced options menu (F8) is available. When Standard is selected, the boot menu appears but only under certain conditions: for example, if there is a startup failure, if you are booting up from a repair disk or installation media, if you have configured multiple boot entries, or if you manually configured the computer to use Advanced startup. When Standard is selected, the F8 key is ignored during boot. Windows 8 PCs start up quickly so there isn't enough time to press F8. For more information, see Windows Startup Settings (including safe mode).
     Note
    The option is available starting with Windows 8 and Windows Server 2012. You can also use the onetimeadvancedoptions to use the Advanced options (F8) menu (Legacy) one time on the next boot.
    bootstatuspolicy policy
    Controls the boot status policy. The boot status policy can be one of the following:
    Boot Status Policy	Description
    DisplayAllFailures	Displays all errors if there is a failed boot, failed shutdown, or failed checkpoint. The computer will fail over to the Windows recovery environment on reboot.
    IgnoreAllFailures	Ignore errors if there is a failed boot, failed shutdown, or failed checkpoint. The computer will attempt to boot normally after an error occurs.
    IgnoreShutdownFailures	Only ignore errors if there is a failed shutdown. If there is a failed shutdown, the computer does not automatically fail over to the Windows recovery environment on reboot. This is the default setting for Windows 8.
    IgnoreBootFailures	Only ignore errors if there is a failed boot. If there is a failed boot, the computer does not automatically fail over to the Windows recovery environment on reboot.
    IgnoreCheckpointFailures	Only ignore errors if there is a failed checkpoint. If there is a failed checkpoint, the computer does not automatically fail over to the Windows recovery environment on reboot. The option is available starting with Windows 8 and Windows Server 2012.
    DisplayShutdownFailures	Displays errors if there is a failed shutdown. If there is a failed shutdown, the computer will fail over to the Windows recovery environment on reboot. Ignores boot failures and failed checkpoints. The option is available starting with Windows 8 and Windows Server 2012.
    DisplayBootFailures	Displays errors if there is a failed boot. If there is a failed boot, the computer will fail over to the Windows recovery environment on reboot. Ignores shutdown failures and failed checkpoints. The option is available starting with Windows 8 and Windows Server 2012.
    DisplayCheckpointFailures	Displays errors if there is a failed checkpoint. If there is a failed checkpoint, the computer will fail over to the Windows recovery environment on reboot. Ignores boot and shutdown failures. The option is available starting with Windows 8 and Windows Server 2012.
    quietboot [ on | off ] Controls the display of a high-resolution bitmap in place of the Windows boot screen display and animation.
    Note Do not use the quietboot option in Windows 8 as it will prevent the display of bug check data in addition to all boot graphics.
    sos [ on | off ]
    Controls the display of the names of the drivers as they load during the boot process. Use sos on to display the names. Use sos off to suppress the display.
    lastknowngood [ on | off ]
    Enables boot to last known good configuration.
    nocrashautoreboot [ on | off ]
    Disables automatic restart on crash.
    resumeobject (id)
    Defines the identifier of the resume object that is associated with this operating system object.
    safebootalternateshell [ on | off ]
    Uses the alternate shell when booted into Safe mode.
    winpe [ on | off ]
    Enables the computer to boot to Windows PE.
    onetimeadvancedoptions [ on | off ]
    Controls whether the system boots to the legacy menu (F8 menu) on the next boot.
    syntax
    Copy
    bcdedit /set {current} onetimeadvancedoptions on
    Display Settings
    bootuxdisabled [ on | off ]
    Disables boot graphics.
    graphicsmodedisabled [ on | off ] Indicates whether graphics mode is disabled and boot applications must use text mode display.
    graphicsresolution
    Defines the graphics resolution, 1024x768, 800x600,1024x600, etc.
    highestmode [ on | off ]
    Enables boot applications to use the highest graphical mode exposed by the firmware.
    Hardware Abstraction Layer (HAL) & KERNEL
    hal file
    Directs the operating system loader to load an alternate HAL file. The specified file must be located in the %SystemRoot%\system32 directory.
    halbreakpoint [ yes | no ]
    Enables the special hardware abstraction layer (HAL) breakpoint.
    kernel file
    Directs the operating system loader to load an alternate kernel. The specified file must be located in the %SystemRoot%\system32 directory.
    useplatformclock [ yes | no ]
    Forces the use of the platform clock as the system's performance counter.
     Note
    This option should only be used for debugging.
    forcelegacyplatform [ yes | no ]
    Forces the OS to assume the presence of legacy PC devices like CMOS and keyboard controllers.
     Note
    This option should only be used for debugging.
    tscsyncpolicy [ Default | Legacy | Enhanced ]
    Controls the times stamp counter synchronization policy. This option should only be used for debugging. Can be Default, Legacy or Enhanced.
    Verification Settings
    testsigning [ on | off ]
    Controls whether Windows 10, Windows 8.1, Windows 8, Windows 7, Windows Server 2008, or Windows Vista will load any type of test-signed kernel-mode code. This option is not set by default, which means test-signed kernel-mode drivers on 64-bit versions of Windows 10, Windows 8.1, Windows 8, Windows 7, Windows Server 2008, and Windows Vista will not load by default. After you run the BCDEdit command, restart the computer so that the change takes effect. For more information, see Introduction to Test-Signing
    nointegritychecks [ on | off ] Disables integrity checks. Cannot be set when secure boot is enabled. This value is ignored by Windows 7 and Windows 8.
    disableelamdrivers [ yes | no ]
    Controls the loading of Early Launch Antimalware (ELAM) drivers. The OS loader removes this entry for security reasons. This option can only be triggered by using the F8 menu. Someone must be physically present (at the computer) to trigger this option.
     Note
    This option should only be used for debugging.
    nx [Optin |OptOut | AlwaysOn |AlwaysOff]
    Enables, disables, and configures Data Execution Prevention (DEP), a set of hardware and software technologies designed to prevent harmful code from running in protected memory locations. For information about DEP settings, see Data Execution Prevention.
    DEP Option	Description
    Optin	Enables DEP only for operating system components, including the Windows kernel and drivers. Administrators can enable DEP on selected executable files by using the Application Compatibility Toolkit (ACT).
    Optout	Enables DEP for the operating system and all processes, including the Windows kernel and drivers. However, administrators can disable DEP on selected executable files by using System in Control Panel.
    AlwaysOn	Enables DEP for the operating system and all processes, including the Windows kernel and drivers. All attempts to disable DEP are ignored.
    AlwaysOff	Disables DEP. Attempts to enable DEP selectively are ignored. On Windows Vista, this parameter also disables Physical Address Extension (PAE). This parameter does not disable PAE on Windows Server 2008.
    Processor Settings
    groupsize maxsize
    Sets the maximum number of logical processors in a single processor group, where maxsize is any power of 2 between 1 and 64 inclusive. Must be an integer of power of 2. By default, processor groups have a maximum size of 64 logical processors. You can use this boot configuration setting to override the size and makeup of a computer's processor groups for testing purposes. Processor groups provide support for computers with greater than 64 logical processors. This boot option is available on 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions. This boot option has no effect on the 32-bit versions of Windows 7.
    Use the groupsize option if you want to force multiple groups and the computer has 64 or fewer active logical processors. For more information about using this option, see Boot Parameters to Test Drivers for Multiple Processor Group Support.
    groupaware [ on | off ]
    Forces drivers to be aware of multiple groups in a multiple processor group environment. Use this option to help expose cross-group incompatibilities in drivers and components. Processor groups provide support for computers with greater than 64 logical processors. This boot option is available on 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions. This boot option has no effect on the 32-bit versions of Windows 7. You can use the groupaware option and the groupsize option to test driver compatibility to function with multiple groups when computer has 64 or fewer active logical processors.
    The groupaware on setting ensures that processes are started in a group other than group 0. This increases the chances of cross-group interaction between drivers and components. The option also modifies the behavior of the legacy functions, KeSetTargetProcessorDpc, KeSetSystemAffinityThreadEx, and KeRevertToUserAffinityThreadEx, so that they always operate on the highest numbered group that contains active logical processors. Drivers that call any of these legacy functions should be changed to call their group-aware counterparts (KeSetTargetProcessorDpcEx, KeSetSystemGroupAffinityThread, and KeRevertToUserGroupAffinityThread).
    For more information about using this option, see Boot Parameters to Test Drivers for Multiple Processor Group Support.
    maxgroup [ on | off ]
    Maximizes the number of groups created in a processor group configuration. The maxgroup on setting assigns NUMA nodes to groups in a manner that maximizes the number of groups for a particular computer. The number of groups created is either the number of NUMA nodes the computer has, or the maximum number of groups supported by this version of Windows, whichever is smaller. The default behavior (maxgroup off) is to pack the NUMA nodes tightly into as few groups as possible.
    Use the maxgroup option if you want to use multiple groups, the computer has 64 or fewer active logical processors, and the computer already has multiple NUMA nodes. This option can also be used to alter the default group configuration of a computer that has more than 64 logical processors.
    Processor groups provide support for computers with greater than 64 logical processors. This option is available on 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions. This boot option has no effect on the 32-bit versions of Windows 7.
    For more information about using this option, see Boot Parameters to Test Drivers for Multiple Processor Group Support.
    onecpu [ on | off ]
    Forces only the boot CPU to be used in a computer that has more than one logical processor. For example, the following command configures the current operating system loader to use one processor.
    syntax
    Copy
    bcdedit /set onecpu on
    Memory Related Settings
    increaseuserva Megabytes
    Specifies the amount of memory, in megabytes, for user-mode virtual address space.
    On 32-bit editions of Windows, applications have 4 gigabyte (GB) of virtual address space available. The virtual address space is divided so that 2 GB is available to the application and the other 2 GB is available only to the system.
    The 4-gigabyte tuning feature, enabled with the increaseuserva option, allows you to increase the virtual address space that is available to the application up to 3 GB, which reduces the amount available to the system to between 1 and 2 GB. The BCEdit /set increaseuserva Megabytes command can specify any value between 2048 (2 GB) and 3072 (3 GB) megabytes in decimal notation. Windows uses the remaining address space (4 GB minus the specified amount) as its kernel-mode address space.
    See 4-Gigabyte Tuning (Windows) for additional information about this feature.
    nolowmem [ on | off ] Controls the use of low memory. When nolowmem on is specified, this option loads the operating system, device drivers, and all applications into addresses above the 4 GB boundary, and directs Windows to allocate all memory pools at addresses above the 4 GB boundary. Note that the nolowmem option is ignored in Windows 8, Windows Server 2012, and later versions of Windows.
    pae [ Default | ForceEnable | ForceDisable ]
    Enables or disables Physical Address Extension (PAE). When PAE is enabled, the system loads the PAE version of the Windows kernel.
    The pae parameter is valid only on boot entries for 32-bit versions of Windows that run on computers with x86-based and x64-based processors. On 32-bit versions of Windows (prior to Windows 8) , PAE is disabled by default. However, Windows automatically enables PAE when the computer is configured for hot-add memory devices in memory ranges beyond the 4 GB region, as defined by the Static Resource Affinity Table (SRAT). Hot-add memory supports memory devices that you can add without rebooting or turning off the computer. In this case, because PAE must be enabled when the system starts, it is enabled automatically so that the system can immediately address extended memory that is added between restarts. Hot-add memory is supported only on Windows Server 2008, Datacenter Edition; Windows Server 2008 for Itanium-Based Systems; and on the datacenter and enterprise editions of all later versions of Windows Server. Moreover, for versions of Windows prior to Windows Server 2008, hot-add memory is supported only on computers with an ACPI BIOS, an x86 processor, and specialized hardware. For Windows Server 2008 and later versions of Windows Server, it is supported for all processor architectures.
    On a computer that supports hardware-enabled Data Execution Prevention (DEP) and is running a 32-bit version of the Windows operating system that supports DEP, PAE is automatically enabled when DEP is enabled and, on all 32-bit versions of the Windows operating system, PAE is disabled when you disable DEP. To enable PAE when DEP is disabled, you must enable PAE explicitly, by using /set nx AlwaysOff and /set pae ForceEnable. For more information about DEP, see Boot Parameters to Configure DEP and PAE.
    For more information about using the pae parameter and the other parameters that affect PAE configuration, see Boot Parameters to Configure DEP and PAE.
    removememory Megabytes
    Removes memory from the total available memory that the operating system can use.
    For example, the following command removes 256 MB of memory from the total available to the operating system associated with the specified boot entry.
    syntax
    Copy
    bcdedit /set {49916baf-0e08-11db-9af4-000bdbd316a0} removememory 256
    truncatememory address Limits the amount of physical memory available to Windows. When you use this option, Windows ignores all memory at or above the specified physical address. Specify the address in bytes.
    For example, the following command sets the physical address limit at 1 GB. You can specify the address in decimal (1073741824) or hexadecimal (0x40000000).
    syntax
    Copy
    bcdedit /set {49916baf-0e08-11db-9af4-000bdbd316a0} truncatememory 0x40000000
    VESA, PCI, VGA, and TPM
    usefirmwarepcisettings [ yes | no ]
    Enables or disables the use of BIOS-configured peripheral component interconnect (PCI) resources.
    msi [ Default | ForceDisable ]
    Can be Default or ForceDisable.
    vga [ on | off ]
    Forces the use of the VGA display driver.
    novga [ on | off ]
    Disables the use of VGA modes entirely.
    tpmbootentropy [ default | ForceEnable | ForceDisable]
    Determines whether entropy is gathered from the trusted platform module (TPM) to help seed the random number generator in the operating system.
    Processors and APICs
    clustermodeaddressing [ integer ]
    Defines the maximum number of processors to include in a single Advanced Programmable Interrupt Controller (APIC) cluster.
    configflags [ integer ]
    Specifies processor-specific configuration flags.
    maxproc [ yes | no ]
    Reports the maximum number of processors in the system.
    numproc [ integer ]
    Uses only the specified number of processors.
    onecpu [ yes | no ]
    Forces only the boot CPU to be used.
    restrictapicluster [ integer ]
    Defines the largest APIC cluster number to be used by the system.
    usephysicaldestination [ yes | no ]
    Forces the use of the physical APIC.
    uselegacyapicmode [ yes | no ]
    Forces legacy APIC mode, even if the processors and chipset support extended APIC mode.
    x2apicpolicy [ enable | disable | default ]
    Enables or disables the use of extended APIC mode, if supported. The system defaults to using extended APIC mode if it is available. Can be Enabled, Disabled or Default.
    Additional Settings
    disabledynamictick [ yes | no ]
    Enables and disables dynamic timer tick feature.
     Note
    This option should only be used for debugging.
    pciexpress [ default | forcedisable]
    Enables or disables PCI Express functionality. If the computer platform supports the PCI Express features and the ACPI _OSC method grants control of the features to the operating system, Windows enables the advanced features through the PCI Express Native Control feature (this is the default). Use the forcedisable option to override the advanced PCI Express features and use legacy PCI Express behavior. For more information, see Enabling PCI Express Native Control in Windows.
    useplatformtick [ yes | no ]
    Forces the clock to be backed by a platform source, no synthetic timers are allowed. The option is available starting in Windows 8 and Windows Server 2012.
     Note
    This option should only be used for debugging.
    xsavedisable [ 0 | 1 ]
    When set to a value other than zero (0), disables XSAVE processor functionality in the kernel.
    Debugger Settings
    To work with the debugger settings, use the following commands.
    Command	Description
    BCDEdit /bootdebug	The /bootdebug boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.
    BCDEdit /dbgsettings	The /dbgsettings option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the BCDEdit /debug option.
    BCDEdit /debug	The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.
    Hypervisor Debugger Settings
    Use the BCDEdit / hypervisorsettings option to set or display the hypervisor debugger settings for the system. For more information, see BCDEdit /hypervisorsettings.
    hypervisordebug [ On | Off ]
    Controls whether the hypervisor debugger is enabled.
    hypervisordebugtype [ SERIAL | 1394 | NET ] Can be SERIAL, 1394, or NET. For more infomation, see BCDEdit /hypervisorsettings.
    Hypervisor Settings
    hypervisorlaunchtype [ Off | Auto ]
    Controls the hypervisor launch options. If you are setting up a debugger to debug Hyper-V on a target computer, set this option to Auto on the target computer. For more information, see Create a Virtual Machine with Hyper-V.
    hypervisorloadoptions NOFORCESNOOP [ Yes | No ]
    Specifies whether the hypervisor should enforce snoop control on system IOMMUs.
    hypervisornumproc number
    Specifies the total number of logical processors that can be started in the hypervisor.
    hypervisorrootproc number
    Specifies the maximum number of virtual processors in the root partition and limits the number of post-split Non-Uniform Memory Architecture (NUMA) nodes which can have logical processors started in the hypervisor.
    hypervisorrootprocpernode number
    Specifies the total number of virtual processors in the root partition that can be started within a pre-split Non-Uniform Memory Architecture (NUMA) node.
    hypervisoruselargevtlb [ yes | no]
    Increases virtual Translation Lookaside Buffer (TLB) size.
    hypervisoriommupolicy [ default | enable | disable]
    Controls whether the hypervisor uses an Input Output Memory Management Unit (IOMMU).
    Drivers and System Root
    driverloadfailurepolicy [ Fatal | UseErrorControl]
    Can be Fatal or UseErrorControl.
    osdevice [ device]
    Defines the device that contains the system root.
    systemroot [ string]
    Defines the path to the system root.
    ems [ On | Off ]
    Enables kernel Emergency Management Services. The BCDEdit /ems option enables or disables kernel Emergency Management Services (EMS) for the specified operating system boot entry. For more information, see BCDEdit /ems.
    The BCDEdit /emssettings option sets the global Emergency Management Services (EMS) settings for the computer. For more information, see For more information, see BCDEdit /emssettings.
##________________________________________  ___________________________



