import math
a = [5,7,8,-2,8,11,13,9,10]
b = []
c = []
d = []
tong = 0
print('Tung so tren 1 dong rieng: ')
for x in a:
    print(x)
for y in a:
    if y%2==0:
        b.append(y)
print('Cac so chan la: ',b)
for z in a:
    if z < 0:
        c.append(z)
print('Cac so am la: ',c)
for i in a:
    if i > 1:
        SNT = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                SNT = False
                break
        if SNT:
            d.append(i)
print('Cac SNT la: ',d)
