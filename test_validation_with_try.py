import unittest
import unittest.mock as mock
from input_validation import validation_with_try as vwt

class AverageTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert vwt.average(85, 90, 95) == 90
    def test_average_exceptiont(self):
        with self.assertRaises(ValueError):
            vwt.average(-90, 89, 78)

if __name__ == '__main__':
    unittest.main()
