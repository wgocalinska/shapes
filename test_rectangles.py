import unittest

import rectangles

class TestRectangles(unittest.TestCase):

    def setUp(self):
        print("SetUp")

    def test_Rect(self):
        rect = rectangles.Rectangle(2, 3)
        data = rect.summary()
        self.assertEqual(6.,data['area'])
        self.assertEqual(10.,data['perimeter'])

    def test_Square(self):
        rect = rectangles.Square(2)
        data = rect.summary()
        self.assertEqual(4.,data['area'])
        self.assertEqual(8.,data['perimeter'])

    def test_Paral(self):
        rect = rectangles.Parallelogram(6, 8, 9)
        data = rect.summary()
        self.assertEqual(54.,data['area'])
        self.assertEqual(28.,data['perimeter'])

    def test_Rhombus(self):
        rect = rectangles.Rhombus(6, 7)
        data = rect.summary()
        self.assertEqual(42.,data['area'])
        self.assertEqual(24.,data['perimeter'])

    def test_Trapeze(self):
        rect = rectangles.Trapeze(4,8,6,10)
        data = rect.summary()
        self.assertEqual(42.,data['area'])
        self.assertEqual(30.,data['perimeter'])

    def test_Ellipse(self):
        rect = rectangles.Ellipse(6,5)
        data = rect.summary()
        self.assertEqual(94.,data['area'])
        self.assertEqual(35.,data['perimeter'])

    def test_Circle(self):
        rect = rectangles.Circle(6)
        data = rect.summary()
        self.assertEqual(113.,data['area'])
        self.assertEqual(38.,data['perimeter'])
