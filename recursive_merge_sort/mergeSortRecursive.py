def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)
    print(arr)

def merge(arr, left, right):
    i = j = k = 0

    # Compare left and right array values
    # and merge to arr
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # merge any left leftovers
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # same but right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

mergeSort([6, 2, 7, 4, 1])