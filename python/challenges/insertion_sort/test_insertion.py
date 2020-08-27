import insertion_sort

def test_insertion_sort():
    assert insertion_sort


def test_insertion_sort_1():
    arr = [8,4,23,42,16,15]
    result = insertion_sort.insertion_sort(arr)
    assert result == [4,8,15,16,23,42]


def test_insertion_sort_2():
    arr = [20,18,12,8,5,-2]
    result = insertion_sort.insertion_sort(arr)
    assert result == [-2,5,8,12,18,20]


def test_insertion_sort_3():
    arr = [5,12,7,5,5,7]
    result = insertion_sort.insertion_sort(arr)
    assert result == [5,5,5,7,7,12]


def test_insertion_sort_4():
    arr = [2,3,5,7,13,11]
    result = insertion_sort.insertion_sort(arr)
    assert result == [2,3,5,7,11,13]

