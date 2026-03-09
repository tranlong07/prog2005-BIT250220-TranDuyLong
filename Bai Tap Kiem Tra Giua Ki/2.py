import math

def selection_sort(a):
    n = len(a)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[max_idx], a[i] = a[i], a[max_idx]
    return a
a = []
for i in range(17, 112):
    if i % 2 != 0:
        a.append(i)
print("Dãy số lẻ tăng dần là:", selection_sort(a))
Day_SNT = []
for i in range(17, 112):
    SNT = True
    if i < 2:
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            SNT = False
            break
    if SNT:
        Day_SNT.append(i)
print("Các số nguyên tố trong danh sách là:", Day_SNT)