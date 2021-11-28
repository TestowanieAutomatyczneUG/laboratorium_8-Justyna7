import unittest
from sample.FizzBuzz import *

class FizzBuzzParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/fizz_buzz_data_test")
      tmpFizzBuzz = FizzBuzz()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp, result = int(data[0]), data[1].strip("\n")
            self.assertEqual(tmpFizzBuzz.game(inp), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
