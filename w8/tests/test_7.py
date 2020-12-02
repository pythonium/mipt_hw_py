from tasks.task7 import get_combinations_with_r
import pytest


def test_get_combinations_with_r():
    assert get_combinations_with_r("cat", 2) == ["aa", "ac", "at", "cc", "ct", "tt"]
    assert get_combinations_with_r("kiwi", 3) == ['iii', 'iii', 'iii', 'iii', 'iik', 'iik', 'iik', 'iiw', 'iiw', 'iiw', 'ikk', 'ikk', 'ikw', 'ikw', 'iww', 'iww', 'kkk', 'kkw', 'kww', 'www']
