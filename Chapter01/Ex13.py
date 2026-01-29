try:
    a=int(input('nhap so a :'))
    b=int(input('nhap so b :'))
    c=a/b
    print('Ket qua la:' ,c)

except ZeroDivisionError:
    print("Error: Khong the chia cho 0.")

except ValueError:
    print("Error: Du lieu khong hop le.")