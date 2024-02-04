def iterative_selection_sort(arr: list):
    i = 0
    j = i+1
    while i < len(arr)-1:
        min_index = i
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
        i += 1
        j = i+1
    
    return arr
