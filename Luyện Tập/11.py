class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('Tieng cua dong vat')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print('gau gau')

dog = Dog('Bun')
print('Ten cho', dog.name)
dog.sound()