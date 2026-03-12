import math

a = float(input('nhap a : '))
b = float(input('nhap b : '))
print(f'Luy thua cua {a} la: ','{:.2f}'.format(a*a))
print(f'Luy thua cua {b} la: ','{:.2f}'.format(b*b))
print(f'Can bac hai cua {a} la: ','{:.2f}'.format(math.sqrt(a)))
print(f'Can bac hai cua {b} la: ', '{:.2f}'.format(math.sqrt(b)))
print(f'Chia lay phan nguyen cua {a} va {b} la: ', '{:.2f}'.format(a//b))
print(f'Chia lay phan du cua {a} va {b} la: ', '{:.2f}'.format(a%b))
print(f'Chia lay phan nguyen cua {b} va {a} la: ', '{:.2f}'.format(b//a))
print(f'Chia lay phan du cua {b} va {a} la: ', '{:.2f}'.format(b%a))