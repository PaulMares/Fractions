class Fraction:
    def __init__(self, numerator:int, denominator:int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError(f"Numerator and denominator must be integers, got {numerator}, {denominator}")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator if denominator > 0 else -numerator
        self.denominator = denominator if denominator > 0 else -denominator


    def __repr__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            if self.denominator == other.denominator:
                new_frac = Fraction(self.numerator + other.numerator, self.denominator)
            else:
                lcm = least_common_multiplier(self.denominator, other.denominator)
                new_frac = Fraction(((self.numerator * int(lcm / self.denominator)) +
                                    (other.numerator * int(lcm / other.denominator))),
                                    lcm)
        elif isinstance(other, int):
            return Fraction(self.numerator + (other * self.denominator), self.denominator)
        else:
            raise NotImplementedError(f"Addition with {other.__class__} not supported (yet (if reasonable))")

        if new_frac.numerator < 0:
            new_frac.positive = False
        return new_frac

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self, other):
        return self.__add__(-other)

    def simplify(self):
        if (self.numerator / self.denominator) % 1 == 0:
            return Fraction(int(self.numerator / self.denominator), 1)
        elif (self.denominator / self.numerator) % 1 == 0:
            return Fraction(1, int(self.denominator / self.numerator))

    def self_simplify(self):
        simp = self.simplify()
        self.numerator = simp.numerator
        self.denominator = simp.denominator

def least_common_multiplier(x:int, y:int) -> int:
    return x * y  # TODO: Change to calculate lcm