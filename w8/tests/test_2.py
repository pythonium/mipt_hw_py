from tasks.task2 import fib_gen
import pytest


def test_fib_gen():
    a = ([1, 1, 2], [1, 1, 2, 3, 5, 8], [1, 1, 2, 3, 5, 8, 13, 21])

    for i in a:
        n = len(a)
        assert list(fib_gen(n)) == i
