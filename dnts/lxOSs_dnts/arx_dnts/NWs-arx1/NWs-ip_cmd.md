________________ ip cmd exp coll!  net-tool pkg : __________________________________
https://phoenixnap.com/kb/linux-ip-command-examples
https://www.cyberciti.biz/faq/linux-ip-command-examples-usage-syntax/
##________________________________________  ___________________________


#####  ==========  help:
ip addr/link/neigh/...  help
ip a/l/r/n  help
-!! use TAB for bash-completion!! works by all subcommands !!

	_______:  nts:
-  reboot and ip configs : Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can use a network manager or automate ip commands using scripts and systemd units ! https://wiki.archlinux.org/index.php/Network_configuration
##________________________________________  ___________________________


#####  ==========  usu. objects:
ip a/l/r/n  help
##________________________________________  ___________________________


#####  ==========  formatting/output of all: (see man ip)
-!  "-c" for color/pretty listing, as :  ip -c   a/l/r/n ;  /OR:  ip -c=always//auto/never ...
-!  "-br" :  TAB/table-formatted, short , as:  ip -c  -br a/l
-!  "-d"  : more details output
-!  "-r"  : hostnames instead IPs, eg by ip -r -c addr
-  "-j -p" : json-output and Prettyi-json-formatting !
-  -4 / -6  : IPv4/6

	_______:  
short-tabular: 	ip -br addr / route / link ...  ; eg ip  -j -p route          ##--on-ubuntu without ???
detailes:     	ip   -s -s  -h  -d   -N  -c   addr / route / link ...         ##--on-ubuntu without -N
details-in-json-aber-pretty-formatted:  ip  -j -p  addr / route / link ...    ##--on-ubuntu without -p
show status of the interface eth0:    ip link show dev eth0
##________________________________________  ___________________________


#####  ==========  link /interfaces :  man ip-link
ip link show dev [device]
statistics for all network interfaces :  ip -s link
up/down (Enabling and disabling network interfaces  :  ip link set <interface-name> up/down
MAC-addr-seting/changin:  ip l set wlan0 address 36:a7:fb:c0:1d:a5  ##--maybe must first down and then up !?
##________________________________________  ___________________________


#####  ==========  address/a : IP-addresses :  man ip-address
ip  a
ip  -4 a  ##--nur IPv4 ; -6 for IPv6
ip addr show dev [interface]
only-up-interfaces-show:   ip link ls/show up
add/del IP:	ip addr add/del [ip_address] dev [interface] ##--ip a del 192.168.1.200/24 dev eth0
eg: add/assign 192.168.1.200/255.255.255.0 to eth0, enter: ip a add 192.168.1.200/255.255.255.0 dev eth0
add a broadcast address to an interface:  ip addr add brd [ip_address] dev [interface] ;-eg:  ip addr add broadcast 172.20.10.255 dev wlan0
add the standard broadcast ( "brd +" :by setting/resetting the host bits of the interface prex) + the address, eg 192.168.1.50 with netmask 255.255.255.0 (/24) with standard broadcast to the interface eth0: ip addr add 192.168.1.50/24 brd + dev eth0 ;
##________________________________________  ___________________________


#####  ==========  routing /r :  man ip-route 
ip r help
ip route list [ip_address]  ##--only routeing of the ip_address
Display routing for 192.168.1.0/24: ip r list 192.168.1.0/24

	_______:  add/del routes/gw :
	-! "gw" bei ifconfig , ist praktisch "via" bei ip , so:
	route add default gw 192.168.1.1   bzw.   ip route add default via 192.168.1.1
	add-route:   ip route add [ip_address] dev [interface]
	add-route-via-gateway:  ip route add [ip_address] via [gatewayIP]
	add-default-route:   ip route add default [ip_address] dev [device]  #bzw:  ip route add default [network/mask] via [gatewayIP]
	del-route:  ip route del [ip_address] ; ip route del default ; ip route del [ip_address] dev [interface]
	- so,
	- Add a new route The syntax is:
	ip route add {NETWORK/MASK} via {GATEWAYIP}
	ip route add {NETWORK/MASK} dev {DEVICE}
	- Add default route using ip :
	ip route add default {NETWORK/MASK} dev {DEVICE}
	ip route add default {NETWORK/MASK} via {GATEWAYIP}
	- eg,
	Add a plain route to network 192.168.1.0/24 via gateway 192.168.1.254:   ip route add 192.168.1.0/24 via 192.168.1.254
	ip route del default
	ip route del 192.168.1.0/24 dev eth0

	_______:  save/backup/restore routing:
	ip route save > /root/routes/route_backup
	ip route restore < /root/routes/route_backup
##________________________________________  ___________________________


#####  ==========  ARPs/neigh/n   :  man ip-neighbour
ip n help ; ip n ;
add/del:   ip neigh add/del [ip_address] dev [interface]
############============ _1coll/exp ....: ================#####################################
ip link set eth1 up/down
ip route change default via 192.168.1.1 dev eth0  ##--change the default gateway to 192.168.1.1 using eth0? 
ip addr add 192.168.50.5 dev eth1
ip addr del 192.168.50.5/24 dev eth1
Add Static Route:  ip route add 10.10.20.0/24 via 192.168.50.100 dev eth0
Remove Static Route :  ip route del 10.10.20.0/24
Add Default Gateway:   ip route add default via 192.168.50.100
