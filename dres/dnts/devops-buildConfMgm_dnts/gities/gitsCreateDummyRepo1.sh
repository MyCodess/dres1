#!/bin/bash -i
set -aue
# - generates/setup a new local dummy git-repo + some branches+commits !

repoName11=${1:?"usage11: ... <new-repo-name>"}

#####  ==========  create dummy git repo1  /:250329 :
# --- shell /cd :
export GIT_CONFIG_SYSTEM=""   GIT_CONFIG_GLOBAL=""    ##--use ONLY local-conf in .git/conf !
RDP11="${vaarAuWorksDP}/gt1"
gitrepopath11="${RDP11}/${repoName11}"
cd ${RDP11} || (echo "==##==ERROR: could not do:  cd ${RDP11}"  &&  exit 3)

# --- init repo:
git init  "${repoName11}"
cdla  "${repoName11}"
# -I:  cat .git/config  #- git config -l
git config user.name "gt-u11"
git config user.email  "gt-u11@loc1"

#--- master-init-commit:
el1d >> f1.txt
git add .
git commit -m "init1-commit1"
git branch -vva

#-------- add few branches based on master and add a few commits for hist: ---
for nn in 1 2; do     #--ad-branches
	git switch -c br${nn}  #-create+switch to br1 based on master!
	for xx in a b c; do    #--add-commits to the branch
		el1d >>  b${nn}${xx}.txt
		git add . ; git commit -m "b${nn}${xx}.txt-commit"
	done
	git log --oneline --decorate --graph --pretty   --date=iso-local
	git switch - #-> back to master
done

#--- infs/status:
#__  set -x
git config -l
git branch -vva
pwd
#__  set +x
echo; echo "----- new repo in:  ${gitrepopath11}  ---------------------------"
echo "do NOT forget to set this in your terminal to work only locally and be able to igonre not readable global git-conf-file:"
echo "cdla ${gitrepopath11} ; export GIT_CONFIG_SYSTEM=""   GIT_CONFIG_GLOBAL="" ; setGitPrompt ;"
echo '-----------------------------------------------------------------------'

