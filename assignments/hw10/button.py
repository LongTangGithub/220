"""
Name: Long Tang
lab10.py
Problem: Develop a program using class and graphics to turn a door in the graphic window to a different color each click
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


class Button:
    def __init__(self, shape, label, height, width):
        self.shape = shape
        self.txt = Text(shape.getCenter(), label)
        w = width / 2.0
        h = height / 2.0
        self.xmax = shape.getCenter().getX() + w
        self.xmin = shape.getCenter().getX() - w
        self.ymax = shape.getCenter().getY() + h
        self.ymin = shape.getCenter().getY() - h

    def get_label(self):
        return self.txt.getText()

    def set_label(self, label):
        self.txt.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.txt.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.txt.undraw()

    def is_clicked(self, point):
        return (self.xmin <= point.getX() <= self.xmax) and (self.ymin <= point.getY() <= self.ymax)

    def color_button(self, color):
        self.shape.setFill(color)



