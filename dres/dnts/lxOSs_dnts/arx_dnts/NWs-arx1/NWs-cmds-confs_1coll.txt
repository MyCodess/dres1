______________ NWs-cmds .... _________________________________________
-!! EXTRA dnts  for "ip" command and wpa !!
##________________________________________  ___________________________


#####  ==========  IP-Address finding/queryin/scannong/...
- own local IP addresse?:  hostname -i
- MAC adr:  ethtool -P wlan0 /eth0 ...  ##OR:  ip link
- nmap (IP and ports scannong): see extra dnts here in NWs-sec.txt ... ! eg: find all IPs in my subnet:  nmap -sn 192.168.1.0/24
##________________________________________  ___________________________


#####  ==========  monitor-/trace-/...-NW-pakets:
	- tcpdump
	- wireshark
	- nmap ( port scanner)  --> see dnts extra in NWs-sec.txt !
	- ss (netstat)
	- traceroute , tracepath, ... ##--The tracepath command provides the MTU for each hop, whereas traceroute does not. ; tracepath simpler and kompakter; traceroute sometimes needs root privileges !
##________________________________________  ___________________________


#####  ==========  DNS ,nslookups...:
	- conf-files-dns-relevant:  /etc/nsswitch.conf  /etc/hosts  /etc/resolv.conf   /etc/systemd/resolved.conf
	- man systemd-resolved.service , resolved.conf , resolv.conf , nsswitch.conf , hosts , 
	- dig  - DNS lookup utility  (in bind package)  ##-- pacman -Syu  bind
	- host - DNS lookup utility  ,// ;
	- nslookup itself is eher obsol!?
##________________________________________  ___________________________


#####  ==========  Listeners,...:  --> see also exp below !
	netcat /nc : (ports-connections) is a simple Unix utility which reads and writes data across network connections, using TCP or UDP protocol. ##also linked as nc ; eg quick-port-connection-tests ! see exp below!
	ncat
	socket
##________________________________________  ___________________________


#####  ==========  HWs-NWs HWs-confs :
    - ethtool  - query or control network driver and hardware settings
	- check if your NW-hardwaware is not physically by hardware button/switch disabled ??:  rfkill list
	- naming eth0 / wlan0 : ensure the traditional (obsol?) NW-cards/-interfaces-names: ln -s /dev/null /etc/udev/rules.d/80-net-setup-link.rules
	- Listing network interfaces: ls /sys/class/net  ;  ip link ;# wirless-cards also: iw dev ;
##________________________________________  ___________________________


#####  ==========  wireless :

	_______:  Services-/Daemons-wireless :only ONE enable/autostart !! :
	systemd , iwd, wpa !

	_______:  wpa : see wpa-nts ! ... sudo  systemctl   restart   dhcpcd.service  wpa_supplicant.service ; ...; /etc/wpa_supplicant/ ; ...

	_______:  iwd:  pacman -S iwd  ;  systemctl enable iwd.service ;

	_______:  systemd: systemctl enable systemd-networkd.service ,

	_______:  tools-wireless:(are just tools; so can be installed anyway, parallel to other NWs-serices !):
	pacman -S core/wireless_tools : iwconfig, iwlist, iwspy, iw dev , ...
	- nmcli , nmtui

	_______:  NetworkManager-gnome-wireless cmds:
	-! https://developer.gnome.org/NetworkManager/stable/nmcli.html  + exp:  https://developer.gnome.org/NetworkManager/stable/nmcli-examples.html
##________________________________________  ___________________________


#####  ==========  lsof as ss-simailar (checking ports): ONLY as root/sudo !!:
	sudo  lsof  -i  #for localhost; /OR with -P for port-numbers instead port-names in /etc/services
	sudo  lsof  -Pi @[hostnameXX]:22 ; /OR  lsof -i @[hostnameXX] :ssh 
	sudo  lsof  -i@192.168.1.7:22,80    ##checking ports 22 and 80
##________________________________________  ___________________________


#####  ==========  legacy net-tools <---> ip (iproute2)  cmd-compare ;  ifconfig/netstat  <---> ip  : ==============
	-----
	Deprecated command 	<---> 	Replacement command(s) :  https://wiki.archlinux.org/title/Network_configuration :
	--------------------------------------------------------------
	arp	        --	ip neighbor
	ifconfig	--	ip address, ip link
	netstat		-- 	ss
	route 	    -- 	ip route
	----------------------------------------
	https://wiki.archlinux.org/index.php/Network_configuration#Network_management
	--- more :
	Deprecated command 	<---> 	Replacement command(s) :
	--------------------------------------------------------------
	arp  --	ip n (ip neighbor)
	ifconfig	--  ip a (ip addr), ip link, ip -s (ip -stats)
	iptunnel  --	ip tunnel
	iwconfig  --	iw
	nameif	 --     ip link, ifrename
	netstat  -- 	ss, ip route (for netstat-r), ip -s link (for netstat -i), ip maddr (for netstat-g)
	route   --  	ip r (ip route)
	--------------------------------------------------------------
	netstat replace by "ss" from  iproute2 ! : man ss
	---
	-!  Arch Linux has deprecated net-tools in favor of iproute2.[2] :
	-! full-listing + exp see :   https://dougvitale.wordpress.com/2011/12/21/deprecated-linux-networking-commands-and-their-replacements/
##________________________________________  ___________________________


#####  ==========  
####################### 1coll-NWs-cmds ... /tr/.... . #####################################
-!! EXTRA dnts  for "ip" command and wpa !!
##________________________________________  ___________________________


