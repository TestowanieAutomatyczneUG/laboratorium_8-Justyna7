from sample.FizzBuzz import *
import unittest
from hamcrest import *

class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.temp = FizzBuzz()

    def testEquals(self):
        assert_that(self.temp.game(5), equal_to("Buzz"))

    def testAnyOf(self):
        assert_that(self.temp.game(5), all_of(equal_to("Buzz"), contains_string("Buzz")))

    def testInstance(self):
        assert_that(self.temp, is_(FizzBuzz))

    def testInstance2(self):
        assert_that(self.temp, instance_of(FizzBuzz))

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
