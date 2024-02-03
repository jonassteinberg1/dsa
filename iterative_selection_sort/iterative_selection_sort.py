def iterative_selection_sort(arr: list):
    i = 0
    j = i+1
    min = arr[i]
    while i < len(arr)-1:
        while j < len(arr):
            if arr[j] < min:
                min = arr[j]
                arr[j] = arr[i]
                arr[i] = min
            j += 1
        i += 1
        min = arr[i]
        j = i+1
    
    return arr

#def main():
#    iterative_selection_sort([5, 0, 9, 1, 1, 2, 3, 0, 6, 3, 8])

#if __name__ == "__main__":
#    main()