"""
usecase for assertRaises
self.assertRaises(TypeError, test_function, args)
"""
import unittest

from fun import division

class TestDivision(unittest.TestCase):

    def test_divison(self):
        actual = division(4,4)
        expected = 1
        
        self.assertEqual(actual,expected,'division() in fun.py has failed')

    def test_zero_by_zero_divsion(self):
        self.assertRaises(ZeroDivisionError,division,0,0)

    def test_by_zero_division(self):
        self.assertRaises(ZeroDivisionError,division,2,0)

    

if __name__ == "__main__":

    unittest.main()
