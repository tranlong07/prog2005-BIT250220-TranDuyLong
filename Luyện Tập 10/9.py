class Person:
    n = 'con nguoi'

    def __init__(self, name, age):
        if age < 0:
            raise ValueError('tuoi phai >0')
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):

        if value < 0:
            raise ValueError('tuoi phai >0')
        self._age = value


    def introduce(self):
        return f'toi la:  {self._name}, {self._age} tuoi '

    @classmethod
    def get_n(cls):
        return f'tat ca la : {cls.n}'

    @staticmethod
    def is_adult(age):
        return age >= 18


    def __eq__(self, other):
        return self._name == other._name and self._age == other._age

    def __str__(self):
        return f'Person(name={self._name}, age={self._age})'

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f'Sinh vien: {self._name}, mssv: {self.student_id} '

    def __str__(self):
        return f'Student(name={self._name}, age={self._age}, id={self.student_id})'

p1 = Person('Long', 18)
p2 = Person('Lam', 18)
s1 = Student('Quoc', 20,'bit250222')

print(p1)
print(s1)

print(p1.introduce())
print(s1.introduce())

print(Person.get_n())

print('da du 18 tuoi : ', Person.is_adult(18))

print('so sanh p1 va p2', p1 == p2)

p1.set_age(25)
print('tuoi moi: ', p1.get_age())