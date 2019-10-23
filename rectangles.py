# coding: utf8
import math
from shape import Shape


class Rectangle(Shape):
    """
    Rectangular shape.
    """

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    """
    Square shape as a specific rectangle.
    """

    def __init__(self, a):
        super().__init__(a, a)


class Parallelogram(Rectangle):

    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Rhombus(Parallelogram):

    def __init__(self, a , h ):
        super().__init__(a, a, h)



class Elipse(Shape):

    def __init__(self, r, b):
        super().__init__()
        self.r = r
        self.b = b

    def area(self):
        return math.pi * self.r * self.b

    def perimeter(self):
        a = float(3/2)
        return math.pi * [a * (self.r + self.b) - math.sqrt(self.r*self.b)]


class Circle(Elipse):

    def __init__(self, r):
        super().__init__(r, r)

