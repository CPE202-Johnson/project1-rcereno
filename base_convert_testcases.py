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
        self.assertEqual(convert(0, 1), "0")

#    def test_baseA(self):
#        self.assertEqual(convert())

#    def test_baseB(self):

#    def test_baseD(self):

#    def test_baseE(self):

 #   def test_baseF(self):

   # def test_baseError(self):


# base 10 and sending in 0
if __name__ == "__main__":
        unittest.main()