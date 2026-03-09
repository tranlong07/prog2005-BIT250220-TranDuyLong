n = int(input("Cỡ của mảng: "))
x = []

for i in range(n):
    y = float(input(f"Nhập phần tử thứ {i}: "))
    x.append(y)

def selection_sort(a):
    n = len(a)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
        print(f"Kết quả sau bước {i+1}: {a}")
    return a

print("Mảng theo thứ tự giảm dần là:", selection_sort(x))
