import unittest
from fractions import Fraction


class FractionsReprTestCases(unittest.TestCase):
    def test_simple(self):
        new_fraction = Fraction(1, 2)
        self.assertEqual("1/2", str(new_fraction))

    def test_negative_numerator(self):
        new_fraction = Fraction(-1, 2)
        self.assertEqual("-1/2", str(new_fraction))

    def test_negative_denominator(self):
        new_fraction = Fraction(1, -2)
        self.assertEqual("-1/2", str(new_fraction))

    def test_negative_both(self):
        new_fraction = Fraction(-1, -2)
        self.assertEqual("1/2", str(new_fraction))

class FractionsEqualityTestCases(unittest.TestCase):
    def test_simple(self):
        fraction_1 = Fraction(1, 2)
        fraction_2 = Fraction(1, 2)
        self.assertEqual(fraction_1, fraction_2)

    def test_negative_equality(self):
        fraction_1 = Fraction(-1, 2)
        fraction_2 = Fraction(1, -2)
        self.assertEqual(fraction_1, fraction_2)

    def test_simplification(self):
        fraction_1 = Fraction(1, 2)
        fraction_2 = Fraction(2, 4)
        self.assertEqual(fraction_1, fraction_2)

class FractionsSimplificationTestCases(unittest.TestCase):
    def test_simple(self):
        fraction_1 = Fraction(2, 4)
        fraction_2 = Fraction(1, 2)
        self.assertEqual(fraction_2, fraction_1.simplify())

    def test_negative(self):
        fraction_1 = Fraction(-2, 4)
        fraction_2 = Fraction(-1, 2)
        self.assertEqual(fraction_2, fraction_1.simplify())

    def test_composite(self):
        fraction_1 = Fraction(4, 6)
        fraction_2 = Fraction(2, 3)
        self.assertEqual(fraction_2, fraction_1.simplify())

class FractionsAddTestCases(unittest.TestCase):
    def test_add_simple(self):
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("3/4", str(res))

    def test_add_self_neg(self):
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("1/4", str(res))

    def test_add_other_neg(self):
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("-1/4", str(res))

    def test_add_both_neg(self):
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 + fraction_2
        self.assertEqual("-3/4", str(res))

class FractionsSubTestCases(unittest.TestCase):
    def test_sub_simple(self):
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("-1/4", str(res))

    def test_sub_self_neg(self):
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("-3/4", str(res))

    def test_sub_other_neg(self):
        fraction_1 = Fraction(1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("3/4", str(res))

    def test_sub_both_neg(self):
        fraction_1 = Fraction(-1, 4)
        fraction_2 = Fraction(-2, 4)
        res = fraction_1 - fraction_2
        self.assertEqual("1/4", str(res))


if __name__ == '__main__':
    unittest.main()
