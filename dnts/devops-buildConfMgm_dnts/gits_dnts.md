_______________ git_dnts ___________________________________________________


############################  dnts-gits:  ########################################################
#####  ==========  docs/helps/refs/...:

	_______:  REFs-docs/Tuts/BKs...:
	- !! RefBK1 == Pro Git , Scott Chacon, Ben Straub , Version 2.1.359-2-g27002dd, 2022-10-03 , ebook-official-dw:   https://git-scm.com/book/ ;
	- !! https://www.git-tower.com/learn/git/faq  , https://www.git-tower.com/learn/git/ebook
	- REF:  https://git-scm.com/doc
	- git on GitHub.com : https://docs.github.com/en/get-started/using-git/about-git
	- man  gittutorial / ...
	- chat-forum:    Libera Chat IRC server:  https://libera.chat/ and try the #git, #github, or #gitlab channels !

	_______:  help-cmds:
	- !  TAB-completing works hervorragend! so use it! even parts-completion,... !!
	- !  DIFF  help/-h : git help xxx == git xxx help == man git-xxx == git -h xxx   <--->   git xxx -h (summary/shorter/ more concise help !)
    - !  git help help
    - !  short/quick helps/params-listings:   git xxx -h    ##--NOT: git -h xxx ! this one long-help/manpage !
	helps-cmds-forms:  git help <verb>  ;  git <verb> --help ;  man git-<verb> ;     ##--eg:  git help config ;  git config -h/--help ;  man git-config ;
	git help <verb>   /OR   git  <verb> --help     ## eg:  git help config   /bzw.  git  config  --help
	git  <verb> -h  ##--shorter-help
    git help  -a|--all      ##--Prints all the available commands
    git help  -g|--guides   ##--Prints a list of the Git concept guides

	_______:  man(-help)-pages:
	- !! TAB-completing works hervorragend! so use it! even parts-completion,... !!
	- !! man giteveryday !!
	man git-<verb>   ## man git-config
	man git / gittutorial / ...
    man git-help / man git help

    _______:  tuts/dres/QRefs/cheats-docs ...:
    git help tutorial / tutorial-2
    git help --guides / -g
    !!  https://www.geeksforgeeks.org/git-tutorial/
    https://www.geeksforgeeks.org/ultimate-guide-git-github/    :  An Ultimate Guide to Git and Github , Quick-Refs-Basics
    https://www.geeksforgeeks.org/list-useful-github-commands/  :  qcky-usu.-cmds
    https://www.geeksforgeeks.org/essential-git-commands/       :  qcky-usu.-cmds-listing

##________________________________________  ___________________________


#####  ==========  Vocabs/DIFFs/Concepts/Allg-Basic-nts ... :

	_______:  Vocabs: areas/parts of GITs-world :
	workTree   <-->   stage/index/cache  <-->  loc-repo/HEAD   <-->   remote-repo
    1- workTree / working-area      :  your local directory where you make the project (write code) and make changes to it !
	2- staging/index/cached_area    :  pre-commit-cached-area between your workTree-and-locRepo ! the next commit will write staged-files into locRepo!
    3- locRepo      :  your local repository where you commit changes to the project before pushing them to the central repository on Github.
    4- remoteRepo   :  remote-Repo, main project on the central/common/remote-server !
    --- more descps:
    - index-area:
        reflects worktree status at latest "git add" cmd! :
        The "index" holds a snapshot of the content of the working tree (1kk: at latest "add" status), and it is this snapshot that is taken as the contents of the next commit.  Thus after making any changes to the working tree, and before running the commit command, you must use the add command to add any new or modified files to the index.  see man git-add
        Git Index may be defined as the staging area between the workspace and the repository. The major use of Git Index is to set up and combine all changes together before you commit them to your local repository.


	_______:  Vocabs...:
	master/main/trunk/devel  :  RF-branch / REF-default-development-branch (can be assigned any other names!)
	origin 	:  default remote-/upstream-repo
	HEAD 	:
        see: https://www.geeksforgeeks.org/git-head/  :
        git show HEAD ;
        The most recent commit to the current checkout branch is indicated by the HEAD ! This means HEAD is just like a pointer that keeps track of the latest commit in your current branch !
        The “current branch” can be thought of as the HEAD. The HEAD is moved to the new branch when you use the “checkout” command to swap branches.
        so: pointer to the current branch bzw. your latest local commit / cu-snapshot-repo / it is a pointer to the local branch (your local latest commit) you’re currently on !
	HEAD^ 	:  parent of HEAD / of current branch pointer
	HEAD~3 	:  parent-parent-parent of HEAD / of current branch pointer
	--
##________________________________________  ___________________________


#####  ==========  concepts/workflow/proces/routes , Gitflow, Workflow :

	_______:  full-routes
	worktree 	<---> 	stage 	<---> 	locRepo 	<---> 	remote-repo
	- Up-Richtung  ---> :  worktree 	---add/rm--->   stage 	---commit---> 	locRepo 	---push---> 	remote-repo     ##--upwards/commit/push-route
    - UnDo-Richtung     :  worktree 	<---reset--- 	stage 	<---restore--- 	locRepo 	<------     	remote-repo     ##--undo/restore-route
	- DW-Richtung  <--- :  worktree 	<---checkout---	stage 	<---checkout HEAD--- 	locRepo 	<---pull/clone/fetch--- 	remote-repo ##--downwards/checkout/pull-route
    git help workflows

	_______:  undos-part-routes/more/... :
	worktree  <--- "checkout -f"   ---  stage/index
	worktree  <---  stage/index  <-- "checkout HEAD" --- LocRepo
	worktree  <--- "reset filex" ---  stage/index
	worktree  <--- "restore --staged --worktree" ---  locRepo
	worktree  <--- "reset  --hard  HEAD [file] " ---  locRepo
	stage     <--- "restore --staged" ---  locRepo

	_______:  steps/procedure/levels of gitting:
	steps-usu:  1-clone the orogin from remote-repo   2-modify/add/rm files in your loc-workTree  3-stage them for next commit (git add/rm/...) 4-commit to local-repo (git commit)  5-sync/push your loc-repo to/with remote/origin-repo!
    git help workflows     ##- An overview of recommended workflows with Git
