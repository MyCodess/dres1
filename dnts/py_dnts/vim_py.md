_____________ python-vims: ______________________________
	-!!  https://realpython.com/vim-and-python-a-match-made-in-heaven/
##________________________________________  ___________________________


#####  ==========  VIM-pythons :

	- !!  https://realpython.com/vim-and-python-a-match-made-in-heaven/
	- check if your vim has python::    vim --version | grep -F '+python'  ##-must be with "+" , means mit-compiled! the prefix "-" means NOT-included !
	- check which py-version is used inside vim:    :python3 import sys; print(sys.version)  ##--python3 or python !
	- !!  :h python  --> if_pyth.txt  !!
	- vim-py-pligins:  vim-jedi (evv-now-default-/_230105) /OR SpaceVim /OR ...  googlen for: vim python introspection-based code completion /OR AutoCompletion ....
	- https://en.wikipedia.org/wiki/Intelligent_code_completion
##________________________________________  ___________________________


#####  ==========  vim-jedi plugin : ==================================================
	- vim-jedi : vim plugin for jedi, an awesome Python autocompletion ,  https://github.com/davidhalter/jedi-vim
	- :h  jedi  ,  :h jedi-vim.txt

	_______:  install vim-jedi plugin :
	- !! checkit first if vim-pkg is compiled with python-features enabled!? usu. yes):  vim --version | grep -F '+python'  #--> must see +python (so with python-features compiled!!) 
	- pacman -S  vim-jedi  ##-bzw.  pacman -Syu community/vim-jedi  --->  ##vim: :help jedi-vim<TAB> ##https://github.com/davidhalter/jedi-vim
	- /usr/share/vim/vimfiles/plugin/jedi.vim ...

	_______:  helps,docs,...:
	:h jedi / jedi-vim.txt   ##bzw. :help jedi-vim<TAB>   ##bzw.   vi /usr/share/vim/vimfiles/doc/jedi-vim.txt
	https://github.com/davidhalter/jedi-vim

	_______:  configs/settings for jedi:
	:h  jedi-vim-configuration , eg:
	deactivate popup-on-dot:  :let  g:jedi#popup_on_dot=0   ##--then you get popup-completion only with keys!   i_<C-x><C-o>  bzw.  Ctrl-Space>  !!
	doc-window NOT closing:   :let  g:jedi#auto_close_doc=0
	Not showing arguments-listings (eg by print disturbing):  :let  g:jedi#show_call_signatures=2  ##shows now in cmd-lines! if =0 then disabled!

	_______:  keys/keybindings/shorcuts for auto-completion-...
	- !!-see-Listing :   :h  jedi-vim-keybindings    bzw.   https://github.com/davidhalter/jedi-vim/blob/master/doc/jedi-vim.txt keybindings !
    - ! omni-completion-keys in insert-mode work all fine !

	--- nts-to-autocompletions in vim / intellisense-code :
    - !!-info-Vocabs:  "intellisense"-code-completion in IDEs  ==  "omni"-completion in vim  (intellisense-completion hat Patent-Schutz !! daher omni in vim !!)
	i_CTRL-N / i_CTRL-p : are ONLY simple "textuell-completion/string-based/NOT-code-API-based" completion (not code/API-completion)!  :find next/prev Completion/match for word in front of the cursor
	In V7, VIM introduced omni completion – given it is configured to recognize Python (if not, this feature is only a plugin away) Ctrl+x Ctrl+o opens a drop down dialog like any other IDE – even the whole Pydoc gets to be displayed in a split window.

    --- keys autocompletion/docs/... :
    - autocompletion in isert-mode:   i_C-Space / i_.  (typing a period in insert mode) / omni-defaults-of: ual <C-X><C-O> and <C-P>/<C-N>     ##??:  i_<TAB>     :  compl.-anything ?
	- show popup-suggetions/listing for under cursor in i_mode:  i_Ctrl-Space>  bzw.  i_<C-x><C-o>   (and then next/prev with i_CTRL-N / i_CTRL-p) : are omni completion keys in insert-mode  : to complete method/properties names (tags-files-based)
	- cancel popup-suggetions (pop-up-win weg! but stay in i-mode): i_<C-e>
	- The usual <C-X><C-O> (omni-/intellisense-compl.) and <C-P>/<C-N> keybindings work as well for next/prev auto-completion-suggestions !
    - pydoc-of-element-show :   "K"

	---  keys for motions/jumpings, more keybindings :
	-! jumpto-definition of under-curson:  g,  ##-jump-back (as always): ctrl-t
	<leader>d                      Go to definition (or assignment)
	<leader>g                      Go to assignment
	<K>                            Show pydoc documentation
	<leader>r                      Rename variables :ALL / refactoring !
	<leader>n                      Show usages of a name (in all your current files...)
	:Pyimport os                 open os.py

	---  Keys-remapping if needed, eg:
	- set the keybinding for starting omnicompletion to <C-N> instead of <Ctrl-Space>, add the following setting to your .vimrc file:  let g:jedi#completions_command = "<C-N>"
