def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f'lan lap thu {i}')
        for j in range(0, n-i-1):
            print(f'so sanh {j} va {j+1}')
            if len(arr[j]) < len(arr[j+1]):
                print('doi cho')
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr
a = []
for i in range(5):
    s = input(f'nhap chuoi: ')
    a.append(s)

print(bubble_sort(a))