##________________________________________  ___________________________


#####  ==========  setup/start a new git-repo/prj:

    _______:  test-cases:
    - !! for testings you can also just do:    git clone <file-path-of-any-locRepo, as its remoteRepo>  ##--so remoteRepo can be a localDirRepo ! and need NOT to be on GitHub/remote/... !

	_______:  
	- git  init [--bare]  #/OR    git clone <remote-repo>
	- ssh user@server git init --bare mysite ##--create new bare git-repo on the remote server !

	_______:  init :
	- converting your current not-gitted Dir into a git-repo, see man git-init :  cd dir1; git init ; git add . ; git commit ;   ##--of-course setting also user.name + user.email

	_______:  clone :
	- clone a repo:  git clone <path/URL>
##________________________________________  ___________________________


#####  ==========  Repos:

	_______:  bare / non-bare Repos:
    - !! https://www.geeksforgeeks.org/bare-repositories-in-git/ :
	- git init/clone  [--bare]
    --- non-bare Repos  (eg your cloned locRepo) :  
        1- default is non-bare (your locRepo usu.)  
        2- has .git-folder  3- has worktree there, after you checkout/clone/pull/... !
        3- "push" NOT allowed to a non-bare-repo by git-defaults! see below !
        - non-bare repos are ones usu. used for your working, so checkout/edit/commit/... there !
    --- bare Repos (eg remote/central repos, GitHub-repos) :
        1- non-default, only-server, remote Repos
        2- has NO worktree and NO .git DIRs, but ONLy the .git-tree-contets in its root-Dir !
        3- no working-are there possible ! only push/pulls/... !
        4-  no commits can be made in a bare repository. The changes made in projects cannot be tracked by a bare repository as it doesn’t have a working tree.
        5- The only possible operations on the Bare Repository are Pushing or Cloning. 
        6- "push" is allowed only to a bare-repo by default !
        - WHY bare-repos?:  Remote/Central Repositories use bare repositories only because git doesn’t allow you to push to a non-bare repository as the working tree will become inconsistent.
        - bare repo is a server-ONLY-gitRepo (as GitHub, or prj-central-repo-server): no working there, so no checkouts/worktree/edits/....; basically ONLY as server for push/pull/clone ....!
        - remote-repos are generally a bare repository (eg GitHub) : a Git repository that has no working directory (NO snapshot checked out on disk). It is just the Git data. In the simplest terms, a bare repository is the contents of your project’s .git directory and nothing else.
    --- relations:    bare <---> non-bare   , relations/converting/cloning/... :
        - a bare repo can be cloned into a non-bare one (git clone) and is what rund-um-die-Uhr-passiert with GitHub-repos !
        - also a non-bare repo can be cloned into a bare one with:  git clone --bare
        - a bare repo hast got no checked-out-snapshots/-worktree ....! has only .git-tree-contents with snapshots-hists,...
        - A bare repository is linked with a local repository, hence the files in .git of local repo should match with the files in the bare repo.
        - "git clone ..."  usu. converts the remote bare-repo into your local working nonbare-repo !
    --- "push" to a non-bare-repo (eg your localRepos) : NOT-good! NOT-allowed by default:
        "push" is ONLY allowed to a bare-Repo as git-default (so eg to GItHub-Repo) !! since the non-bare-worktree will become inconsistent/oerwriten ! see below !
        so By default, push/updating a branch in a non-bare repository is denied, because it will make the index and worktree inconsistent !
        if you still want to be able to push into a non-bare repo (so braking git-defaults ! NOT a goot idea; then the worktree there can get be un-synced then!!), then on the remote no-bare repo must set:
        git config --global receive.denyCurrentBranch updateInstead  ##--so in this case, the remote worktree will be also updated by any push ! (so not getting out-of-sync!)
        and then after push you have to do in your non-bare-repo: git reset –hard  ##--but anyay dumm sowas ! so keep the default and do NOT do that!
##________________________________________  ___________________________


#####  ==========  configs:

	git help config  (bzw. man git-config)  +  https://git-scm.com/docs/git-config   +  RefBK1---Customizing Git--p.335

	_______:  configsFiles-overwriting-order :
    ---  1 < 2 < 3 < 4  :
	1- OS/System-settings    / --system  :     [prefix]/etc/gitconfig  bzw. mswin:  <GIT-installPath>/etc/gitconfig     ##-- git config  --system 
	2- User-Global-Settings: / --global  :  ~/.gitconfig   bzw.   ~/.config/git/config  ##-- all user global-settings  "git config --global ..." go there !
	3- Repo-Local-Settings   /  --local  :  <repo-dir>/.git/config    ##-- all user non-global-settings  "git config  ..."  go there !  git config  --local  #-overwrites all others !
	4- cmdLine-configs-params   per cmd  :  eg,   git config  user.name   "gt-u2"
    git config  --system / --global / --local / --worktree / --file ...

	_______:  query-configs / show-configs :
	- !!  git config --list  --show-origin      ##--show-all-cu-configs-(and-their-files) ! if several entries for the same key (from diff config-files), then the LAST one is taken by git!
	- git config  [--show-origin]  user.name   ##--show only user.name-EFFEKTIV-value ;  so:  git config  [--show-origin]  <key>
    - git config  user.email / core.bare / ...
	-listing-all-cu-configs (must be in Repo-Dir!):  git config --list  ##--bzw. all in:  .git/config + ~/.gitconfig  + /etc/gitconfig  ...

	_______:  most-common-configs (without --global then for the current gitRepo/Dir !):
	git config  --global core.editor vim
	git config  --global diff.tool gvimdiff
	git config  user.name   "gt-u2"
	git config  user.email  "gt-u2@2209arx"
	git config  remote.origin.url=/up1/varu/varau/wks/gt1/grepo3
	-- 0more / RefBK1---Customizing : -------------------
	git config --global commit.template ~/.gitCommitMsg1.txt  ##--prj-commit-template, eg for commit-Vorgaben/styles/Hinweise/...
	git config --global core.pager ''         ##--no-paging, so not-using "less"
	git config --global core.excludesfile ~/.gitignore_global  ##--globaly for all my prjs/repos ignore thies files (instead per Repo in .gitignore)
	git config --global color.ui false/true    ##--turn off colors in terminal! colors:  normal, black, red, green, yellow, blue, magenta, cyan, or white
	git config --global color.branch , color.diff , color.interactive , color.status ##--eg:  git config --global color.diff.meta "blue black bold"
	git config --global core.whitespace ...   ##--whitespace-handlings
	--- MsWin-Lx-Configs, CRLF / LF :  see   RefBK1---Customizing Git--p.342 :
	git config --global core.autocrlf true    ##--if your worktree on MsWindows machine, set it to true — this converts LF endings into CRLF when you check out code: auto-converting CRLF line endings into LF when you add a file to the index, and vice versa when it checks out code onto your filesystem
	git config --global core.autocrlf input   ##--if your worktree on Lx : convert CRLF to LF on commit but not the other way around by setting core.autocrlf to input:
	git config --global core.autocrlf false   ##--if your team working ONLY-on-MsWindows !
