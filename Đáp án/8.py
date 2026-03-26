class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def show_info(self):
        print(f'Ten: {self.name}, Tuoi: {self.age}, GPA: {self.gpa}')

    def is_scholarship(self):
        return self.gpa >= 3.5
class ITStudent(Student):
    def __init__(self, name, age, gpa, language):
        super().__init__(name, age, gpa)
        self.language = language

    def show_info(self):
        super().show_info()
        print(f'Ngon ngu lap trinh: {self.language}')

    def is_excellent(self):
        return self.gpa >= 3.5

s1 = ITStudent('Long', 18, 3.9, 'Python')
s1.show_info()
print('Hoc bong: ', s1.is_scholarship())
print('Xuat sac: ', s1.is_excellent())
