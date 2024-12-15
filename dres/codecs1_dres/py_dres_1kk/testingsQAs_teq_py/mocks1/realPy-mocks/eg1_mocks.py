##--:see  https://realpython.com/python-mock-library/

from unittest.mock import Mock

def hist_calls1():
    """
    Assertions and Inspection:   https://realpython.com/python-mock-library/
    Mock instances store data on how you used them. For instance, you can see if you called a method, how you called the
    method, and so on. There are two main ways to use this information.
    unittest.mock.Mock().assert_called_xxx() methods can be applied to mocked objects/libs/... !
    see its pydocRef for listing!
    """
    json = Mock()
    json.loads('{"key": "value"}')

    json.loads.assert_called()
    json.loads.assert_called_once()
    json.loads.assert_called_with('{"key": "value"}')
    json.loads.assert_called_once_with('{"key": "value"}')

    ##--UnComment to get exception, due to second-time-call:
    ##__ json.loads('{"key2": "value2"}'); json.loads.assert_called_once()   ##---> EXCEPTION! it was called twice! not once !!

##############################  main: #############################
hist_calls1()

