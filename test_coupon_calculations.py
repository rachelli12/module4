""""
Program name: test_coupon_calculations.py
Author: Rachel Li
Last date modified: 06/10/2020

The purpose of this program is to test coupon_calculations.py
"""
import unittest
import coupon_calculations as cc

class MyTestCase(unittest.TestCase):
    #def calculate_price(value_under_ten, cash_coupon, percent_coupon)
    def test_price_under_ten(self):
        value_under_ten = 8.99
        shipping = 5.95
        self.assertAlmostEqual(((cc.calculate_price(value_under_ten,5,10) + shipping)*1.06), 10.11, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_ten, 5, 15) + shipping)*1.06), 9.90, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_ten, 5, 20) + shipping)*1.06), 9.69, places=2)
    def test_price_under_between_ten_thirty(self):
        value_under_between_ten_thirty = 18.99
        shipping = 7.95
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_ten_thirty, 5,10) + shipping)*1.06), 21.77, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_ten_thirty, 5, 15) + shipping)*1.06), 21.03, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_ten_thirty, 5, 20) + shipping)*1.06), 20.29, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_ten_thirty, 10,10) + shipping)*1.06), 17.00, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_ten_thirty, 10, 15) + shipping)*1.06), 16.53, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_ten_thirty, 10, 20) + shipping)*1.06), 16.05, places=2)
    def test_price_under_between_thirty_fifty(self):
        value_under_between_thirty_fifty = 38.99
        shipping = 11.95
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_thirty_fifty, 5,10) + shipping)*1.06), 45.09, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_thirty_fifty, 5, 15) + shipping)*1.06), 43.29, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_thirty_fifty, 5, 20) + shipping)*1.06), 41.49, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_thirty_fifty, 10,10) + shipping)*1.06), 40.32, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_thirty_fifty, 10, 15) + shipping)*1.06), 38.79, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_between_thirty_fifty, 10, 20) + shipping)*1.06), 37.25, places=2)
    def test_price_under_over_fifty(self):
        value_under_over_fifty = 78.99
        shipping = 0.00
        self.assertAlmostEqual(((cc.calculate_price(value_under_over_fifty, 5,10) + shipping)*1.06), 70.59, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_over_fifty, 5, 15) + shipping)*1.06), 66.66, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_over_fifty, 5, 20) + shipping)*1.06), 62.74, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_over_fifty, 10,10) + shipping)*1.06), 65.82, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_over_fifty, 10, 15) + shipping)*1.06), 62.16, places=2)
        self.assertAlmostEqual(((cc.calculate_price(value_under_over_fifty, 10, 20) + shipping)*1.06), 58.50, places=2)

if __name__ == '__main__':
    unittest.main()
