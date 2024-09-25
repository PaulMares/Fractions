import unittest
from fractions import least_common_multiplier, float_to_fraction, Fraction


class LCMTestCases(unittest.TestCase):
    def test_LCM_equal(self):
        """Tests that the LCM of two equal numbers is the same number."""
        self.assertEqual(2, least_common_multiplier(2, 2))

    def test_LCM_min_is_mul(self):
        """Tests the LCM of two numbers whose LCM is equal to their multiplication (worst-case scenario)."""
        self.assertEqual(15, least_common_multiplier(5, 3))

    def test_LCM_min_is_not_mul(self):
        """Tests the LCM of two numbers whose LCM is not equal to their multiplication."""
        self.assertEqual(12, least_common_multiplier(4, 6))

class FloatToFractionTestCases(unittest.TestCase):
    def test_int(self):
        """Tests that an integer converts to the equivalent fraction."""
        self.assertEqual(Fraction(5,1), float_to_fraction(5.0))

    def test_rational_positive(self):
        """Tests that a rational float converts to the equivalent fraction."""
        self.assertEqual(Fraction(1,2), float_to_fraction(0.5))

    def test_rational_negative(self):
        """Tests that a rational negative float converts to the equivalent fraction."""
        self.assertEqual(Fraction(-1,2), float_to_fraction(-0.5))



if __name__ == '__main__':
    unittest.main()