#####  ==========  HWs-NW , adapters, ...:
ip link show dev <xx>
ip link set <interface> up|down  ##--!! The UP in the output "<BROADCAST,MULTICAST,UP,LOWER_UP>... state DOWN" is what indicates the interface is up, not the later state DOWN.
##________________________________________  ___________________________


#####  ==========  host cmd /DNS-lookup exp:
host  heise.de
host  www.vim.org   8.8.8.8    ##--no-local-DNS-server needed! queries directly google-DNS 8.8.8.8 !
##________________________________________  ___________________________


#####  ==========  dig  cmd /DNS-lookup exp:
dig www.vim.org
dig @8.8.8.8   www.vim.org     ##--no-local-DNS-server needed! queries directly google-DNS 8.8.8.8 !
##________________________________________  ___________________________


#####  ==========  traceroute exp :
-! if firewall/... blocks traceroute-functions (sending ICMP pakets ...), then use traceroute -T ... which uses TCP-SYN to find the route!
##________________________________________  ___________________________


#####  ==========  ifconfig exp , and compare ip :
ifconfig eth0 192.168.1.1 netmask 255.255.255.0   ##-- configures the eth0 device with an IP address of 192.168.1.1 in a /24 network.
ifconfig eth1 inet6 add fdd6:551:b09e::/128       ##-- configures eth1 with an additional IPv6 address of fdd6:551:b09e:: 
show all NWs settings: ifconfig
show all NWs interfaces (egal ob up/down): ifconfig  -a
ifconfig  eth0
ifconfig eth0 up/down
ifconfig eth0 172.16.25.125  ## will set the IP address to interface eth0.
ifconfig eth0 netmask 255.255.255.224
ifconfig eth0 broadcast 172.16.25.63  ##--Assign a Broadcast Address to a Network Interface
ifconfig eth0 172.16.25.125 netmask 255.255.255.224 broadcast 172.16.25.63
ifconfig eth0 mtu 1000
ifconfig eth0 promisc/-promisc  ##Enable/disabl/disable Promiscuous Mode
ifconfig eth0 allmulti/-allmulti  ##--Enable/disable All-Multicast Mode For an Interface
Add New Alias to Network Interface :   ifconfig eth0:0 172.16.25.127
verify the newly created alias : “ifconfig eth0:0” 
Remove Alias to Network Interface:   ifconfig eth0:0 down
change the MAC (Media Access Control) address of an eth0 network interface:  ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF
- ipv6:
ifconfig eth0 add/del 2001:0db8:0:f101::1/64 ; ##--Add/del an IPv6 Address to a Network Interface

	_______:  ifconfig <---> ip exp:
enable/disable device:   # ifconfig eth0 down/up  # ip link set eth0 down/up
add/del the IP address:   ifconfig eth0 add/del 192.168.80.174    ##==  ip addr add/del 192.168.80.174 dev eth0   ##-- assigns/del the IP address 192.168.80.174 to the interface eth0.
add MAC Address:   ifconfig eth0 hw ether 00:0c:29:33:4e:aa    ##==   ip link set dev eth0 address 00:0c:29:33:4e:aa
Set MTU value to 2000 :  ifconfig eth0 mtu 2000   ##==  ip link set dev eth0 mtu 2000
Enable or Disable multicast flag:  ifconfig eth0 multicast  ##==  ip link set dev eth0 multicast on
Setting the transmit queue length.  # ifconfig eth0 txqueuelen 1200 # ip link set dev eth0 txqueuelen 1200
Enable or disable all multicast mode.  # ifconfig eth0 allmulti # ip link set dev eth0 allmulti on
Enable/Disable ARP Protocol: # ifconfig eth0 arp/-arp    # ip link set dev eth0 arp on/off

	_______:  route (obsol pre "ip"):
-! see exp in man route ,at end!
route add default gw 192.168.1.1 eth0
route add -host 192.168.1.3 reject  ##-- prevents traffic from reaching the host 192.168.1.3
##________________________________________  ___________________________


#####  ==========  LISTENER-creating/testing/communicating-exp   on port X (for tests/troubleshooting/...):
netcat -l -p 8585 ;/OR  nc -l -p  8585      ##--Gnu-netcat here ! creates a server listening on port 8585 !   /usr/bin/nc -> ./netcat
ncat -lk   8585       ##--is in nmap pkg ! is NOT nc !!
socket -sl 8585       ##--was in book-H.M., aber not available on arch !?!?
- port-communication-test-exp (you see then messages like "talk" in both terminals):
	on-pc1:  netcat -l -p 8585
	on-pc2:  netcat  pc2  8585   ##--NO-firewall-blocking-between !!
	write text in each terminal, you see the text in other terminal ! like talk-ing !

	_______:  eg terminal--browser:
- in terminal do:  netcat -l  -p 8585
- then in browser do:  http://localhost:8585/  ##--check that lo device is up, toherwise do:  ip link set lo up ; and check with ip addr ;
- you should see in terminal the browser access, and then wire something in listener-terminal, and with ctrl-c or soooooo see in browser!

	_______:  eg terminal--terminal:
- in listener-terminal:   netcat -l -p 8585  ##--or nc instead netcat. the same !
- in sender-terminal:     netcat  localhost 8585  ##-- then wirte some texts there
- you should see the sender-terminal-texts in listener-terminal !

	_______:  simulating with ssh binding adress -L :
ssh -L .... :  Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, so eg:
- in terminal:  ssh -L 8585:www.gnu.org:80  localhost  ##--now localhost-port-8585 is gebunden to www.gnu.org:80 !!
- in browser :  http://localhost:8585/
- then the browser goes to website of www.gnu.org  !!
##________________________________________  ___________________________


#####  ==========  
