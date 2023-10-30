##________________________________________  ___________________________


#####  ==========  nvidia-org-drivers install on x17-ub128 /_200803 :
-!! https://wiki.archlinux.org/index.php/NVIDIA
https://nouveau.freedesktop.org/wiki/KernelModuleParameters/

	_______:  my card?? 
- x17 /Xps17: ---
u1@2004arx arx-dnts]$ lspci -k | grep -A 2 -E "(VGA|3D)"
02:00.0 VGA compatible controller: NVIDIA Corporation GF106M [GeForce GT 445M] (rev a1)
	Subsystem: Dell Device 046c
	Kernel driver in use: nouveau

	_______:  Codename of the card in x17: https://nouveau.freedesktop.org/wiki/CodeNames/ :
NVC3 (GF106):	GeForce GT (440, 445M, 545, 555M, 630M, 635M), GTS 450, GTX 460M Quadro 2000 (D), 2000M

	_______:  AUR:
nvidia-390xx-utils.tar.gz; tar -xzvf ...;   [u1@2004arx nvidia-390xx-utils]$ makepkg -si
[u1@2004arx nvidia-390xx]  makepkg  -si ;   ##Installing nvidia-390xx package AUR
optional: Installing nvidia-390xx-settings ...

	_______:  --- pos-installs:
nvidia-xconfig  bzw.  nvidia-settings
(for cmds see: nvidia<TAB>) ....

	_______:  -!! vconsole-resolution-Problem:
after installtion all fine, BUT the vconsole-Resolution does NOT work (not font but RESOLUTION !!) and came back to VGA !!
obv. had got nothing to do with the vconsole-font, but with the Resolution! obv, see:
https://wiki.archlinux.org/index.php/NVIDIA#DRM_kernel_mode_setting
	nvidia 364.16 adds support for DRM (Direct Rendering Manager) kernel mode setting. To enable this feature, add the nvidia-drm.modeset=1 kernel parameter. ...
https://wiki.archlinux.org/index.php/Kernel_mode_setting:
	Kernel Mode Setting (KMS) is a method for setting display resolution and depth in the kernel space rather than user space
	Note: The proprietary NVIDIA driver (since 364.12) also implements kernel mode-setting, but it does not use the built-in kernel implementation and it lacks an fbdev driver for the high-resolution console.
probably must deactivate the Kernel-KMS !?!?
-- _1kk:
- the real possible resolutions of your adapter can be listed by: boot, go to GRUB-cmdline by pressing "c", enter grub-cmd:  videoinfo /OF vbeinfo
- in X17 it vconsole-resolution was changed/ok by adding "set gfxmode=1280x800x32" directly to /boot/grub/grub.cfg  /OR can add to /etc/default/grub ...
  but then for each PC must be adapted! (if booting from the USB-stick)
  just only with nvidia-drm.modeset=1 kernel parameter not worked!

	_______:  --- Nouveau <---> NVidia:
- nvidia blaklicts the Nouveau drivers in :  /usr/lib/modprobe.d/nvidia-390xx-dkms.conf  ##in x17-arx; for others see /usr/lib/modprobe.d/nvidia-xxx.conf
- blacklisting   within /etc/modprobe.d/ or /usr/lib/modprobe.d/ ! check them ! /OR  
	Nouveau driver is disabled by passing the following kernel parameters:   modprobe.blacklist=nouveau  ## https://wiki.archlinux.org/index.php/Nouveau#Kernel_parameters
	/OR nouveau-kernelparam:  nouveau.modeset=1  ##--  modeset : Whether the driver should be enabled. 0 for disabled, 1 for enabled, 2 for headless ; see https://nouveau.freedesktop.org/wiki/KernelModuleParameters/
##________________________________________  ___________________________


#####  ==========  uninstalling/deactivating/switching between  Nouveau <---> NVidia  :

	_______:  -- switching between  Nouveau <---> NVidia  , WITHOUT uninsatalling:

	_______:  Tips and tricks:  Keep NVIDIA driver installed , go to Nouveau :   https://wiki.archlinux.org/index.php/Nouveau   :
- If you want to keep the proprietary NVIDIA driver installed (and are not using OpenGL), but want to use the Nouveau driver,
comment out nouveau blacklisting in /etc/modprobe.d/nouveau_blacklist.conf, /usr/lib/modprobe.d/nvidia.conf, or /usr/lib/modprobe.d/nvidia-dkms.conf modifying it as follows:
#blacklist nouveau
And tell Xorg to load nouveau instead of nvidia by creating the file /etc/X11/xorg.conf.d/20-nouveau.conf with the following content:
Section "Device"
    Identifier "Nvidia card"
    Driver "nouveau"
