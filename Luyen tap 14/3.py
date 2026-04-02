def hinh1():
    n = 4
    print('h1: ')
    for i in range(n):
        print("1 " * n)
hinh1()
def hinh2():
    n = 4
    print('h2: ')
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
hinh2()
def hinh3():
    n = 4
    print('h3: ')
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
hinh3()
def hinh4():
    n = 4
    print('h4: ')
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
hinh4()
def hinh5():
    print('h5: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
hinh5()
def hinh6():
    n = 4
    print('h6: ')
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
hinh6()
def hinh7():
    n = 4
    print('h7: ')
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print(i, end=" ")
        print()
hinh7()
def hinh8():
    n = 4
    print('h8: ')
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
hinh8()
def hinh9():
    n = 4
    print('h9: ')
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if i == n:
                if j <= i:
                    print(j, end="")
                else:
                    print(2 * i - j, end="")
            else:
                if j == 1 or j == 2 * i - 1:
                    print(1, end="")
                else:
                    print(" ", end="")
        print()
hinh9()
