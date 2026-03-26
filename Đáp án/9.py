with open("students.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        name = input("Nhập tên: ")
        score = input("Nhập điểm: ")
        f.write(f"{name} - {score}\n")

print("\nDanh sách sinh viên:")
with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())