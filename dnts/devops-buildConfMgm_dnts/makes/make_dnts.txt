_________________ GNU make / MakeFile : __________________________________________



#####  ==========  nts/URLs/hlps/...:
    https://www.gnu.org/software/make/manual/
##________________________________________  ___________________________


#####  ========== debugs/drys/chks/... make:
    - !! make  -n bzw. --dry-run ...  :  print cmds (even if @cmd1 ) BUT not execute them (except some exceptions)
    - !! make  --debug=print  ...  ##--shows all recipes that are executed even if they are silent (so as -n  BUT + execution of cmds!)! see man make
    - !! make  --debug=basic  ...  ##--bzw:   make -d ...  /OR --debug=all/basic/verbose/jobs/... ; see man make
##________________________________________  ___________________________



#####  ==========  make-"rules" /targets, ... Allg:
    _______:  DEF:   make-RULES :
        - a make-rule consinsts of : targets + prerequisites + recipes !
        - meaning:  rule-target (files,...) depend on prerequisites ! and if any prerequisite is changed bzw. newer than target-files, then ---> execute all its recipes ! 
        - syntax of a make-rule:
        targets : prerequisites (depends on ...)
            <TAB>  recipes
        - recipes MUST be prefixed with a  <TAB> ! bzw. .RECIPEPREFIX var ! so the TAB can be redefined by setting RECIPEPREFIX = <my-recipe-prefix-1> !

    _______:  targets/goals:
    - DEFAULT target/goal (if calling make with NO target): is the first target in the makefile , by default!
##________________________________________  ___________________________


#####  ==========  recipes/actions:
    - ! "@"  : NOT-echoing the current cmdiline during execution! sg:  @echo "infoline: ...."
##________________________________________  ___________________________


#####  ==========  VARs:
    - !! see here dres--vars1.makefile  !
    - see manual:  6 How to Use Variables in  make.pdf  /bzw:  info make "using variables" !
    - VARs-names:  [alnum_] safe!! are case-SEnsitive ! variable names containing characters other than letters, numbers, and underscoresshould be considered carefully /avoided! make.pdf--Ch-06
    - VARS-references/using-syntax:  $(var1) , ${var1} , $var1  ,all same!

    _______:  VARs-setting/Auflösung:
    - !! in a makefile: erst werden ALLE VARs bis ENDe aufgelöst/gesetzt, erst danach wird ein RULE/Target ausgewertet/ausgeführt! so, also VARs-setting AFTER a rule-definition are set/evaluated/extended BEFORE executing rules recipes !
    - VARS-references/using/extensons/Auflösung : four Types ! see above dres--vars1.makefile and make.pdf--CH-6.2 :
    1- " = " , var1 = val1  , AUflösung/expansion of values: during runtime + recursively ! so dynamically (NOT-statically-on-its-line!) 6.2.1 Recursively Expanded Variable Assignment , 
        -!! so do NOT refence it itself as: var = "${var1}-xxx" ! then infinite-loop-ERROR !!
    2- " ::= " bzw.  " := " same/posix-:: , staticly-expanded-on-its-line-ONLY!  : 6.2.2 Simply Expanded Variable Assignment :
       The value of a simply expanded variable is scanned once, expanding any references to other variables and functions, when the variable is defined (on its line) ! 
    - ! your first choice for assignments must be "::=" ! (is the usual assigment in other langs/scripts/...)
    - undefine vars:  undefine  var1
    - ! .VARIABLES   :  listing-of-all-global-vars-incl-shellEnvVars+MakeGlobalVars (not-target-specific/private/...):  @echo  "${.VARIABLES}"

    _______:  shell-ENV-vars , cmdline-VARs :
    - ! overriding any makefile-VARs on the cmdline simply by calling as :   make var1=XXX  ...  ##--then ANY settings of var1 in the makefile itself will be IGNORED! see make.pdf--6.7 The override Directive
    - ! Variables provided on the command line (and in the environment if the ‘-e’ option is in force) will take precedence to the makefile-VARs !
    - ! make without "-e" : then  makefile-VARs overwrite the shell-ENV-vars with the same name !

##________________________________________  ___________________________

