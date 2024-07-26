CommonMark  Markdown notes:
==============================================================================


#####  ==========  docs /nts /...:

	_______:  Refs:
	- https://commonmark.org/
	- https://spec.commonmark.org/
    - [try-it-online](https://spec.commonmark.org/dingus/)

	_______:  nts:
    - **abbreviations**:  **mdCm** == MarkDown-CommonMark-Variation , **mdGfm** == MarkDown-GitHub-Variation/GFM
	- CommonMark is the basic/subset of GitHub/GitLab/Reddit/Qt/StackOverflow/Swift/....-MarkDown-syntax !
	- GitHub-GFM-MD is so just a superset of CommonMark (GitHub-addies for links, references, ...)
##________________________________________  ___________________________

#####  ==========  setup /parser /cmds /...:

	_______:  Linux-setup:
    - pacman -Sy  cmark   ##--parser
    - man cmark (commonMark) , cmark-gfm (github-flavor-commonMark)
    - cmark      --to html  --hardbreaks  0-mdCm-CommonMark_dnts.md   >|  0-mdCm-CommonMark_dnts.md.html   ##--also  --safe  , but is default! (cmark-gfm ahs only --unsafe param !)
    - cmark-gfm  --to html  --hardbreaks  0-mdCm-CommonMark_dnts.md   >|  0-mdCm-CommonMark_dnts.md.html   ##--just to get sure that it is fine also with mdGFM !

	_______:  python-addies-mdCm :
    - pacman  -Ss commonmark  ;
    - pacman -Sy  python-commonmark ;
    - /usr/bin/cmark-py3 ...
    - /usr/lib/python3.10/site-packages/commonmark/tests/run_spec_tests.py
    - community/python-commonmark  :  Python parser for the CommonMark Markdown spec
    - doutils-addies:  python-myst-parser  , python-recommonmark , ...
    - html2text :  pacman  -Sy  community/python-html2text ; html2text --help ;
        - eg: html2text  --single-line-break  --ignore-emphasis --ignore-images  --dash-unordered-list  --asterisk-emphasis  --body-width 0  t1.html > t1.html.md
    - 

	_______:  vim addies:
    - vim highlights some underscores as error (disturbing, but correct)! to disable it:
      the line that defines it as error (vim90) is in: /usr/share/vim/vim90/syntax/markdown.vim , as: ```syn match markdownError "\w\@<=\w\@=" ```
      so copy this line into  (system:) /usr/share/vim/vimfiles/after/syntax/markdown.vim /OR (user:) ~/.vim/after/syntax/markdown.vim AND delete the underscore out of that there to overwrite the vim-defaults for markdown files ! 
##________________________________________  ___________________________



###  ##############################  1coll/... : ######################################################
#####  ==========  
##________________________________________  ___________________________



