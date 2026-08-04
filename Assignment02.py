class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

    def display_developer(self):
        self.display()
        print("Programming Language:", self.language)


m = Manager("Sunil", 101, "HR")
d = Developer("Raju", 102, "Python")

print("Manager Details:")
m.display_manager()

print("\nDeveloper Details:")
d.display_developer()