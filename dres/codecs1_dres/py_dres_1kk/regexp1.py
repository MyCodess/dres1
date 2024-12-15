#!/usr/bin/env  python3

#################### fistures :  #############################################
s1 = "Mayer  abc def ghi xxx yy"
s2 = "kkk mmm Mayer NNN rst www zzz"
s3 = s1 + "\n" + s2
l1=list(range(0,5))
tup1=tuple(range(20,25))
dic1={x: (x*3).upper() for x in "abcdef"}
set1=set(dic1.values())
##__  dic1={x: x**2 for x in range(0,5) }
##__  print ("-" * 20) ; print(s3) ; print(l1) ; print(tup1) ; print(dic1) ; print(set1) ; print ("-" * 20) ;

##############################################################################
print ("-" * 20) ; 
import re
s = s3
print(re.search(r"^M[ae][iy]er", s))
print(re.match(r"^M[ae][iy]er", s))
print(re.search(r"^M[ae][iy]er", s, re.MULTILINE))
print(re.search(r"^M[ae][iy]er", s, re.M))
print(re.match(r"^M[ae][iy]er", s, re.M))

##############################################################################
print ("-" * 20) ; 
import re
s1 = "He is called Meyer but he isn't German."
s2 = "Mayer is a very common Name"
s3 = s1 + "\n" + s2
print(re.search(r"M[ae][iy]er", s1))
print(re.search(r"M[ae][iy]er", s2))
print(re.match (r"M[ae][iy]er", s1)) 
print(re.match (r"M[ae][iy]er", s2))  
print ("---s3: match() does NOT find even with MULTILINE, but search with ^ does: " ) ; 
##__ The previous example also shows that the multiline mode doesn't affect the match method. match() never checks anything but the beginning of the string for a match. /www.python-course.eu/python3_re.php.html :
print(re.search("M[ae][iy]er", s3))
print(re.search("^M[ae][iy]er", s3))
print(re.match (r"M[ae][iy]er", s3)) 
print(re.search("^M[ae][iy]er", s3, re.MULTILINE))
print(re.match (r"M[ae][iy]er", s3, re.MULTILINE)) 

##############################################################################
print ("-" * 20) ;
print(re.search(r"Python\.$","I like Python."))
print(re.search(r"Python\.$","I like Python. and Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl.", re.M))


