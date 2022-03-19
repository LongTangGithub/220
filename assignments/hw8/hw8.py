"""
Name: Long Tang
hw8.py

Problem: Develop programs and modifying them  with conditional control structures

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: Brooke Duvall
"""
import math
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    sum = 0
    for i in range(len(nums)):
        sum += (nums[i])
    return sum


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    list_nums = []

    for i in range(len(nums)):
        num_split = nums[i].split(", ")
        to_numbers(num_split)
        square_each(num_split)
        list_nums.append(sum_list(num_split))
    return list_nums


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)

    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)

    circle_two = Circle(center, radius)
    circle_two.setFill("light green")
    circle_two.draw(win)

    text_1 = Text(Point(5, 5), "The circles overlap")
    text_2 = Text(Point(5, 5), " The circles do not overlap")

    if did_overlap(circle_one, circle_two):
        text_1.draw(win)
    else:
        text_2.draw(win)

    close_text = Text(Point(5, 6), "Click again to close")
    close_text.setSize(20)
    close_text.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    dist = math.sqrt((circle_one.getCenter().getX() - circle_two.getCenter().getX()) ** 2 + (
            circle_one.getCenter().getY() - circle_two.getCenter().getY()) ** 2)
    return dist < circle_one.getRadius() + circle_two.getRadius()


if __name__ == '__main__':
    pass
