import unittest 
from taxcalculator import *

#Tests - checking the boundaries of the and output of the salary calculator
class TestTaxBands(unittest.TestCase):
    def test_personalAllowance(self):
        self.assertEqual(calculateTaxedSalary(1),'1.00')
        self.assertEqual(calculateTaxedSalary(3000),'3000.00')
        self.assertEqual(calculateTaxedSalary(12500),'12500.00')

    def test_basicRate(self):
        self.assertEqual(calculateTaxedSalary(12501),'10000.80')

    def test_higherRate(self):
        self.assertEqual(calculateTaxedSalary(50001),'30000.60')
        self.assertEqual(calculateTaxedSalary(150000),'90000.00')

    def test_additionalRate(self):
        self.assertEqual(calculateTaxedSalary(150001),'82500.55')
        self.assertEqual(calculateTaxedSalary(300000),'165000.00')

if __name__ == '__main__':
    unittest.main()

