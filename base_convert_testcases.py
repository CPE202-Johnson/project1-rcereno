import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_base0(self):
        with self.assertRaises(ValueError):
            convert(0, 1)

    def test_base07(self):
        self.assertEqual(convert(0,8), "0")

    def test_baseA(self):
        self.assertEqual(convert(10, 16), "A")

    def test_baseB(self):
        self.assertEqual(convert(11, 16), "B")

    def test_baseD(self):
        self.assertEqual(convert(13, 16), "D")

    def test_baseE(self):
        self.assertEqual(convert(14, 16), "E")

    def test_baseF(self):
        self.assertEqual(convert(15, 16), "F")

    def test_baseError(self):
        with self.assertRaises(ValueError): # used to check for value error
            convert(7, 18)

if __name__ == "__main__":
        unittest.main()