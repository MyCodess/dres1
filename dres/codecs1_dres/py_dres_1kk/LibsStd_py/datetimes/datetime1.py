#!/usr/bin/env  python3

############### datetime module : pydoc datetime , RefDocsPy--/library/datetime.html : ######################################
import  datetime as dt
import time  ##--just for certain comparisions,...

print ("\n====================== datetime.date class : ============================================")
print ("--- nts:  1-Gregorian Calendar :  years 365/366 days , from 01.01.0001 ! ,  2-Epoch/Lx: from 01.01.1970 , 3- Gregorian+Epoch: Gregorian from 01.01.1970 ")
print ("--- nts:  date() has got NO time attributs/infos! otherwise use datetime.datetime() objects !")
d1 = dt.date(2010,1,1)     ##-- 2000-01-01 , initialized to 01.Jan.2000
d1_iso = dt.date.fromisoformat("2100-01-01")     ##-- type (d1_iso) is <class 'datetime.date'>
today1 = dt.date.today()    ##-- 
print ("- new date object initialized to  :   ", dt.date(2000,1,1))

print ("\n----- conversions/initializations to/from date() objects:   ")
print ("- str-iso --> date-object , new date object from str-iso-format  YYYY-MM-DD :   ", dt.date.fromisoformat("2000-01-01"), type (d1_iso))
print ("- date()-object --> str-iso /YYYY-MM-DD:   ", d1.isoformat())
print ("- date()-object --> str-customized-formatting:   ", d1.strftime("%A %d. %B %Y"))
print ("- date()-object --> str-customized-formatting--as-formatParams: The {1} is {0:%d}, the {2} is {0:%B} ".format(d1, "day", "month"))  ##--I-see strftime descp for %-tags !
print ("- date()-object --> time-tuple , as in time.localtime():   ", dt.date.timetuple(d1))
print ("- int (number of DAYs from 01.01.0001 ,so NOT-from-Epoch but abosolut-days-number, and based on Gregorian Calendar) --> date()-object :   ", dt.date.fromordinal(2000 * 365) , type(dt.date.fromordinal(3650)) )
print ("- int/float/Timestamp (number of SECONDS from epoch + Gregorian Calendar based) --> date()-object :   ", dt.date.fromtimestamp(time.time()), dt.date.fromtimestamp(60*60*24*365*(2023-1970)) )
print ("- date()-object -->  int (number of days /Gregorian-from-Epoch:   ", dt.date(2000,1,1).toordinal() )

print ("\n----- date() funcs:   ")
print ("- today / current date:   ", dt.date.today())
print ("- date in ISO-format:   ", dt.date.isoformat(dt.date.today()))


print ("\n====================== datetime.datetime class : ============================================")
print ("--- nts:  datetime.datetime is Gregorian calendar based + assumes there are exactly 3600*24 seconds in every day ! ")
print ("--- nts:  see corresponding funcs of date() ! similar !")
dt1 = dt.datetime(2010,1,1, 2,3,4)
dt1_iso = dt.datetime.fromisoformat("2010-01-01T01:02:03")
todayt1 = dt.datetime.now()   ##--so same as :  dt.datetime.today()    ##-- 
print ("- new datetime object initialized to :   ",   dt.datetime(2010,1,1, 2,3,4))

print ("\n----- conversions/initializations to/from datetime() objects:   ")
print ("- str-iso --> datetime-object :  ", dt.datetime.fromisoformat('2011-11-04T00:05:23+04:00'), type (dt1_iso))
print ("- datetime()-object --> str-iso /YYYY-MM-DDTHH:mm:ss:   ", dt1.isoformat())
print ("- datetime()-object --> str-customized-formatting:   ", dt1.strftime("%A %d. %B %Y"))
print ("- datetime()-object --> time-tuple , as in time.localtime():   ", dt.datetime.timetuple(dt1))
print ("- datetime()-object --> int /to-ordinals:   ", dt.datetime.toordinal(dt1))
print ("- datetime()-object --> int/float/timestamp:   ", dt.datetime.timestamp(dt1))  ##--I-similar to time.time()
print ("- int (number of DAYs from 01.01.0001 ,so NOT-Epoch, + Gregorian Calendar) --> datetime()-object :   ", dt.datetime.fromordinal(2000 * 365) , type(dt.datetime.fromordinal(3650)) )
print ("- int/float/Timestamp (number of SECONDS from epoch + Gregorian Calendar based) --> date()-object :   ", dt.datetime.fromtimestamp(time.time()), " ,another int: ", dt.datetime.fromtimestamp(60*60*24*365*(2023-1970)+(60*60*2)) )
print ("- datetime()-object -->  int (number of days /Gregorian-from-Epoch:   ", dt.datetime(2000,1,1).toordinal() )

print ("\n----- datetime() funcs:   ")
print ("- today now / current datetime:   ", dt.datetime.now() ,  dt.datetime.today() )
print ("- today now UTC / current datetime UTC:   ", dt.datetime.utcnow() )

print("_______________________________________________________________________")

