# chatgpt
def iterative_traditional_bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [6, 5, 4, 4, 0, 1, 2, 3]
print(iterative_traditional_bubble_sort(arr))