#!/bin/bash
set -x
echo  "__  ===== Wireless-NW-connection: ======================== "
echo  "__  see   https://wiki.archlinux.org/index.php/Network_configuration/Wireless#iw  : "
export wlName1=wlp3s0   ##--x15-wirless-adapter-name
echo  "__ listing of wireless devices and infos :"
iw dev   ##--listin of wireless devices and infos
echo  "__ check link/dev status :"
iw dev  $wlName1   link  ##--check link status
echo  "__ get statistic information of the dev :"
iw dev  $wlName1  station dump   ##--get statistic information, such as the amount of tx/rx bytes, signal strength...
echo  "__ activate , bring dev up :"
ip link set   $wlName1   up
echo  "__ verify that the interface is up :"
ip link show $wlName1
echo  "__ Discover access points (check yourself with less /OR .. ): "
iw dev $wlName1  scan
echo "__ !! due to WPA", you need now a WP"-capable-client for PW !! as WPA supplicant  /OR iwd ... ! see dnts or link above!!"
exit 0


echo "=====######### ERROR!! you may NOT have reached here !!  #####======"
exit 3
