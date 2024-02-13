import math


class Shape:
    def calculate_area(self):
        pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def calculate_area(self):
            return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.calculate_area()
        return total_area
mycircle = Circle(9)
myRectangle =
