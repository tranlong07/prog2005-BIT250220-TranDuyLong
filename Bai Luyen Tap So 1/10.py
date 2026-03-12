File = "SanPham.txt"
def Them_SanPham():
    code = input('Nhap ma sp: ')
    name = input('Nhap ten sp: ')
    price = float(input('Nhap gia: '))
    with open(File, "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")

def Doc_SanPham():
    sanpham = []
    with open(File, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                code, name, price = line.split(";")
                sanpham.append([code, name, float(price)])
    return sanpham

def HienThi_SanPham(sanpham):
    print('\nDS San Pham: ')
    for i in sanpham:
        print(f"{i[0]} - {i[1]} - {i[2]}")


def sapxep_giasanpham(sanpham):
    return sorted(sanpham, key=lambda x: x[2], reverse=True)

while True:
    print('Them SP(1)')
    print('Hien thi SP(2)')
    print('Sap xep theo gia giam dan(3)')
    print('Close(4)')
    a = input('Chon chuc nang')
    if  a == "1":
        Them_SanPham()
    elif a == "2":
        products = Doc_SanPham()
        HienThi_SanPham(products)
    elif a == "3":
        products = Doc_SanPham()
        sorted_products = sapxep_giasanpham(products)
        print("\nDS sau khi sap xep :")
        HienThi_SanPham(sorted_products)
    elif a == "4":
        break
    else:
        print('Vui long chon lai')