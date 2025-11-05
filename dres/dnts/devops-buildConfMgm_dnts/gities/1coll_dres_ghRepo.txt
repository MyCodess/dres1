##__________________________ dres-gitting/GH __________________________________


#####  ==========  /:231001 :  GH-infs after creations:
https://github.com/MyCodess/dres

##-- Quick setup — if you’ve done this kind of thing before
https:// or ssh:  git@github.com:MyCodess/dres.git

##-- or create a new repository on the command line
echo "# dres" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:MyCodess/dres.git
git push -u origin main

##-- or push an existing repository from the command line
git remote add origin git@github.com:MyCodess/dres.git
git branch -M main
git push -u origin main
##--
##________________________________________  ___________________________


#####  ==========  /:231001 :  git-/GH-setup for dres:
[u1@2209arx dres_git]$ date; pwd
2023-10-01T20:25:54 CEST
/up1/mnt/VARUfs/varu/varau/wks/gits_w1/dres_git
##--
[u1@2209arx dres_git]$    export  GH_TOKEN='....'
[u1@2209arx dres_git]$ gh repo create -d "dres_dnts_w1"  --public  dres
Created repository MyCodess/dres on GitHub
##--
[u1@2209arx dres_git]$ git init  --initial-branch=main
Initialized empty Git repository in /up1/mnt/VARUfs/varu/varau/wks/gits_w1/dres_git/.git/
##--
[u1@2209arx dres_git]$ git add .
[u1@2209arx dres_git]$ git commit -a -m "initial-setup"
[u1@2209arx dres_git]$ git remote add origin git@github.com:MyCodess/dres.git
[u1@2209arx dres_git]$ git push -u origin main
##--
[u1@2209arx dres_git]$ git switch -c wk1
	 git add .
	 git commit -a -m "gits_GH_Repos_setups_dnts"
	 git status 
	 gh  pr  create  --title  "gits_GH_Repos_setups_dnts--$($cudts2)" --body "$($cudts2) : new dnts for gits_GH_Repos_setups"
	 gh pr merge wk1
##--
##________________________________________  ___________________________

