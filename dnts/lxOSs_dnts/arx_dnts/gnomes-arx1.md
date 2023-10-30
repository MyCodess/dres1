##________________________________________  ___________________________


#####  ==========  
-!!   man dconf(1)  ,  dconf(7), gsettings(1), dconf-editor(1)
-!!  editting/modifying/setting/...:   gsettings(1), dconf-editor(1)
##________________________________________  ___________________________


#####  ==========  dump /printout /search in dconf database/configs:

	_______:  mit dconf :
- DIFF:   dconf dump : is recursive /subtree !!  <--->   dconf list   : listing inly direct-nodes of key-values !
-!!  dconf-database/config-file (binary):  ~/.config/dconf/user
-!!  dump whole dconf-database :   dconf dump /  >  dconf-txt.log
-!!  search/finding something :    dconf dump /  | grepi terminal  ;/OR  dconf dump /  | grepi favorite-apps

	_______:  mit gsettings :
- listings :
gsettings list-schemas
gsettings list-recursively  | sort | uniq >| gsettings-${USER}-${uueHostname}-${sysTg}-$($cudts).log
gsettings list-recursively  | grepi  favorite-apps
gsettings list-recursively  | grepi terminal
##________________________________________  ___________________________


#####  ==========  StartMenu:
-  favorites:   dconf dump /     | grepi favorite-apps   --->   '/org/gnome/shell/favorite-apps'
-  favorites:   gsettings list-recursively    | grepi  favorite-apps   --->  org.gnome.shell   favorite-apps
##________________________________________  ___________________________


#####  ==========  Terminal :
-! dconf dump /  | grepi terminal   -->   /org/gnome/terminal/legacy/  bzw.   [org/gnome/terminal/legacy/profiles:]
dconf list /org/gnome/terminal/legacy/profiles:/
gsettings list-schemas | grepi terminal
gsettings list-recursively   org.gnome.Terminal.ProfilesList
gsettings list-recursively   org.gnome.Terminal.Legacy.Settings
##________________________________________  ___________________________


#####  ==========  caps_lock disabling:
org.gnome.desktop.input-sources xkb-options   ['caps:none']
##________________________________________  ___________________________


#####  ==========  coll:
