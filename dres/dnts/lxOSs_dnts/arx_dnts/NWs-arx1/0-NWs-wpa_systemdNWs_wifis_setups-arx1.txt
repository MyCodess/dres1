________________ NWs, wireless, ... arx : _____________________________________________
https://wiki.archlinux.org/index.php/Network_configuration
https://wiki.archlinux.org/index.php/Network_configuration/Wireless
https://wiki.archlinux.org/index.php/Category:Network_configuration
https://wiki.archlinux.org/index.php/Category:Networking
https://wireless.wiki.kernel.org/

	_______:  
https://github.com/nicolaka/netshoot
############################# __CP__ von 2209arx-NW-setupo see _RF there! : #################################

	_______:  NW-HWs/adapters :
	- NW-cards-traditional-naming !! for removable/USB-install is better the traditional naming of NW-cards as eth0/wlan0 ! otherwise on each PC thw wlan-card is named differently and then the wpa_supplicant -i xxx does NOT work properly !!
	- check that traditional-NW-cards-naming (eth0/wlan0) is used:   ip link ##-- must shows wlan0/eth0 ! otherwise do (requires probably reboot):
	#_  ln -s  /dev/null  /etc/udev/rules.d/80-net-setup-link.rules    ##--requires reboot ...; check it : ip link
	--!! RF-Kill errors  : check the physical-Schalter for NW-cards ! 
	any error-msg with "due to rf-kill ..." usu. means the NW-hardware is physically disabled (with schalter/switch or is in Flugmodus)! so turn the schalter/switch on!
	and with "ip link" : you must see it is <...,UP> !! check if all hardwares are on (not-turned-off physically):  rfkill list

	_______:  Not-parallel-NW-services !!:
	- we use ONLY   dhcpcd.service  wpa_supplicant.service  (managed by systemd/systemctl) !! wpa_supplicant for (wireless-)cards-configs and WPA-keys-Mgm, and dhcpcd as dhcp-client-daemon to retrieve the IP from the router!
	- so we are not using systemd-NW-managers or Gnome-NW-Managers! so check them:
	so MUSt be DISabled:   systemctl status   systemd-networkd.service   systemd-resolved.service  ##--if not disabled, then systemctl disable .... ! not-only stop, but disable !!
	Gnome-NW-managers may NOT be installed at all !

	_______:  setup wpa:
	- nedd two wpa-file: wpa-wlans-config-file (known-wlans PWs,names,...) + wpa-start-systemd-file (cmdline-to-start-service) :
	- systemctl   stop  dhcpcd.service  wpa_supplicant.service
	- wpa-config-file:   cpt  uue-wpa-config-file.conf  /etc/wpa_supplicant/0-uue-wpa-wlans1.conf  ##--is the uue-wpa-config-file containing params for kúue-known-wlans/bibs/...!
	- systemd-wpa-start-file:  /either-with:  systemctl edit  wpa_supplicant.service  /OR-manually:  cpt  uue-wpa-start.conf /etc/systemd/system/wpa_supplicant.service.d/0-uue_wpa_systemd_start.conf , containing exactly:
	Service]
	ExecStart=
	ExecStart=/usr/bin/wpa_supplicant -u  -s  -c  /etc/wpa_supplicant/0-uue-wpa-wlans1.conf  -i wlan0
	- reload its configs to systemd-runtime:  systemctl daemon-reload
	-! check tha the above file is loaded for the service:   systemctl   status   wpa_supplicant.service

	_______:  start services:
	systemctl   enable    dhcpcd.service  wpa_supplicant.service ##--in case that were disabled.
	systemctl   stop  dhcpcd.service  wpa_supplicant.service  ##-- just infs:  ip a; ip link; ip r;  
	other terminal:   journalctl -fe -n5   ##check the output os starts:
	systemctl   start  dhcpcd.service  wpa_supplicant.service
	checks:  ip a/r/l ; ping 9.9.9.9 ; ping  google.de ; ...
