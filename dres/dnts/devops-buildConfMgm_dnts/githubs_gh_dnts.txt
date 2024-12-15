_________________ "gh" / GItHub-CLI/-commandline dnts : ___________________________________

#####  ==========   Vocabs/DIFFs/Allg-nts/COncepts/...:
	-!! DIFF:   gh  <--->  git cmd !!   GitHub-CLI/gh is NOT the same as  git cmd ! so eg auth-Token of gh does NOT work for git cmd !!

	_______:  docs:
	https://cli.github.com/manual/  ,  https://cli.github.com  ,  https://docs.github.com/en/github-cli/github-cli/about-github-cli 
	- install-pkg:  pacman -S  github-cli

	_______:  helps:
	- man gh ; man gh-<tab> ; ... ; eg: man gh-auth ; ...
	- helps:  gh <CR> ; gh help ;  gh help <cmd> ; ... ; eg: gh help auth ; gh help environment ; ...
##________________________________________  ___________________________


#####  ==========   ENV-vars-gh:
	gh help environment
##________________________________________  ___________________________


#####  ==========   configs-gh:
	-! man pages are with "-" instead <space>, so eg: man gh-auth-login is for "gh auth login" !
	man gh-config gh-config-list  gh-config-set  gh-config-get ...
	~/.config/gh/config.yml
	gh config  list  ##-query/listing cu-configs
	gh config set editor vim         ##--man gh-config-set
##________________________________________  ___________________________


#####  ==========    login/auth : gh auth login :
	- gh help auth ;    man gh-auth  gh-auth-login   gh-auth-logout ...

	_______:  login :
	- man gh-auth-login :
	$ gh auth login       ## start interactive setup
	$ gh auth login --with-token < mytoken.txt       ## authenticate against github.com by reading the token from a file  /OR do: export GH_TOKEN=<token> ...
	$ gh auth login --hostname enterprise.internal   ## authenticate with a specific GitHub instance
	- gh auth status  ##-check-it

	_______:  token-login:
	-!! this works for gh-cmds , BUT NOT for git-cmds !! so OK for eg: gh auth status ; ... BUT not for:  git push   ##-to-remote-github-server !
        - for git-cmds must do additional git-auth-cmds... /OR edit manualyy the store-file (default:  ~/.git-credentials ! :
	man gh-auth-login ; gh help environment :
	create your authentication-token 1)either through web-login : profile->developer-settings  bzw.  https://github.com/settings/tokens  2) or gh auth login #without setting GH_TOKEN , and then export the token !
	export  GH_TOKEN=ghp_....  ##--!after setting the envVar, your login is already recognized! incl. useer-name+repos+...!
	/OR instead ENV :  gh auth login  --with-token  ##--see man gh-auth-login
	check-it:  gh auth status  #/OR   gh auth token  #Print the auth token gh is configured to use
	gh auth login    ##-- /OR if noenvVar, then:  gh auth login  --with-token
	/OR if no VAR, then save the created online-token to file and (reads-ONLY-from-StdInput !):    gh auth login --with-token  <<<"$GH_TOKEN"   ##--/OR:  < mytoken.txt

	_______:  ssh gh:
	man  gh-ssh-key ;
	gh ssh-key list
##________________________________________  ___________________________


#####  ==========   gh-shell / aliases / ...:
	aliases:  gh alias set	xxxx '.....' #eg:  gh alias set epicsBy 'issue list --author="$1" --label="epic"' ; gh epicsBy vilmibm  #=> gh issue list --author="vilmibm" --label="epic"
##________________________________________  ___________________________


#####  ==========   repo gh:
	man gh-repo  gh-repo-...
	- create:  man gh-repo-create ; gh repo create  -d "gh-created-repo11"  --private  repo11  ##--MUST specify --private/public/internal ! no defaults for that ! see man !
	- create from local-repo:   gh repo create --source ...
	- create interactively  :   gh repo create
	- clone to cu-loc-dir:      gh repo --clone  repo11  #/OR:  gh repo clone <repository> [<directory>]     ##--Clone the new repository to the current directory
	- gh repo list / delete / ...
##________________________________________  ___________________________


#####  ==========   pull-request gh / gh pr ... :
	man gh-pr gh-pr-...
##________________________________________  ___________________________


