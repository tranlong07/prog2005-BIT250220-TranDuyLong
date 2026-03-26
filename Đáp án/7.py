class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}")

    def is_scholarship(self):
        return self.gpa >= 3.5

s1 = Student("Nguyen Van A", 20, 3.6)
s1.show_info()
print("Học bổng:", s1.is_scholarship())