############################## 2004arx-firtst-trys--200400 : ##################################################
########## systemd-networkd + systemd-resolved (DNS) + wpa (wirless-conn): ######################################
	--- docs/nts:
	man systemd-networkd , systemd.network , systemd-resolved , networkctl , systemd.link
	https://wiki.archlinux.org/index.php/Systemd-networkd  ,  https://wiki.archlinux.org/index.php/Systemd-resolved
	--- dhcp-client NOT needed (is integrated in systemd-networkd :
	- systemd-networkd  has an integrated dhcp-client!
	-! NO other dhcpcd/resolver/... may be running or enabled !
	-! NEVER two running NW-managers/dhcpcd/... !
	--- check if your NW-hardwaware is not physically/button deactivated?:  rfkill list  ##--for errors with RF-kill ! usu. means physically the hardware is switched off with schalter !!
	--- wpa integrating/hooked to systemd-NW (for wpa-details itself see extra-section below! here short and mainly hook for systemd-NW!) :
	- for wirless connections still systemd-networkd needs wpa_supplicant /OR iwd /...
	- wpa-service can be started before and INdependent of systemd-nw-services! so start it first and then you can restart/change systemd-services !:
	- /etc/wpa_supplicant/wpa_supplicant_uue1_wlan0.conf   ##-- check if there+OK the wpa-itself-config-file-for-wlan_APs!? details see wpa-section here below !
	- config/edit systemd-wpa-service-unit-start and overwrite the exec-line to include your config file :
		- vi  /etc/systemd/system/wpa_supplicant.service.d/00-wpa_uue1_wlan0.conf    (/OR systemctl edit  wpa_supplicant.service ) :
		[Service]
		ExecStart=  ##--must be nulled first !!
		ExecStart=/usr/bin/wpa_supplicant -u  -s  -c /etc/wpa_supplicant/wpa_supplicant-uue1_wlan0.conf  -i wlp1s0
	- systemctl daemon-reload   ##--after ANY unit-files-changes do it to reload the modifications !! 
	- systemctl  enable  wpa_supplicant.service ;
	- check the start:  journalctl -fe -n5 (or -xe -n5 ##-for-mor-helps) ; then:
	- systemctl  start   wpa_supplicant.service ;
	--- MAC-random/anonym:
	-!! the anonymization/random-MAC for wlan-interface happens already by wpa, so before systemd-NW. So it is done already in wpa-conf /etc/wpa_supplicant/wpa_supplicant_uue1_wlan0.conf 
	- but here also done for other interfaces in systemd-NW (NOT-checked! if ok??) in /etc/systemd/network/* files with: [Link] MACAddressPolicy=random , and [DHCPv4] Anonymize=true
	--- systemd-NW:
	- systemctl  enable  systemd-resolved.service   systemd-networkd.service
	- systemd-networkd defaults obv. does NOT mange wlan-interfaces. but with wpa now should do that. so add it:
		vi  /etc/systemd/network/25-wireless-uue1.network  (/OR systemctl edit   systemd-networkd.service):
		[Match]
		Name=wl*
		[Network]
		DHCP=yes
	- systemctl daemon-reload   ##--after ANY unit-files-changes do it to reload the modifications !! 
	- systemctl  start   systemd-resolved.service   systemd-networkd.service
	--- for DNS per systemd-resolved.service :
	- ln  -sf  /run/systemd/resolve/stub-resolv.conf  /etc/resolv.conf  ; ##--/OR to /run/systemd/resolve/resolv.conf ,  see https://wiki.archlinux.org/index.php/Systemd-resolve , dman systemd-resolved.service(8)
	- !! if again back to dhcpcd, then MUST remove it !
	- conf-files-dns-relevant.  /etc/nsswitch.conf  /etc/hosts  /etc/resolv.conf   /etc/systemd/resolved.conf
	- man systemd-resolved.service , resolved.conf , resolv.conf , nsswitch.conf , hosts , 
	--- checks:
	- resolvectl status ;    networkctl status ;  ##--all interfaced MUST be managed+configured !
	- ip addr ;    ip r ; ....
	--- cmds:
	resolvectl status ;
	networkctl status ;
	resolvectl query archlinux.org  ; ##--like nslookup
	ll /sys/class/net/
########## wpa_supplicant + dhcpcd.service : ###############################################################
	----- docs:
	-! man wpa_supplicant , wpa_supplicant.conf , wpa_passphrase , wpa_cli , dhcpcd/dhclient ,  systemd.network
	-! https://wiki.archlinux.org/index.php/WPA_supplicant
	- technical-details-docs (check pacman -Ql wpa....) somewhere like:  /usr/share/doc/wpa_supplicant/... ##--gunzip *gz ....
	----- install/setup:
	- pacman -Suy  core/dhcpcd  core/wpa_supplicant
	-! wpa_supplicant pkg itself has NO dhcp-client integrated! so irgendein dhcp-client must be also installed AND mitgestarted/hooked !
	-! hidden-APs:  wpa_supplicant  is  WAP2 capable  + AND settings for hidden-APs!! see the table in  https://wiki.archlinux.org/index.php/Network_configuration/Wireless#Utilities
	- dhcp-hook:    dhcp-client must be manually started... to obtain IP! wpa does NOT do dhcp automatically!! dhcpcd has a hook that can launch wpa_supplicant implicitly, see  https://wiki.archlinux.org/index.php/Dhcpcd#Hooks
	----- PW/key of WPA2 in wpa_supplicant.conf encrypted (not-cleartext) as passphrase :
		- cmdline, generating an enc-PSK-key for that PW of WPA2:     wpa_passphrase     MYSSID   "MY-PW-1"  ;
		- /OR from a file:    wpa_passphrase MYSSID < passphrase.txt ;
		- /OR interactively:  simply invoke wpa_passphrase without specifying the passphrase. It will then prompt for it to be entered in the standard input where users can paste it even if it contains special characters....
		-! later for wpa_supplicant cmdline or in configfile: PW of APs with WPA2/PSK is either quoted "my-pw1", or not-quoted-but-enc-PSK-output of:   wpa_passphrase  SSID "my-pw1" ##--if you just enter wpa_passphrase  SSID , then he asks interactively the PW !
		-- in config file:
		- If security is not a concern, the passphrase can also be defined in clear text in the network section by enclosing it in quotes:   psk="passphrase" ; if NOT-qutoed, then its is encoden-PSK , output of wpa_passphrase !
		- if the network does not have a passphrase, e.g. a public Wi-Fi, then set in network-block:   key_mgmt=NONE  ; bzw. in wpa_cli :  > set_network  <your-cu-NW-No>  key_mgmt NONE
	----- hidden APs:
		 -!!  for hidden-APs/-stations the cmds in Anleitungen does NOT work!! you hace to use cmds for hidden-APs!!
		 - for  hidden APs, in the  scanning-result the SSID is not clear text!
	----- connection (after establishing connection manually start dhcpcd wlan0, to obtain IP !!)):
		- onliner (ONLY root-shell! not sudo):   wpa_supplicant  -B  -i  wlan0  -c <(wpa_passphrase "bibliothek1-AP" "06.01.2020cC")  ;  ##-- or without -B (not-Daemon), or in debuuging mode,...
		- /OR start wpa_supplicant ; then interactively wpa_cli + dhcpd (see below) ;
		- /OR with config-file:  wpa_supplicant -B -i  <wlan0>  -c  <.../myAP1.cfg>  ##--see below
	----- steps for setup/config-arx1-OK-1912 :
		tools:   sudo wpa_supplicant , wpa_passphrase , wpa_cli , dhcpcd/dhclient :   see https://wiki.archlinux.org/index.php/WPA_supplicant
		wpa_supplicant package, which includes the main program wpa_supplicant, the passphrase tool wpa_passphrase, and the text front-end wpa_cli.
		-! hidden-AcceccPoints/SSIDs : MUST add scan_ssid=1 in the network block (eg gnerated by:  wpa_passphrase   gc1-5gh   "12...+....15"  /OR manually -creted-config-file  !?!?  with  WPA_supplicant / wpa_cli  + at the end "dhcpcd wlan0" to get an IP ! see:  https://wiki.archlinux.org/index.php/WPA_supplicant
			... Tip: To configure a network block to a hidden wireless SSID, which by definition will not turn up in a regular scan, the option scan_ssid=1 has to be defined in the network block (in config-file).  see https://wiki.archlinux.org/index.php/WPA_supplicant#Configuration
		--- one-line-manually-start-connect in a root-console (NOT-sudo, due to subproccess) :   wpa_supplicant  -B  -i  wlan0  -c <(wpa_passphrase "bibliothek1-AP" "06.01.2020cC")  ##-- (or without -B in vorderground, to see messages) in a root-console (not sudo! due to sub-proccess (....) ), eg:   wpa_supplicant  -B  -i  wlan0  -c <(wpa_passphrase "bibliothek1-AP" "06.01.2020cC")
		--- steps manually connect, as root/sudo:
		- start it manually :  wpa_supplicant -B -i  <wlan0>  -c  <.../myAP1.cfg>   ##--/OR ohne -B , so not-Daemon ,but in forground, too see problems,...
		  /OR systemd-start/enabling...:   systemctl  enable/start/stop/disable/status/...  wpa_supplicant    ##--  wpa_supplicant.service 
		---> if not deamon, you see connection/authentication established in console!
		- dhcpcd  wlan0 #---> done
		- checkit with ...: ip addr , ip r , ip link , ping , .....
		- the AP-password in the config file can be in cleartext  with:  psk="12....15"  /OR  encrypted-generated with eg:  wpa_passphrase   gc1-5gh   "12....15"  
		then, just take its ouput, add scan_ssid=1  as first line in network block and put it in the config file /OR directly in cmdline
		--- eg config-file  ~/gc1-5gh.cfg:
		ctrl_interface=/run/wpa_supplicant
		update_config=1
		country=DE
		network={
			scan_ssid=1
			ssid="gc1-5gh"
			psk="12....15"  ##--here as cleartext-PW, eg ok for BiB-AP  /OR enc-output-of:  wpa_passphrase  "gc1-5gh" "12....15" ,  then ohne " as : psk=b7cdd0342e0e41266e771740cae28fb1a8459181f1762037574780e249646cec
		}
		---
		- dhcp:  Once association is complete, you must obtain an IP address, for example, using dhcpcd ... (wpa does NOT do dhcp stuff automatically !!)
	----- dhcpcd + wpa-hook for it:
		-!! https://wiki.archlinux.org/index.php/Dhcpcd
		- if liked, set a hook by dhcpcd.service for starting wpa-stuff:  https://wiki.archlinux.org/index.php/Dhcpcd#10-wpa_supplicant
		so configure the dhcpcd.service  to start also the  wpa_supplicant.service mit ! so setting a hook by dhcpcd to start the wpa-service:
		Enable this hook by creating a symbolic link, which ensures the current version is used, even after package updates:
		ln -s /usr/share/dhcpcd/hooks/10-wpa_supplicant /usr/lib/dhcpcd/dhcpcd-hooks/
		- dhcpcd executes all scripts found in /usr/lib/dhcpcd/dhcpcd-hooks/ in a lexical order. See dhcpcd.conf(5) and dhcpcd-run-hooks(8) for details.
		--- DNS / naming :
		if naming does not work, just as quick-woraround, you can enter the gateway/router/naming-serer manually in /etc/resolv.conf ! it will be by next reboot/... overwritten anyway by dhcp-service or so ...
		or try??:   systemctl stop  dhcpcd.service  ;  systemctl start  dhcpcd.service ##-and then check if /etc/resolv.conf  was updated !?!?
		see also:  man  dhcpcd;  systemctl status dhcpcd.service ; man 
		--- OR us resolvecon serivice of systemd for naming:
		systemctl   enable systemd-resolved.service

	_______:  /OR:
	----- interactively connect to an AP with wpa_cli  (after already having started wpa_supplicant):
		- listing of availablae APs/SSIDs : wpa_cli ; >scan ; > scan_results ;  ##-after already having started wpa_supplicant
		# wpa_cli  ##--> goes into interactive shell.
		> scan
		OK ...
		> scan_results
		bssid / frequency / signal level / flags / ssid
		00:00:00:00:00:00 2462 -49 [WPA2-PSK-CCMP][ESS] MYSSID
		11:11:11:11:11:11 2437 -64 [WPA2-PSK-CCMP][ESS] ANOTHERSSID
		> add_network
		0                       ##--Each network is indexed numerically, so the first network will have index 0.
		> set_network 0 ssid "MYSSID"
		> set_network 0 psk "MY-Password-1"  ##--PW-nts:  /OR the PSK key generated by wpa_passphrase, then NOT-quoted ! if no PW needed then replace the line with:  > set_network 0 key_mgmt NONE
		> enable_network 0
		<2>CTRL-EVENT-CONNECTED - Connection to 00:00:00:00:00:00 completed (reauth) [id=0 id_str=]
		> save_config
		OK
		> quit
		- Once association is complete, you must obtain an IP address, for example, using dhcpcd ... (wpa does NOT do dhcp stuff automatically !!)
	----- config-file:
		- can be located anywhere ...
		- man  wpa_supplicant.conf ;
		- a basic configuration file can be generated with:     wpa_passphrase MYSSID "passphrase" > /etc/wpa_supplicant/example.conf
		- hidden APs:  
		- If security is not a concern, the passphrase can also be defined in clear text in the network section by enclosing it in quotes:   psk="passphrase"
		- if the network does not have a passphrase, e.g. a public Wi-Fi, then set in network-block:   key_mgmt=NONE
	----- boot-time-start bzw. systemd :
		https://wiki.archlinux.org/index.php/WPA_supplicant#At_boot_(systemd)
		-! modified the systemd-cservice-file to add the configfile  (on ubuntu the @wlan0 variation does not exist, as in arx-docs!): 
		/bin/systemctl   enable  wpa_supplicant.service
		vi  /etc/systemd/system/dbus-fi.w1.wpa_supplicant1.service  ##: ergaenze the exec-line with "-c <config-file>"
		/bin/systemctl   start  wpa_supplicant.service  ##--> so checkit! maybe dhclien needed!?!?
	----- MAC-randomizing/spoofing with wpa, so dynamic MAC:
		-!! see  https://wiki.archlinux.org/index.php/MAC_address_spoofing#wpa_supplicant
		-! and see tech-docs in:  /usr/share/doc/wpa_supplicant/examples/wpa_supplicant.conf.gz  , man wpa_supplicant.conf	 ##check location with pacman -Ql wpa...
		Add this to your configuration: /etc/wpa_supplicant/wpa_supplicant-wlan0.conf  ##--1kk woul set 2 instead 1 , to keep the OUI-prefix (intel/cisco/...) ; see /usr/share/doc/wpa_supplicant/examples/wpa_supplicant.conf.gz :
			mac_addr=1
			preassoc_mac_addr=1
			gas_rand_mac_addr=1
		-! for eventuell needed naming of links/NW-cards, then use its udev-path ! see https://wiki.archlinux.org/index.php/Network_configuration#Change_interface_name
############# __1END__ wpa-setup ________ #############################################################
############# more/other approaches for networkd/notworkManager/... : #################################
##________________________________________  ___________________________


#####  ==========  WiFi-Menu-auswahl, wie NetworkManager aber cmdline-dialog :
	pacman -Syu  netctl
	sudo wifi-menu
##________________________________________  ___________________________


#####  ==========  iwd  (arx-Community-Repo)
	iwd  is  WAP2 capable  + AND settings for hidden-APs!!   see the table in  https://wiki.archlinux.org/index.php/Network_configuration/Wireless#Utilities
	so with:   iwd + iwdcl + dhcpcd  , see https://wiki.archlinux.org/index.php/Iwd

	_______:  arx-install-stepsok-1912 :
	pacman -Syu  iwd ;
	systemctl  start  iwd.service ;
	iwctl  ##---> interactive-prompt, >help , see cmds for hidden APs ! for non-hiddens see cmds in   https://wiki.archlinux.org/index.php/Iwd
	dhcpcd wlan0 ;

	_______:  
##======================================================###############################
