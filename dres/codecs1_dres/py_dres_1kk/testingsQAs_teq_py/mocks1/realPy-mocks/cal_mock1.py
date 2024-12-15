"""
https://realpython.com/python-mock-library/
mock datetime and set the .return_value for .today() to a day that you choose:
In the example, .today() is a mocked method.
You’ve removed the inconsistency by assigning a specific day to the mock’s .return_value.
That way, when you call .today(), it returns the datetime that you specified.
"""

import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
##__1org:  datetime = Mock()
datetime.datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()

