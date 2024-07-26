-!! resume: use only:  00-xx/00_xx  and 0xx  !! so, but NOT:  00xx   (it somes after 0xx in FileExplorer !!)
##________________________________________  ___________________________


#####  ==========  making the test-dir:
##-- NOT using -xxx , 0=aa.txt,... and any ESC-required-names in either Lx/MsWins !
mkdircd d1;
touch  00-aa.txt 00_aa.txt 00aa.txt 00-nts-sortOrder_00Names.txt 00rr.txt 0-aa.txt 0_aa.txt 0aa.txt 0Bac.txt 0nts.txt 0rr.txt aa Aa -aa.txt _aa.txt bb CC d1 DD Md Zy zz
##________________________________________  ___________________________


#####  ==========  man ascii :
 Tables
       For convenience, below are more compact tables in hex and decimal.
          2 3 4 5 6 7       30 40 50 60 70 80 90 100 110 120
        -------------      ---------------------------------
       0:   0 @ P ` p     0:    (  2  <  F  P  Z  d   n   x
       1: ! 1 A Q a q     1:    )  3  =  G  Q  [  e   o   y
       2: " 2 B R b r     2:    *  4  >  H  R  \  f   p   z
       3: # 3 C S c s     3: !  +  5  ?  I  S  ]  g   q   {
       4: $ 4 D T d t     4: "  ,  6  @  J  T  ^  h   r   |
       5: % 5 E U e u     5: #  -  7  A  K  U  _  i   s   }
       6: & 6 F V f v     6: $  .  8  B  L  V  `  j   t   ~
       7: ' 7 G W g w     7: %  /  9  C  M  W  a  k   u  DEL
       8: ( 8 H X h x     8: &  0  :  D  N  X  b  l   v
       9: ) 9 I Y i y     9: '  1  ;  E  O  Y  c  m   w
       A: * : J Z j z
       B: + ; K [ k {
       C: , < L \ l |
       D: - = M ] m }
       E: . > N ^ n ~
       F: / ? O _ o DEL

	_______:  --  Dec.Ord of:
$  pyhton -B
>>> ord("-")
45
*>>> ord("0")
48
*>>> ord("_")
95
>>> 
##________________________________________  ___________________________


#####  ==========  outputs :
-! ll is fine (always 00x before 0x) , BUT in FileExplorer/Firefox/.... NOT-so !
-!! so resume:  in both Explorerec+ ll OK: 00-xx and 00_xx are before 0x !! 
	BUT 0-x/0_x are before 00... in Explorer !

	_______:  ---
ll output:  (ll  ==  'ls   -p  --group-directories-first  --time-style=long-iso  --color=never -l')
2022-01-28T13:41:29 CET
total 4
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 12:56 00-aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 13:38 00.aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 12:56 00_aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 13:03 00aa.txt
-rw-rw-r-- 1 u1 gu1 1189 2022-01-28 13:41 00-nts-sortOrder_00Names.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 12:56 0-aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 12:56 0_aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 12:56 0aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 13:01 -aa.txt
-rw-rw-r-- 1 u1 gu1    0 2022-01-28 12:59 _aa.txt
##________________________________________  ___________________________


#####  ==========  
