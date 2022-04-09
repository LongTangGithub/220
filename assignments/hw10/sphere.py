"""
Name: Long Tang
hw10.py
Problem: Develop programs that consist of boolean values, class/objects, and decision/repetition structures
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        area = 4 * math.pi * (self.radius ** 2)
        return area

    def volume(self):
        vol = (4.0 / 3.0) * math.pi * (self.radius ** 3)
        return vol