#####  ==========   GitHub-Actions gh:
	-! to use gh in GitHub Actions, add GH_TOKEN: ${{ github.token }} to "env". ##man gh-auth-login
	man  gh-run  gh-run-...
	man  gh-workflow
##________________________________________  ___________________________


#####  ==========   gist per gh:
	man  gh-gist gh-gist-<tab>
	gh gist create -d "bash-getopts-with-default-params-1"   /up1/w1/dc1k/dres/codecs1_dres/shs_UxLx_dres_1kk/bashs/getoptsdef3-uue.tpl.bash 
	gh gist list ; gist delete ecb60e2a22dd1dbac1fa674e9437e7e1 ; 
##________________________________________  ___________________________


#####  ==========   ########## 1coll-"gh"-CLI : #############################################################

	_______:  issues:
	gh issue create --title "My new issue" --body "Here are more details."
	gh issue create --title "My new issue" --body "Here are more details." --assignee @me,monalisa --label "bug,help wanted" --project onboarding --m

	_______:  
##################################################################################################
##________________________________________  ___________________________


#####  ==========   ########## trys_1coll/done ... ########################################################
##________________________________________  ___________________________


#####  ==========  /:230401 : cronjobs-drafts : pullRequest-from-remote/arx-with-gh_cmd , github-remote-cmd-pullreq-seq1 (for cronjob,...):

	_______:  > see gb1.sh !

	_______:  --- repo1 (pub)
-- stat:
expg  GH_TOK
cdlla  /up1/varu/varau/wks/gh1/repo1
[u1@2209arx repo1]$ gh repo list
[u1@2209arx repo1]$ git remote -vv
origin	https://github.com/MyCodess/repo1 (fetch)
origin	https://github.com/MyCodess/repo1 (push)
[u1@2209arx repo1]$ git status
On branch br1
nothing to commit, working tree clean
-- change+commit:
[u1@2209arx repo1]$ git switch br1
[u1@2209arx repo1]$ el1d  "br1-mod" >| f1_flg.txt 
[u1@2209arx repo1]$ git  commit -a -m "br1-commit--for-pr"
[u1@2209arx repo1]$ git push -v  ##-- [ --set-upstream origin br1 ]
-- pr:
[u1@2209arx repo1]$ gh  pr  create  --title  "gh_cmd-pr1--$($cudts2)"  --body "$($cudts2) : gh_cmd-pr-created on 2209arx for br1-merge-into-main"
[u1@2209arx repo1]$ gh  pr  merge -m br1

	_______:  --
-- if like: create+delete repoXX :
expg  GH_TOK
gh  repo  create  -d "gh-cmd-repo-created-$($cudts2)"  --public  repo61
gh  repo  delete  --yes   repo61
_____________________________________________________________________________

	_______:  ----------- pullReq-cmd on private-repo:  gb_act1 is private-repo (anscheinend sieht man dann nicht activities in pub !?)

	_______:  started in:
	expg  GH_TOK
	/up1/varu/varau/wks/gh1/gb-actions1/gb_act1
	origin	https://github.com/MyCodess/gb_act1 (fetch)
	origin	https://github.com/MyCodess/gb_act1 (push)
	[u1@2209arx gb_act1]$ git status
	On branch br1
	Your branch is up to date with 'origin/br1'.

	_______:  all acts:
declare -x GH_TOKEN="ghp_....!

	_______:  create a pull-req:
el1d "br1-for-pullReq-gh" >> flg1.txt
git commit -a    -m  "$($cudts2)-pullReq-2"
git push --verbose 
gh  pr  create --title "gh-pr-create-1"  --body "$($cudts2) : gh created pr from arx-cmd on br1"
gh  pr  list
gh  pr  merge -m    <pr-No.>
gh  pr  list

	_______:  create/delete repo12 :
gh  repo  create  -d "gh-cmd-repo-created-$($cudts2)"  --private  repo12
gh  repo  delete  --yes  repo12
##________________________________________  ___________________________


#####  ==========  gh CLI done /:230214  : 
OL-create-your-auth-token for mycodess
export  GH_TOKEN=ghp_....
gh auth status
gh auth login

	_______:  
gh repo clone https://github.com/MyCodess/py-dres1
##________________________________________  ___________________________

