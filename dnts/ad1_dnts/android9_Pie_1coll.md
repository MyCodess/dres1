##________________________________________  ___________________________


#####  ==========  SMS in Pie/android-9 :
-? SMS saved in /data/user_de/0/com.android.providers.telephony/databases/mmssms.db  ?? (needs rooting to see?)
- https://android.stackexchange.com/questions/228746/android-9-pie-where-are-sms-stored-please-what-is-the-path-to-the-sms-database :
- the sms are stored in the database: " /data/user_de/0/com.android.providers.telephony/databases/mmssms.db" which need root privileges to access it or edit it.
- If you don't have root access, you can interact with the table sms in this database using ADB:
- list all SMS :    adb shell content query --uri content://sms
- list SMS from +2121212121  :  adb shell content query --uri content://sms --projection address:date:date_sent:body --where 'address=+2121212121'
##________________________________________  ___________________________


#####  ==========  