##________________________________________  ___________________________


#####  ==========  set / vim-options-settings / configs-hints in vim for py 

	_______:  PEP 8 adaptions for vim , https://realpython.com/vim-and-python-a-match-made-in-heaven/ :
	-!  To add the proper PEP 8 indentation, add the following to your .vimrc:
	au  BufNewFile,BufRead   *.py    set  tabstop=4 softtabstop=4 shiftwidth=4 textwidth=79 expandtab autoindent fileformat=unix foldmethod=indent  set foldlevel=99 encoding=utf-8
	let python_highlight_all=1 ; syntax on
	-
	for loading another filetypes you can add another au cmds as eg:  au BufNewFile,BufRead *.js, *.html, *.css   set tabstop=2 softtabstop=2 shiftwidth=2
	- PEP-8-recommended:  tabstop=4/8??  shiftwidth=4  softtabstop=4  expandtab    ##--(python-editors/convention: no TAB, only spaces for indents. BUT uue uses TABs)
	- 1kk/evv default:    tabstop=4      shiftwidth=4  softtabstop=4  noexpandtab  ##--(without jedi-vim)
	- 1kk is using jedi-vim which sets them all, but 1kk-default is::  tabstop=4 ! (and noexpandtab ?? but is NOT standard !!)
	- Flake8-vim plugin  : PEP-8-checker for vim+py  https://vimawesome.com/plugin/flake8-vim
	- see also:  https://wiki.python.org/moin/Vim
##________________________________________  ___________________________


#####  ==========  tags/tagging/.. for ins-completion  i_ctrl-x i_ctrl-], 0ct.2012-nts: 

	_______:  generating tags-files   (as in perl stuff, here py-prj is "prj2" which points to /up1/varu/varau/prjs/py1/):
	mkdircd  ${prj2TagsDP}/system_python2.7/   #so now: /up1/varu/varau/prjs/py1/etc/tagsdir/system_python2.7/
	ctags -R /usr/lib/python2.7/     ##-!- do NOT use the link ctags -R /usr/lib/python/  due to later newer releases; so you have correct pathes in the generated tags-file for this release anyway!
	in your-/user.after.vim.config.file /up1/.cuue/etc/vims/after/ftplugin/python.vim  (/OR manually in each python-vim-buffer):  setlocal  tags+=${prj2TagsDP}/**/tags,
	- done!   see details about tags in pl-vim.txt and in vims.txt
##________________________________________  ___________________________


#####  ==========  plugins more for vim+py :
	https://wiki.python.org/moin/Vim
	https://github.com/gmarik/Vundle.vim.git  ??
	- SpaceVim (not checked yet but looks comprehensive-IDE !? 2chk!! ?but more for NeoVim??) :  )https://spacevim.org/use-vim-as-a-python-ide/
	-! SimpylFold (folding-for-py):  correct folding for Python  ,  https://github.com/tmhedberg/SimpylFold
	- indentpython.vim  :  autoindent will help, but in some cases (like when a function signature spans multiple lines), it doesn’t always do what you want, especially when it comes to conforming to PEP 8 standards. To fix that, you can use the indentpython.vim extension:  https://github.com/vim-scripts/indentpython.vim
	- YouCompleteMe  auto-complete plugin (also using jedi) for many langs (Under the hood, YouCompleteMe uses a few different auto-completers, (including Jedi for Python): https://github.com/ycm-core/YouCompleteMe
	- Flake8-vim : PEP-8-checker (py-Linter) for vim+py  https://vimawesome.com/plugin/flake8-vim
	- File Browsing / Explorer in vim+py : NERDTree is a file system explorer for the Vim editor , https://github.com/preservim/nerdtree
	- Git integration into vim:  Fugitive is the premier Vim plugin for Git.  https://github.com/tpope/vim-fugitive
##________________________________________  ___________________________


#####  ==========  Virtualenv/env and vim-auto-completion:
	https://realpython.com/vim-and-python-a-match-made-in-heaven/ :
	VIM, by default, doesn’t know anything about virtualenv, so you have to make VIM and vim-plugins  aware of your virtualenv by adding the following lines of code to .vimrc:
    -----
    " python with virtualenv support
    py << EOF
    import os
    import sys
    if 'VIRTUAL_ENV' in os.environ:
      project_base_dir = os.environ['VIRTUAL_ENV']
      activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
      execfile(activate_this, dict(__file__=activate_this))
    EOF
    -----
##________________________________________  ___________________________

