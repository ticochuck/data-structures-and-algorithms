from array_binary_search import __version__
from array_binary_search.array_binary_search import BinarySearch

def test_version():
    assert __version__ == '0.1.0'


def test_pass():
    actual = BinarySearch([1,2,3,4,5,6], 4)
    expected = 3
    assert actual == expected


def test_fail():
    actual = BinarySearch([1,2,3,4,5,6], 4)
    expected = 0
    assert actual != expected