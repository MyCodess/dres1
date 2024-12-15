##--see:  https://www.pythontutorial.net/python-unit-testing/python-patch/
import unittest
from unittest.mock import MagicMock, patch

import total
'''
Three ways to call patch():
- Decorators for a function or a class.
- Context manager
- Manual start/stop
as @patch decorator, the method gets an additional argument which is an instance of the MagicMock.
'''

class TestTotal(unittest.TestCase):
 
    ##--------- 1) Using patch() as a decorator :
    ##-II- Because of the @patch decorator, the test_calculate_total() method has an additional argument to the end of the args-list which is an instance of the MagicMock. Note that you can name the additional parameter whatever you want.
    # now the mock_read object will be called instead of the total.read() function, you can pass any filename to the calculate_total() function:
    @patch('total.read')
    def patch1(self, add1:int , mock_read):
        mock_read.return_value = [0, 1, 2, add1]
        result = total.calculate_total("f1.txt")
        self.assertEqual(result, 6)

    def test_patch1(self):
        self.patch1(3)

    ##----------- 2) Using patch() as a context manager (with-stmt):
    ##-I- patch in "with"/context-manager: It means that within the with block, the patch() replaces the total.read() function with the mock_read object.
    def test_calculate_total_1(self):
        with patch('total.read') as mock_read:
            mock_read.return_value = [1, 2, 3]
            print (mock_read.nonExistFunc1())  ##-OK! so you can call anything on mocked-obj! if not defined, nothing! if its returned_value is defined, then this value!
            result = total.calculate_total('')
            self.assertEqual(result, 6) 

    ##----------- 3) Using patch() manually :
    def test_calculate_total_2(self):
        # start patching
        patcher = patch('total.read')
        # create a mock object
        mock_read = patcher.start()
        # assign the return value
        mock_read.return_value = [1, 2, 3]
        # test the calculate_total
        result = total.calculate_total('')
        self.assertEqual(result, 6)
        # stop patching
        patcher.stop()
        
    ##-- manualy-without "patch()" but directly with MagicMock:
    def test_calculate_total_3(self):
        total.read = MagicMock()
        total.read.return_value = [1, 2, 3]
        result = total.calculate_total('')
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()

