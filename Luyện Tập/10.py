class SinhVien:
    dem = 0

    def __init__(self, diem):
        self.diem = diem
        SinhVien.dem += 1

    @classmethod
    def dem_so_sinh_vien(cls):
        return cls.dem

sv1 = SinhVien(8.0)
sv2 = SinhVien(7.5)
sv3 = SinhVien(9.0)

print('So luogn sinh vien la: ', SinhVien.dem_so_sinh_vien())