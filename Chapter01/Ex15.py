n=3
for i in range(1,n+1):
    print("TT SV: ")
    x = input(f"Ten SV{i}: ")
    Toan = float(input(f"Diem Toan cua sv{i}: "))
    Ly = float(input(f"Diem Ly cua sv{i}: "))
    Hoa = float(input(f"Diem Hoa cua sv{i}: "))
    print(x, "diem trung binh: ", (Toan+Ly+Hoa)/3)