________________ files-managers in Lx : browsing/managing files ..: ________________________________
-! see http://en.wikipedia.org/wiki/Comparison_of_file_managers
-!! GTK-default-bookmarks-file (used by all GTK-filemanagers as thunar/pcmanfm/nautilius/...):  ~/.config/gtk-3.0/bookmarks
##________________________________________  ___________________________


#####  ==========  Thunar / Xfce4  ##--->  see _RF in arx-dnts/xfce1-arx1-dnts.txt ! /_200400
##________________________________________  ___________________________


#####  ==========  pcmanfm / PCMan File Manager /LXDE
	- https://wiki.archlinux.org/title/PCManFM
	- ! is GTK-app ! so:
	- bookmarks: GTK-default-bookmarks-file, ~/.config/gtk-3.0/bookmarks
##________________________________________  ___________________________


#####  ==========  File-Managers-Auflistung + short-nts: GUI+Terms big+small:
-! see http://en.wikipedia.org/wiki/Comparison_of_file_managers

	_______:  -- GUI-FilesMgm:
pcmanfm : !good,light ..., OK! , lightweight Gtk+ filemanager, LXDE-desktop, https://www.lxde.org/...
Thunar	: !good,light ..., OK! , lightweight Gtk+ filemanager, Xfce4-desktop, freedesktop.org.-conform,  action-scripts with shell-scripts,  http://xfce.org/ 
--
nautilus, Files :Ubuntu, Gnome,...
Midori	: !good web-browser with konqueror-like-fasility, but not really file managers with copy/move/...
Konqueror:  KDE
nemo :      Mint
Xfe  :      Xfe
spacefm
(treeline)

	_______:  -- Norton-Commander-Clonies 7 half-terminal: opens an extra window, but NC-like two panes...:
gentoo	: more gui, but two-pane simple NC-style, no-bookmarks!?
tuxcmd

	_______:  -- Terminal-FilesBrowsers-fully , opend in consoles:
ytree
lfm
vifm	: vim-style
##________________________________________  ___________________________


#####  ==========  Nautilus/"Files"-settings (gnome-default-file-manager):

	_______:  configs:
- with gsettings or GUI ubuntu/dconf bzw. in Gnome/gconf !

	_______:  sidebar: bookmarks, places,...:
- places:   ~/.config/user-dirs.dirs 
- bookmarks in nautilus Files:  ~/.config/gtk-3.0/bookmarks

	_______:  gsettings:  set/get features:
- gsettings get org.gnome.nautilus.preferences tabs-open-position
- gsettings set org.gnome.nautilus.preferences tabs-open-position 'end'
- gsettings list-recursively  | grepi org.gnome.nautilus  | sed -e 's/  */    ---    /g'
- gsettings list-recursively  | grepi nautilus   ##OR better org.gnome.nautilus

	_______:  protocols-nautilus (with more plugins, then even more ):  http://wiki.ubuntuusers.de/Nautilus :
- Virtuelle Ordner: Nautilus kann bestimmte Verzeichnisse und Dateien zusammenfassen und als virtuelle Ordner darstellen :
burn:/// 	Daten, die für das Brennen auf ein Medium vorgemerkt sind
network:/// 	Anzeige der Netzwerkumgebung
trash:/// 	Papierkorb
computer:/// 	Übersicht der eingehängten Dateisysteme
- protocols:
Protokoll 	Beispiel 	Beschreibung
Samba 	smb://rechnername/freigabe 	Linux-Pendant zur Windows-Dateifreigabe. Über Samba kann man auf Freigaben anderer Windows- und Linuxrechner zugreifen.
FTP 	ftp://192.168.0.1 	Beliebtes Protokoll zum Dateitransfer
WebDAV 	dav://login@example.com/ordner bzw. davs://login:passwort@example.com 	Protokoll zur Bereitstellung von Dateien über das Internet
SSH 	ssh://benutzer@server:port/pfad/ordner 	Protokoll zur sicheren und unkomplizierten Datenübertragung zwischen Linux/Unix-Systemen (Angabe der Portnummer nur erforderlich, wenn diese vom Standardport 22 abweicht)
sftp 	sftp://benutzer:passwort@server:port 	Siehe SSH
##________________________________________  ___________________________


#####  ==========  Nautilus-Actions + Nautilus-Scripts:
-!! DIFF:  Nautilus-Actions (configured with nautilus-actions-config-tool , as kind of plugins )  <==>  Nautilus-Scripts: which are just normal executables/shell-scripts added in nau-scripts-dir, so easier/comfortable than a-actions!!

	_______:  Nautilus-Scripts :
- output of nautilus-script on /up1/BM1s/Ws  of:    export | grep -i nautilus 
declare -x GIO_LAUNCHED_DESKTOP_FILE="/etc/xdg/autostart/nautilus-autostart.desktop"
declare -x INSIDE_NAUTILUS_PYTHON=""
declare -x NAUTILUS_SCRIPT_CURRENT_URI="file:///up1/BM1s"
declare -x NAUTILUS_SCRIPT_SELECTED_FILE_PATHS="/up1/BM1s/Ws
declare -x NAUTILUS_SCRIPT_SELECTED_URIS="file:///up1/BM1s/Ws
declare -x NAUTILUS_SCRIPT_WINDOW_GEOMETRY="1109x583+39+24"

	_______:  Nautilus-Actions :
-! after any changes in n-actions do quitting:  nautilus -q 
dpkg --listfiles nautilus-actions
/usr/bin/nautilus-actions-config-tool
/usr/share/doc/nautilus-actions/html/
##________________________________________  ___________________________


#####  ==========  xfe file manager:
- from Xfe-desktop
- bookmarks/configs-user in : ~/.config/xfe/xferc
