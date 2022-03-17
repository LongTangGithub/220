"""
Name: Long Tang
lab8.py
Problem: Develop a program where two circles move in opposite directions if there's a collision
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from random import randint
from graphics import *


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)


def get_random(move_amount):
    rtnInteger = randint(-move_amount, move_amount)
    return rtnInteger


def did_collide(ball_1, ball_2):
    dist = math.sqrt((ball_1.getCenter().getX() - ball_2.getCenter().getX()) ** 2 + (
            ball_1.getCenter().getY() - ball_2.getCenter().getY()) ** 2)
    return dist < ball_1.getRadius + ball_2.getRadius


def hit_vertical(ball, win):
    height = win.getHeight() - ball.getRadius
    return ball.getCenter().getY() >= height or ball.getCenter().getY() <= ball.getRadius()


def hit_horizontal(ball, win):
    width = win.getwidth() - ball.getRadius
    return ball.getCenter().getX() >= width or ball.getCenter().getX() <= ball.getRadius()


def bumper():
    win = GraphWin("JoyRide", 500, 500)
    win.setBackground("white")

    ball_1 = Circle(Point(randint(50, 450), randint(50, 450)), 50)
    ball_1.setOutline("black")
    ball_1_color = get_random_color()
    ball_1.setFill(ball_1_color)
    ball_1.draw(win)

    ball_2 = Circle(Point(randint(50, 450), randint(50, 450)), 50)
    ball_2.setOutline("black")
    ball_2_color = get_random_color()
    while ball_2_color == ball_1_color:
        ball_2_color = get_random_color()
    ball_2.setFill(ball_2_color)
    ball_2.draw(win)

    direction_1 = 10
    direction_2 = 20
    while not (win.checkMouse()):
        time.sleep(0.25)

        ball_1.move(direction_1, direction_2)
        ball_2.move(direction_1, direction_2)

    win.getMouse()
    win.close()


bumper()
