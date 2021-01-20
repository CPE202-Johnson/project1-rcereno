import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101") # given test case that uses a base of 2

    def test_base4(self):
        self.assertEqual(convert(30,4),"132") # given test case that uses a base of 4

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C") # given test case that uses a base of 16 and also returns a string with a hex value from 12 to C

    def test_base0(self):
        with self.assertRaises(ValueError): # extra test case that uses the ValueError raise from the function, although I could've removed it and this test case
            convert(0, 1)

    def test_base07(self):
        self.assertEqual(convert(0,8), "0") # test case with a num of 0 and returns as 0

    def test_baseA(self):
        self.assertEqual(convert(10, 16), "A") # test case to check if 10 converts to A

    def test_baseB(self):
        self.assertEqual(convert(11, 16), "B") # test case to check if 11 converts to B

    def test_baseD(self):
        self.assertEqual(convert(13, 16), "D") # test case to check if 13 converts to D

    def test_baseE(self):
        self.assertEqual(convert(14, 16), "E") # test case to check if 14 converts to E

    def test_baseF(self):
        self.assertEqual(convert(15, 16), "F") # test case to check if 15 converts to F

    def test_baseError(self):
        with self.assertRaises(ValueError): # used to check for value error, although wasn't necessary
            convert(7, 18)

if __name__ == "__main__":
        unittest.main()