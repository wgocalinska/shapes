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

class Trapeze(Parallelogram):

    def __init__(self, a, b, h, a2):
        super().__init__(a, b, h)
        self.a2 = a2

    def area(self):
        return round(0.5*(self.a + self.a2) * self.h)

    def perimeter(self):
        x = (self.b ** 2 - self.h ** 2) ** 0.5
        try:
            if x > 0:
                y = self.a2 - x
                d = (y ** 2 + self.h ** 2) ** 0.5
                return round(self.a + self.b + self.a2 + d)
            elif x ==0:
                return round(self.a + self.b + self.a2 + self.h)
        except TypeError:
            print("such trapeze does not exist")

class Ellipse(Shape):

    def __init__(self, r, b):
        super().__init__()
        self.r = r
        self.b = b

    def area(self):
        return round(math.pi * self.r * self.b)

    def perimeter(self):
        return round(math.pi * (3/2 * (self.r + self.b) - math.sqrt(self.r*self.b)))


class Circle(Ellipse):

    def __init__(self, r):
        super().__init__(r, r)

    def draw(self):
        plt.close('all')
        circle = plt.Circle((0, 0), self.r)
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.add_artist(circle)
        ax1.margins(10)
        plt.show()

