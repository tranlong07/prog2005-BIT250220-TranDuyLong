n = int(input('Nhap so luong: '))
dic = {}
tong_so_tuoi = 0
dem = 0
for i in range(1, n+1):
    x = input(f'sv{i}: ')
    y = int(input(f'tuoi sv{i}: '))
    dic[x] = y
print(dic)
for i in dic:
    tong_so_tuoi += dic[i]
    dem += 1
tuoi_tb = tong_so_tuoi / dem
print("Tuoi trung binh:", tuoi_tb)

def selection_sort(dic):
    a = list(dic.items())
    b = len(a)
    for i in range(b):
        max_idx = i
        for j in range(i + 1, b):
            if a[j][1] > a[max_idx][1]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a
print(selection_sort(dic))