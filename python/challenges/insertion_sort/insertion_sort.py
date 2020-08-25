def insertion_sort(arr):

    for i in range(1, len(arr)):

        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j -1

        arr[j+1] = temp
        print(arr)
    
    return arr



arr = [8,4,23,42,16,15]
insertion_sort(arr)
