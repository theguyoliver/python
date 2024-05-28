class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print('Animals live on :', self.habitat)

    def sound(self):
        print('Varies from animal to animal')


class Dog(Animal):
    def __init__(self):
        super().__init__('Kennel')

    def sound(self):
        print('Woof sound')


d = Dog()
d.print_habitat()
d.sound()
