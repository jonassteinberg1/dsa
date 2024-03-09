def iterative_insertion_sort(arr: list):
    
    for j in range(1, len(arr)):
        hold = None
        for i in range(j-1, -1, -1):
            if arr[j] < arr[i] and hold is None:
                hold = i
            elif arr[j] < arr[i] and arr[j] < arr[hold]:
                hold = i
        if hold is None:
            continue
        else:
            arr[hold], arr[hold+1:j+1] = arr[j], arr[hold:j]
        
    return arr

#iterative_insertion_sort([1, 1, 1, 1, 1])
