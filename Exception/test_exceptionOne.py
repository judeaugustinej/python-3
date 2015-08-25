#Test case for exceptionOne.py

import unittest

from exceptionOne import mySquare

class TestForMySquare(unittest.TestCase):

    def test_for_pos_interger(self):
        """Test for positive interger"""
        expected = 9
        actual   = mySquare(3)
        self.assertEqual(expected,actual,"Bug in exceptionOne.py")

    def test_for_neg_integer(self):
        """Test for a negative interger"""
        expected = 25
        actual   = mySquare(-5)
        self.assertEqual(expected,actual,"Bug in expectionOne.py")

    def test_for_exception_handling(self):
        self.assertRaises(TypeError,mySquare,'veeraarava')


if __name__ == "__main__":
   unittest.main()

#Output
"""
[sunkaray@SUT-LNX-1 jude]$ python3 test_exceptionOne.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
[sunkaray@SUT-LNX-1 jude]$
"""
"""
