#!/usr/bin/env   python

################### time shorties : #################################################
import time as t
print ("\n========== built-in module time : pydoc time , RefDocsPy/library/time.html: ==================================")
print ("- epoch definition on my system/OS ?? :", t.asctime(t.gmtime(0)), t.ctime(0), t.gmtime(0), sep=" , " )

print ("\n----- basically 3 presentaion forms of time:   1-string-local-time ,  2-seconds-since-epoch/ usu. 01.01.1970 ,  3-time-tuple (struct-time objects with 9 fields) : -----")
print ("-\t here examples for NOW-local-time, but all these funcs can be parameterized for specific times :")
print ("- now-time as str-local-time:  \t\t", t.ctime() ,  ", same as: ", t.asctime(t.localtime()))
print ("- now-time as seconds-since-epoch / nano.sec. (so timestamp):  \t", t.time(),  round(t.time(), 2), t.time_ns(), sep=" , ")  
print ("- now-time as time-tuple/time-struct ,  UTC/GMT:  ", t.gmtime() )  
print ("- now-time as time-tuple/time-struct ,localtime:  ", t.localtime())

print ("\n----- Conversions of the above time formats/presentations: ------------")
print ("- tuple-to-str/local : time-tuple/-struct to str-local-time : asctime([tuple]) -> string : \t", t.asctime(t.localtime(100000)))  
t11=t.localtime() ;  print (f"- tuple-to-str--customized-formatting (eg ISO-format) : {t11[0]}-{t11[1]:02d}-{t11[2]:02d}--{t11[3]:02d}-{t11[4]:02d}-{t11[5]:02d} {t.tzname}") ; 
print ("- tuple-to-seconds/local : time-tuple/-struct to str-local-time : mktime(tuple) -> float : inverse of localtime() : \t", t.mktime(t.localtime(100000)))  
print ("- tuple-to-seconds/UTC : time-tuple/-struct to str-local-time : mktime(tuple) -> float : inverse of localtime() : \t", t.mktime(t.gmtime(100000)))  
print ("- seconds-to-str/local : seconds-since-epoch to str-local-time : ctime(seconds) -> string : \t", t.ctime(50000), " == ", t.asctime(t.localtime(50000)))  
print ("- seconds-to-tuple/local : seconds-since-epoch to time-tuple/-struct-localtime : localtime([seconds]) -> (...) : inverse of mktime() : \n\t", t.localtime(50000))  
print ("- seconds-to-tuple/UTC,GMT : seconds-since-epoch to time-tuple/-struct-UTC,GMT : gmtime([seconds]) -> (...) : \n\t", t.gmtime(50000))  

print ("\n----- Perfomance timers, so no dateTime but just time-fifferences between 2 calls in seconds/nano ...! the start-/reference-point unclear/irrelevant :)")
print ("-- with time.perf_counter() :")
print ("- seconds.[fractional-seconds]-diff:  ", t.perf_counter(), t.sleep(0.1), t.perf_counter())
print ("- seconds.[fractional-seconds]-diff--rounded-to-1/100.sec:  ", round(t.perf_counter(), 2), t.sleep(0.1),  round(t.perf_counter(), 2))
print ("- seconds.[fractional-seconds]-diff--printed-to-1/100.sec:  ",  f"{t.perf_counter():.2f}",  t.sleep(0.1), "{:.2f}".format(t.perf_counter()))
print ("- nano-seconds-diff ():  ", t.perf_counter_ns(), t.sleep(0.1), t.perf_counter_ns())
print ("-- with time-funcs... : time.time() returns a good int timestamp! seconds/nonoseconds sich epoch, with fractionals if there! :")
print ("- seconds.[fractional-seconds]-diff--rounded-to-1/100.sec:  ", round(t.time(), 2) , t.sleep(0.2) , round(t.time(), 2) )
print ("- seconds (no-fractions):  ", t.mktime(t.localtime()))

print ("\n----- formatted by strftime,...")
print ("- ISO/evv:", t.strftime("%Y-%m-%d"), "more exp:", t.strftime("%m"), t.strftime("%S"), t.strftime("%c"), t.strftime("%S"), t.strftime("%x--%X"), sep=" , ")
print ("- parsing a string for the formatted time (output of ctime): ", t.strptime("Sat Jan  7 16:20:40 2023"))

print ("\n----- ")
