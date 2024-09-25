import unittest
from fractions import Fraction


class FractionsReprTestCases(unittest.TestCase):
    def test_simple(self):
        """Test that a new fraction has the expected values."""
        new_fraction = Fraction(1, 2)
        self.assertEqual("1/2", str(new_fraction))

    def test_negative_numerator(self):
        """Test that a new fraction is negative due to the numerator's sign."""
        new_fraction = Fraction(-1, 2)
        self.assertEqual("-1/2", str(new_fraction))

    def test_negative_denominator(self):
        """Test that a new fraction is negative due to the denominator's sign."""
        new_fraction = Fraction(1, -2)
        self.assertEqual("-1/2", str(new_fraction))

    def test_negative_both(self):
        """Test that a new fraction is positive if both the numerator and denominator are negative."""
        new_fraction = Fraction(-1, -2)
        self.assertEqual("1/2", str(new_fraction))

class FractionsEqualityTestCases(unittest.TestCase):
    def test_simple(self):
        """Test that two identical fractions are equal."""
        fraction_1 = Fraction(1, 2)
        fraction_2 = Fraction(1, 2)
        self.assertEqual(fraction_1, fraction_2)

    def test_negative_equality(self):
        """Test that two negative fractions are equal."""
        fraction_1 = Fraction(-1, 2)
        fraction_2 = Fraction(1, -2)
        self.assertEqual(fraction_1, fraction_2)

    def test_simplification(self):
        """Test that an equivalent fraction is equal in value."""
        fraction_1 = Fraction(1, 2)
        fraction_2 = Fraction(2, 4)
        self.assertEqual(fraction_1, fraction_2)

    def test_diff_signs_inequality(self):
        """Test that two fractions with equal absolute value but different sign are not equal."""
        fraction_1 = Fraction(-1, 2)
        fraction_2 = Fraction(1, 2)
        self.assertNotEqual(fraction_1, fraction_2)

class FractionsSimplificationTestCases(unittest.TestCase):
    def test_simple(self):
        """Test that two equivalent fractions are equal with the simplest simplification
        (numerator is multiple of denominator or vice versa)."""
        fraction_1 = Fraction(2, 4)
        fraction_2 = Fraction(1, 2)
        self.assertEqual(fraction_2, fraction_1.simplify())

    def test_negative(self):
        """Test that two equivalent negative fractions are equal with the simplest simplification
        (numerator is multiple of denominator or vice versa)."""
        fraction_1 = Fraction(-2, 4)
        fraction_2 = Fraction(-1, 2)
        self.assertEqual(fraction_2, fraction_1.simplify())

    def test_composite(self):
        """Test that two equivalent fractions are equal with harder simplification
        (numerator and denominator are composite numbers and aren't multiples of each other)."""
        fraction_1 = Fraction(4, 6)
        fraction_2 = Fraction(2, 3)
        self.assertEqual(fraction_2, fraction_1.simplify())

    def test_different_compositions_inequality(self):
        """Test that two fractions that are not equivalent are unequal after simplification."""
        fraction_1 = Fraction(4, 6)
        fraction_2 = Fraction(8, 10)
        self.assertNotEqual(fraction_2.simplify(), fraction_1.simplify())

class FractionsAddFractionsTestCases(unittest.TestCase):
    def test_add_simple(self):
        """Test addition with the same denominator."""
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("3/4", str(res))

    def test_add_self_neg_simple(self):
        """Test addition with the same denominator and a negative self."""
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("1/4", str(res))

    def test_add_other_neg_simple(self):
        """Test addition with the same denominator and a negative other."""
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("-1/4", str(res))

    def test_add_both_neg_simple(self):
        """Test addition with the same denominator and two negatives."""
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("-3/4", str(res))

class FractionsSubFractionsTestCases(unittest.TestCase):
    def test_sub_simple(self):
        """Test subtraction with the same denominator."""
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("-1/4", str(res))

    def test_sub_self_neg_simple(self):
        """Test subtraction with the same denominator and a negative self."""
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("-3/4", str(res))

    def test_sub_other_neg_simple(self):
        """Test subtraction with the same denominator and a negative other."""
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("3/4", str(res))

    def test_sub_both_neg_simple(self):
        """Test subtraction with the same denominator and two negatives."""
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("1/4", str(res))


if __name__ == '__main__':
    unittest.main()
