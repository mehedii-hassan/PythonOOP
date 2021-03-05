class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area of shape class")


class Triangle(Shape):

    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ", area)


class Rectangle(Shape):

    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ", area)


t1 = Triangle(20, 10)
t1.area()

r1 = Rectangle(30, 20)
r1.area()
