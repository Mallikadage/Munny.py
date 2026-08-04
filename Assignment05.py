from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Manager Salary:", self.salary)


class Developer(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Developer Salary:", self.salary)


m = Manager(50000)
d = Developer(40000)

m.calculate_salary()
d.calculate_salary()