"""
Long Tang
lab5.py
Manipulating Strings/List and using Python Graphics
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def triangle():
    win = GraphWin("Triangle", 500, 500)
    win.setBackground("white")

    txt = Text(Point(250, 275), "Click to close!")
    txt.setSize(15)
    txt.draw(win)

    txt2 = Text(Point(250, 75), "Click on three points!")
    txt2.setSize(15)
    txt2.draw(win)

    # three mouse clicks
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    # triangle
    tri = Polygon(p1, p2, p3)
    tri.setOutline("black")
    tri.setFill("green")
    tri.draw(win)

    # length for 3 sides
    a = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    b = math.sqrt((p2.getX() - p3.getX()) ** 2 + (p2.getY() - p3.getY()) ** 2)
    c = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    # Calculate for perimeter
    perimeter = a + b + c

    # Calculate for area
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # print out area and perimeter
    message = "perimeter: " + str(perimeter)
    message_2 = "area: " + str(area)
    txt_area = Text(Point(250, 325), message_2)
    txt_area.setSize(15)
    txt_area.draw(win)
    txt_perimeter = Text(Point(250, 370), message)
    txt_perimeter.setSize(15)
    txt_perimeter.draw(win)

    win.getMouse()
    win.close()


triangle()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    # input
    string = input("Enter a string: ")  # String is 'Python Program'

    # First character
    first_character = string[0]
    print("First character:", first_character)  # output = P

    # Second character
    second_character = string[1]
    print("Second character:", second_character)  # output = y

    # Characters in positions 2-5
    position = string[2:5]
    print(position)  # output: tho

    # Concatenate the first and last characters
    last_character = string[-1]
    combine = first_character + last_character
    print(combine)  # output: Pm

    # First three characters, 10 times
    third_character = string[2]
    characters = (first_character + second_character + third_character) * 10
    print(characters)  # PytPytPytPytPytPytPytPytPytPyt

    # Number of characters in the string
    number = len(string)
    print(number)  # output: 14


process_string()


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    list1 = values[1] + values[3]
    print(list1)

    list2 = values[0] + values[2]
    print(list2)

    list3 = values[1]
    hi = list3 * 5
    print(hi)

    list4 = values[2:5]
    print(list(list4))


process_list()


def another_series():
    pass


def target():
    win = GraphWin("Target", 500, 500)
    win.setBackground("grey")

    white = Circle(Point(250, 250), 180)
    white.setFill("white")
    white.draw(win)

    black = Circle(Point(250, 250), 160)
    black.setFill("black")
    black.draw(win)

    blue = Circle(Point(250, 250), 140)
    blue.setFill("blue")
    blue.draw(win)

    red = Circle(Point(250, 250), 120)
    red.setFill("red")
    red.draw(win)

    yellow = Circle(Point(250, 250), 100)
    yellow.setFill("yellow")
    yellow.draw(win)

    win.getMouse()
    win.close()


target()
