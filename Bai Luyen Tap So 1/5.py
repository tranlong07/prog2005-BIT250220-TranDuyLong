m = int(input('Nhap so hang: '))
n = int(input('Nhap so cot: '))
A = []
print('Nhap cac phan tu trong mat tran: ')
for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        row.append(x)
    A.append(row)
print('Ma Tran: ')
for row in A:
    print(row)
r = int(input('Nhap hang can xem (r-1): '))
print('Hang',r,'la:',A[r])
c = int(input('Nhap cot can xem (c-1) : '))
col = []
for i in range(m):
    col.append(A[i][c])
print(f'Cot {c} la: ', col)
max_value = A[0][0]
for i in range(m):
    for j in range(n):
        if A[i][j] > max_value:
            max_value = A[i][j]
print('GTLN La: ', max_value)