##________________________________________  ___________________________


#####  ==========  status + log + history :

	_______:  status
	- short-summary-status:   git status -S

	_______:  log (viewing commit history,...):
	- !! git log doesn’t show all the branches all the time ! git log will only show commit history below the branch you’ve checked out ! see RefBK1-p68 !
	- show ALL commits:   git log --all   ##--by default, git log will only show commit history interesting for you, so below the branch-pointer you’ve checked out.
	- remote-log-show:  git log   origin/master  ##--bzw.  git log  <remoterepo-name>/<remote-branch-name>
	- git log <certain branch>  ##--To show commit history for the desired branch you have to explicitly specify it:
	- git  log  -p -1  ##-- bzw. --patch  : shows diffs/patches between commits; here with -1 only for latest commit!
	- git log --stat  ##--shows some abbreviated stats for each commit
	- git log --pretty=oneline  ## prints each commit on a single line
	- customized/own-log-output (reports) with: --pretty=format ##as in:  git log --pretty=format:"%h - %an, %ar : %s"
	- git log --since=2.weeks
	- git shortlog

	_______:  misc history...:
	- "rewrite commit history" (--amend / rebase / ...): !NOT-good! Avoid!:  history is "rewritten" whenever existing commits are manipulated through eg: rebase / amending-commits/...: commits will receive new SHA-1 hashes, making them completely new commit objects from Git's perspective ! every changes of commits-hashes is a BAD-style and problems for others who are based/branched based on this hash!!
	- user-name-changing of earlier commits:  git commit --amend --author="John Doe <john@doe.org>"
##________________________________________  ___________________________


#####  ==========  commmits/staging(add,rm)/worktree/changing/modifying/versioning/...:

	- ! every commit -> creates a snapshot!  Every time you perform a commit, you’re recording a snapshot of your project that you can revert to or compare to later !
	- ! check always the cmds outputs for helps: in (...) notes are great TIPs for problems/next-steps/... !
	- staging with: git  add/rm/...

    _______:  worktree-gitFileyTypes:
    - Untracked: In this stage, the Git repository is unable to track the file, which means that the file is never staged nor it is committed.
    - Tracked: When the Git repository tracks a file, which means the file is committed but is not staged in the working directory.
    - Staged: In this stage, the file is ready to be committed and is placed in the staging area waiting for the next commit.
    - Modified/Dirty: When the changes are made to the file i.e. the file is modified but the change is not yet staged/commited.
    --
    - After the changes are done in the working area, the user can either update these changes in the GIT repository or revert the changes.

	_______:  "git add" :  puts/stages  worktree-changes  to the index(stage)/locRepo :
	- ! "add" is NOT only add-files, but: git add is a multipurpose command:  tracking new files, to stage files, and ...; think of it more as “add precisely this content to the next commit” rather than “add this file to the project”.  /RefBK1--progit.pdf
    - ! NOT use  "git add *"  ,sinde * is then interpreted by the shell and NOT by git ! and then strange results!! then:
    - !  DIFF:  git add *.txt (NOT-use!)  <--->  git add “*.txt”   ##--:so:  *.txt is shell-extension: add all text files of the current directory to staging area  <--->   “*.txt” is git-expansion: add text files of entire project (recursiely-tree) to staging area !
    - ! git add -A / -all [dir1]  (?is it default for get add . ??) : 
        this will stage all the changes, all the modified, deleted, new, renamed, created, ... files, in the entire working tree.
        this puts a snapshot of the current worktree status into the index for the next commit, INCL. modified/added/deleted/renamed/... files! so basically ANY changes in the WHOLE worktree (not only the current dir, if nor dir1-arg specified!)
        == is same as "git add . ; git add -u" IF you are in the prj-rootDir! git add . stages only the changes in the current directory and not it’s parent directory.
    - git add -u /-–update :  It add all the modified and deleted files but not any untracked/new files and it does this for the entire tree.

	_______:  commits, "git commit ..." :
	- commit of not-staged-files : "commit -a ..." (umgehen von staging with add/rm/...) :  git commit -a -m "...."
	- history- of last 2 commits:  git log -2  [-p]  ##-- and -p for details/diffs !

	_______:  files renaming/moving/deleting/ ...:
	- ! renaming: do it with: git mv f1  f1-new !! otherwise has git no history about the file and is considered as: deleted file + added new file ! 
	- ! deleting a file from branch for next commit: rm f1; git rm -r --cached . ; git add . ;  git commit -m "Clean up ignored files" ;
	- ! git rm f1  ##--delete f1 from workTree+staging and stage its removal for next commit !
	- ! git rm --cached f1  ##--delete f1 only from staging area !

	_______:  stash :
	- stash : temporary saving of worktree changes without commiting (eg: before a pull or switch-to-new-topic-branch, ...)
	- git stash  [ --include-untracked ... ]  ##--saving (unfinished) works/changes, whithout doing commit (because not finished yet ...) !
	- opposite of stash local changes is :   git reset --hard   ##--which throws away the local changes (eg before a pull,...)
	- continue from latest stash point: git siwitch <branch-stashed) ; git  stash  pop ;
    git stash        ##--To move staged files to stash area which are present in staging area.
    git stash pop    ##--To get back the files which are present in stash area.
    git stash clear  ##--To clear the stash folder.

	_______:  clean-ups:
	- git-clean - Remove untracked files from the working tree
	- git clean -fd  ##-- !-carfull! !

	_______:  miscs-commits:
	- cherry-pick (Notfall / not-good!) / integrate selected, individual commits from any branch into your current HEAD branch: git cherry-pick af02e0b  [ --no-commit ]
