n = input('Nhap ten: ')
n = n.strip()

a = n.split()

b = []
for i in a:
    b.append(i.capitalize())

c = " ".join(b) #Gen code ( đoạn này em chưa hình dung ra cách để join vào ạ...)
print('Ten chuan: ', c)