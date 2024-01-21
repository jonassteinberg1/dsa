def mergeSortIterative(arr: list):
    dac(arr)
    sort(arr)

def dac(arr: list):
    
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        elif arr[0] <= arr[1]:
            continue
    
    compare(2, 3)
    compare(3, 4)

def sort(arr: list):
    pass

mergeSortIterative([1, 2, 6, 3, 9, 9, 0])
