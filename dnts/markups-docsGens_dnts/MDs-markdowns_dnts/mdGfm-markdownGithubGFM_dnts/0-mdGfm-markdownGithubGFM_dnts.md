________________________ GitHub Flavored Markdown /GFM / mdGfm _______________________


#####  ==========  docs/nts/vocabs:
	_______:  refs/specs/intros:
    - !! [intro](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
    - !! [specs](https://github.github.com/gfm/)
    - <https://github.com/phseiff/github-flavored-markdown-to-html>
    - <https://en.wikipedia.org/wiki/Markdown#GitHub_Flavored_Markdown>

	_______:  vocabs/nts:
    - "GitHub Flavored Markdown" == GFM == mdGfm /in-evv
    - ! GFM is based on CommonMark, so github-addies make it an upperset of CommonMark!
______________________________________________________________________________


#####  ==========  setup-loc-Lx +cmds for  gh_md_to_html  :
	_______:  packages-install on Lx:
    - ! GFM is based on CommonMark  (so github-addies make it an upperset of CommonMark!) , so to parse them just install either CommonMark-md-parser /OR GitHub-md-parser:
    - pacman -Sy  cmark-gfm  ##--/OR cmark  for CommonMark-org, without GItHub-addies !
    - pip3 install gh-md-to-html   ##--bzw:  python3 -m pip install gh-md-to-html
    - optionals:  python3 -m pip install gh-md-to-html[pdf_export]  ,  python3 -m pip install gh-md-to-html[offline_conversion]
    - see <https://github.com/phseiff/github-flavored-markdown-to-html>  :

	_______:  cmds eg on Lx:
    - cmark-gfm   -t html gh1.md  >| gh1.md.html     ##--/OR with --unsafe for parsing HTML-tags !  ##--see man  cmark-gfm    
______________________________________________________________________________


#####  ==========  
______________________________________________________________________________


#####  ==========  
______________________________________________________________________________

