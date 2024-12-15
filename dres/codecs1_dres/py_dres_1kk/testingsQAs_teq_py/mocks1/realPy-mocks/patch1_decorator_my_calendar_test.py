"""
here patch the funcs/objects of the external source-file: patch1_my_calendar :
https://realpython.com/python-mock-library/#patch
patch() as a Decorator:
here pathes  the requests-lib of the external module patch1_my_calendar.py :
"""
import unittest
from patch1_my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch('patch1_my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
