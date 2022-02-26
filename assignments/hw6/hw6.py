"""
Long Tang
hw6.py
Tackling functions that accept arguments and return values using strings and modifying objects in parameter
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def cash_converter():
    integer = input("enter an integer: ")  # Prompt user for integer input: 7
    sentence = "That is ${:.2f}".format(float(integer))  # format the float of the integers 2 decimals
    print(sentence)  # output: That is $7.00


cash_converter()


def encode():
    message = input("enter a message: ")  # Prompt user for the message input: The time has come, the Walrus said
    key = input("enter a key: ")  # Prompt user for the key input: 7

    cipher = "".join(chr(ord(c) + int(key)) for c in message)  # grab every character (c) in message and add key to
    # it; and concatenate into a string
    print(cipher)  # output: [ol'{ptl'ohz'jvtl3'{ol'^hsy|z'zhpk


encode()


def sphere_area(radius: float):  # set radius to be a float
    area = float(4 * math.pi * radius * radius)  # use the area formula of a sphere and make it into a float
    return area


def sphere_volume(radius: float):
    volume = float((4 / 3) * math.pi * math.pow(radius, 3))  # use  the volume formula of a sphere and make it into a
    # float
    return volume


print("Surface area: ", sphere_area(3))  # output: 113.09733552923255
print("Volume: ", sphere_volume(3))  # output: 113.09733552923254


def sum_n(number: int):  # set number variable to an integer
    sum = 0  # initialize sum
    for i in range(1, number + 1):  # loop start at 1 and loops until the number + 1 is reached
        sum += i  # updated sum with the index i
    return sum


def sum_n_cubes(number: int):
    sum = 0
    for i in range(1, number + 1):
        sum += i ** 3  # update sum with index i and raise it by 3 since its subed
    return sum


print("total: ", sum_n(2))  # output: 3
print("total: ", sum_n_cubes(2))  # output: 9


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")

    newEncoded = []  # initialize list
    newResult = " "

    for i in range(len(message)):  # loop every character of message and key
        newEncoded.append(((ord(message[i]) - 65) + (ord(key[i % len(key)]) - 65)) % 58)  # add the unicode of the
        # first index i in the message and key together then mod 58

    for i in newEncoded:
        newResult += chr(int(i) + 65) + ""  # take the new result from newEncoded, apply chr, and 65; "" to make it
        # no space

    return newResult  # make the new result return as a string


print(encode_better())
