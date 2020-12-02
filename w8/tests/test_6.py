from tasks.task6 import get_combinations
import pytest


def test_get_combinations():
    assert get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"]
    assert get_combinations("kiwi", 3) == ['k', 'i', 'w', 'i', 'ik', 'kw', 'ik', 'iw', 'ii', 'iw', 'ikw', 'iik', 'ikw', 'iiw']
