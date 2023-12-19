import math
from math import gcd
class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """Initialize a Fraction object.

        PRE: num and den have to be a integer, den have to be different from 0
        POST: Fraction is initialized with the given numerator and denominator,
              reduced to its simplest form.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
         
        common = math.gcd(num, den)
        self.num = num // common
        self.den = den // common
    @property
    def numerator(self):
        """Get the numerator of the fraction.

        PRE: self have to be a fraction and self.num have to be defined
        POST: Returns the numerator of the fraction.
        """
        return self.num
    
    @property
    def denominator(self):
        """Get the denominator of the fraction.

        PRE: self have to be a fraction and self.den have to be defined
        POST: Returns the denominator of the fraction.
        """
        return self.den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction.

        PRE: self have to be a fraction self.num and self.den have to be defined
        POST: Returns a string representation of the fraction.
        """
        return f"{self.num}/{self.den}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        PRE: self have to be a fraction and self.num and self.den have to be defined
        POST: Returns a string representation of the fraction as a mixed number.
        """
        whole_part = self.num // self.den
        remainder = self.num % self.den
        return f"{whole_part} {remainder}/{self.den}"

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions.
        
        PRE: self and other have to be a fraction, other.den have to be different from 0?
             self.num and self.den have to be defined
        POST: Returns a new Fraction object representing the sum of self and other.
        """
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE: other and self have to be a fraction, other.den have to be different from 0,
             self.num and self.den have to be defined
        POST: Returns a new Fraction object representing the difference of self and other.
        """
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)


    def __mul__(self, other):
        """Overloading of the * operator for fractions.

        PRE: other and self have to be a fraction, other.den have to be different from 0,
             self.num and self.den have to be defined
        POST: Returns a new Fraction object representing the product of self and other.
        """
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions.

        PRE: other have to be a fraction, other.den and other.num have to be different from 0,
             self.num and self.den have to be defined
        POST: Returns a new Fraction object representing the division of self by other.
        """
        if other.den == 0 or other.num == 0:
            raise ValueError("Denominator and Nominator of the divisor cannot be zero.")

        new_num = self.num * other.den
        new_den = self.den * other.num

        return Fraction(new_num, new_den)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE: other and self have to be a fraction, self.den have to be different from 0,
             self.num and self.den have to be defined
        POST: Returns a new Fraction object representing self raised to the power of the given exponent.
        """
        new_num = self.num ** (other.num / other.den)
        new_den = self.den ** (other.num / other.den)

        return Fraction(new_num, new_den)
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions.

        PRE: other and self have to be a fraction, self.num and self.den have to be defined
        POST: Returns True if self is equal to other, False otherwise.
        """
        return self.num * other.den == other.num * self.den
        
    def __float__(self) :
        """Returns the decimal value of the fraction.

        PRE: self have to be a fraction, self.num and self.den have to be defined
        POST: Returns the decimal value of the fraction as a float.
        """
        return self.num / self.den
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0.
        PRE: self have to be a fraction and self.num have to be defined
        POST: Returns True if the fraction is zero, False otherwise.
        """
        return self.num == 0


    def is_integer(self):
        """Check if a fraction is an integer.

        PRE: self have to be a fraction and self.den have to be defined
        POST: Returns True if the fraction is an integer, False otherwise.
        """
        return self.den == 1
    
    def is_proper(self):
        """Check if the absolute value of the fraction is less than 1.

        PRE: self have to be a fraction, self.num and self.den have to be defined
        POST: Returns True if the fraction is a proper fraction, False otherwise.
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE: self have to be a fraction and self.num have to be defined
        POST: Returns True if the fraction is a unit fraction, False otherwise.
        """
        return self.num == 1

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction.

        PRE: self and other have to be a fraction, self.num and self.den have to be defined
        POST: Returns True if the absolute value of the difference between self and other is a unit fraction, False otherwise.
        """
        return abs(self.num * other.den - other.num * self.den) == 1

