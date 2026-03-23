
m = int(input('nhap so hang: '))
n = int(input('nhap so cot: '))
if m == '' or n == '':
    print('nhap lai : ')
else:
    A = []
    print('nhap cac phan tu trong ma tran: ')
    for i in range(1,m+1):
        row = []
        for j in range(1,n+1):
            x = int(input(f'A[{i}][{j}]= '))
            row.append(x)
        A.append(row)
    print('Ma Tran: ')
    for row in A:
        print(row)
    B = []
    print('nhap cac phan tu trong ma tran: ')
    for i in range(1,m+1):
        row = []
        for j in range(1,n+1):
            x = int(input(f'B[{i}][{j}]= '))
            row.append(x)
        B.append(row)
    print('Ma Tran: ')
    for row in B:
        print(row)
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    print('Ma tran tong: ')
    for row in C:
        print(row)