##________________________________________  ___________________________


#####  ==========  undos /restore / go-back,rewind / ...:

	_______:  see + nts:
	- !! https://www.git-tower.com/learn/git/faq/
	- !! overwriting/discarding local uncommitted worktree changes and untracked files can NOT be undone !!

	_______:  DIFFs-undo-cmds:     restore <-->  Reset  <-->  revert :
	See "Reset, restore and revert" in git(1) for the differences between the three commands. (in man git) :
	here their main-funcs as default (but with additional params each can do more; eg restore --staged ...):
	-- nts:
	- grob:   restore : worktree-undos  <-->  reset : commit-undos  <-->  revert : remote+... undos :
	- git restore :  is newer than reset cmd and yet experimental! so, may be changed!  man git-restore  
	- reset <--> revert : for UNcommits:  git revert will make sure that a new commit is created to revert the effects of that unwanted merge. This is in contrast to git reset, where we effectively "remove" a commit from the history. That's also the reason why git revert is a better solution in cases where you've already pushed to a remote.
	- reset overlaps a bit with others !
	- also consider:  -amend param of commit , and also rebase concepts !
	--
	- git restore :  undo-workTree-edits /UNedit     : restoring files in the working tree from either the index or locRepo or another commit/locRepo.
	- git-reset   :  undo-branch(-commits)/UNcommit  :  updating your branch
	- git reset   :  undo-stage  /UNstage            : can also be used to restore the index (overlapping funcs with git restore)
	- git revert  :  undo-commits /UNcommits (+remote) : revert a commit, by producing a new commit with contrary changes, so back to the previous commit ! making a new commit that reverts the changes made by other commits

	_______:  restore : undo-files-in-workTree :
	- git restore             ##--restore from Stage --> workTree    ##--opposite-of  git add !!
	- git restore --staged    ##--restore from locRepo --> Stage    ##--opposite-of  git commit !!
	- git restore --staged --worktree   ##--restore from locRepo --> Stage --> workTree

	_______:  reset:
	git reset  --hard  HEAD         ##-- LocRepo --> workTree (overwrite modifications in workTree with locRepo-file ! discard all cahnges in worktree and overwrite them with locRep-latest-snapshot !
	git reset  --hard  HEAD <file>  ##-- LocRepo --> workTree (overwrite modifications in workTree with locRepo-file !
	git reset  [commit-ID]          ##-- Undo all commits after [commit], preserving changes locally (in workTree)! deletes ALL commit after that commit-ID (but revert is safer)
	git reset  --hard [commit-ID]   ##-- undo & Discards all history and changes back to the specified commit
	git reset  --keep <commit-ID>   ##-- undo & Discards all history and changes back to the specified commit AND preserve uncommited worktree/local changes !

	_______:  revert:
	Using the revert command doesn't delete any commits. Quite the contrary: it creates a new revision that reverts the effects of a specified commit:
	git revert    <commit-ID>       ##--reverting that commit and creating new one!
	git checkout <commit-ID>        ##--view/read-only of that commit !
	- undo a commit that has already been pushed to a shared branch on a remote repository : git revert ... ##--bad-idea-always: git push --force ... !

	_______:  UNstaging (restore / reset / HEAD):
	- UNstaging (cancel previuos add): git restore  --staged <file> /OR reset  /OR git reset HEAD <file> : rueckgaengig machen, so vom nächsten commit rausnehmen! vom cache/index-area entfernen !
	- git restore  : also un-delete files, undo files, ...; also after checkout to get the target branch into the workingDir !
	- undo changes of fileX in workTree : git restore  ##-same as:    git checkout -- fileX
	git reset  HEAD <file>    ##-- undo staging of the file that was added in the staging area ;so: LocRepo --> stage (UNstaging / cancel previuos add / abgleichen)
    git checkout <file>       ##-- LocRepo --> worktree : Blow away all changes since the last commit of the file#
    git reset –soft HEAD^     ##-- undo last commit and bring file to staging area
    git reset –soft HEAD^^    ##-- undo last two commits and bring file to staging area
    git reset –hard HEAD^     ##-- undo last commit and remove file from the staging area as well(In case we went horribly wrong).

	_______:  commits-amend/modifying :
	- ! see: https://www.git-tower.com/learn/git/faq/delete-commits ,  https://www.git-tower.com/learn/git/faq
	git commit --amend ... ;
	- !! use "--amend" ONLY whenever you want to change / edit your very LAST and UNPUSHED/not-pushed commit.
	- Amend only works with the very LAST/previous commit.
	- Amend rewrites the commit history in your repository: the old commit is replaced by a completely new one (a new and different commit object). This makes it very important that you don't amend (= rewrite) commits that you've already published to a remote repository! Because in that case, your colleagues might have already based their work on this commit - which you would try to replace using "amend".
	rebase concepts ...
	git reset --soft/--hard  HEAD~1/commid-id  ##--eg:  git reset --hard 0ad5a7a6

	_______:  back to ...
	- back to an earlier commit /OK: git checkout -b old-project-state 0ad5a7a6  ; ##--not modifying hists/logs ...! only checkout old-status into a new branch! NOT touching or even removing any other commits or branches.
	- back to an earlier commit /??: git reset --hard 0ad5a7a6      ##--This will rewind your HEAD branch to the specified version. All commits that came after this version are effectively undone; your project is exactly as it was at that point in time.
	- back to an earlier commit  /?: git reset --soft 0ad5a7a6      ##--Git will keep all the changes in those "undone" commits as local modifications:

	_______:  merge-undos:
	- ! undo-a-merge bzw. goback to pre-merge:  git reset --hard <commitID-before-merge> ###--bzw. if newly merge-point, then:  git reset --hard HEAD~1
	- ! undo-a-pushed/remote-merge:  git revert -m 1 <merge-commit-hash>

    _______:  buggy-commit-seaching:
    git bisect  --help
    - git binary search to find the commit that introduced a bug, by asking "BAD commit" + "latest still good commit" ...

	_______:  misc-undos:
	- UNdelete-branch : !?!?: git reflog ... ##-if deletion hasn't been too long ago , ...then Using that commit's SHA-1 hash, you are then able to recreate the branch, maybe!
	- UNdelete-a-file :  https://www.git-tower.com/learn/git/faq/restoring-deleted-files :
	- UNdelete-a-file of current branch (file-delete-not-commited yet):  git checkout HEAD <filename>
	- UNdelete-a-file of current branch (file-delete-commited already, but NOT-pushed! ):  git reset --hard HEAD~1  ##-- !! the command will discard changes to tracked files after the specified commit !
