##________________________________________  ___________________________


#####  ==========  transfering this tpl for a new devnts-lang (eg java / J_):
cddevnts ; mkdir -p javas/j_wp ; cdlla javas
(cd /up1/w/docs_m/devres/0devNts/00_tpl_langs/ ; find -type f -iname "*xx_*") | sed -e 's/xx_/j_/g' | xargs touch
##________________________________________  ___________________________


#####  ==========  tpl generated by:
mkdir xx_wp
(cd /up1/w/docs_m/devres/0devNts/pl ; find -type f) | sed -e 's/pl_/xx_/g' | xargs touch