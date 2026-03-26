n = int(input('Nhập số của bạn: '))
if n < 1 or n > 9:
    print('Vui lòng nhập 1 số trong khoảng 1-9')
else:
    print(f'Bảng cửu chương của {n} là: ')
    for i in range(1,11):
        print(f'{n}*{i} = {n*i}')
