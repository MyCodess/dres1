##______ if booting with only a simple bash in single-mode, then hier setting the KB and ... : _______
#- eg usage for checking s2ram with a minimal system, without init.d-scripts,,...

##-I-GRUB-- menu.lst:  kernel   /boot/vmlinuz-2.6.34.7-0.5-default root=/dev/sda6 resume=/dev/sda5  init=/bin/bash , 
#- see: /usr/share/doc/packages/suspend/README.s2ram-whitelist  AND http://en.opensuse.org/SDB:ACPI_suspend_debugging

##---- KeyBoard-Layout:  loadkeys de.map.gz
#find /usr/share/kbd/keymaps/ --iname "*de*"
#find /usr/share/kbd/keymaps/ -iname "*de*"
# loadkeys de-latin1.map.gz
loadkeys  de-latin1-nodeadkeys.map.gz  # loads: /usr/share/kbd/keymaps/i386/qwertz/de-latin1-nodeadkeys.map.gz

##--- mounting manualy minimal system:
mount /sys
#-I- for s2disk is swap-part must be there:
# swapon -a

##-- full-steps-info: --------- from: http://en.opensuse.org/SDB:ACPI_suspend_debugging  :
# mount /proc and /sys:
# mount /proc
# mount /sys
# for suspend to disk, activate swap here. Not necessary for suspend to RAM:
# swapon -a

##-- 
# invoke suspend to RAM ("disk" for suspend to disk):
# echo mem > /sys/power/state   #OR do s2ram  ...
# echo disk > /sys/power/state  #OR do s2disk ...
