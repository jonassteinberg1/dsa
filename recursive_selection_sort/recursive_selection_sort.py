def recursive_selection_sort(arr: list, i=0, j=1, min_index = 0):
    
    # base case
    if i > len(arr)-2:
        return arr
    
    # iteration
    for j in range(j, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            min_index = i
    # recursion
    recursive_selection_sort(arr, i+1, i+2, min_index=i+1)
    # uncertain if this is needed
    return arr
