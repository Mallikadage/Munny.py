class Student():
    def __init__(self,name):
        self.name=name
    def __eq__(self,other):
        return self.name==other.name
s1=Student("Mallika")
s2=Student("Mallika")
s3=Student("Munny")
print(s1==s1)
print(s1==s3)
        