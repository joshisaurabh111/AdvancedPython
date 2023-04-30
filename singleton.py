from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def print_data(self):
        """ Implement in child class """

class PersonSingle(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingle.__instance == None:
            PersonSingle("John", 0)
        return PersonSingle.__instance
    
    def __init__(self, name, age):
        
        if PersonSingle.__instance != None:
            raise Exception('Singleton cannot be instantiated more then once')
        else:
            self.name = name
            self.age = age
            PersonSingle.__instance = self
    
    @ staticmethod
    def print_data():
        print(f"Nmae: {PersonSingle.__instance.name}, Age: {PersonSingle.__instance.age}")

        
p = PersonSingle('Sourabh', 30)
print(p)
p.print_data()