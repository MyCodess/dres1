#!/bin/bash

##--II-for nts+coll+more... see extra txt-file  apts-dpkgs-gsets-ubts.sh.txt !!
##--DIFF:   AllPkgs : all-pkgs-in-Repos+Locally   <-->  InstPkgs  :  Only-Locally-Installed-PKGs

cd ${syysTgLogsDP} ||  exit 3
echo  "==================== Start Updating dPKG + apt listings :  ===============" ; date ;

echo  "----- gSettings-listing-USER: -----------------------------";
gsettings list-recursively  | sort | uniq >| gsettings-${USER}-${uueHostname}-${syysTg}-$($cudts).log

echo  "----- installedPKGs-listing-oneLiners: --------------------";
dpkg-query  -l   |  grep  ^i    >|  instPkgs-list-oneLiners---dpkg-query_list.log    ##--do NOT sort it! the first column is NOT pkg-name, but its flags/status! see man dpkg-query
##--OK also:   dpkg -l | grep ^i

echo  "----- installedPKGs-listing-formatted: --------------------";
dpkg-query  -f '${binary:Package}---Stat1::${db:Status-Status}\n'  -W  | sort | fgrep -i "Stat1::installed" | sed 's/---.*//' >|   instPkgs-list-onlyNames---dpkg-query_list.log

echo  "----- allPKGs-listing-namesOnly: --------------------------";
apt-cache  pkgnames | sort >|  allPkgs-list-namesOnly---apt-cache_pkgnames.log
apt list            | sort >|  allPkgs-list-stat---apt_list.log   ##--shows additionaly if the package is installed, and also package-versions!

echo  "----- allPKGs-listing-infos-descriptions (long, 5 min): -----------" ; date ;
apt-cache  pkgnames | sort  | xargs apt-cache  show  >|  allPkgs-infos---apt-cache_show.log   ;  date;

echo  "----- installedPKGS_Files-listing-full (longer, 10 min): ----";
for ii in $(cat ./instPkgs-list-onlyNames---dpkg-query_list.log); do echo;echo;echo "================== $ii : ==========" ; dpkg-query -L $ii ; done   >|  instPkgs-filesListings---dpkg-query_L.log ;
date;

echo  "======= __1END__  Updating dPKG + apt listings !  ===============" ; echo ;
exit 0;



