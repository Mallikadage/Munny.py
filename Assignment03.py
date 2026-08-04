class Shape:
    def display(self):
        print("This is a Shape")


# Derived class
class Circle(Shape):
    def area(self, radius):
        print("Area of Circle:", 3.14 * radius * radius)


# Derived class
class Rectangle(Shape):
    def area(self, length, width):
        print("Area of Rectangle:", length * width)


# Main Program
c = Circle()
r = Rectangle()

print("Circle:")
c.display()
c.area(5)

print("\nRectangle:")
r.display()
r.area(4, 6)