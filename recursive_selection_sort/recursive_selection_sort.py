def recursive_selection_sort(arr: list, i=0, j=1):
#    while i < len(arr)-1:
#        min_index = i
#        while j < len(arr):
#            if arr[j] < arr[min_index]:
#                min_index = j
#            j += 1
#        arr[i], arr[min_index] = arr[min_index], arr[i]
#        i += 1
#        j = i+1
    
    # base case
    if i >= len(arr)-1:
        return arr
    
    for i in range(i, len(arr)):
        min_index = i
        if arr[j] < arr[min_index]:
            min_index = j
            j += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    recursive_selection_sort(arr, i+1, i+2)

def main():
    recursive_selection_sort([5, 5, 0, 9, 3])

if __name__ == "__main__":
    main()
