import unittest
from prostokat import *
from parameterized import parameterized, parameterized_class
from nose2.tools import params


class ProstokatParameterizedPackage(unittest.TestCase):
    def setUp(self):
        self.tmp = Prostokat()

    @parameterized.expand([
        (1, 1, "*"),
        (0, 0, ""),
        (0, 1, ""),
        (1, 0, ""),
        (3456, 0, ""),
        (0, 16787, ""),
        (12, 1, "*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*"),
        (1, 3, "***"),
        (3, 2, "**\n**\n**"),
        (2, 3, "***\n***"),
        (2, 2, "**\n**"),
        (3, 3, "***\n* *\n***"),
        (4, 4, "****\n*  *\n*  *\n****"),
        (3, 4, "****\n*  *\n****"),
        (4, 3, "***\n* *\n* *\n***"),
        (4, 2, "**\n**\n**\n**"),
        (2, 4, "****\n****"),
        (5, 5, "*****\n*   *\n*   *\n*   *\n*****")
    ])
    def test_one_parameterized(self, int1, int2, expected):
        self.assertEqual(self.tmp.prostokat(int1, int2), expected)

    @parameterized.expand([
        (1, []),
        ([], 0),
        ([], []),
        ([1], 0),
        ([3, 4, 5, 6], [0]),
        ({}, 16787),
        (12, {}),
        (1.8, 3),
        (3, 2.8),
        (2.4, 3.4),
        ({}, {}),
        ({3: 15}, 44),
        ("4", 4),
        (3, "4"),
        ("4", "3"),
    ])
    def test_exceptions_parameterized(self, int1, int2):
        self.assertRaises(Exception, self.tmp.prostokat, int1, int2)


@parameterized_class(('int1', 'int2', 'expected', 'exception'), [
    (1, 1, "*", False),
    (0, 0, "", False),
    (0, 1, "", False),
    (1, 0, "", False),
    (3456, 0, "", False),
    (0, 16787, "", False),
    (12, 1, "*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*", False),
    (1, 3, "***", False),
    (3, 2, "**\n**\n**", False),
    (2, 3, "***\n***", False),
    (2, 2, "**\n**", False),
    (3, 3, "***\n* *\n***", False),
    (4, 4, "****\n*  *\n*  *\n****", False),
    (3, 4, "****\n*  *\n****", False),
    (4, 3, "***\n* *\n* *\n***", False),
    (4, 2, "**\n**\n**\n**", False),
    (2, 4, "****\n****", False),
    (5, 5, "*****\n*   *\n*   *\n*   *\n*****", False),
    (1, [], "Typ musi miec warosc Int", True),
    ([], 0, "Typ musi miec warosc Int", True),
    ([], [], "Typ musi miec warosc Int", True),
    ([1], 0, "Typ musi miec warosc Int", True),
    ([3, 4, 5, 6], [0], "Typ musi miec warosc Int", True),
    ({}, 16787, "Typ musi miec warosc Int", True),
    (12, {}, "Typ musi miec warosc Int", True),
    (1.8, 3, "Typ musi miec warosc Int", True),
    (3, 2.8, "Typ musi miec warosc Int", True),
    (2.4, 3.4, "Typ musi miec warosc Int", True),
    ({}, {}, "Typ musi miec warosc Int", True),
    ({3: 15}, 44, "Typ musi miec warosc Int", True),
    ("4", 4, "Typ musi miec warosc Int", True),
    (3, "4", "Typ musi miec warosc Int", True),
    ("4", "3", "Typ musi miec warosc Int", True),
])
class ProstokatParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Prostokat()

    def test_second_parameterized(self):
        if self.exception:
            self.assertRaises(Exception, self.tmp.prostokat, self.int1, self.int2)
        else:
            self.assertEqual(self.tmp.prostokat(self.int1, self.int2), self.expected)


@params(
    (1, 1, "*", False),
    (0, 0, "", False),
    (0, 1, "", False),
    (1, 0, "", False),
    (3456, 0, "", False),
    (0, 16787, "", False),
    (12, 1, "*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*", False),
    (1, 3, "***", False),
    (3, 2, "**\n**\n**", False),
    (2, 3, "***\n***", False),
    (2, 2, "**\n**", False),
    (3, 3, "***\n* *\n***", False),
    (4, 4, "****\n*  *\n*  *\n****", False),
    (3, 4, "****\n*  *\n****", False),
    (4, 3, "***\n* *\n* *\n***", False),
    (4, 2, "**\n**\n**\n**", False),
    (2, 4, "****\n****", False),
    (5, 5, "*****\n*   *\n*   *\n*   *\n*****", False),
    (1, [], "Typ musi miec warosc Int", True),
    ([], 0, "Typ musi miec warosc Int", True),
    ([], [], "Typ musi miec warosc Int", True),
    ([1], 0, "Typ musi miec warosc Int", True),
    ([3, 4, 5, 6], [0], "Typ musi miec warosc Int", True),
    ({}, 16787, "Typ musi miec warosc Int", True),
    (12, {}, "Typ musi miec warosc Int", True),
    (1.8, 3, "Typ musi miec warosc Int", True),
    (3, 2.8, "Typ musi miec warosc Int", True),
    (2.4, 3.4, "Typ musi miec warosc Int", True),
    ({}, {}, "Typ musi miec warosc Int", True),
    ({3: 15}, 44, "Typ musi miec warosc Int", True),
    ("4", 4, "Typ musi miec warosc Int", True),
    (3, "4", "Typ musi miec warosc Int", True),
    ("4", "3", "Typ musi miec warosc Int", True),
)
def test_dodatkowe_Test(int1, int2, expected, exception):
    print("xxx")
    temp = Prostokat()
    if exception:
        with unittest.TestCase.assertRaises(Exception):
            temp.prostokat(int1, int2)
    else:
        assert temp.prostokat(int1, int2) == expected

if __name__ == '__main__':
    unittest.main()
