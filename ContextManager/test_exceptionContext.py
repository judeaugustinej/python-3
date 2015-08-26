import unittest

from exceptionContext import myDivide
from exceptionContext import mySquare

class TestCustomContextManager(unittest.TestCase):

    def test_mydivide(self):
        actual   = myDivide(9,3)
        expected = 3
        self.assertEqual(actual,expected,'mydivision is a failure')

    def test_mydivde_exception(self):
        self.assertRaises(TypeError,myDivide,'1','4')

    def test_mydivide_exception_zero_division(self):
        self.assertRaises(ZeroDivisionError,myDivide,1,0)

    def test_mysquare(self):
        actual   = mySquare(-5)
        expected = 25
        self.assertEqual(actual,expected)

    def test_mysquare_expection_type_error(self):
        self.assertRaises(TypeError,mySquare,'3')

if __name__ == "__main__":
    unittest.main()
"""
[sunkaray@SUT-LNX-1 exceptions]$ python3 test_exceptionContext.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
[sunkaray@SUT-LNX-1 exceptions]$

"""
