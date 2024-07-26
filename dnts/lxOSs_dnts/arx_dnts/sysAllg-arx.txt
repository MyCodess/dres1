___________ systemAllg as Filesystem-Hierarchy, STDs, sys-infs, ... _________________________
##________________________________________  ___________________________


#####  ==========  Filesystem_Hierarchy_Standard :
https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard  , FHS compliance

	_______:  tmpfs / procfs /.... temoorary system filesystems:
	/proc/ 	:  process and kernel Information-on-fly  of the current boot.
	/run/  	:  running system status/information since last boot; Run-time variable data: e.g., currently logged-in users and running daemons; /OR:  /var/run/
	/sys/ 	:  devices, drivers, and some kernel features 
	- Files under this directories must be either removed or truncated at the beginning of the boot process, but this is not necessary on systems that provide this directory as a temporary filesystem (tmpfs).
	- /proc/ files provide a lot of information about the system as well as the kernel; It is suggested to use sysfs over procfs because it has defined structure and procfs became a mess over time.
##________________________________________  ___________________________


#####  ==========  /proc/ , procfs :
-!!  https://wiki.archlinux.org/index.php/Procfs   :
https://wiki.archlinux.org/index.php/Category:Pseudo_filesystems
- Kernel & system information : There are many files under /proc which provide a lot of information about the system as well as the kernel. There are too many to cover them all here, but some of them are listed below with brief information about what they are.
	/proc/cpuinfo - informations about CPU
	/proc/meminfo - information about the physical memory
	/proc/vmstats - information about the virtual memory
	/proc/mounts - information about the mounts(mount)
	/proc/filesystems - information about active filesystems
	/proc/uptime - current system uptime
	/proc/cmdline - kernel command line
	/proc/<pid>  -  every process currently running status/infs
	- Processes currently running: Inside /proc/<pid> is stored information about every process currently running. Below is an example showing some of the PIDs currently running

	_______:  Modification-Usage:
	-! Altering files in /proc allows us to manipulate kernel in runtime.
	To read from proc file, we can use cat: cat /proc/cmdline (run as the regular user).
	To write to the file, we can use echo: echo 1 > /proc/sys/kernel/sysrq (run as the root user).
-! It is suggested to use sysfs over procfs because it has defined structure and procfs became a mess over time.
##________________________________________  ___________________________


#####  ==========  Libraries :
system-libraries searched in following seq:
	1- LD_LIBRARY_PATH  env-var, if set
	2- $PATH
	3- /etc/ld.so.conf.d/  ,then in /etc/ld.so.conf
	4- /lib*/  bzw.  /usr/lib*/
##________________________________________  ___________________________


#####  ==========  SysRq :
	https://wiki.archlinux.org/title/Keyboard_shortcuts#Kernel_(SysRq)
	https://en.wikipedia.org/wiki/Magic_SysRq_key
	https://docs.kernel.org/admin-guide/sysrq.html
	try/activate just once (not-persistent):  sysctl kernel.sysrq=1  # /OR   echo "1" > /proc/sys/kernel/sysrq
	enable/persistent:  kernel-param (in grub.cfg):  sysrq_always_enabled=1 
	in /proc/sys/kernel/sysrq :  0 == disable sysrq completely ; 1 == enable all functions of sysrq ; >1 - bitmask of selected functions! see https://docs.kernel.org/admin-guide/sysrq.html

	_______:  Keys/Shhortcuts for SysRq:
	- SysRq-cmd-keys (keep all three pressed together):  <Alt> + <SysRq> + <SysRq-cmd-shortcut>    #eg: Alt+SysRq+s  : Sync/Flush data to disk !
	- <SysRq>-key:  usu. the <Print/Druck>-key ! :
		on lv13:  "Druck/print" ! so <Alt>+<Druck>+<SysRq-cmd-shortcut> ; eg: <Alt>+<Druck>+e : terminate all processe gracefully (no-crash! just end)!
		on lv13 also better: <Alt>+<Fn>+s (Fn+s activates the SysRq-Mode) and then keep only Alt and press the SysRq-cmd eg <h> for help!
		otherwise for SysRq-key see https://docs.kernel.org/admin-guide/sysrq.html  bzw. google! bzw. <Alt>+<Fn>+s then keep only Alt and press the SysRq-letter ! works also on Lv13 !
	-! outputs of SysRq-keys in journalctl /OR console (eg: tasks-listtings/ CPU-regs/ ...) will be written into the console bzw. journalctl !! so:    journalctl  -e -f
	- keys-shortcuts-Listing: <Alt> + <SysRq> + h  ##-then see journalctl/console !  on lv13 worked only whith second-key-variant: <Alt>+<Fn>+s then still <Alt>+<h>
	-! key-shortcuts--main-ones (remember by "busier"):
		<Alt>+<SysRq>+ b :Reboot-sofort (not-sauber! crash-reboot!) , u :umount-all, s :Sync-disks, i :Kill-all-procs-immediately-except-INIT (crash-proc/SIGKILL), e :end-/terminate-all-procs-nice-except-INIT (clean/no-crash/SIGTERM), r :Take control of keyboard back from X ;
		clean-keys-if-problem, then: s , r , e , t, 
		full-listing in https://docs.kernel.org/admin-guide/sysrq.html  bzw. https://en.wikipedia.org/wiki/Magic_SysRq_key
	- key-shortcuts-cmds of listing/showing, good for tests, eg: m :dump current memory, t :tasks/procs listing, l :CPUs-backtraces

	_______:  SysRq-shortcuts-/-keys-listing:    <Alt>+<SysRq>+
	b	    Will immediately reboot the system without syncing or unmounting your disks.
	c	    Will perform a system crash and a crashdump will be taken if configured.
	d	    Shows all locks that are held.
	e	    Send a SIGTERM to all processes, except for init.
	f	    Will call the oom killer to kill a memory hog process, but do not panic if nothing can be killed.
	g	    Used by kgdb (kernel debugger)
	h	    Will display help (actually any other key than those listed here will display help. but ``h`` is easy to remember :-)
	i	    Send a SIGKILL to all processes, except for init.
	j	    Forcibly "Just thaw it" - filesystems frozen by the FIFREEZE ioctl.
	k	    Secure Access Key (SAK) Kills all programs on the current virtual console. NOTE: See important comments below in SAK section.
	l	    Shows a stack backtrace for all active CPUs.
	m	    Will dump current memory info to your console.
	n	    Used to make RT tasks nice-able
	o	    Will shut your system off (if configured and supported). (kind of crash! nicht-sauber!
	p	    Will dump the current registers and flags to your console.
	q	    Will dump per CPU lists of all armed hrtimers (but NOT regular timer_list timers) and detailed information about all clockevent devices.
	r	    Turns off keyboard raw mode and sets it to XLATE.
	s	    Will attempt to sync all mounted filesystems.
	t	    Will dump a list of current tasks and their information to your console.
	u	    Will attempt to remount all mounted filesystems read-only.
	v	    Forcefully restores framebuffer console
	v	    Causes ETM buffer dump [ARM-specific]
	w	    Dumps tasks that are in uninterruptable (blocked) state.
	x	    Used by xmon interface on ppc/powerpc platforms.  Show global PMU Registers on sparc64.  Dump all TLB entries on MIPS.
	y	    Show global CPU Registers [SPARC-64 specific]
	z	    Dump the ftrace buffer
	0-9 Sets the console log level, controlling which kernel messages will be printed to your console. (``0``, for example would make it so that only emergency messages like PANICs or OOPSes would make it to your console.)
##________________________________________  ___________________________


#####  ==========  
