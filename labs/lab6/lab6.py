"""
Long Tang
lab6.py
Developed a program to implement the Vigenere cipher
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *  # import graphics from the graphics.py


def vigenere():
    win = GraphWin("Vigenere", 500, 500)  # implements a window where drawings can be done
    win.setBackground("white")

    message = Text(Point(80, 65), "Message to code")  # The text "Message to code"
    message.setSize(15)  # set font size to 15
    message.draw(win)  # draw it

    message_box = Entry(Point(278, 67), 35)  # Entry(center point, width) -> built-in function that allows input in box
    message_box.draw(win)

    key = Text(Point(80, 120), "Enter keyword")
    key.setSize(15)
    key.draw(win)

    key_box = Entry(Point(243, 120), 25)
    key_box.draw(win)

    encode_box = Rectangle(Point(150, 145), Point(300, 230))  # encode box
    encode_box.setOutline("black")
    encode_box.setFill("white")
    encode_box.draw(win)

    encode_txt = Text(Point(225, 185), "Encode")  # "Encode" text place within the encode box
    encode_txt.setSize(16)
    encode_txt.draw(win)

    win.getMouse()  # get user click
    encode_box.undraw()  # make the encode box disappear
    encode_txt.undraw()  # male the encode text disappear along with the encode text

    result_msg = Text(Point(250, 300), "Resulting Message")
    result_msg.setSize(15)
    result_msg.draw(win)

    win.getMouse()

    message = message_box.getText()
    message = message.upper()  # make the user input message all uppercase
    message = message.replace(" ", "")  # make the user input message to have no space between them by replacing

    key = key_box.getText()
    key = key.upper()  # make the user input key all uppercase
    key = key.replace(" ", "")  # make the user input key to have no space between them by replacing

    newEncoded = []
    newResult = []

    for i in range(len(message)):
        newEncoded.append(((ord(message[i]) - 65) + (ord(key[i % len(key)]) - 65)) % 26)

    for i in newEncoded:
        newResult.append(chr(int(i)+65))

    newKeys = Text(Point(250, 325), newResult)
    newKeys.draw(win)

    txt = Text(Point(250, 490), "Click Anywhere to Close Window!")
    txt.setSize(13)
    txt.draw(win)

    win.getMouse()
    win.close()


vigenere()
