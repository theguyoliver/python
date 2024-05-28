class Employee:
    def __init__(self, iden, name):
        self.iden = iden
        self.name = name

    def display(self):
        print(f"ID: {self.iden}\nName: {self.name}")


emp = Employee(1, 'Coder')
emp.display()

del emp.iden
try:
    print(emp.iden)
except AttributeError:
    print('emp.id is not defined')

del emp
try:
    emp.display()
except NameError:
    print('emp is not defined')

