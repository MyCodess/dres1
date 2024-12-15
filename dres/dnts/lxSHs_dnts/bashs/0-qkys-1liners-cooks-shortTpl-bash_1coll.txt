__________ bash: quickies,colls,cookies,... __________
exit 3
-!! see also /up1/w/docs_m/devres/bins_coll_devres for collected-org-ones/WPs/full-scripts/Muster/...
-!! see also Bash_QRef_Ore_0607.pdf
##________________________________________  ___________________________


#####  ==========  seq-of-numbers-printing-LOOPs :
	for (( ii=0 ; ii < 10 ; ii++ )); do echo $ii ; done
	for (( ii=10 ; ii ; ii-- )) ; do echo $ii ; done
	for ii in $(seq 1 5) ; do echo "$ii" ; done   ##reuires seq !  man seq
	ii=0;    while (( ii++ < 10)); do echo $ii; done
	-!! 2-digits-seq (prefix-0  if ii < 10) :
	for (( ii=1 ; ii < 15 ; ii++ )); do if (( $ii<10 )) ; then echo "0${ii}"; else echo "${ii}"; fi ; done
##________________________________________  ___________________________


#####  ==========  Loops: for/while/until/... also with arithmetics:

	_______:  for-arithmetic-loop:  see: help for
	for (( ii=0 ; ii < 10 ; ii++ )); do echo $ii ; done
	for (( initialisation ; ending condition ; increment/decrement/update )); do  statements...; done
	which is Equivalent to: (( EXP1 ));  while (( EXP2 )); do COMMANDS ; (( EXP3 )) ; done
##________________________________________  ___________________________


#####  ==========  testFiles-generate-quickies ... , dummy vars/files/...: ########
	- dummy text file:    for ((ii=101; ii<110 ; ii++ )); do echo -e "$ii\t $(($ii+30))\t $(($ii+50))"; done>> f1.txt
	- dummy array-bash:   for ((ii=0 ; ii<5 ; ii++)); do ar1[$ii]="$ii$ii" ; done ;  echo ${ar1[*]} ; echo ${#ar1[@]} ; ...
##________________________________________  ___________________________


#####  ==========  case modifications of VARs (small / capital letters conversions):
    - see man bash /"Case modification. "
    - convert-whole-VAR-value-all-to-capital-letter with ^ ,eg:  echo ${vaarAuDP^^}
    - convert ONLY all "u" letters to capital letter:  echo ${vaarAuDP^^u}
    - convert ONLY the first letter, if is is "a" : v11=ab/cd/ef ; echo ${v11^a}
##________________________________________  ___________________________


