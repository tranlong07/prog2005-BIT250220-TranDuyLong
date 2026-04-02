def hinh1():
    print('Hinh1: ')
    n = 4
    for i in range(n):
        for j in range(n):
            print("*", end="  ")
        print()
hinh1()
def hinh2():
    print('Hinh2: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        for k in range(n-i):
            print(" ", end=" ")
        print()
hinh2()
def hinh3():
    print('Hinh3: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(n-i+1):
            print("*", end=" ")
        for k in range(i):
            print(" ", end=" ")
        print()
hinh3()
def hinh4():
    print('Hinh4: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()
hinh4()
def hinh5():
    print('Hinh5: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hinh5()
def hinh6():
    print('Hinh6: ')
    n = 4

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                print("*", end=" ")
            elif i == 2 and (j == 1 or j == 3):
                print("*", end=" ")
            elif i == 3 and (j == 1 or j == 2):
                print("*", end=" ")
            elif i == 4 and j == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hinh6()
def hinh7():
    print('Hinh7: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(1, i + 1):
            if k == 1 or k == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hinh7()
def hinh8():
    print('Hinh8: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if i == 1:
                if j == n:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif i == 2:
                if j == n - 1 or j == n + 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif i == 3:
                if j == n - 2 or j == n or j == n + 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif i == 4:
                if j % 2 == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()
hinh8()
def hinh9():
    print('Hinh9: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if i == n:
                if j % 2 == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif j == n - i + 1 or j == n + i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hinh9()
def hinh10():
    print('Hinh10: ')
    n = 4
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if i == 1:
                if j % 2 == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif i == 2:
                if j == n - 2 or j == n + 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif i == 3:
                if j == n - 1 or j == n + 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif i == 4:
                if j == n:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()
hinh10()