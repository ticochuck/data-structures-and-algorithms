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

arr1 = [4,8,15,16,23,42]
key = 23
arr2 = [11,22,33,44,55,66,77]
key2 = 90

def test_passB2():
    actual = BinarySearch([4,8,15,16,23,42], 23)
    expected = 4
    assert actual == expected


def test_failB2():
    actual = BinarySearch([4,8,15,16,23,42], 23)
    expected = 1
    assert actual != expected


def test_passB2_not_in():
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected


def test_failB2_not_in():
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = 1
    assert actual != expected