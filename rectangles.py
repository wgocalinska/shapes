# coding: utf8
import math
from shape import Shape

class Trapeze(Shape):

    def __init__(self, a, b, c, h):
        super().__init__()
        self.base1 = a
        self.base2 = b
        self.side = c
        self.h = h

    def perimeter(self):
        if self.base2 > self.base1:
            x = (self.side ** 2 - self.h ** 2) ** 0.5
            y = self.base2 - x
            d = (y ** 2 + self.h ** 2) ** 0.5
            return self.base1 + self.base2 + self.side + d
        if self.base1 > self.base2:
            x = (self.side ** 2 - self.h ** 2) ** 0.5
            y = self.base1 - x
            d = (y ** 2 + self.h ** 2) ** 0.5
            return self.base1 + self.base2 + self.side + d


    def area(self):
        return (self.base1 + self.base2) * self.h * 0.5


class Parallelogram(Trapeze):

    def __init__(self, a, b, c, h):
        super().__init__(a, a,  c, h)


    def perimeter(self):
        return 2 * (self.base1 + self.side)


    def area(self):
        return self.base1 * self.h


class Rhombus(Parallelogram):

    def __init__(self, a , h ):
        super().__init__(a, h)


class Rectangle(Parallelogram):

    base1 = None
    side = None

    def __init__(self, a, c):
        super().__init__(a, a, c, c)

    def area(self):
        return self.base1 * self.side


class Square(Rectangle):

    def __init__(self, base1):
        super().__init__(base1,base1)





class Circle(Shape):

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return math.pi * (self.r)**2

    def perimeter(self):
        return 2 * math.pi * self.r

class Elipse(Shape):

    def __init__(self, a,b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        return  math.pi *[3/2 * (self.a + self.b) - (self.a * self.b) * 0.5]