class UniuyoStudents  :
    def essence_of_uni(self):
        print('To get a degree and then use it to get a job')


class Pharmacy:
    def __init__(self):
        self.num_courses = 100
        self.block = 'ACB'
        self.faculty = 'Pharmacy'

    def favorite_course(self):
        print('I no get, I just dey pass exam first')


class QuantitySurvey(UniuyoStudents):
    def __init__(self):
        self.num_courses = 80
        self.block = 'QS lecture hall, perm site'
        self.faculty = 'Environmental Studies'
# our init block is just like the constructor of our function. If we want to call a function to
# output its values it needs to be specified in a separate function


class EmmanuelOliver(UniuyoStudents, Pharmacy):
    def __init__(self):
        UniuyoStudents.__init__(self)
        Pharmacy.__init__(self)
        self.admission_year = 2018

    def emm_attributes(self):
        self.essence_of_uni()
        year_of_admission = self.admission_year
        print(year_of_admission)


if __name__ == '__main__':
    c = QuantitySurvey()
    e = EmmanuelOliver()
    e.emm_attributes()
    # c above is an object/ instance of the class QuantitySurvey()
    n = c.block
    print(n)
    c.essence_of_uni()
