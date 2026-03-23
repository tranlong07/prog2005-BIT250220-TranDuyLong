import math
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,29]
n = int(input('nhap so phan tu muon them vao: '))
for i in range(1, n+1):
    b = int(input(f'nhap phan tu thu {i}:  '))
    a.append(b)
print(a)
dem = 0
tong_snt = 0
d =[]
c = int(input('nhap so muon check: '))
for j in a:
    if j == c:
        dem += 1
print(f'so lan xuat hien cua {j} la {dem}')
for k in a:
    e = True
    if k < 2:
        continue
    for n in range(2, int(math.sqrt(k))+1):
        if k % n == 0:
            e = False
            break
    if e:
        d.append(k)
print('day snt la', d)
for m in d:
    tong_snt += m
print('tong snt la: ', tong_snt)
print('sap xep dsach',sorted(a))
print('sap xep dsach',sorted(d))
a.clear()
d.clear()
print(a)
print(d)

