"""
Name: Long Tang
lab10.py
Problem: Develop a program using class and graphics to turn a door in the graphic window to a different color each click
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

from door import Door
from button import Button


def main():
    win = GraphWin("Test", 500, 500)
    win.setBackground("grey")

    exit_box = Rectangle(Point(150, 25), Point(350, 150))
    exit_txt = Button(exit_box, "Exit", 300, 150)
    exit_txt.draw(win)

    door_box = Rectangle(Point(150, 175), Point(350, 470))
    door_txt = Door(door_box, "Closed", 200, 295)
    door_txt.color_door('red')
    door_txt.draw(win)

    # Need to double-click
    while not exit_txt.is_clicked(win.getMouse()):
        if exit_txt.is_clicked and door_txt.is_clicked(win.getMouse()):
            if not door_txt.is_secret():
                door_txt.open("white", "Open")
                door_txt.set_secret(True)
            elif door_txt.is_secret():
                door_txt.open("red", "Closed")
                door_txt.set_secret(False)

    win.close()


main()
