class Shape:
    def area(self):
        print("Area of Shape")


class Circle(Shape):
    def area(self):
        radius = 5
        print("Area of Circle =", 3.14 * radius * radius)


class Rectangle(Shape):
    def area(self):
        length = 10
        breadth = 5
        print("Area of Rectangle =", length * breadth)


class Triangle(Shape):
    def area(self):
        base = 8
        height = 6
        print("Area of Triangle =", 0.5 * base * height)


# Runtime Polymorphism
s = Circle()
s.area()

s = Rectangle()
s.area()

s = Triangle()
s.area()