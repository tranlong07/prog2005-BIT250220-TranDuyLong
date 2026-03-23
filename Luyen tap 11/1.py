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

arr = []
for a in range(1, 6):
    n = input(f'nhap chuoi thu {a}: ')
    arr.append(n)
print(insert_sort(arr))