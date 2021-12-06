class Shape:

    def area(self):
        raise NotImplementedError()

    def perimeter(self):
        raise NotImplementedError()


# class Point(Shape):
#     pass
#
#
# class Line(Shape):
#     pass


class Triangle(Shape):
    pass


class Circle(Shape):
    pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(3, 4)
print(rectangle.area())

shape = Shape()
print(shape.area())

my_list = [rectangle, shape]