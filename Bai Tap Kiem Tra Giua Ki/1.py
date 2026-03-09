import math
a = float(input("Hệ số a: "))
b = float(input("Hệ số b: "))
c = float(input("Hệ số c: "))
max_value = max(a, b, c)
min_value = min(a, b, c)
print("Số lớn nhất là:", max_value)
print("Số nhỏ nhất là:", min_value)
print(f"Phương trình bậc 2 của bạn là {a}x^2 + {b}x + {c} = 0")
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình có 1 nghiệm:", x)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)