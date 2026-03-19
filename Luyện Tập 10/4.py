n = input('nhap chuoi: ')
dem = 0
if n == "":
    print('vui long nhap lai')
else:
    for i in n:
        dem += 1
    print('do dai chuoi la: ', dem)