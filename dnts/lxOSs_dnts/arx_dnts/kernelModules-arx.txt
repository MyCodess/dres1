__________________ Kernel-Modules for HWs/devs/.... : _________________________________________
##________________________________________  ___________________________


#####  ==========  docs-WPs Kernel-Modules:
-!! https://wiki.archlinux.org/index.php/Kernel_module

	_______:  man :
- man 5  sysfs ,  man sysfs
man lsmod, insmod(8), modprobe(8), modinfo(8) depmod(8)
man  lspci  ,  lsusb ,
man See modules-load.d(5) , man modprobe.d
- also check udev_dnts and  man udev ,  systemd-udevd.service(8), udevadm(8)
##________________________________________  ___________________________


#####  ==========  pathes1:
/usr/lib/modules/kernel_release	 : Modules are stored in /usr/lib/modules/kernel_release. You can use the command uname -r to get your current kernel release version.
/etc/modprobe.d/ 	: configuration files ; Configuration files in this directory can have any name, given that they end with the .conf extension. https://wiki.archlinux.org/index.php/Kernel_module
/etc/modules-load.d/  : man See modules-load.d(5) : Kernel modules can be explicitly listed in files under /etc/modules-load.d/ for systemd to load them during boot. (!! usu. NOT needed. all work is done by UDEV in runtime automatik...) 
##________________________________________  ___________________________


#####  ==========  listing/querying/infs  of loaded  Modules/Drivers :
-!  /proc/  :  process and kernel Information-on-fly  of the current boot.
- Some modules are loaded as part of the initramfs (boot).  mkinitcpio -M  shows them!

	_______:  listings/DIRs of modules-files ....
	- DIRs-listing of all existing Kernel modules files (not all loaded!) in the system-DIRs:
		ubuntu:  /lib/modules/`uname -r`/kernel/drivers/ : Kernel modules , as /lib/modules/2.6.8-1.521/kernel/drivers/
		archlx:   Modules are stored in    /usr/lib/modules/kernel_release. You can use the command uname -r to get your current kernel release version.
	- lsmod : listing loaded modules;  show what kernel modules are currently loaded in the current-boot/system, which just nicely formats the contents of the /proc/modules
	- /proc/modules  :  currently loaded modules

	_______:  infs/query:  https://wiki.archlinux.org/index.php/Kernel_module :
	To show what kernel modules are currently loaded: $ lsmod | sort ;   lspci | sort ;
	To show information about a module: $ modinfo module_name
	To list the options that are set for a loaded module: $ systool -v -m module_name
	To display the comprehensive configuration of all the modules: $ modprobe -c | less
	To display the params/configuration of a particular module: $ modprobe -c | grep module_name
	List the dependencies of a module (or alias), including the module itself: $ modprobe --show-depends module_name
	--- info-queries:
		- show information about a module:                  modinfo module_name
		- show options that are set for a loaded module:    systool -v -m module_name    (if-not-installed,then:   sudo apt install sysfsutils )
		- show comprehensive configuration all modules:     modprobe -c | less
		- show  the configuration of a particular module:   modprobe -c | grep module_name
		- show  dependencies of a module :                  modprobe --show-depends module_name

	_______:  lspci (listing of HWs attached to PCI-interfaces and their modules):
	- kernel-drivers in use?:   lspci  -k  ;
	- lspci  -k   /bzw.   lsusb  -v[vv] :  listing of loaded drivers/modules:  To check if the driver for your card has been loaded, check the output of the lspci -k  or  lsusb -v command, depending on if the card is connected by PCI(e) or USB. You should see that some kernel driver is in use, for example:
	- lspci  -tvvv  ##tree of PCI-Bus-Attached-Devices
	- lspci  -k     # Kernel-modules/-driver-listing:    
	- Graphik-Adapter/VGA/Display-Card  driver??:    lspci -k  | grep -i -A4 vga
	- cat /usr/share/hwdata/pci.ids  ##see man lspci

	_______:  lsusb -vvv ...
	-  cat  /usr/share/hwdata/usb.ids  : A list of all known USB ID's (vendors, products, classes, subclasses and protocols). man lsusb ;

	_______:  initramfs included modules bzw. ontents of the default initramfs :    lsinitcpio  /boot/initramfs-linux.img
