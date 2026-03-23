def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print (f'Chon {arr[i]} lam key')
        j = i - 1
        while j >= 0 and len(arr[j]) < len(key):
            arr[j + 1] = arr[j]
            j -= 1
            print('Chuyen sang so khac trong day thanh key')
        arr[j + 1] = key
        print(f'sau khi chen key la : {arr}')
    return arr
def binary_search(arr,x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = []
for a in range(1, 6):
    n = input(f'nhap chuoi thu {a}: ')
    arr.append(n)
print(insert_sort(arr))

arr.sort()
print(arr)
x = input('chuoi can tim: ')
c = binary_search(arr,x)
if c!=-1:
    print(f'tim thay tai vi tri {c}')
else:
    print("chịu")