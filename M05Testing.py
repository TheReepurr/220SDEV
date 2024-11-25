from fractions import Fraction
import unittest


# Implementation of the sum function
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


# Test cases using unittest
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """Test that it can sum a list of integers"""
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """Test that it can sum a list of fractions"""
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(1))


if __name__ == '__main__':
    unittest.main()
