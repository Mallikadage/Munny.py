class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        self.display()
        print("Roll No:", self.roll_no)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display()
        print("Subject:", self.subject)


s = Student("Mallika", 20, 101)
t = Teacher("Ramesh", 40, "Python")

print("Student Details:")
s.display_student()

print("\nTeacher Details:")
t.display_teacher()