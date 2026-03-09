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