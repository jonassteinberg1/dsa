def recursive_bubble_sort(arr: list, i, j):
    if i <= len(arr) - 2 and j <= len(arr) - 1:
        if  arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
            recursive_bubble_sort(arr, i, j)
    elif i <= len(arr) - 2:
        if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j = i + 1
        recursive_bubble_sort(arr, i, j)
    elif i <= len(arr) - 2 and j <= len(arr) - 1:
        j += 1
        recursive_bubble_sort(arr, i, j)
    else:
        recursive_bubble_sort(arr, i, j)
    return arr

recursive_bubble_sort([3, 1, 2, 4, 0], 0, 1)

