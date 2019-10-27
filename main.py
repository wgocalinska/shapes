# coding: utf8
import rectangles


square2 = rectangles.Square(2)
print(square2.summary())


parallelogram1 = rectangles.Parallelogram(6, 8, 9)
print(parallelogram1.summary())


rhombus1 = rectangles.Rhombus(6,7)
print(rhombus1.summary())


trap1 = rectangles.Trapeze(4,8,6,10)
print(trap1.summary())


ellipse1 = rectangles.Ellipse(6,5)
print(ellipse1.summary())


circle1 = rectangles.Circle(6)
print(circle1.summary())
circle1.draw()
