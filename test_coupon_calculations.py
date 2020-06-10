"""
Program
"""
import unittest
import unittest.mock as mock
from store import coupon_calculations as cc

class MyTestCase(unittest.TestCase):
    #def calculate_price(price, cash_coupon, percent_coupon):
    def test_price_under_ten(self):
        value_under_ten = 8.99 #shipping $5.95
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 5, 10), 10.60, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 5, 15), 10.40, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 5, 20), 10.20, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 10, 10), 6.10, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 10, 15), 6.15, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 10, 20), 6.20, places=4)


if __name__ == '__main__':
    unittest.main()

