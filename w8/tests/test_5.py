from tasks.task5 import get_permutations
import pytest

def test_get_permutations():
    assert get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"]
    assert get_permutations("kiwi", 3) == ['iik', 'iik', 'iiw', 'iiw', 'iki', 'iki', 'ikw', 'ikw', 'iwi', 'iwi', 'iwk', 'iwk', 'kii', 'kii', 'kiw', 'kiw', 'kwi', 'kwi', 'wii', 'wii', 'wik', 'wik', 'wki', 'wki']
