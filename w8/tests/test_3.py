import pytest
from tasks.t3 import my_map, my_zip, my_enumerate

@pytest.mark.parametrize('a,b', [(['a', 'b', 'c'], [1, 2, 3]), (['a', 's', 'd', 'f'], [1, 2, 3])])
def test_zip(a, b):
    assert my_zip(a, b) == zip(a, b)

@pytest.mark.parametrize('f,i', [(str, [1, 2, 3]), (int, ['1', '2', '3'])])
def test_map(f, i):
    assert my_map(f, i) == map(f, i)

@pytest.mark.parametrize('somelist', [([1, 2, 3, 4, 5, 6, 7, 8])])
def test_enumerate(somelist):
    assert my_enumerate(somelist) == enumerate(somelist)
