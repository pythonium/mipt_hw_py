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


print(MyComplexMath.sqrt(-4))
print(MyMath.sqrt(-4))


#staticmethod ничего не сможет сделать с классом, а нам нужно было, чтобы метод мог использовать какую-то информацию о классе, поэтому classmethod
