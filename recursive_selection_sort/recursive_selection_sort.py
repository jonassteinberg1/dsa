def recursive_selection_sort(arr: list, i: int=0):
    
    # base case
    if i > len(arr)-2:
        return arr
    
    # iteration
    min_index = i
    for idx in range(i+1, len(arr)):
        if arr[idx] < arr[min_index]:
            min_index = idx
    arr[i], arr[min_index] = arr[min_index], arr[i]
    # recursion
    recursive_selection_sort(arr, i+1)
    # uncertain if this is needed
    return arr