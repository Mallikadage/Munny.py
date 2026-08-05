class Student():
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def __str__(self):
        return f"Name:{self.name},Roll:{self.roll},Marks:{self.marks}"
    def __repr__(self):
         return f"Student('{self.name},{self.roll},{self.marks})"
    def __eq__(self,other):
        if isinstance(other,Student):
               return self.roll==other.roll
        return False
s1=Student("Mallika",101,46)
s2=Student("Ravi",102,67)
s3=Student("vijaya",102,89)
print(s1)
print((repr(s1)))
print(s1==s2)
print(s1==s3)
 
       
           