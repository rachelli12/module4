"""
Program name: test_validation_with_try.py
Author: Rachel Li
Last date modified: 06/10/2020

Purpose of this program is to test validation_with_try.py
"""
import unittest
import unittest.mock as mock
import validation_with_try as vwt

class AverageTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert vwt.average(85, 90, 95) == 90
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            vwt.average(-90, 89, 78)
    def test_average_second_exception(self):
        with self.assertRaises(ValueError):
            vwt.average(90, -89, 78)
    def test_average_third_exception(self):
        with self.assertRaises(ValueError):
            vwt.average(90, 89, -78)

if __name__ == '__main__':
    unittest.main()
