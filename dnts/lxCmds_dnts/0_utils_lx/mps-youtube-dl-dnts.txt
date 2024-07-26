_________________________ youtube-dl-dnts.txt _______________________________________
##________________________________________  ___________________________


#####  ==========  update manually:
https://github.com/ytdl-org/youtube-dl/blob/master/README.md#how-do-i-update-youtube-dl
	whichll youtube-dl  ;##then:
	sudo wget https://yt-dl.org/latest/youtube-dl -O   /usr/bin/youtube-dl
	sudo chmod a+x    /usr/bin/youtube-dl
	hash -r
--########## audioOnly/MP3-DWs from YT-music /_181200+.... : #################################
-########################## coll/FAQ/....: ################################################
##________________________________________  ___________________________


#####  ==========  best only audio in mp3 convert:
If you want mp3, just tell youtube-dl that:
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=uWusmdmc0to
will get you an audio version (-x, short for --extract-audio) in or converted to mp3 (that's the --audio-format option). youtube-dl will automatically pick the best quality and most appropriate format.
https://stackoverflow.com/questions/49804874/dowload-the-best-quality-audio-file-with-youtube-dl
##________________________________________  ___________________________


#####  ==========  directly download audio from a YouTube video instead of first downloading audio+video with best audio quality:
https://stackoverflow.com/questions/49804874/dowload-the-best-quality-audio-file-with-youtube-dl
...
If you want ONLY mp3, just tell youtube-dl that:
youtube-dl -x --audio-format mp3 [--audio-quality 320k ] https://www.youtube.com/watch?v=uWusmdmc0to
will get you an audio version (-x, short for --extract-audio) in or converted to mp3 (that's the --audio-format option). youtube-dl will automatically pick the best quality and most appropriate format.
Note that the listed qualities are just guesses. In practice, opus is superior to anything else, but vorbis is picked for compatibility (refer to this related answer of mine for more details), so that will be picked.
While you can use -f to select a particular format, this is intended for people who want lower quality because of limited bandwidth or storage space, or for debugging. By default, youtube-dl already downloads the highest quality.
--
Thanks for your reply. I read on more sites that Opus is the best. But why does youtube-dl download the Vorbis file when I use: youtube-dl -f bestaudio youtube.com/watch?v=uWusmdmc0to ?? It's not the best one available. – jeroenws Apr 13 at 18:49
As laid out in the linked answer, that's because of compatibility concerns. If you can play/convert opus, you can pass in -f 'bestaudio[format="opus"]/bestaudio/best'. – phihag Apr 13 at 21:27
##________________________________________  ___________________________


#####  ==========  directly download audio from a YouTube video instead of first downloading audio+video and then extracting the audio? :
https://askubuntu.com/questions/423508/can-i-directly-download-audio-using-youtube-dl   
- Can I directly download audio from a YouTube video instead of first downloading audio+video and then extracting the audio?
if you already have the video link ...
Run, as example:
youtube-dl -F http://www.youtube.com/watch?v=HRIF4_WzU1w
This will list the various download formats available for this url (audio and video).
$ youtube-dl -F http://www.youtube.com/watch?v=HRIF4_WzU1w
[youtube] Setting language
[youtube] HRIF4_WzU1w: Downloading webpage
[youtube] HRIF4_WzU1w: Downloading video info webpage
[youtube] HRIF4_WzU1w: Extracting video information
[info] Available formats for HRIF4_WzU1w:
format code extension resolution  note
171         webm      audio only  DASH webm audio , audio@ 48k (worst)
140         m4a       audio only  DASH audio , audio@128k
160         mp4       192p        DASH video
133         mp4       240p        DASH video
134         mp4       360p        DASH video
135         mp4       480p        DASH video
17          3gp       176x144
36          3gp       320x240
5           flv       400x240
43          webm      640x360
18          mp4       640x360     (best)
Now, choose desired audio format. I went for 140
Run:
youtube-dl -f 140 http://www.youtube.com/watch?v=HRIF4_WzU1w
##________________________________________  ___________________________


#####  ==========  Download Audio from YouTube
https://gist.github.com/umidjons/8a15ba3813039626553929458e3ad1fc
# Download single entry
youtube-dl -i --extract-audio --audio-format mp3 --audio-quality 0 YT_URL
# Download playlist
youtube-dl -ict --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 https://www.youtube.com/playlist?list=UUCvVpbYRgYjMN7mG7qQN0Pg
# Download playlist, --download-archive downloaded.txt add successfully downloaded files into downloaded.txt
youtube-dl --download-archive downloaded.txt --no-overwrites -ict --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --socket-timeout 5 https://www.youtube.com/playlist?list=UUCvVpbYRgYjMN7mG7qQN0Pg
# Retry until success, no -i option
while ! youtube-dl --download-archive downloaded.txt --no-overwrites -ct --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --socket-timeout 5 <YT_PlayList_URL>; do echo DISCONNECTED; sleep 5; done
##________________________________________  ___________________________


#####  ==========  Download only the mp3 audio track from youtube video  :
https://www.slashgeek.net/2016/06/24/5-youtube-dl-tips-might-not-know/
...
Sometimes you don’t really care about downloading the whole video, you only want the audio and it can be easily done using youtube-dl without having to download the video first and then extract the audio from it. As seen from the output of previous --list-format command youtube stores audio and video formats separately, so youtube-dl just downloads the audio file, usually in m4a or webm format and then converts it into mp3. Using this command: youtube-dl --extract-audio --audio-format mp3 video-url. You will need ffmpeg or avconv for this to work since the audio needs to be converted to your preferred mp3 format.
youtube-dl --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=9D05ej8u-gU
 9D05ej8u-gU: Downloading webpage
 9D05ej8u-gU: Downloading video info webpage
 9D05ej8u-gU: Extracting video information
 9D05ej8u-gU: Downloading MPD manifest
[download] Destination: The Most Astounding Fact - Neil deGrasse Tyson-9D05ej8u-gU.webm
[download] 100% of 2.93MiB in 00:02
[ffmpeg] Destination: The Most Astounding Fact - Neil deGrasse Tyson-9D05ej8u-gU.mp3
Deleting original file The Most Astounding Fact - Neil deGrasse Tyson-9D05ej8u-gU.webm (pass -k to keep)
If you don’t care about converting audio to mp3 format and want to keep the original format. You can download the specific audio format using the format code shown before.
##________________________________________  ___________________________


#####  ==========  
