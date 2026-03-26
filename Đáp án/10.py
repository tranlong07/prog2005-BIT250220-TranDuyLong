import matplotlib.pyplot as plt

names = ["An", "Bình", "Cường","Lâm","Quốc"]
scores = [7, 8.5, 9, 8, 9.5]

plt.bar(names, scores)

plt.title("Điểm sinh viên")
plt.xlabel("Tên")
plt.ylabel("Điểm")

plt.show()