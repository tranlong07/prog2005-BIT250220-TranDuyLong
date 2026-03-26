class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}")

    def is_scholarship(self):
        return self.gpa >= 3.5

class ITStudent(Student):
    def __init__(self, name, age, gpa, major):
        super().__init__(name, age, gpa)
        self.major = major

    def display_info(self):
        super().display_info()
        print(f"Chuyên ngành: {self.major}")

    def is_excellent(self):
        return self.gpa >= 3.8

s1 = Student("An", 20, 3.6)
s1.display_info()
print("Học bổng:", s1.is_scholarship())

s2 = ITStudent("Bình", 21, 3.9, "CNTT Và TT")
s2.display_info()
print("Học bổng:", s2.is_scholarship())
print("Xuất sắc:", s2.is_excellent())