##________________________________________  ___________________________


#####  ==========  diffs/compares :

	_______:  compares/diffs between ... :
	- git diff             ##-diff of  workTree  <-->  stage/index:   
	- git diff  --cached   ##-diff of  stage    <-->  locRepo:   
	- git diff  --HEAD     ##-diff of  workTree  <-->  locRepo:   
	- git  diff  <commit_id1>   <commit_id2>
	- remoteRepo  <--> locRepo :  git branch -a ; git fetch origin/master ; git diff origin/master  master   ##--instead master can be any branch, as: orgin/br2 my-br ;

	_______:  diff/compare changed files ... :
	!! git diff : as default shows diff between working-tree <---> staged ones (so NOT commited ones!!) ! so if you have staged all changes (eg with git add), then no output is shown by git diff !!
	if wanted diffs between already staged <---> local-repo/commited, then use:  git diff --staged [bzw. --cached ; are synonyms]  ! so:
	If you want to see what you’ve staged that will go into your next commit, you can use git diff --staged. This command compares your staged changes to your last commit:

	_______:  difftool :
	git  difftool  --tool=gvimdiff
	git  difftool  --tool-help  ##-- to see what is available on your system
##________________________________________  ___________________________


#####  ==========  branching : merging/checkout/query/diffs-branchs/... locally :

	- !! It’s important to note that when you switch branches in Git, files in your working directory will change. !!
	- !! branching is extremely cheap! ONLY the SHA-1-code will be copied (as the branch pointer to a snapsho)! so only 40 chars copy !! branching is ONLY a pointer to a snapshot !!

	_______:  nts-creating/switching a branch:
	- !! if conflicts by switching branches, then git will NOT switch! so will not change your workTree !
	- !! Switching to a branch will CHANGE your workTree-files (git switch /OR checkout) !!your workTree will overwritten with the snapshot of the target branch (if not new, .c)!
	--  switching into a branch (checkout/switch/branch) does two things:
	1- It moves the HEAD pointer to that branch
	2- fetches/revertes the files in your working directory back to the snapshot that the branch points to.
	3- If Git cannot do it cleanly, it will not let you switch at all !

	_______:  "Tracking Branches" / “Upstream Branch" with :
	- ! see https://www.git-tower.com/learn/git/faq/track-remote-upstream-branch
	- "Tracking" binds/connects/assocciates a local-branch to a remote-branch, as counterparts for each other :
	In theory, local and remote branches in Git are completely separate items. In practice, however, in makes lots of sense to see them as counterparts - connected in a so-called "tracking connection".
	you can do all thing also without Tracking, but Tracking makes remotes-cmds (pull/push/diff/...) just easier, otherwise have to specify params for remote-cmds !
	when you tell a local branch to "track" a remote branch, you create a connection between these two branches. Your local branch now has a "counterpart" on the remote server.
	Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks is called an “upstream branch”).
	Tracking branches are local branches that have a direct relationship to a remote branch. If you’re on a tracking branch and type git pull, Git automatically knows which server to fetch from and which branch to merge in. RefBK1-p.92 + man git-checkout !
	- -u  ==  --set-upstream  ,as cmds-params to identify upstream for tracking! eg git push -u /OR git branch -u ; ...
	- git push -u origin  br1  ##--first-time publishing/pushin of loc-branch br1 into the remote-repo! tracking is now set by -u !!
	- git checkout -b <branch> <remote>/<branch>  ==  git checkout --track origin/serverfix == git checkout -b <branch> --track <remote>/<branch>  : ##--with these cmds sets git the tracking-connection between local-->remote-branch !
	- git checkout --track  <remote>/<branch>    ##--crate a new branch based on remote/branch and track it as upstream !
	- git branch -u origin/br1 ##-- br1 was already on remote, but forgotten setting tracking. so now can add tracking to your local-branch br1 !
	- auto-trackings: git clone/checkout/... automatically set the upstream-tracking-branch für the locBranch ! you can later modify/change it !
	- +renaming the tracking-branch:  git checkout -b sf origin/serverfix
	- re-tracking / changing the tracking branch:   git branch  --set-upstream-to origin/serverfix
	- shortcuts for upstream-trackings @{upstream} or @{u}, eg:   git merge @{u}  ==  git merge origin/master
	- query/show the tracking-branches:   git branch -vv

	_______:  creating/switching/checkingOut-branch-cmds (git checkout -v / switch -c ):
	- see:  https://www.git-tower.com/learn/git/faq/create-branch  :
	- create-only a new branch:  git branch br1 : does NOT switch to br1 !! it ONLY creates it! checkit with git branch/status/log (git log --oneline --decorate) and see it where the HEAD refers to! HEAD points to the current branch !
	- create-only a new branch based on base-branchX:  git branch <new-branch> <base-branchX>
	- create-only a new branch based on certain-commit/-tag:  git branch <new-branch>  <commitID/tagID>
	- create-only a new branch from a remote branch: git branch --track <new-branch>   <remote-repo>/<base-branch>  ##-/OR:  git checkout --track  <remote-repo>/<base-branch>
	- create-only a new branch on remote-repo /bzw. push/publish your new local-branch into remote-repo (not-having that branch):  git push -u origin <local-branch>   ##-- !! so use git-push ,not git-branch ...!
	- switcht to an existing branch (updates workTree):  git switch <branch-name>  #/OR:  git  checkout <branch-tag/commit-hash/ ...>
	- creating + switching to a new branch:   git checkout -b  <new-branch-name>  #/OR:  git switch -c new-branch
	   checkout -b  == git branch + checkout  ;   git switch -c  ==  git branch + switch
	- return to your previously checked out branch: git switch  -
	- checkout-remote-branch:  git checkout --track origin/br1

	_______:  show/query-branch-infs:
	- "HEAD ->" points to your cu-branch !
	- git branch -vv  ##--shows-details, BUT all relative to the latest fetch/pull-status (so locRepo)! not accessing the remoteRepo !! see RefBK1--p.94 !
	- shows-details-compared-to-remoteRepo:  git fetch --all ; git branch -vv ;
	- history of commits of a certain branch:    git log <certain branch>  
	- git log --oneline --decorate  ##-- git log --oneline --decorate --graph --all

	_______:  diffs-branches & re-windings/undos ...:
	git diff  br1  br2   ##--  git diff  master  origin/master
	git reset commit-xxx  ; git restore .  ##--rewind/go-back to certain commit (delte newer ones) AND then restore the current workTree to it !

	_______:  merge-branches (syncs), modify, :
	git  merge  master  ##--Combines master into the current branch. This is usually done in pull requests ...
	aborting/cancel/undo-started-merge-try : git merge --abort ; 
	GUI:  git  mergetool ##--settiing of merge.tool ... ##-- tools:  https://www.git-tower.com/learn/git/ebook/en/command-line/tools-services/diff-merge-tools#start

	_______:  merge-conflicts-solving:
	- ! steps-merge-conflicts:  1-solve-conflict (see below) ; 1-mark it as solved with: git add <filepath>  ; 3- git commit ...; ##--see https://www.git-tower.com/learn/git/faq/solve-merge-conflicts
	- slove-conflict-with-canceling-merge:   aborting/cancel/undo-started-merge-try : git merge --abort ; 
	- slove-conflict-with-ours/theirs:   git checkout  --ours/--theirs  path/to/conflict-file.css ; git commit ... ;
	- slove-conflict-with-edit-file-manually (so mixed of -ours/theirs): edit+save file; git commit ...
	- ! undo-a-merge bzw. goback to pre-merge:  git reset --hard <commitID-before-merge> ###--bzw. if newly merge-point, then:  git reset --hard HEAD~1
	- ! undo-a-pushed/remote-merge:  git revert -m 1 <merge-commit-hash>

	_______:  tags / tagging of release,...:
	- checkout tagX:  git checkout v2.0
	- create-branch-based on tagX:  git checkout -b new-branch v2.0
	- git  tag  xxx  ##--release-tag,...

	_______:  rebase :
	- ! DIFF rebase <--> merge ! : https://www.git-tower.com/learn/git/faq/rebase
	- ! Therefore, please never rebase PUBLISHED/pushed/remote-public commits!
    - git rebase  :  Three tasks are performed by git rebase 
        1. Move all changes to master which are not in origin/master to a temporary area.
        2. Run all origin master commits.
        3. Run all commits in the temporary area on top of our master one at a time, so it avoids merge commits.
	- step:  be on the target/receiving branch (usu. master /main) and merge/rebase the topic-branch into it, as: git switch master;  git rebase br1 ; ##--so, goes br1-changes into the master-branch !

	_______:  deleting-branch:
	- git branch -d br1  ##--delete br1 branch; all must be clean/committed/merged !
	- git branch -D br1  ##--delete br1 branch, force, even if not-committed/merged-stuff ... (just throw it away !)
	- remoteRepo-branch-delete:   git push  <remoteRepo> --delete <remote-branch-name>  ##eg:  git push origin --delete br22

	_______:  renamings/modifyings-branch-infs:
	- renamaing :  git branch --move  cuName  newName ;  git push --set-upstream origin  newName ; ##-- !! the newNam-branch has no remoteRepo assigned! so you have to set it, if pushing to remote !
