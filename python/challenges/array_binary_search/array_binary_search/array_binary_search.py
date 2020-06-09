#linear 
def BinarySearch(arr, n):
    """[Without utilizing any of the built-in methods available 
    to your language, return the index of the array’s element 
    that is equal to the search key, 
    or -1 if the element does not exist.]

    Args:
        arr ([list]): [sorted array]
        n ([type]): [search key]
    """
    count = 0
    if n not in arr:
        return -1
    for i in arr:
        if i == n:
            return count
        count += 1

arr1 = [4,8,15,16,23,42]
key = 15
arr2 = [11,22,33,44,55,66,77]
key2 = 90
print(BinarySearch(arr1, key))
print(BinarySearch(arr2, key2))

#recursive
def BinarySearch2(arr, n):
    """[test split in half]

    Args:
        arr ([list]): [description]
        n ([integer]): [description]
    """
    middle = len(arr) // 2
    #print(middle)
    print(f"n is {n} and arr middle is {arr[middle]}")
    if n == arr[middle]:
        return n
    elif arr == []:
        return -1
    elif n < arr[middle]:
        arr = arr[:middle]
        print(arr[0])
        BinarySearch2(arr, n)
    elif n > arr[middle]:
        arr = arr[middle+1:]
        print(arr)
        BinarySearch2(arr, n)
        

#print(BinarySearch2(arr1, key))
#print(BinarySearch2(arr2, key2))
