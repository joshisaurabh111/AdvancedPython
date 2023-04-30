from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method() ->  None:
        """ Interface Method """

class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Student Name"

    def person_method(self):
        print('I am a student')

class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Teacher Name"

    def person_method(self):
        print('I am a Teacher')






class PersonFactory:

    @staticmethod
    def build_person(perosn_type: str):
        if perosn_type == 'S':
            return Student()
        if perosn_type == 'T':
            return Teacher()


if __name__ == "__main__":

    p1 = Student()
    p1.person_method()
    t1 = Teacher()
    t1.person_method()

    # Using the factoy method to create a person
    # and determine at runtime if he is supposed
    # to be a teacher or a student
    choice  = input("What type of person do you want to create? \n")
    person = PersonFactory.build_person(choice)
    person.person_method()