"""
Long Tang
lab4.py
Developed a valentine greeting card by applying knowledge from objects and graphics
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def greeting_card():
    win = GraphWin("LT", 500, 500)
    win.setBackground("pink")
    heart = Polygon(
        [Point(250, 125), Point(125, 50), Point(10, 145), Point(125, 250), Point(250, 375), Point(375, 250),
         Point(490, 145), Point(375, 50), Point(250, 125)])
    heart.setOutline("black")
    heart.setFill("red")
    heart.draw(win)

    text = Text(Point(250, 400), "Happy Valentine's Day!")
    text.setSize(25)
    text.setOutline("white")
    text.setStyle("italic")
    text.draw(win)

    line = Line(Point(450, 375), Point(335, 275))
    line.setArrow("last")
    line.draw(win)
    for i in range(15):
        time.sleep(.1)
        dx = -30
        dy = -20
        line.move(dx, dy)

    text = Text(Point(250, 450), "Click anywhere to close")
    text.setSize(20)
    text.draw(win)
    win.getMouse()
    win.close()


greeting_card()
