"""
https://realpython.com/python-mock-library/
.side_effect can also be an iterable.
The iterable must consist of return values, exceptions, or a mixture of both.
The iterable will produce its next value every time you call your mocked method.
For example, you can test that a retry after a Timeout returns a successful response:
--
The first time you call get_holidays(), get() raises a Timeout.
The second time, the method returns a valid holidays dictionary.
These side effects match the order they appear in the list passed to .side_effect.
"""
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_retry(self):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successful response
        assert get_holidays()['12/25'] == 'Christmas'
        # Finally, assert .get() was called twice
        assert requests.get.call_count == 2

if __name__ == '__main__':
    unittest.main()
