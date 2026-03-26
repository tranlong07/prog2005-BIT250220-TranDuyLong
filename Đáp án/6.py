n = int(input('Nhập số lượng danh sách của bạn: '))
x = []
for i in range(1, n+1):
    a = int(input('Nhập số: '))
    x.append(a)
for j in x:
    if j > 10:
        print('Số đầu tiên > 10 là: ',j)
else:
        print('Không có số nào > 10')
