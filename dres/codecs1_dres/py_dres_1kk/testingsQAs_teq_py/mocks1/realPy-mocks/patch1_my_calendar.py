"""
https://realpython.com/python-mock-library/#patch
patch() as a Decorator bzw. patch() as a Context Manager :
here only the source-file to be patched in ints test-file!
see its test-files which mocks the requests-lib of this module!
"""

import requests
from datetime import datetime

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
