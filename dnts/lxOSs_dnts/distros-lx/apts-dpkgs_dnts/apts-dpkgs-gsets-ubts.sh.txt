_______________________ dnts zu apt/dplg/gsettings/.....: _____________________________________________
exit 3

#####  ==========  apts-nts :
	- "apt" itself is NOT considered here that much, but can be also uses for many cases instead following cmds! see also man apt !
	- do NOT use "apt" itself in scripts! see man apt ! but the outcommented-prev-"apt-cmds works also fine for now!!
	- DIFF:   AllPkgs : all-pkgs-in-Repos+Locally (apt cmds) <-->  InstPkgs  :  Only-Locally-Installed-PKGs (dpkg cmds)
	- aptitude is used here seldom, but many cmds here can be also done by aptitude ! see man aptitude , but more in Ref:  /usr/share/doc/aptitude/html/
    - ! If Debian says "The following packages have been kept back:", do:   sudo apt-get dist-upgrade  ##/OR?: apt-get --with-new-pkgs upgrade  #and-then:  apt-get install <list of packages kept back>
##________________________________________  ___________________________


#####  ==========  gSettings:
    echo  "----- gSettings-listing-USER: -----------------------------";
    gsettings list-recursively  | sort | uniq >| gsettings-${USER}-${uueHostname}-${syysTg}-$($cudts).log
##________________________________________  ___________________________


#####  ==========  install/uninstall/remove packages :
    -  apt install <packageName>
    -  apt remove <packageName>  ##--uninstall/delete pkg
##________________________________________  ___________________________


#####  ==========  Listing-/search-installedPkgs :

    -ok-OnlyNames-with-apt:   apt --installed list   #-/OR  dpkg-query  -l   ##oneliners
    --- listing + grep + sed + cmds ...:
    -ok:  dpkg  --list | grep  ^i   >|  instPkgs-list-oneLiners---dpkg_list.log          ##--it invokes finally dpkg-query   --list ; so same; see man dpkg , so same as dpkg-query -l ....
    -ok-listing-lines-but-without-header:      dpkg-query   --list  |  tail -n +6
    -ok-OnlyNames-with-sed-installed-and-purged-ones:   dpkg-query  -l  | tail -n +6 |  sed  's/^[^ ]* *//;s/ .*//'  | sort   ##--contains also prev-installed and purged ones, so also not-installed-now any more!
    -ok-OnlyNames-with-sed--ONLY-installed-now:         dpkg-query  -l  | grep ^ii |sed 's/^[^ ]* *//;s/ .*//' | sort
    -ok-OnlyNames-with-dselction-param:   dpkg  --get-selections | sort | grep -v deinstall | sed 's/\s.*//' >|   instPkgs-list-onlyNames---dpkg_list.log
    -ok-OnlyNames-directly-with-format-option/params:   dpkg-query   -f '${binary:Package}---Stat1::${db:Status-Status}\n'  -W  | sort | fgrep -i "Stat1::installed" | sed 's/---.*//'   ##--withour Stat-flag  still not-installed/prev-purged-pkg-names still there!
    -ok-OnlyNames-BUT-partly-shortened-names!!:   dpkg-query  -l   |  tail -n +6 | grep -i "^.i" | sed 's/ii *//;s/\s.*//' | sort    >|   instPkgs-list-onlyNames---dpkg_list.log  ##--BUT columns/pkg-names are partly cut/adapted/shortened to the column-width !!
    --- listing-instPkgs.sh :
    echo  "----- installedPKGs-listing-oneLiners: --------------------";
    dpkg-query  -l  >|  instPkgs-list-oneLiners---dpkg-query_list.log    ##--do NOT sort it! the first column is NOT pkg-name, but its flags/status! see man dpkg-query
    echo  "----- installedPKGs-listing-formatted: --------------------";
    dpkg-query  -f '${binary:Package}---Stat1::${db:Status-Status}\n'  -W  | sort | fgrep -i "Stat1::installed" | sed 's/---.*//' >|   instPkgs-list-onlyNames---dpkg-query_list.log
    ---
    - listing-installed-pkgs+infos+descriptions: --> basically NOT needed as seperate log file! for Infos just check the allPkgs-infos---apt-cache_show.log ! but here in case:
    -ok:  apt --installed list  | sed  's/\/.*//;s/^Listing..*//' | xargs  apt-cache  show >|  instPkgs-show--apt-cache_show_installed.log
    -ok:  dpkg-query   --list  |  sed  's/[^\s]*//;s/\s.*$//'  | sort  | xargs apt-cache  show  >|  instPkgs-infos---apt-cache_show.log
    -ok:  dpkg-query   -f '${binary:Package}---Stat1::${db:Status-Status}\n'  -W  | sort | fgrep -i "Stat1::installed" | sed 's/---.*//'  xargs apt-cache  show  >|  instPkgs-infos---apt-cache_show.log
##________________________________________  ___________________________

#####  ==========  Listing-/search-ALLpkgs:
    -  apt-cache  search  street               ##--search for  *street* in names+description/infos of ALLPkgs
    -  apt-cache  search --names-only street   ##--search for  *street* in only names  of ALLPkgs
    -  aptitude search street  ##--same-as   aptitude search "?name(street)"  ##--search for  *street* in only names  of ALLPkgs
##________________________________________  ___________________________


#####  ==========  allPKGs.sh :
    echo  "----- allPKGs-listing-namesOnly: --------------------------";
    apt list >| apt-list-allPkg.log
    apt-cache  pkgnames | sort >| allPkgs-list-namesOnly---apt-cache_pkgnames.log
    echo  "----- allPKGs-listing-infos-descriptions (long, 3min): -----------";
    apt list  | sed  's/\/.*//;s/^Listing..*//' | xargs  apt-cache  show >|  apt-show-allPkg.log
    apt-cache  dumpavail  bzw.  dump  ##--shows tech-details in local-package-acache saved about ALLpkgs in Repos+locally   #!--ok--ohter-format/output:   
    apt-cache  pkgnames | sort  | xargs apt-cache  show  >|  allPkgs-infos---apt-cache_show.log
##________________________________________  ___________________________



#####  ==========  files-query/listings + reverse : to which package belongs this file?:
    -to-which package belongs this file?:   dpkg-query   -S   /usr/sbin/chroot
    -file-reverse-query:   dpkg-query -S  filename-search-pattern... ##--search  for  packages  that  own  files corresponding to the given pattern! see man dpkg-query 
##________________________________________  ___________________________


#####  ==========  installedPKGS_Files.sh :
    # list upgradables pkgs:  apt list --upgradable
    # sudo apt full-upgrade
    echo  "----- installedPKGS_Files-listing-full (longer, 5min): ----";
    dpkg-query   -l  |  sed  's/[^\s]*//;s/\s.*$//'  |  xargs  dpkg-query -S    >|    instPkgs-filesListing---dpkg-query_list.log  ##-ok--FilesListing-of-instPkgs !    
    #-ReDo1-is--long:  
    for ii in $(cat ./instPkgs-list-onlyNames---dpkg-query_list.log); do echo;echo;echo "================== $ii : ==========" ; dpkg-query -L $ii ; done   >|  instPkgs-filesListings---dpkg-query_L.log
    date;
    echo  "======= ENDr  Updating dPKG + apt listings !  ==============="
    echo ; exit 0;
##________________________________________  ___________________________

