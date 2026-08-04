class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow")

class Cow(Animal):
    def sound(self):
        print("Cow moos: Moo Moo")

a = Animal()
d = Dog()
c = Cat()
cw = Cow()

a.sound()
d.sound()
c.sound()
cw.sound()