##________________________________________  ___________________________


#####  ==========  remote-syncs: clone/pull/merge/push/sync-remote-repos :

	_______:  nts-remotes:
	- !! master & remote-master (origin/master) are two different branches. each is just a normal branch! but you can keep them synced! however they are finally just two differen/independent branches !
    - !! for testings you can also just do:    git clone <file-path-of-any-locRepo, as its remoteRepo>  ##--so remoteRepo can be a localDirRepo ! and need NOT to be on GitHub/remote/... !

	_______:  infs-querys / manage remote:
	git remote show ;  git remote -v ; ...
	git remote add  <alias/name>  <url1> ;
	git remote remove/rename  <alias/name>  ;
	git ls-remote ;

	_______:  sync-nts (sync with remote : fetch/pull/push/... ) :
	- ! DIFF-syncy-cmds:  fetch  <--> pull  <--> merge:
	- ! git  fetch : remoteRepo --> locRepo (NOT-checkedout! NO-worktree-update !), so fetch down any changes from remote repository to local repository
	- ! git merge :  ONLY-loc-branches merging ! NO-remoteRepo-syncs at all !! is for loc-repo     --> loc-workTree !
	- ! git pull  == fetch + merge (so remoteRepo-->locRepo-->workTree !) ; prefere git fetch+merge than pull !

	_______:  fetch :
	- !! git fetch ... : updates-locRepo-from-remoteRepo--BUT-NOT-worktree/cu-branch/HEAD !! use fetch + git merge to update the remoteBranch into your cu-branch ! :
	    It’s important to note that when you do a fetch that brings down new remote-tracking branches, you don’t automatically have local, editable copies of them.
	    In other words, in this case, you do NOT have a new loc-branch checkedout in your worktree — BUT you have only an origin/br1 pointer that you can’t modify/checkout/ ... .  /RefBK1-p.92
	- update/sync your localRepo with the remoteRepo (NOT-worktree !):  git fetch <remote> ##-:  fetches any data from remoteRepo that you don’t yet have, and updates your local database, moving your origin/master pointer to its new, more up-to-date position
	- git fetch   	:  remote-repo  --> loc-repo (NOT-workTree! so NOT-merge !)  - !! fetch does NOT update files in workTree !! brings ONLY the latest status of remote-repo into loc-repo ! so  ONLY updates your local-repo! but NOT merging/updating with your working-Dir!! for that use pull !!
	- git fetch br1 : get only branch br1 from remote-repo into the locRepo (NOT-workTree! no merge!)
	- git fetch -a 	##-fetch everything from the remote, so when you check difference,
	- ! fetch-remote + update-worktree: use fetch + merge : git fetch origin/br1 ; git merge  origin/br1  ;

	_______:  pull:
	- git pull  [remote-repo-name]  [remote-branch-name]   ##--eg:  git pull origin master ; #-if "tracking"-conf of the cu-branch/HEAD already defined, then enough: git pull ;
	- git pull  == git fetch + merge-into-CUrrent-branch/HEAD/WorkTree #so: fetch-from-remote-the-branch + merge-into-workTree  ##--so: remote-repo  --> loc-repo --> loc-workTree-merging ! automatically fetch and then merge that remote branch into your current branch /workTree !
	- pull generally fetches data from the [remote-]server you originally cloned from and automatically tries to merge it into the code you’re currently workingtree/cu-branch/HEAD !
	- ! pull-target/destination of the integration, however, is independent of a tracking connection and is always the same: your local HEAD branch and, thereby, your working copy / your cu-branch !
	- pull + overwrite my local changes:  see https://www.git-tower.com/learn/git/faq/git-force-pull

	_______:  push :
    - !! always first pull contents from the remote repo before pushing so that you are updated with other team members’ work
    - !! "git push ..." is NOT-only remote-upload/sync, but is a general-cmd for all-remote-mgm (eg, deleting a remote branch,...)
	- git push [ -u REMOTE-NAME BRANCH-NAME ]  :  locRepo --> remoteRepo  ##--BUT it does NOT addd tracking-conf to the loc-br! (so for the next push, again you have to specify all!) #better always  with -u /adding-tracking-conf for later pushes! 
	- push branch + renaming on remote (not-good-idea!) :  git push -u origin  loc-br-name:remote-br-name  ##--with -u also setting the br-tracking for later pushes !
	- push-new-loc-Branch-to-remote:  git push -u remote-repo-name   loc-br-name  ##-git push -u origin br12 ;
	- set/config remote-target for a local branch:   git push --set-upstream origin corrected-branch-name
	- renaming-remote-branch-pushed:   git push REMOTE-NAME LOCAL-BRANCH-NAME:REMOTE-BRANCH-NAME
	- delete a remote branch or tag :  git push REMOTE-NAME:BRANCH-NAME  bzw.  git push --delete origin br1   ##--strange-syntax, but it says: push nothing into BRANCH-NAME on REMOTE-NAME. Because of this, git push deletes the branch on the remote repository.
    - delete a remote tag:  git push --delete origin v5.5.5
    - see also:  https://www.geeksforgeeks.org/pushing-changes-to-a-git-repository/

	_______:  branch-remote  <--> local-branch :
	- ! local and remote branches actually have NOTHING to do with each other (except just tracking, if configured!). They are completely separate objects in Git. so, deleting one would NOT delete the other (even if tracking established ...)!
	- ! listing of ALL branches loc+remote+trackings+...:   git branch -vva
	-  listing of loc/remote branches:  git branch -v [-r]  ##--remote-branches-listing with -r
	- ! deleting a remote branch (on the remote-server): NOT git-branch BUT git-push!:   git  push  <remoteRepo/origin> --delete  <remote-branch-name> ##-eg: git  push  origin  -d  b23  ##-- !! the "git branch -r ..." ONLY deltes the remote-branch in your locRepo!! not on the remote-server!!
	- git checkout -b br11 origin/br11  ##-- Branch br11 set up to track remote branch br11 from origin.  Switched to a new branch 'br11'
	This gives you a local branch that you can work on that starts where origin/serverfix is. RefBK1-p.92
