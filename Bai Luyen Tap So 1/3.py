n = int(input('Nhap mot so tu 1 den 9: '))
if n < 1 or n > 9 :
    print('Nhap mot so tu 1 den 9')
else:
    print(f'Bang cuu chuong cua {n} la: ')
    for i in range (1,11):
        print(f'{n}*{i} = {n*i}')

