
class Teacher:
    def mantra(self):
        print('The sole aim of teaching is to groom people who can take over from you')


class Student(Teacher):
    def __init__(self):
        super().__init__()

    def student_mantra(self):
        print(self.mantra())


class YouTuber(Student):
    def __init__(self):
        super().__init__()

    def role_model(self):
        print('Mr Beast')


y = YouTuber()
y.role_model()