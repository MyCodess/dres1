#!/usr/bin/python
# -- https://docs.python.org/3/library/zoneinfo.html

"""
- !! Naive and timezone-aware datetime objects:  Python’s datetime.datetime objects have a tzinfo attribute that can be used to store time zone information, represented as an instance of a subclass of datetime.tzinfo. When this attribute is set and describes an offset, a datetime object is aware. Otherwise, it’s naive.  see django-docs/topics/i18n/timezones.html
- You can use is_aware() and is_naive() to determine whether datetimes are aware or naive.
- now time if is_naive():  import datetime;  now = datetime.datetime.now()
- now time if is_aware():  from django.utils import timezone ; now = timezone.now()  ##--for django; for py-stdlib checkit !

"""

from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
import zoneinfo

print("============================== listing all timezones: ===============================")
for ii in sorted(zoneinfo.available_timezones()): print(ii)

print("\n============================== datetime-timezoned: ==================================")
dt = datetime(2020, 10, 31, 14, tzinfo=ZoneInfo("Europe/Berlin"))
print(dt, "  TZ-name: ", dt.tzname())
usc1 = (ZoneInfo("US/Central"))
# -1OK:  print(dt.astimezone(ZoneInfo("US/Central")), "  TZ-name: ", dt.tzname())
print(dt.astimezone(usc1), "  USC time of: TZ-name: ", dt.tzname())
dt_add = dt + timedelta(days=1)
print("+1day: ", dt_add,  "  TZ-name: ",dt_add.tzname())
