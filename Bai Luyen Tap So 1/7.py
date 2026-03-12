class Student:
    def __init__(self,Ten, Diem):
        self.Ten = Ten
        self.Diem = Diem
sv1 = Student('Tran Duy Long', 10)
sv2 = Student('Tran Lam', 9.5)
print('Sinh vien thu nhat la: ',sv1.Ten,',Diem: ', sv1.Diem)
print('Sinh vien thu hai la: ',sv2.Ten,',Diem: ', sv2.Diem)

