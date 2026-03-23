a = int(input('nhap day so cua ban: '))
b = []
c = []
tong = 0
for i in range(1, a+1):
    n = int(input(f'nhap phan tu {i}: '))
    b.append(n)
print(b)
for j in b:
    if j % 2 == 0:
        c.append(j)
print('day so chan la: ',c)
for k in c:
    tong += k
print('tong cac so chan la: ',tong)
