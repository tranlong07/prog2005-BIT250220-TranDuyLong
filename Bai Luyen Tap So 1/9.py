class Student:
    def __init__(self,Ten, Diem):
        self.Ten = Ten
        self.Diem = Diem
    def display(self):
        print(f"Sinh vien {self.Ten} co diem la {self.Diem}")
sv1 = Student('Tran Duy Long', 10)
sv2 = Student('Tran Lam', 9.5)
sv1.display()
sv2.display()
