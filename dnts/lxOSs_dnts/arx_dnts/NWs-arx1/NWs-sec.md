____________________ NWs-Security .....: _______________________________________
##________________________________________  ___________________________


#####  ==========  
-!!  https://sectools.org
-!!  https://nmap.org/
##________________________________________  ___________________________


#####  ==========  nmap
https://linuxhint.com/30_nmap_examples/

	_______:  
subnetworks as:   192.168.43.0/24  /OR 192.168.43.*  /OR    2004arx/24  ...

	_______:  DNS-points:
if problems with systemd-resolved as DNS-server!, so  do:   nmap  -n (No DNS resolution)  /OR-local-DNS:   [ --system-dns ]  
DNS/resolve:   faster host-scanning if no-DNS and no-ports-scanning,  so  -n (No DNS resolution)  /OR-local-DNS if resolve-problems:   [ --system-dns ]  
! BUT in manpage:   [ --system-dns ]  should be langsamer !?!?

	_______:  hosts-scanning-exp: 
faster only-hosts-scanning if :  no-ports-scanning with:  -sn !
faster if -n (no DNS)
hosts-scanning in my NW (quick, no-ports-scanning with -sn , so hosts-listing-only , and with -n for no-DNS/only-nummeric and faster):
	nmap      -sn  2004arx/24  ;
	nmap  [-n]  -sn   192.168.43.0/24     ##/OR 192.168.43.*  ; --no-DNS:   nmap  -n  -sn   192.168.43.*

	_______:  ports-scanning-exp:
	-- nmap :
	sigle-host-ports-scan:  nmap  [-n]  2004arx
	all-ports-scan on all-hosts-in-subnet	:  nmap     [ --system-dns ]  2004arx/24
	all-ports-scan on one-host	 	:  nmap [ --system-dns ]  2004arx
	certain-ports-scan on subnet 	:  nmap [ --system-dns ]  -p 80,22,139,21,23   192.168.43.*
	ports-range-scan on subnet  	:  nmap [ --system-dns ]  -p 22-80   linuxhint.com
	subnet-ports-scan:   nmap  192.168.43.1-30  ##all hosts from 01 to 30 in the subnet, do port-scanning
	-- check ifs port xx is open??:
	sudo  ss -tulpn | grep LISTEN  ##- netstat deprecated replacement!
	sudo  ss  --tcp  --listening -n
	sudo  lsof -i:22
	telnet localhost 22   ##check simply if port 22 open? if open, you see: ... Connected to ...
	/dev/tcp/{HostName}_OR_{IPAddrress}>/{port}” syntax to check if a TCP port is open on a Linu

	_______:  ARPs-scan-exp:
- Nmap ARP scan main features belong now to Nping, a tool belonging to the Nmap suite, the following examples include 2 using Nmap and one using Nping.
nmap -sn -PR 192.168.*.*
