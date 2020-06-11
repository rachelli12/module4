""""
Program
"""
import unittest
import coupon_calculations as cc

class MyTestCase(unittest.TestCase):
    #def total = calculate_total(calculate_shipping(calculate_price(price, cash_coupon, percent_coupon)))
    def test_price_under_ten(self):
        value_under_ten = 8.99 #shipping $5.95
        self.assertAlmostEqual(cc.cost, 10.11, places=4)
        self.assertAlmostEqual(cc.cost, 9.90, places=4)
        self.assertAlmostEqual(cc.cost, 9.69, places=4)
        self.assertAlmostEqual(cc.cost, 5.34, places=4)
        self.assertAlmostEqual(cc.cost, 5.40, places=4)
        self.assertAlmostEqual(cc.cost, 5.45, places=4)


if __name__ == '__main__':
    unittest.main()
