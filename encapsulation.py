class Person:

    def __init__(self, name, age, gender) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    # Property is a function to define a class
    # object private or public and represent
    # a property like display
    @property
    def Name(self):
        return self.__name
    
    # onject setter are mandatory, cannot have the
    # same function with the name defined above
    # If it is not a different annotation it will
    # throw an error
    @Name.setter
    def Name(self, value):
        self.__name = value

    # Static method is unrelated to the objects 
    # of a class. Can be called with the class
    # name itself or using an object of a class
    # also, but it does not identify any property
    # or attribute of the class or the object
    @staticmethod
    def myStatMethod():
        print('This is unrelated to the class')

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, num):
        if num > self.__age and num > 0:
            self.__age = num
        else:
            print("Age cannot be smaller than before")


Person.myStatMethod()

p1 = Person('Sourabh', 30, 'M')
print(p1.Name)
p1.Age = 21
print(p1.Age)

p1.myStatMethod()