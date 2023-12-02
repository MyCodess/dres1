##--see:  https://www.pythontutorial.net/python-unit-testing/python-patch/
import unittest
from unittest.mock import MagicMock, patch

import total

class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        total.read = MagicMock()
        total.read.return_value = [1, 2, 3]
        result = total.calculate_total('')
        self.assertEqual(result, 6)


    ##-II- Because of the @patch decorator, the test_calculate_total() method has an additional argument to the end of the args-list which is an instance of the MagicMock. Note that you can name the additional parameter whatever you want.
    # now the mock_read object will be called instead of the total.read() function, you can pass any filename to the calculate_total() function:
    @patch('total.read')
    def patch1(self, add1:int , mock_read):
        mock_read.return_value = [0, 1, 2]
        result = total.calculate_total("f1.txt")
        self.assertEqual(result, 3)

    def test_patch1(self):
        self.patch1(2)

    ##---patch in "with"/context-manager: It means that within the with block, the patch() replaces the total.read() function with the mock_read object.
    def test_calculate_total(self):
        with patch('total.read') as mock_read:
            mock_read.return_value = [1, 2, 3]
            print (mock_read.nonExistFunc1())  ##-OK! so you can call anything on mocked-obj! if not defined, nothing! if its returned_value is defined, then this value!
            result = total.calculate_total('')
            self.assertEqual(result, 6) 

if __name__ == "__main__":
    unittest.main()

