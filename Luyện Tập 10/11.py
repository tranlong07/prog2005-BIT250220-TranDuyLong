def bai1():
    def lay_ten_file(path):
        vi_tri = path.rfind("\\")
        return path[vi_tri + 1:]

    def lay_ten_bai_hat(path):
        ten_file = lay_ten_file(path)
        vi_tri = ten_file.rfind(".")
        return ten_file[:vi_tri]

    duong_dan = "d:\\music\\muabui.mp3"

    print(lay_ten_file(duong_dan))
    print(lay_ten_bai_hat(duong_dan))
def bai2():
    a = input('Nhap chuoi ki tu: ')
    b = input('Nhap ki tu can tim: ')
    dem = 0
    for i in a:
        if i == b:
            dem += 1
    print(f'ki tu {b} xuat hien: {dem} lan')
def bai3():
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    n = int(input('Nhap so cua ban: '))
    print(f'{n}! = ', factorial(n))
def bai4():
    n = input('nhap chuoi: ')
    dem = 0
    if n == "":
        print('vui long nhap lai')
    else:
        for i in n:
            dem += 1
        print('do dai chuoi la: ', dem)
def bai5():
    from matplotlib import pyplot as plt
    import numpy as np

    x = np.arange(0, 5, 0.0001)
    y = x ** 2
    z = np.sqrt(x)

    plt.figure(figsize=(5.5, 2))
    plt.subplot(1, 2, 1)
    plt.title('x**2')
    plt.plot(x, y, 'b')
    plt.subplot(1, 2, 2)
    plt.title('sqrt(x)')
    plt.plot(x, z, 'r')
    plt.show()
def bai6():
    n = input('nhap chuoi: ')
    reversed_s = ""
    for i in n:
        reversed_s = i + reversed_s
    print('dao nguoc: ', reversed_s)
def bai7():
    while True:
        n = input('nhap key')
        if n == 'python123':
            break
def bai8():
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            print(f'lan lap thu {i}')
            for j in range(0, n - i - 1):
                print(f'so sanh {j} va {j + 1}')
                if arr[j] < arr[j + 1]:
                    print('doi cho')
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
        return arr

    a = [1, 2, 3, 4, 5]
    print(bubble_sort(a))
def bai9():
    class Person:
        n = 'con nguoi'

        def __init__(self, name, age):
            if age < 0:
                raise ValueError('tuoi phai >0')
            self._name = name
            self._age = age

        def get_age(self):
            return self._age

        def set_age(self, value):

            if value < 0:
                raise ValueError('tuoi phai >0')
            self._age = value

        def introduce(self):
            return f'toi la:  {self._name}, {self._age} tuoi '

        @classmethod
        def get_n(cls):
            return f'tat ca la : {cls.n}'

        @staticmethod
        def is_adult(age):
            return age >= 18

        def __eq__(self, other):
            return self._name == other._name and self._age == other._age

        def __str__(self):
            return f'Person(name={self._name}, age={self._age})'

    class Student(Person):
        def __init__(self, name, age, student_id):
            super().__init__(name, age)
            self.student_id = student_id

        def introduce(self):
            return f'Sinh vien: {self._name}, mssv: {self.student_id} '

        def __str__(self):
            return f'Student(name={self._name}, age={self._age}, id={self.student_id})'

    p1 = Person('Long', 18)
    p2 = Person('Lam', 18)
    s1 = Student('Quoc', 20, 'bit250222')

    print(p1)
    print(s1)

    print(p1.introduce())
    print(s1.introduce())

    print(Person.get_n())

    print('da du 18 tuoi : ', Person.is_adult(18))

    print('so sanh p1 va p2', p1 == p2)

    p1.set_age(25)
    print('tuoi moi: ', p1.get_age())
def bai10():
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            print(f'lan lap thu {i}')
            for j in range(0, n - i - 1):
                print(f'so sanh {j} va {j + 1}')
                if len(arr[j]) < len(arr[j + 1]):
                    print('doi cho')
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
        return arr

    a = []
    for i in range(5):
        s = input(f'nhap chuoi: ')
        a.append(s)

    print(bubble_sort(a))

while True:
    chon = input('chon bai: ')
    if chon == '1':
        bai1()
    elif chon == '2':
        bai2()
    elif chon == '3':
        bai3()
    elif chon == '4':
        bai4()
    elif chon == '5':
        bai5()
    elif chon == '6':
        bai6()
    elif chon == '7':
        bai7()
    elif chon == '8':
        bai8()
    elif chon == '9':
        bai9()
    elif chon == '10':
        bai10()
    elif chon == 'out':
        break

