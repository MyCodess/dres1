import unittest
from my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    ##--I-this setUp() wil be executed EVERYTIME before each test-Method! so here we use the class-setup-method, which will be used once per class!
    ##__  def setUp(self): self.calculation = Calculations(8, 2)
    @classmethod
    def setUpClass(self):
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, 'The quotient is wrong.')

def main():
    if __name__ == '__main__':
        unittest.main()

main()

