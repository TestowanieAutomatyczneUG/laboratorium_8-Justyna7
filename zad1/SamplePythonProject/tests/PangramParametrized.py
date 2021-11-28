import unittest
import sys
sys.path.insert(1, '../src/sample')
from pangram import *

from parameterized import parameterized, parameterized_class
import math



class PangramParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        self.assertEqual(math.floor(input), expected)

    def setUp(self):
        self.tmp = is_pangram

    @parameterized.expand([
        ('5', False),
        ('sefsxc465fvhbm', False),
        ('aqswdefrDefrgthyjukilopZXCVbnm', True)
    ])
    def test_one_parameterized(self, string, expected):
        self.assertEqual(self.tmp(string), expected)


@parameterized_class(('string', 'expected'), [
    ('10', False),
    ('AqSwDeFrGtHy18JuKiloPZXCvbnM', True),
    ('QWERTYUIOPSADFGHJKLZXCVBNM', True),
])
class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = is_pangram

    def test_second_parameterized(self):
        self.assertEqual(self.tmp(self.string), self.expected)


if __name__ == '__main__':
    unittest.main()
