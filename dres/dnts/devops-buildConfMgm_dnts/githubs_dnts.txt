________________ github_dnts : _______________________________________________
- /:230213  main-try-sta !
-!! abbrev. for GItHub == gb !! (NOT "gh" ! due to confusion with "gh"-CLI !! so "gh" is always "gh"-CLI )
-! for "gh"-CLI see extra dnts !

#####  ==========  !! DIFFs / DEFs :

	_______:  !! DIFFS :  git-cmdline (Linus)  <--->  GhitHub-CLI / gh  <--->  git-vom-GitHub
	- git /git-scm /git-cmdline vom Linus, so original git cmdline on Lx https://git-scm.com  ! here just refered as "git" /git-cmdline
	- "gh" CLI /  GhitHub-CLI  : cmd/CLI for using/communicating with GitHub-Servers/Repos 
	- git-GhitHub : GitHub is not using git 100 same; so eg user.name/... differes a bit or so ,...
##________________________________________  ___________________________


#####  ==========   URLs-Std:
	github.com/<owner>/<repository>/contribute  :  If you already know what project you want to work on, you can find beginner-friendly issues in that repository by visiting
	https://github.com/github/docs/stargazers  :  To view everyone who has starred a repository, add /stargazers to the end of the URL of a repository. For example, to view stargazers for the github/docs repository,...
##________________________________________  ___________________________


#####  ==========   GitHub-Usages:
	see: docs-gb:  Get started bzw. Get started/Using GitHub/

	_______:  keyboard-shortcuts :
	-! on any page just "?" brings keyboard-shortcuts-listing for that page ! see https://docs.github.com/en/get-started/using-github/keyboard-shortcuts
	-! listing-of shortcuts:   https://docs.github.com/en/get-started/using-github/keyboard-shortcuts

	_______:  GitHub Command Palette :
	https://docs.github.com/en/get-started/using-github/github-command-palette
	Ctrl+K on any ol-page! 

	_______:  Markdown editing: ---> see extra dnts in markups-dir !!
	[intro]<https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>
	[specs]<https://github.github.com/gfm/>
##________________________________________  ___________________________


#####  ==========   git/git-scm in github (so: org-cmdline-git from Linus using for github repos ... ):
	!!  https://docs.github.com/en/get-started/using-git
	https://docs.github.com/en/get-started/getting-started-with-git/
	- auth /git : The Git username is not the same as your GitHub username !
##________________________________________  ___________________________


#####  ==========   API-/REST-API-github:
	https://docs.github.com/en/rest
	-! curl / javascript API requests !
##________________________________________  ___________________________


#####  ==========   ########## cmds_miscs_1coll ... : #####################################################

	_______:  create NEW repo per cmd:
	see more methods (curl/api/gh/js/...) in:  https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-a-repository-for-the-authenticated-user
	-- per API/curl:
	curl -u  <username, eg mycodess>  https://api.github.com/user/repos -d '{"name":"repo11","private":false}'  ##--more-params in above link! as:
	curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer <YOUR-TOKEN>" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/user/repos -d '{"name":"Hello-World","description":"This is your first repo!","homepage":"https://github.com","private":false,"is_template":true}'
##________________________________________  ___________________________


####################  trys_1coll/done ... : #######################################################
#####  ==========  github--MyCodess-repo1-cmdlines-c&p : Quick setup /ssh-URLs :
- create a new repository on the command line
echo "# repo1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:MyCodess/repo1.git  ##--/OR:  https://github.com/MyCodess/repo1.git
git push -u origin main
- or push an existing repository from the command line
git remote add origin git@github.com:MyCodess/repo1.git
git branch -M main
git push -u origin main
- ...
##________________________________________  ___________________________

