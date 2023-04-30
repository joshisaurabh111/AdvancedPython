from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        """ Interface Method """

class Person(IPerson):

    def person_method(self):
        print('I am a Person')

class ProxyPerson(IPerson):

    # This is still yeilding to an error
    # Fix this before upload
    def __init__(self):
        super().__init__('ProxyPerson')
        self.person = Person()

    def person_method(self):
        print('I am the proxy functionality')
        self.person.person_method()

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()