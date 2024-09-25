from typing import Self

class Fraction:
    def __init__(self, numerator:int, denominator:int):
        """Create a new fraction.

        :param numerator: The numerator of the fraction.
        :param denominator: The denominator of the fraction.
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError(f"Numerator and denominator must be integers, got {numerator}, {denominator}")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator if denominator > 0 else -numerator
        self.denominator = denominator if denominator > 0 else -denominator


    def __repr__(self) -> str:
        """Return a string representation of the fraction.

        :return: Returns the fraction as a string of form 'numerator/denominator'.
        """
        return "%d/%d" % (self.numerator, self.denominator)

    def __eq__(self, other:Self|int) -> bool:
        """Check if self's value is equal to other.
        Simplifies Fraction types before testing.
        Currently supports Fraction and int.

        :param other: Another Object to test against.
        :return: True if self is equal to other, False otherwise.
        """
        self_simp = self.simplify()
        if isinstance(other, Fraction):
            other_simp = other.simplify()
            return self_simp.numerator == other_simp.numerator and self_simp.denominator == other_simp.denominator
        elif isinstance(other, int):
            return self_simp.numerator == other and self_simp.denominator == 1
        else:
            return False

    def __add__(self, other:Self|int) -> Self:
        """Adds self and other.
        Currently supports Fraction and int.

        :param other: Object to perform addition with.
        :return: A Fraction that is the result of adding self and other, simplified.
        """
        if isinstance(other, Fraction):
            if self.denominator == other.denominator:
                new_frac = Fraction(self.numerator + other.numerator, self.denominator)
            else:
                lcm = least_common_multiplier(self.denominator, other.denominator)
                new_frac = Fraction(((self.numerator * int(lcm / self.denominator)) +
                                    (other.numerator * int(lcm / other.denominator))),
                                    lcm)
        elif isinstance(other, int):
            new_frac = Fraction(self.numerator + (other * self.denominator), self.denominator)
        else:
            raise NotImplementedError(f"Addition with {other.__class__} not supported (yet (if reasonable))")

        if new_frac.numerator < 0:
            new_frac.positive = False
        return new_frac.simplify()

    def __neg__(self) -> Self:
        """Negation of the fraction.

        :return: The negative of itself.
        """
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self, other:Self|int) -> Self:
        """Subtracts other from self.
        Currently supports Fraction and int.

        :param other: Object to perform subtraction with.
        :return: A Fraction that is the result of subtracting other from self, simplified.
        """
        return self.__add__(-other)

    def simplify(self) -> Self:
        """Simplifies self to its simplest form.

        :return: A simplified Fraction object.
        """
        if (self.numerator / self.denominator) % 1 == 0:
            return Fraction(int(self.numerator / self.denominator), 1)
        elif (self.denominator / self.numerator) % 1 == 0:
            return Fraction(1, int(self.denominator / self.numerator))
        else:
            return self

    def self_simplify(self):
        """Simplifies self in place."""
        simp = self.simplify()
        self.numerator = simp.numerator
        self.denominator = simp.denominator

def least_common_multiplier(x:int, y:int) -> int:
    """Finds the least common multiplier for two int.

    :param x: The first int.
    :param y: The second int.
    :return: The least common multiplier for x and y.
    """
    return x * y  # TODO: Change to calculate lcm