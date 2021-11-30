import unittest
from sample.FizzBuzz import *
from parameterized import parameterized, parameterized_class
import math

class FizzBuzzParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        self.assertEqual(math.floor(input), expected)

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
    ])
    def test_one_parameterized(self,number, expected):
        self.assertEqual(self.tmp.game(number), expected)


@parameterized_class(('number', 'expected'), [
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
])
class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.game(self.number), self.expected)


if __name__ == '__main__':
    unittest.main()
