"""
Name: Long Tang
hw10.py
Problem: Develop programs that consist of boolean values, class/objects, and decision/repetition structures
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_smile = self.mouth.getCenter()
        mouth_smile_clone = mouth_smile.clone()
        mouth_smile_clone.move = (7, mouth_smile / 2)
        mouth_one = self.mouth.getP1()
        mouth_two = self.mouth.getP2()
        mouth_pos_one = Line(mouth_one, mouth_smile_clone)
        mouth_pos_two = Line(mouth_two, mouth_smile_clone)
        mouth_pos_one.draw(self.window)
        mouth_pos_two.draw(self.window)

    def shock(self):
        shock_mouth_pos = self.mouth.getCenter()
        shock_mouth = self.left_eye.clone()
        shock_mouth.move(shock_mouth_pos)
        shock_mouth.draw(self.window)

    def wink(self):
        wink_mouth = self.mouth.getCenter()
        wink_mouth_clone = wink_mouth.clone()
        wink_mouth_clone.move(2, wink_mouth / 2)
        mouth_one = self.mouth.getP1()
        mouth_two = self.mouth.getP2()
        mouth_pos_one = Line(mouth_one, wink_mouth_clone)
        mouth_pos_two = Line(mouth_two, wink_mouth_clone)
        mouth_pos_one.draw(self.window)
        mouth_pos_two.draw(self.window)
        eye = self.left_eye.getCenter()
        eye_one = eye.getX()
        eye_two = eye.getY()
        eye_one_pos = eye_one + eye
        eye_two_pos = eye_two + eye
        self.left_eye.undraw()
        eye_pos = Line(Point(eye_one_pos, eye_one), Point(eye_two_pos, eye_two))
        eye_pos.draw(self.window)

