def iterative_bubble_sort(arr: list):
    i, j = 0, 1
    while i <= len(arr) - 2 and j <= len(arr) - 1:
        # swap and since j isn't at the end of the array
        # it could still be the case that one of the
        # other numbers needs to be swapped
        if arr[i] > arr[j] and j < len(arr) - 1:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        # swap but since j is at the end of the array
        # then it could not be the case that another
        # number may need to be swapped hence
        # now move left up and compare
        elif arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j = i + 1
        # no swap and j still has room
        elif j < len(arr) - 1:
            j += 1
        # no swap but j was at the end
        # so we move both left and right up
        else:
            i += 1
            j = i + 1

    return arr