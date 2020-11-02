import math
import cmath

class MyMath:

    pi = 3.14
    _complex = False  #encapsulation


    @staticmethod
    def sin(x):
        return math.sin(x)


    @classmethod
    def is_complex(cls):   #polymorphism
        return cls._complex

    @classmethod
    def sqrt(cls, x):

        if cls.is_complex():
                cmplx = cmath.sqrt(x)
                return (cmplx.real, cmplx.imag)
        elif x >= 0:
                return math.sqrt(x)

        else:
                raise ValueError("cannot extract square root from negative number")



class MyComplexMath(MyMath):     #inheritance

    _complex = True


class Complex:


    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag

    def __str__(self):
        return f'{self.__real} + {self.__imag}i' if self.__imag >= 0 else f'{self.__real} {self.__imag}i'

    def __add__(self, other):
        return Complex(self.__real + other.__real, self.__imag + other.__imag)

    def __sub__(self, other):
        return Complex(self.__real - other.__real, self.__imag - other.__imag)

    def __truediv__(self, other):
        a1 = self.__real
        a2 = other.__real
        b1 = self.__imag
        b2 = other.__imag
        divisor = a2**2 + b2 **2
        return Complex((a1*a2 + b1*b2)/divisor, (b1*a2 - a1*b2)/divisor)

    def __mul__(self, other):
        return Complex(self.__real * other.__real - self.__imag * other.__imag, self.__real * other.__imag + self.__imag * other.__real)

    def __abs__(self):
        return math.sqrt(self.__real**2 + self.__imag**2)

    def arg(self):
        return math.asin(self.__imag/abs(self))

    def __pow__(self, n):
        return Complex((abs(self)**n)*math.cos(n*self.arg()), (abs(self)**n)*math.sin(n*self.arg()))

    def __neg__(self):
        return Complex(-self.__real, -self.__imag)
