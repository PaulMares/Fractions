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
        self.denominator = abs(denominator)


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
            raise NotImplementedError(f"Operations with {other.__class__} not supported (yet (if reasonable))")

    def __ne__(self, other:Self|int) -> bool:
        """Check if self's value is not equal to other.
        Simplifies Fraction types before testing.
        Currently supports Fraction and int.

        :param other: Another Object to test against.
        :return: True if self is not equal to other, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other:Self|int) -> bool:
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) > (other.numerator * self.denominator)
        elif isinstance(other, int):
            return self.numerator > (other * self.denominator)
        else:
            raise NotImplementedError(f"Operations with {other.__class__} not supported (yet (if reasonable))")

    def __le___(self, other:Self|int) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other:Self|int) -> bool:
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) >= (other.numerator * self.denominator)
        elif isinstance(other, int):
            return self.numerator >= (other * self.denominator)
        else:
            raise NotImplementedError(f"Operations with {other.__class__} not supported (yet (if reasonable))")

    def __lt__(self, other:Self|int) -> bool:
        return not self.__ge__(other)

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
            raise NotImplementedError(f"Operations with {other.__class__} not supported (yet (if reasonable))")

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

    def __mul__(self, other:Self|int) -> Self:
        """Multiplies self and other.
        Currently supports Fraction and int.

        :param other: Object to perform multiplication with.
        :return: A Fraction that is the result of multiplying self and other, simplified."""
        if isinstance(other, Fraction):
            new_frac = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            new_frac = Fraction(self.numerator * other, self.denominator)
        else:
            raise NotImplementedError("Operations with {other.__class__} not supported (yet (if reasonable))")

        return new_frac.simplify()

    def __truediv__(self, other:Self|int) -> Self:
        """Divides self by other.
        Currently supports Fraction and int.

        :param other: Object to perform division with.
        :return: A Fraction that is the result of dividing self by other, simplified."""
        if isinstance(other, Fraction):
            new_frac = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int):
            new_frac = Fraction(self.numerator, self.denominator * other)
        else:
            raise NotImplementedError("Operations with {other.__class__} not supported (yet (if reasonable))")

        return new_frac.simplify()

    def __pow__(self, power) -> Self:
        return Fraction(self.numerator ** power, self.denominator ** power)

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def __floor__(self):
        return Fraction(self.numerator - (self.numerator % self.denominator), self.denominator)

    def __ceil__(self):
        return Fraction(self.numerator + self.denominator - (self.numerator % self.denominator), self.denominator)

    def __floordiv__(self, other:Self|int) -> int:
        return (self.__truediv__(other)).__int__()

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def simplify(self) -> Self:
        """Simplifies self (not in-place) to its simplest form.

        :return: A simplified Fraction object.
        """
        gcd = greatest_common_divisor(self.denominator, self.numerator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def self_simplify(self):
        """Simplifies self (in-place) to its simplest form."""
        simp = self.simplify()
        self.numerator = simp.numerator
        self.denominator = simp.denominator

    def equal_approx(self, other:Self|int, threshold:Self|int=None) -> bool:
        """Checks if other is approximately equal to self by checking if it's within threshold of self.
        Threshold is an absolute magnitude and is checked as (self - threshold) and as (self + threshold).
        Threshold defaults to 1/1000.
        Currently supports Fraction and int.

        :param other: The object to compare to.
        :param threshold: The maximum difference allowed between self and other. Checked in both directions.
        :return: True if other is between self and self + threshold (or between self and self - threshold),
        False otherwise.
        """
        if threshold is None:
            threshold = Fraction(1, 1000)

        threshold = abs(threshold)

        return self.__add__(threshold) > other > self.__sub__(threshold)

def least_common_multiplier(x:int, y:int) -> int:
    """Finds the least common multiplier for two int.

    :param x: The first int.
    :param y: The second int.
    :return: The least common multiplier for x and y.
    """
    return abs(int(x / greatest_common_divisor(x, y)) * y)

def greatest_common_divisor(x:int, y:int) -> int:
    """Finds the greatest common divisor for two int.

    :param x: The first int.
    :param y: The second int.
    :return: The greatest common divisor for x and y.
    """
    a = abs(x)
    b = abs(y)

    if a == b:
        return x

    while b != 0:
        t = b
        b = a % b
        a = t

    return a

def float_to_fraction(x:float, decimal_places=-1) -> Fraction:
    """Converts a float to a Fraction.
    Iteratively multiplies the float by 10 until it becomes an int (or reaches the specified number of decimal places),
    then sets the denominator to the appropriate exponentiation of 10 to make a Fraction of equal value.

    :param x: The float to convert ot a Fraction.
    :param decimal_places: The number of decimal places that will be used for the denominator. If negative, will use all
                           decimal places. Defaults to -1 (all decimal places).
    :return: A Fraction with the same value as the given float.
    """
    denominator = 1
    while (x % 1) != 0 and decimal_places != 0:
        denominator *= 10
        x *= 10
        decimal_places -= 1
    return Fraction(int(x), denominator).simplify()