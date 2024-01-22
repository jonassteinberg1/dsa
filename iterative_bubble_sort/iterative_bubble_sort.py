def iterative_bubble_sort(arr: list):
    i, j = 0, 1
    while i <= len(arr) - 2 and j <= len(arr) - 1:
        if arr[i] > arr[j] and j < len(arr) - 1:
            arr[i], arr[j] = arr[j], arr[i]
            j = j + 1
        elif arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j = i + 1
        elif j < len(arr) - 1:
            j += 1
        else:
            i += 1
            j = i + 1

    return arr