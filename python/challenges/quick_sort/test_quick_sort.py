import quick_sort

def test_merge_sort():
    assert quick_sort


def test_merge_sort_1():
    arr = [8,4,23,42,16,15]
    left = 0
    n = len(arr)
    right = n - 1
    result = quick_sort.quick_sort(arr,left,right)
    assert result == [4,8,15,16,23,42]


def test_merge_sort_2():
    arr = [20,18,12,8,5,-2]
    left = 0
    n = len(arr)
    right = n - 1
    result = quick_sort.quick_sort(arr,left,right)
    assert result == [-2,5,8,12,18,20]


def test_merge_sort_3():
    arr = [5,12,7,5,5,7]
    left = 0
    n = len(arr)
    right = n - 1
    result = quick_sort.quick_sort(arr,left,right)
    assert result == [5,5,5,7,7,12]


def test_merge_sort_4():
    arr = [2,3,5,7,13,11]
    left = 0
    n = len(arr)
    right = n - 1
    result = quick_sort.quick_sort(arr,left,right)
    assert result == [2,3,5,7,11,13]