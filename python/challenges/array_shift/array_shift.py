arr = [4,8,15,23,42]
x = 16

def shift(arr, x):
    count = 0
    arra = []
    arrc = []
    arrb = [0]

    arrb[0] = x

    for i in arr:
        count += 1 

    if ((count / 2) % 2 == 0):
        middle = count / 2
    else: 
        middle = (count // 2) + 1 
    arra = arr[:middle]
    arrc = arr[middle:]
    arrd = arra + arrb + arrc

    print(arrd)

shift(arr, x)