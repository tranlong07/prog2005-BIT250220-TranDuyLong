n = int(input('Nhap so luong nhan vien: '))
d = []
for i in range(1,n+1):
    a = input(f'ten nhan vien {i}: ')
    b = input(f'nhap tuoi nhan vien {i}: ')
    c = input(f'id nhan vien {i}: ')
    d.append([a,b,c])
with open('nhanvien.txt','w', encoding='utf-8') as f:
    for nv in d:
        f.write(f'Ten: {nv[0]},Tuoi: {nv[1]},ID: {nv[2]}\n')
with open('nhanvien.csv','w', encoding='utf-8') as f:
    for nv in d:
        f.write(f'Ten: {nv[0]},Tuoi: {nv[1]},ID: {nv[2]}\n')
