from tasks.task4 import get_cartesian_product
import pytest


def test_get_cartesian_product():
    assert get_cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert get_cartesian_product([1, 34, 47], [31, 47, 90]) == [(1, 31), (1, 47), (1, 90), (34, 31), (34, 47), (34, 90), (47, 31), (47, 47), (47, 90)]
