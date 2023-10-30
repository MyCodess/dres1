________________  virtualizations-kvm-hypervisor-arx : __________________
##________________________________________  ___________________________


#####  ==========  
	-!! https://wiki.archlinux.org/title/KVM
##________________________________________  ___________________________


#####  ==========  cmds:
	- Hardware support is there??:  $ LC_ALL=C lscpu | grep Virtualization
	- kernel support is there??:  zgrep CONFIG_KVM /proc/config.gz  ##--I The module is available only if it is set to either y or m !
	- kernel modules are automatically ??:  lsmod | grep kvm
