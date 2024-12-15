#!/bin/bash

##-- showing/listing/finding  XDG-start-menu-files  in the current system based on XDG-specs and also their default values!
##-- see specs:  http://standards.freedesktop.org/basedir-spec/latest/
##--II-- home == user-dirs, syys == global-OS-dirs, user-dirs are prereferenced! home/user-dir are usu. a single dir, but syys-dirs are usu. colon-separated-DIRs !


##----- Info-outputs of current-XDG-Vars:
echo;
echo "============== Current System XDG-Vars: =============="
export | grep XDG | sort
echo "======================================================"
echo

##----- DEFAULT-xdg-values, if the var is not defined (see XDG-specs): 
export xdg1_config_home="${XDG_CONFIG_HOME:-$HOME/.config/}"
export xdg1_config_syys_dirs="${XDG_CONFIG_DIRS:-/etc/xdg}"
export xdg1_data_home="${XDG_DATA_HOME:-$HOME/.local/share}"
export xdg1_data_syys_dirs="${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}"

##----- CONFIG-dirs of system + user/HOME:  
export xdg1_config_syys_dirs="${xdg1_config_syys_dirs//:/  }"    ##-replace colon with space to use it as parameter for find command!
echo "=   xdg1_config_syys_dirs  are:  "  $xdg1_config_syys_dirs
export  xdg1_config_all_dirs="$xdg1_config_home   $xdg1_config_syys_dirs"
echo "=== xdg1_config_all_dirs  are:  "  $xdg1_config_all_dirs

##----- DATA-dirs of system + user/HOME:
export xdg1_data_syys_dirs="${xdg1_data_syys_dirs//:/  }"    ##-replace colon with space to use it as parameter for find command!
echo "=   xdg1_data_syys_dirs    are:  "  $xdg1_data_syys_dirs
export  xdg1_data_all_dirs="$xdg1_data_home   $xdg1_data_syys_dirs"
echo "=== xdg1_data_all_dirs    are:  "  $xdg1_data_all_dirs


##----- ALL-xdg-dirs:
export xdg1_all_dirs="$xdg1_config_all_dirs  $xdg1_data_all_dirs"
echo "=   xdg1_all_dirs         are:  "  $xdg1_all_dirs

##-  find $xdg1_all_dirs -iname "*${1}*"

echo;
