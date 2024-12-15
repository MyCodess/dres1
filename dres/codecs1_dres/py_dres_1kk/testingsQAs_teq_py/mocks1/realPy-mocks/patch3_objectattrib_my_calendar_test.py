"""
here patch the funcs/objects of the external source-file: patch1_my_calendar :
https://realpython.com/python-mock-library/#patch
Patching an Object’s Attributes :
Let’s say you only want to mock one method of an object instead of the entire object. You can do so by using patch.object().

For example, .test_get_holidays_timeout() really only needs to mock requests.get() and set its .side_effect to Timeout:
In this example, you’ve mocked only get() rather than all of requests. Every other attribute remains the same.

patch.object() takes the same configuration parameters that patch() does. But instead of passing the target’s path, you provide the target object, itself, as the first parameter.
The second parameter is the attribute of the target object that you are trying to mock. You can also use object() as a context manager like patch().

! WATCH import-stmt:   from patch1_my_calendar import requests, ...
"""

import unittest
from patch1_my_calendar import requests, get_holidays
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
            with self.assertRaises(requests.exceptions.Timeout):
                get_holidays()

if __name__ == '__main__':
    unittest.main()

