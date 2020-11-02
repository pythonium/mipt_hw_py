import math
from my_mathematics.math import MyMath, MyComplexMath, Complex
from my_mathematics.linear_algebra import Vector
import math
import cmath
import pytest

@pytest.mark.parametrize('x',[(0),(1),(2),(3)])
def test_sin(x):
    assert MyMath.sin(x) == math.sin(x)

@pytest.mark.parametrize('x',[(2),(4),(16),(25)])
def test_sqrt(x):
    assert MyMath.sqrt(x) == math.sqrt(x)


@pytest.mark.parametrize('x',[(-2),(4),(-16),(25)])
def test_complex_sqrt(x):
    assert MyMath.sqrt(x) == cmath.sqrt(x)

@pytest.mark.parametrize('inp, exp',[(Complex(1, 2) + Complex(3, 4), "4 + 6i"), (Complex(2, 4) + Complex(4, -16), "6 -12i")])
def test_complex_add(inp, exp):
    assert inp == exp

@pytest.mark.parametrize('inp, exp',[(Complex(1, 2) - Complex(3, 4), "-2 -2i"), (Complex(2, 4) - Complex(4, -16), "-2 + 20i")])
def test_complex_sub(inp, exp):
    assert inp == exp

@pytest.mark.parametrize('inp, exp',[(Complex(1, 2) * Complex(3, 4), "-5 + 10i"), (Complex(2, 4) * Complex(4, -16), "72 -16i")])
def test_complex_mul(inp, exp):
    assert inp == exp

@pytest.mark.parametrize('inp, exp',[(Complex(1, 4) / Complex(2, 8), "0.5 + 0i"), (Complex(-2, 1) / Complex(1, -1), "-1.5 -0.5i")])
def test_complex_div(inp, exp):
    assert inp == exp

@pytest.mark.parametrize('inp, exp',[(abs(Complex(8, 6)), 10), (abs(Complex(3, 4)), 5), abs((Complex(12, 5)), 13)])
def test_complex_abs(inp, exp):
    assert inp == exp
