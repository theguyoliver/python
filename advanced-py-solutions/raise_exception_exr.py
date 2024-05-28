class AdultException(Exception):
    pass


class IsMajor(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) < 18:
            return self.age
        else:
            raise AdultException

    def display_person(self):
        try:
            print('Age ->', self.get_minor_age())
        except AdultException:
            print('Adults are not allowed here')
        finally:
            print('Name:', self.name)


p = Person('Emmanuel', 17)
Person('Old Man', 67).display_person()
# p.get_minor_age()
p.display_person()