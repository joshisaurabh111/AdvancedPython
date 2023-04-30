from abc import ABCMeta, abstractclassmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):

    @abstractclassmethod
    def __init__(self, no_of_employees):
        """ Implement in child class """

    @abstractstaticmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartment):

    def __init__(self, no_of_employees):
        self.no_of_employees = no_of_employees

    def print_department(self):
        print(f"Accounting Department : {self.no_of_employees}")

class Development(IDepartment):

    def __init__(self, no_of_employees):
        self.no_of_employees = no_of_employees

    def print_department(self):
        print(f"Development Department : {self.no_of_employees}")

class ParentDepartment(IDepartment):

    def __init__(self, no_of_employees):
        self.no_of_employees = no_of_employees
        self.base_employees = no_of_employees
        self.sub_dept = []

    def add(self, dept):
        self.sub_dept.append(dept)
        self.no_of_employees += dept.no_of_employees


    def print_department(self):
        print("Parent Department")
        print(f"Parent department Base Employees : {self.base_employees}")
        for dept in self.sub_dept:
            dept.print_department()
        print(f"Total number of employeers: {self.no_of_employees}")

dept1 = Accounting(200)
dept2 = Development(170)
parent_dept = ParentDepartment(30)

parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()
