from tasks.task9 import quad_sum, maximize
import pytest

@pytest.mark.parametrize(('input', 'exp_output'), [([[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]], 206)], ([[9, -7, 1, 6, 3, 9], [874, 465, -4], [1, 1, 1], [6, 6, 6]], 758))
def test_maximize():

    assert maximize(input, m = 1000) == exp_output