##________________________________________  ___________________________


#####  ==========  ignore:

	https://github.com/github/gitignore
    https://www.geeksforgeeks.org/what-is-git-ignore-and-how-to-use-it
	man gitignore

    _______:  Vorlagen-for-all-langs.... of .gitignore:   https://github.com/github/gitignore :
    - !! https://github.com/github/gitignore
    - Python.gitignore   :  https://github.com/github/gitignore/blob/main/Python.gitignore
    - ArchLinuxPackages.gitignore  :  https://github.com/github/gitignore/blob/main/ArchLinuxPackages.gitignore

    _______:  sytax/regex:
    - comments "#" , pathSep "/" ,
    - ignore-ALL-ext1 (recursive) "*.ext1" ,
    - **/any_name:  It is used to match any file or directory with the name any_name
    - any_name/**:  It is used to match anything that is inside the directory of the name any_name. for example webdev/** matches all the files inside webdev directory.
##________________________________________  ___________________________


#####  ==========  credentials / authentications / logins /security :

	_______:  see:
	- ! see RefBK1--p.329-- Credential Storage  : saving/caching credentials !
	- ! man  git-credential  git-credential-cache  git-credential-store ...
	- ! alternatives:  cache | store | Git Credential Manager  ##--eg: git config --global credential.helper cache ; /OR git config --global credential.helper 'store --file ~/.my-credentials'

	_______:  store:
	git config --global credential.helper store   ##--stores them in ~/.git-credentials   #/OR with own file:  git config --global credential.helper 'store --file ~/.my-credentials'
##________________________________________  ___________________________


#####  ==========  Utils/... : ===================================================
	
    - gitweb  ; man gitweb
##________________________________________  ___________________________


#####  ==========  add-ons/APIs/Plugins/... ======================================

	_______:  -- python-git:
	- ! Dulwich  , https://www.dulwich.io/ , see RefBK1--Dulwich--p.480
##________________________________________  ___________________________


#####  ==========  shell/bash and git:

    _______:  bash-propmpt setting to show the current active git branch + full-path (caould add into ~/.bashrc , but then non-git-dirs not-beatiful!):
    parse_git_branch() { git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/' ; } ; export -f parse_git_branch ;
    export PS1="\u@\h \[\e[32m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "
    - see https://thucnc.medium.com/how-to-show-current-git-branch-with-colors-in-bash-prompt-380d05a24745
    - colors for PS1 fonts:  We use this sequence \[\e[32m\] to set the color of the text goes after that sequence, until another color is set. In this sequence, \[ and \] are used to mark the start and end of non-printing characters. Between them, \e denotes an ASCII escape character, and follows by [32m, which is the actual color code. see  https://misc.flogisoft.com/bash/tip_colors_and_formatting
##________________________________________  ___________________________


#################  trys git all: ####################################################################################
#####  ==========  try-GItHub-with-"git"-cmds-/:230321  :

    cdlla  /up1/varu/varau/tests/gh1
    git config [ --global ] credential.helper store   ##--/OR with own file:  git config [ --global ] credential.helper 'store --file ~/.my-credentials'
    git clone  https://github.com/MyCodess/py-dres1
    git config user.name "gt_loc1"
    git config user.email  "gt_loc1@2209arx.l1nw"
    echo "##---- $($cudts2) remote-edit-1 --------"   >| py_dres_1kk/t1.py
    #if needed :  git add .
    git  commit -a  -m "$($cudts2)--remote-edit1"
    git push
##________________________________________  ___________________________


#####  ==========  try-/:230311 1coll  :  based on man giteveryday /INDIVIDUAL DEVELOPER (PARTICIPANT)  :

    cdte ;
    git clone  /up1/varu/varau/wks/gt1/grepo1  gt-tt4
    cdlla /up1/mnt/VARUfs/varu/varau/tests/gt-tt4
    git config user.name "gt-u4"
    git config user.email  "gt-u4@2209arx"
    git switch  -c  br1  master
    [u1@2209arx gt-tt4]$ el1d "__br1__add1" >> py_dres/f1.flg.txt 
    [u1@2209arx gt-tt4]$ git commit -a -s -m "br1-edit1"
    git format-patch  master
    view 0001-br1-edit1.patch
    --in-origin:
    [u1@2209arx grepo1]$ el1d "origin_master__add1" >> py_dres/f3.flg.txt
    [u1@2209arx grepo1]$ git commit -a -s -m "origin-edit1"
    --
##________________________________________  ___________________________


#####  ==========  try-/:230305  :

    2023-03-05T16:16:59 CET
    [u1@2209arx wks]$ mkdircd gt1
    /up1/mnt/VARUfs/varu/varau/wks/gt1
    git init "grepo1"
    cdlla grepo1  ##--  /up1/varu/varau/wks/gt1/grepo1
    git config --list  ##--bzw.   cat  .git/config
    cp -a /up1/w1/dc1k/dres/codecs1_dres/py_dres*   .
    [u1@2209arx grepo1]$ git config user.name "gt-u1"
    [u1@2209arx grepo1]$ git config user.email  "gt-u1@2209arx"
    git commit  --dry-run
    git commit -m "init1-commit1"
    ##--- clone loc try: (open a fully new terminal):
    cdte ;  git clone /up1/varu/varau/wks/gt1/grepo1   gt-te1  ##--repo-clone now in /up1/varu/varau/tests/gt-te1
    [u1@2209arx gt-te1]$  git config user.name   "gt-u2"
    [u1@2209arx gt-te1]$  git config user.email  "gt-u2@2209arx"
    touch  py_dres/f2.txt ; git commit  -v ;
    git  status ;
    git  add  *  ;  gitt commit  -v -m "u2-commit-1" ;
    git  status ;
##________________________________________  ___________________________


#####  ==========  try-/:220326 , wpad-gits1 /:220326 :

	_______:  1cu-nts:
	- Read-BM:  ProGit.pdf--Branching-chapter

	_______:  DIRs...-cu1/wk1 :
	/up1/w1/dc1k/dres/dnts/buildsCfgMgm/gits_dnts.txt
	/up1/prjs/gt1/tests

	_______:  try1-
	--- globs /u1 :
	git config --global user.name "u1loc"
	git config --global user.email "u1@localhost"
	# query them:   git config --list  --show-origin
	--- gd1 :
	mkdircd  /up1/prjs/gt1/tests/d1_gt ;
	git init    ;
	git branch -m br1 ;  ##--current-branch-named-to br1
	git add .   ;
	git commit  -m "initial-branch-1--br1" ;
	--- gd2 : yt-dlp :
	[u1@2004arx 0gits1]$  mkdircd  /up1/prjs/gt1/tests/d2_gt
	[u1@2004arx /d2_gt]$  git  clone  https://github.com/yt-dlp/yt-dlp
##________________________________________  ___________________________


#########################################################################################################

#################  1coll-gits-all : #################################################################################
#####  ==========  steps-usu (github-docs): https://docs.github.com/en/get-started/using-git/about-git :

    # see also:   git help workflows
    # download a repository on GitHub to our machine
    # Replace `owner/repo` with the owner and name of the repository to clone
    git clone https://github.com/owner/repo.git
    # change into the `repo` directory
    cd repo
    # create a new branch to store any new changes
    git branch my-branch
    # switch to that branch (line of development)
    git checkout my-branch
    # make changes, for example, edit `file1.md` and `file2.md` using the text editor
    # stage the changed files
    git add file1.md file2.md
    # take a snapshot of the staging area (anything that's been added)
    git commit -m "my snapshot"
    # push changes to github
    git push --set-upstream origin my-branch
##________________________________________  ___________________________



#####  ==========  github-default-cmds-drafts/-suggestions after creating a new empty repo:
    --- create a new repository on the command line
    echo "# prv1" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin git@github.com:MyCodess/prv1.git
    git push -u origin main
    --- …or push an existing repository from the command line
    git remote add origin git@github.com:MyCodess/prv1.git
    git branch -M main
    git push -u origin main
    --- or ...
##________________________________________  ___________________________

