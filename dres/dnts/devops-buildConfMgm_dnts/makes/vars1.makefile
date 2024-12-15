##-- descp1:  variables setting/referencing/usage in makefiles !! see make.pdf : 6 How to Use Variables ! bzw.  info make "using variables" !
##-- see manual/info for four types of makefile-VARs-setting/referencing, whereas the differ in their expanding/Auflösung ...!
##--
##-- USAGE1:  make  -f  <myname>  all1  [v1=XXXX ...]
##
##----------- dnts:
#- ! erst werden ALLE vars in makefile ausgewertet/expanded (egal wo sie definiert sind), und erst danach wird der make-target/recipes ausgeführt !! check here values of LIST1 v1 !
#- ! DIFF :  make-VARs  <--->   shell-/bash-vars ! see eg below!
#- ! recursive-assignments (eg: v5 = "$v5 abc" ) are NOT allowed for "=" ! but ok for "::=" !
##----------- ----------------------------

LIST1 ::= aa bb cc
v1 = 111
v2 = dynamic-v2 ${v1} ${LIST1}                ##--I: 6.2.1 Recursively Expanded Variable Assignment with simply "="  : its references are expanded later whenever this variable is substituted/used in runtime!
v3 ::= doublePoint_static-v3 ${v1} ${LIST1}  ##--I: 6.2.2 Simply Expanded Variable Assignment with ‘:=’ or-posix: ‘::=’ : its value is expanded/aufgelöst ONLY here !
v1 = 333
v3 ::= doublePoint_static-v3-redefined ${v1} ${LIST1}  ##--I: 6.2.2 Simply Expanded Variable Assignment with ‘:=’ or-posix: ‘::=’ : its value is expanded/aufgelöst ONLY here !

.PHONY : all1  varsSettings1  varsToShell1  varsMore1  shellEnvVars1

all1 : varsSettings1  varsToShell1  varsMore1  shellEnvVars1

varsSettings1  :
	@echo;
	@echo '========== varsSettings1 : DIFF setting VARs with = , ::=/:=  =========='
	@echo "__value_of_LIST1:  ${LIST1}"
	@echo "__value_of_v1:  ${v1}"
	@echo "__value_of_v2:  ${v2}"
	@echo "__value_of_v3:  ${v3}"

varsToShell1  :
	@echo;
	@echo '========== DIFF: shell-vars-using  <--->  gmake-vars-using :  =========='
	@echo '-- DIFF :  make-VARs, referencing with "$"  <--->   shell-/bash-vars (eg in recipes), so referecnsing with "$$" --'
	@for i in ${LIST1}; do echo  "${v1} : $${i}" ; done

varsMore1  :  target1var1 := target-specific-var1
varsM%  shell% :  pattVar1 := pattern-specific-var1  ##--defined var ONLY in matching regex targets !
varsMore1  :
	@echo;
	@echo '========== varsMore1 ====================================='
	@echo "substitution in var-values, here replace hh by XX:  ${LIST1:hh=XX}"
	@echo "computed var-names : ${a}"
	@echo "var set by a shell-call : ${varShell1}"
	@echo "var  append values with += OP : ${varAppend1}"
	@echo "target-specific-var:  ${target1var1}"
	@echo "pattern-specific-var  :  ${pattVar1}"
	@echo "MAKE-builtin-vars  :  ${MAKEFILE_LIST} ${.DEFAULT_GOAL} ${MAKE_TERMOUT} ${.RECIPEPREFIX} ${.VARIABLES} ${} ${}"
	##__All-VARs-listing:  @echo "listing-of-all-global-vars-incl-shellEnvVars+MakeGlobalVars (not-target-specific/private/...): ${.VARIABLES}"

vaarAuTmpDP ::= overridden-shellVar1  ##--I-try calling make with+without "-e" and see diff!  with -e this overwriting of shell-var has NO effect !
prjTmpDP ?= check-shellVar1-if-set    ##--if already in shell set, then this has NO effect now with ?=...  !
shellEnvVars1  :
	@echo;
	@echo '========== shellEnvVars1 are  accessible in make and can be overwritten : =================='  ##--see make.pdf 6.10 Variables from the Environment
	@echo "Shell-EnvVars are all accessible in make, eg:  ${q_syysTg}"   ##--all shell-envVars are accessible , but can be overwritten by make-vars with same-name !
	@echo "Shell-EnvVars can be overwritten/overridden in make, eg:  ${vaarAuTmpDP}"
	@echo "Shell-EnvVars can be checked if set by ?= ... , eg:  ${prjTmpDP}"
	@echo "target-specific-var NOT accessible in other targets! :  ${target1var1}"
	@echo "pattern-specific-var  :  ${pattVar1}"

v1 = 123
v1 ?= new11  ##--has no effects, since v1 is already defined !!
LIST1 ::= hh jj kk

##--------------------- more/advanced-vars-settings .... : ----------------------------------
##-- computed var-names:
x=y
y=zzz
a := $($(x))
##--value from shell:
varShell1 != ls .  ##--executes a shell cmd and return its value !
varAppend1 :=  "${v1}"
varAppend1 +=  added1  ##--same as varAppend1 := $varAppend1 added1
##--I:  undefine vars as:   undefine v2
##--

