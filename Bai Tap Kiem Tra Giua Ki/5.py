def bai1():
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
def bai2():
    import math

    def selection_sort(a):
        n = len(a)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if a[j] > a[max_idx]:
                    max_idx = j
            a[max_idx], a[i] = a[i], a[max_idx]
        return a
    a = []
    for i in range(17, 112):
        if i % 2 != 0:
            a.append(i)
    print("Dãy số lẻ tăng dần là:", selection_sort(a))
    Day_SNT = []
    for i in range(17, 112):
        SNT = True
        if i < 2:
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                SNT = False
                break
        if SNT:
            Day_SNT.append(i)
    print("Các số nguyên tố trong danh sách là:", Day_SNT)
def bai3():
    n = int(input("Nhập n: "))
    print("Hình 1:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
    print("Hình 2:")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print("* ", end="")
        print()
def bai4():
    n = int(input("Cỡ của mảng: "))
    x = []

    for i in range(n):
        y = float(input(f"Nhập phần tử thứ {i}: "))
        x.append(y)

    def selection_sort(a):
        n = len(a)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if a[j] > a[max_idx]:
                    max_idx = j
            a[i], a[max_idx] = a[max_idx], a[i]
            print(f"Kết quả sau bước {i + 1}: {a}")
        return a
    print("Mảng theo thứ tự giảm dần là:", selection_sort(x))




while True:
    Menu = input("Chọn bài : ")
    if Menu == '1':
        bai1()
    elif Menu == '2':
        bai2()
    elif Menu == '3':
        bai3()
    elif Menu == '4':
        bai4()
    elif Menu == 'Thoát':
        break










