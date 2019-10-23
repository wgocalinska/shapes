import unittest

import rectangles

class TestRectangles(unittest.Testcase):

    def setUp(self):
        print("SetUp")

    def test_Rect(self):
        rect = rectangles.Rectangle(2,3)
        data = rect.summary()
        self.assertEqual(6.,data['area'])
        self.assertEqual(10.,data['perimeter'])

    def test_Square(self):
        rect = rectangles.Square(2)
        data = rect.summary()
        self.assertEqual(4.,data['area'])
        self.assertEqual(9.,data['perimeter'])