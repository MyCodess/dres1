________ sockets-communication in Bash. __________
##________________________________________  ___________________________


#####  ==========  eg: cyberciti.biz  1105:
http://www.cyberciti.biz/tips/spice-up-your-unix-linux-shell-scripts.html
Bash Socket Programming
Under bash you can open a socket to pass some data through it. You don't have to use curl or lynx commands to just grab data from remote server. Bash comes with two special device files which can be used to open network sockets. From the bash man page:
/dev/tcp/host/port - If host is a valid hostname or Internet address, and port is an integer port number or service name, bash attempts to open a TCP connection to the corresponding socket.
/dev/udp/host/port - If host is a valid hostname or Internet address, and port is an integer port number or service name, bash attempts to open a UDP connection to the corresponding socket.
-- You can use this technquie to dermine if port is open or closed on local or remote server without using nmap or other port scanner:
# find out if TCP port 25 open or not
(echo >/dev/tcp/localhost/25) &>/dev/null && echo "TCP port 25 open" || echo "TCP port 25 close"
-- You can use bash loop and find out open ports with the snippets: 
echo "Scanning TCP ports..."
for p in {1..1023}
do
  (echo >/dev/tcp/localhost/$p) >/dev/null 2>&1 && echo "$p open"
done
Sample outputs:
Scanning TCP ports...
22 open
53 open
80 open
139 open
445 open
631 open

	_______:  ----- In this example, your bash script act as an HTTP client:
#!/bin/bash
exec 3<> /dev/tcp/${1:-www.cyberciti.biz}/80
printf "GET / HTTP/1.0\r\n" >&3
printf "Accept: text/html, text/plain\r\n" >&3
printf "Accept-Language: en\r\n" >&3
printf "User-Agent: nixCraft_BashScript v.%s\r\n" "${BASH_VERSION}"   >&3
printf "\r\n" >&3
while read LINE <&3
do
   # do something on $LINE
   # or send $LINE to grep or awk for grabbing data
   # or simply display back data with echo command
   echo $LINE
done

	_______:  --------
--! A Note About GUI Tools and Cronjob
You need to request local display/input service using export DISPLAY=[user's machine]:0 command if you are using cronjob to call your scripts. For example, call /home/vivek/scripts/monitor.stock.sh as follows which uses zenity tool:
@hourly DISPLAY=:0.0 /home/vivek/scripts/monitor.stock.sh

	_______:  -
See the bash man page for more information:
man bash
##________________________________________  ___________________________


#####  ==========  
