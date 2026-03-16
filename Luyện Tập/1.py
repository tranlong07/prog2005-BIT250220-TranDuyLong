def bmi():
    weight = float(input('Nhap can nang: '))
    height = float(input('Nhap chieu cao: '))
    return  weight / (height * height)
print('Chi so BMI la: ', round(bmi(),2))