#def recursive_traditional_bubble_sort(arr: list, i=0):
#    # base case
#    if i >= len(arr) - i:
#        return arr
#    
#    if arr[i] > arr[i+1]:
#        arr[i], arr[i+1] = arr[i+1], arr[i]
#        return recursive_traditional_bubble_sort(arr, 0)
#    else:
#        return recursive_traditional_bubble_sort(arr, i + 1)

# chatgpt version
def recursive_traditional_bubble_sort(arr, n=None):
    # handles case of empty list
    # 'n' is better thought of as the
    # length of the list *left* to sort
    if n is None:
        n = len(arr)
    
    # Base case: when the length of
    # the list left to sort is 1
    # the list is fully sorted
    if n == 1:
        return arr

    # the leftward indexes are the last
    # to be sorted so we're decrementing
    # the length of the list left to be
    # sorted *from the left* hence n - 1
    #
    # bubble sort requires comparing every
    # element against all others so there
    # needs to be a way to iterate over remaining
    # list member: the for loop works for this
    # because its native incrementation can be used
    # as a way to increment the list indexes being
    # compared
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # adds another frame to the call stack where
    # the length of the list is decremented
    # by one. we're used to list lengths staying
    # the same and to be sure ours does -- but the length
    # being measured here is the rest of the list
    # to still be sorted and in bubble sort that's the
    # left portion, hence decrementing from right to left 
    recursive_traditional_bubble_sort(arr, n - 1)

    return arr

    
print(recursive_traditional_bubble_sort([-3, -1, -2]))
