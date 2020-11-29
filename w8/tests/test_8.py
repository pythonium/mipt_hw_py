from tasks.task8 import compress_string
import pytest

@pytest.mark.parametrize(('input', 'exp_output'), [('1222311', [(1, '1'), (3, '2'), (1, '3'), (2, '1')]), ('ayyylmaooooo', [(1, 'a'), (3, 'y'), (1, 'l'), (1, 'm'), (1, 'a'), (5, 'o')])])
def test_compress_string(input, exp_output):
    assert compress_string(input) == exp_output
