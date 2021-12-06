from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# class Point(Shape):
#     pass
#
#
# class Line(Shape):
#     pass


class Triangle(Shape):
    def area(self):
        pass

    def perimeter(self):
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


# rectangle = Rectangle(3, 4)
# print(rectangle.area())

shape = Shape()