def bubble_sort(arr):
    dem = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            dem += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, dem
print(bubble_sort([5,2,8,1,3]))

