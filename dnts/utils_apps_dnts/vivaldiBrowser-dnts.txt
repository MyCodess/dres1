___________ vivaldi-browser-lx _____________________________
-!! all-protocols  same as chrome://
##________________________________________  ___________________________


#####  ==========  settings-misc:
- realpython/linkedin-stuff (their login-demand after a while!): they save files/flags/even-cookies as data in  "~/.config/vivaldi/Default/Local\ Storage/" !
	so just removing their cookies does NOT help! so to get rid of their login-Aufforderung or ... just either:
	rm -rf  "~/.config/vivaldi/Default/Local\ Storage/"   #/OR:
	chrome://settings/siteData   ##-!! JA, chrome://...  , NOT vivaldi://... !!    ##-and remove einzelne ...  ##/OR:
	there : set "Keep local data only until you quit your browser"  + whitelist ("Allow") sites where you need to keep persistent data.
	/OR:  use private-browsing for them ! 
- extensions/plugins from chrome-webstore, is missing "add/install" button, then: setting->privacy->google-extensions-> "Web Store" MUST be active/enabled! /_230115  ;
##________________________________________  ___________________________


#####  ==========  URLs-for-configs  /_190400 :
-!!  https://wiki.archlinux.de/title/Vivaldi#Browserinterne_Seiten_und_Funktionen
-!!  vivaldi://...   same-as  chrome://...
-!!  vivaldi://vivaldi-urls	  bzw.  chrome://chrome-urls    --> listing-all-internal-URLS of vivaldi !
vivaldi://about/   bzw.  help-->about menupoint
vivaldi://settings/   bzw.  chrome://settings/
vivaldi://settings/all/
vivaldi://settings/general/
vivaldi://settings/passwords/
vivaldi://gpu   Graphics Feature Hardware GPU infs ...

	_______:  
vivaldi://flags/   bzw.   chrome://flags/
Video/audio-autoplay-disabling:  vivaldi://flags/#autoplay-policy  --> Document needs user ...!

	_______:  configs-DIRs...:
- DIR:  vivaldi://about or menu > Help-->About  ,then:  directory listed under Profile Path, minus Default.
https://help.vivaldi.com/article/full-reset-of-vivaldi/#backup
~/.config/vivaldi/Default/
~/.config/vivaldi/Default/Bookmarks

	_______:  
https://wiki.archlinux.de/title/Vivaldi
##________________________________________  ___________________________


#####  ==========  DIRs-vivaldi:
/home/u1/.cache/vivaldi/
/home/u1/.config/vivaldi/
/home/u1/.config/vivaldi/Default
--
see Listing in Backup Vivaldi data in :   https://help.vivaldi.com/desktop/install-update/full-reset-of-vivaldi/  :
Here are some of the key elements stored under the Default folder ( /home/u1/.config/vivaldi/Default ):
Bookmarks 	 – contains bookmarks and information from Speed Dials.
Notes 	– notes taken in the Notes Panel.
Sessions 	–  saved tabs sessions.
Login Data 	– website passwords. Note: This file is encrypted and is only usable on the machine that created it.
Preferences  (in MsWin: Preferences and Local App Settings\mpognobbkildjkofajifpdfhcoklimli ) 	– Vivaldi settings and configuration.
Web Data 	– autofill data.
Current Session 	– data on open tabs.
History 	– website history.
Cookies 	– website data.
--########################### coll : ###########################################################
##________________________________________  ___________________________


#####  ==========  
ist of Vivaldi URLs
vivaldi://about
vivaldi://accessibility
vivaldi://appcache-internals
vivaldi://apps
vivaldi://blob-internals
vivaldi://bluetooth-internals
vivaldi://bookmarks
vivaldi://chrome
vivaldi://chrome-urls
vivaldi://components
vivaldi://crashes
vivaldi://credits
vivaldi://device-log
vivaldi://devices
vivaldi://dino
vivaldi://discards
vivaldi://download-internals
vivaldi://downloads
vivaldi://extensions
vivaldi://flags
vivaldi://gcm-internals
vivaldi://gpu
vivaldi://help
vivaldi://histograms
vivaldi://history
vivaldi://indexeddb-internals
vivaldi://inspect
vivaldi://interstitials
vivaldi://interventions-internals
vivaldi://invalidations
vivaldi://linux-proxy-config
vivaldi://local-state
vivaldi://media-engagement
vivaldi://media-internals
vivaldi://net-export
vivaldi://net-internals
vivaldi://network-error
vivaldi://network-errors
vivaldi://newtab
vivaldi://ntp-tiles-internals
vivaldi://omnibox
vivaldi://password-manager-internals
vivaldi://policy
vivaldi://predictors
vivaldi://print
vivaldi://process-internals
vivaldi://quota-internals
vivaldi://safe-browsing
vivaldi://sandbox
vivaldi://serviceworker-internals
vivaldi://settings
vivaldi://signin-internals
vivaldi://site-engagement
vivaldi://suggestions
vivaldi://supervised-user-internals
vivaldi://sync-internals
vivaldi://system
vivaldi://terms
vivaldi://thumbnails
vivaldi://tracing
vivaldi://translate-internals
vivaldi://usb-internals
vivaldi://user-actions
vivaldi://version
vivaldi://webrtc-internals
vivaldi://webrtc-logs
For Debug
The following pages are for debugging purposes only. Because they crash or hang the renderer, they're not linked directly; you can type them into the address bar if you need them.
vivaldi://badcastcrash/
vivaldi://inducebrowsercrashforrealz/
vivaldi://crash/
vivaldi://crashdump/
vivaldi://kill/
vivaldi://hang/
vivaldi://shorthang/
vivaldi://gpuclean/
vivaldi://gpucrash/
vivaldi://gpuhang/
vivaldi://memory-exhaust/
vivaldi://ppapiflashcrash/
vivaldi://ppapiflashhang/
vivaldi://quit/
vivaldi://restart/
##________________________________________  ___________________________


#####  ==========  