EndSection
- If you already used the NVIDIA driver, and want to test Nouveau without reboot, make sure the 'nvidia' module is no longer loaded:
# rmmod nvidia
Then load the 'nouveau' module:
# modprobe nouveau
And check that it loaded fine by looking at kernel messages:
$ dmesg
##________________________________________  ___________________________


#####  ==========  
--############################ _1coll : ###########################################
##________________________________________  ___________________________


#####  ==========  nouveau-kernel-params:
Nouveau Kernel Module Parameters
Each of these parameters expects a value. Most are simple booleans, and can be set with foo=1 for enable or foo=0 for disable. The rest have detailed explanations of the values they're allowed to take on.
perflvl/perflvl_wr (removed in 3.13)
Specify nouveau.perflvl_wr=7777 in order to be able to switch performance levels at runtime via /sys/class/drm/cardN/device/performance_level. You can also specify nouveau.perflvl=N to switch to a specific performance level on boot.
pstate (removed in 4.5)
Specify nouveau.pstate=1 in order to be able to switch performance levels at runtime via /sys/class/drm/cardN/device/pstate. Starting in 4.5, this is available by default in debugfs, at /sys/kernel/debug/dri/*/pstate
WARNING: Power management is a very experimental feature and is not expected to work. If you decided to upclock your GPU, please aknowledge that your card may overheat. Please check the temperature of your GPU at all time!
runpm
Force enable 1 or disable 0, runtime power-managment. The default only for Optimus systems is -1.
noaccel
Disable kernel/abi16 acceleration (i.e. 1 for disable acceleration, 0 for enable).
nofbaccel
Disable fbcon acceleration (i.e. 1 for disable acceleration, 0 for enable).
modeset
Whether the driver should be enabled. 0 for disabled, 1 for enabled, 2 for headless
config
This provides a way to configure various parts of the driver, it is a comma-separate list of a=b key/value pairs. The values are all integers (use 0/1 for booleans) except for NvBios which is a string.
$engine: Whether to enable/disable the engine, e.g. PDISP=0
NvAGP: The agp mode (0 for disable) to force (starting with 4.3)
NvBios: Specify VBIOS source as one of OpenFirmware/PRAMIN/PROM/ACPI/PCIROM/PLATFORM, or a filename passed to request_firmware
NvBoost: Specify the Boost mode for Fermi and newer. 0: base clocks (default) 1: boost clocks 2: max clocks (starting with 4.10)
NvClkMode: Force a particular clock level on boot. Note that this does not parse hex, so for clock mode f, pass in 15.
NvClkModeAC: Same as NvClkMode, when the power is plugged in
NvClkModeDC: Same as NvClkMode, when running off battery
NvFanPWM: Enable use of PWM for the fan, auto-detect by default
NvForcePost: Whether to force a POST of the device, off by default
NvGrUseFW: Whether to load FW for PGRAPH on NVC0
NvI2C: ??, off by default
NvMemExec: Perform memory reclocking
NvMSI: Use MSI interrupts, on by default on the chipsets that support it
NvMXMDCB: Sanitize DCB outputs from the BIOS, on by default
NvPCIE: NV40 family only, whether to use PCI-E GART, on by default
NvPmEnableGating: Enables clockgating for Kepler GPUs
Here is a list of engines:
DEVICE
DMAOBJ
PBSP
PCE0
PCE1
PCE2
PCRYPT
PDISP
PFIFO
PGRAPH
PMPEG
PPM
PPPP
PVP
SW
debug
This works just like the config option, but the values are all debug levels (one of fatal, error, warn, info, debug, trace, paranoia, spam). Note that in order for a debug level to work, CONFIG_NOUVEAU_DEBUG must be set to at least that level.
CLIENT
$subdev (e.g. PDISP=debug)
Here is a list of the available subdevices:
BARCTL
DEVINIT
GPIO
I2C
INSTMEM
MXM
PBUS
PIBUS
PLTCG
PTHERM
PTIMER
VBIOS
any engine (see above)
Example: nouveau.debug="PTHERM=debug,PTIMER=debug"
agpmode (removed in 4.3)
AGP mode, 0 to disable AGP
vram_pushbuf
Create DMA push buffers in VRAM
ignorelid
Ignore ACPI lid status
duallink
Allow dual-link TMDS (on by default)
tv_norm
Default TV norm. Default is PAL. Valid values: PAL, PAL-M, PAL-N, PAL-Nc, NTSC-M, NTSC-J, hd480i, hd480p, hd576i, hd576p, hd720p, hd1080i.
This only applies to cards that don't have external encoders.
tv_disable
Disable TV-out detection
Links: InstallNouveau index
Last edited Thu Apr 30 15:21:12 2020
##________________________________________  ___________________________


#####  ==========  ======================================================