##________________________________________  ___________________________


#####  ==========  loading/adding modules ...:
- Manual module loading:	 modprobe module_name
- Manaully load a module by filename (i.e. one that is not installed in /usr/lib/modules/$(uname -r)/): # insmod filename [args]
- systemd auto-load addtional modules (plus UDEV):  /etc/modules-load.d/xxx.conf
##________________________________________  ___________________________


#####  ==========  Un-load manually:
To unload a module: # modprobe -r module_name
Or, alternatively: # rmmod module_name
##________________________________________  ___________________________


#####  ==========  Blacklisting of modules:
https://wiki.archlinux.org/index.php/Kernel_module#Blacklisting
- boot-/initramfs-loaded-modules-listing:  mkinitcpio -M  ##--Some modules are loaded as part of the initramfs. mkinitcpio -M will print out all automatically detected modules:

	_______:  Using files in /etc/modprobe.d/ :
Create a .conf file inside /etc/modprobe.d/ and append a line for each module you want to blacklist, using the blacklist keyword. If for example you want to prevent the pcspkr module from loading:
	/etc/modprobe.d/nobeep.conf
	# Do not load the 'pcspkr' module on boot.
	blacklist pcspkr
-!! Note: The blacklist command will blacklist a module so that it will not be loaded automatically, but the module may be loaded if another non-blacklisted module depends on it or if it is loaded manually.
However, there is a workaround for this behaviour;
the "install" command instructs modprobe to run a custom command instead of inserting the module in the kernel as normal, so you can force the module to always fail loading with:
/etc/modprobe.d/blacklist.conf
	...
	install module_name /bin/true
	...
This will effectively blacklist that module and any other that depends on it.

	_______:  Using kernel command line:
Tip: This can be very useful if a broken module makes it impossible to boot your system.  You can also blacklist modules from the bootloader.
Simply add  module_blacklist=modname1,modname2,modname3   to your bootloader's kernel line, as described in Kernel parameters.
Note: When you are blacklisting more than one module, note that they are separated by commas only. Spaces or anything else might presumably break the syntax.
##________________________________________  ___________________________


#####  ==========  configs of Kernel-Modules:

	_______:  nts1:
	-!! https://wiki.archlinux.org/index.php/Kernel_module 
	- Def:  Kernel modules are pieces of code that can be loaded and unloaded into the kernel upon demand. They extend the functionality of the kernel without the need to reboot the system.

	_______:  configs-of-modules-by-systemd/udev automatically done (for manually handling/configs of modules see here below!):
	- configs:  /etc/modprobe.d/  , /etc/modules-load.d/ , kernel-boot-params ,  -->but all mainly done now by systemD/udev :
	-!! systemd/udev , Automatic module loading with systemd : Today, all necessary modules loading is handled automatically by udev, so if you do not need to use any out-of-tree kernel modules, there is no need to put modules that should be loaded at boot in any configuration file.
	- /etc/modules-load.d/  : additional-boot-time-kernel-modules: Kernel modules can be explicitly listed in files under /etc/modules-load.d/ for systemd to load them during boot. ...
	- show configs/params of currently loaded module xx :   modprobe -c | grep module_name

	_______:  Manually-handling/managing-modules (not automatically by systemD/udev):
	-!! https://wiki.archlinux.org/index.php/Kernel_module#Manual_module_handling
	- pakcage  kmod  ;   man kmod
	- To load a module: # modprobe module_name
	- To load a module by filename (i.e. one that is not installed in /usr/lib/modules/$(uname -r)/): # insmod filename [args]
	- To unload a module: # modprobe -r module_name Or, alternatively: # rmmod module_name

	_______:  Manully-configs of modules (not automatically by systemD/udev):
	-!! https://wiki.archlinux.org/index.php/Kernel_module#Setting_module_options
	- 
##________________________________________  ___________________________


#####  ==========  
