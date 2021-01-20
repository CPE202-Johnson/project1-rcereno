import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba']) # given test case

    def test_perm_gen_lex02(self):
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) # test case using the example in the instructions file

    def test_perm_gen_lex03(self):
        self.assertEqual(perm_lex.perm_gen_lex(''), []) # test case for an empty string

    def test_perm_gen_lex04(self):
        self.assertEqual(perm_lex.perm_gen_lex('r'), ['r']) # test case for a single character in the string

    def test_perm_gen_lex05(self):
        self.assertEqual(perm_lex.perm_gen_lex('l'), ['l']) # test case for a single character in the string

    def test_perm_gen_lex06(self):
        self.assertEqual(perm_lex.perm_gen_lex('art'), ['art', 'atr', 'rat', 'rta', 'tar', 'tra']) # test case for a different 3-letter word

#    def test_perm_gen_lex03(self):
#        self.assertEqual(perm_lex.perm_gen_lex('bob'), ['bob', 'bbo', 'obb', 'obb', 'bbo', 'bob'])

if __name__ == "__main__":
        unittest.main()
