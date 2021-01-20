import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250)) # covers all of the conditions

    def test_bear_02(self):
        self.assertTrue(bears(42)) # covers the first base case

    def test_bear_03(self):
        self.assertFalse(bears(53)) # covers when it will return false as it is not possible to win with this n value

    def test_bear_04(self):
        self.assertFalse(bears(41)) # covers the second base case

    def test_bear_05(self):
        self.assertFalse(bears(0)) # covers when n = 0 or if n is less than 42

    def test_bear_06(self):
        self.assertTrue(bears(1260)) # uses all 3 conditions

    def test_bear_07(self):
        self.assertFalse(bears(45)) # covers a false/lose situation

    def test_bear_08(self):
        self.assertTrue(bears(672)) # tests the divisible by 4 condition twice

    def test_bear_09(self):
        self.assertTrue(bears(210)) # tests the conditions of divisible by 5 and the conditions for an even number

if __name__ == "__main__":
    unittest.main()
