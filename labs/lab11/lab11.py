"""
Name: Long Tang
lab11.py
Problem: Develop a program using class and graphics to make a three door game
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from random import randint
from lab10.door import Door
from lab10.button import Button


def three_door_game():
    win = GraphWin("Three Door Game", 500, 500)
    win.setBackground("blue")

    secret_door_txt = Text(Point(250, 150), 'I have a secret door')
    secret_door_txt.setSize(15)

    click_guess_secret = Text(Point(250, 450), 'Click to guess which is the secret door!')
    click_guess_secret.setSize(15)

    win_lose = Rectangle(Point(200, 55), Point(50, 125))
    win_lose.draw(win)
    line_box = Line(Point(122, 55), (Point(122, 125)))
    line_box.draw(win)

    correct = Text(Point(250, 120), 'You win!')

    win_txt = Text(Point(90, 45), 'Wins')
    win_txt.setSize(15)
    win_txt.draw(win)
    win_count = Text(Point(90, 85), '0')
    win_count.setSize(15)
    win_count.draw(win)

    incorrect = Text(Point(250, 120), 'Sorry, incorrect!')

    lose_txt = Text(Point(165, 45), 'Losses')
    lose_txt.setSize(15)
    lose_txt.draw(win)
    lose_count = Text(Point(165, 85), '0')
    lose_count.setSize(15)
    lose_count.draw(win)

    door_1 = Rectangle(Point(50, 175), Point(150, 430))
    door_1_txt = Door(door_1, 'Door 1', 250, 295)
    door_1_txt.color_door('grey')
    door_1_txt.draw(win)

    door_2 = Rectangle(Point(200, 175), Point(300, 430))
    door_2_txt = Door(door_2, 'Door 2', 250, 295)
    door_2_txt.color_door('grey')
    door_2_txt.draw(win)

    door_3 = Rectangle(Point(350, 175), Point(445, 430))
    door_3_txt = Door(door_3, 'Door 3', 250, 295)
    door_3_txt.color_door('grey')
    door_3_txt.draw(win)

    quit_box = Rectangle(Point(450, 25), Point(290, 115))
    quit_txt = Button(quit_box, 'Quit', 250, 295)
    quit_txt.draw(win)

    replay = Text(Point(250, 470), 'Do you want to play again?')

    win_count.setText("0")
    win_cnt = 0

    lose_count.setText("0")
    lose_cnt = 0
    play_again = False
    click_guess_secret.draw(win)
    secret_door_txt.draw(win)
    while not play_again:

        sec = randint(0, 3)
        if sec == 1:
            door_1_txt.set_secret(True)
            door_2_txt.set_secret(False)
            door_3_txt.set_secret(False)
        elif sec == 2:
            door_2_txt.set_secret(True)
            door_1_txt.set_secret(False)
            door_3_txt.set_secret(False)
        elif sec == 3:
            door_3_txt.set_secret(True)
            door_2_txt.set_secret(False)
            door_1_txt.set_secret(False)

        if quit_txt.is_clicked(win.getMouse()):
            play_again = True
            win.close()

        else:
            clicked = win.getMouse()
            while door_1_txt.is_secret():
                if door_1_txt.is_clicked(clicked):
                    door_1_txt.color_door('green')
                    correct.draw(win)
                    win_cnt += 1
                    win_count.setText(str(win_cnt))

                else:
                    door_1_txt.color_door('green')
                    if door_2_txt.is_clicked(clicked):
                        door_2_txt.color_door("red")
                    elif door_3_txt.is_clicked(clicked):
                        door_3_txt.color_door("red")
                    incorrect.draw(win)
                    lose_cnt += 1
                    lose_count.setText(str(lose_cnt))
                secret_door_txt.undraw()
                click_guess_secret.undraw()
                replay.draw(win)
                break

            while door_2_txt.is_secret():
                if door_2_txt.is_clicked(clicked):
                    door_2_txt.color_door('green')
                    correct.draw(win)
                    win_cnt += 1
                    win_count.setText(str(win_cnt))
                else:
                    door_2_txt.color_door('green')
                    if door_1_txt.is_clicked(clicked):
                        door_1_txt.color_door("red")
                    elif door_3_txt.is_clicked(clicked):
                        door_3_txt.color_door("red")
                    incorrect.draw(win)
                    lose_cnt += 1
                    lose_count.setText(str(lose_cnt))
                secret_door_txt.undraw()
                click_guess_secret.undraw()
                replay.draw(win)
                break

            while door_3_txt.is_secret():
                if door_3_txt.is_clicked(clicked):
                    door_3_txt.color_door('green')
                    correct.draw(win)
                    win_cnt += 1
                    win_count.setText(str(win_cnt))

                else:
                    door_3_txt.color_door('green')
                    if door_2_txt.is_clicked(clicked):
                        door_2_txt.color_door("red")
                    elif door_1_txt.is_clicked(clicked):
                        door_1_txt.color_door("red")
                    incorrect.draw(win)
                    lose_cnt += 1
                    lose_count.setText(str(lose_cnt))
                secret_door_txt.undraw()
                click_guess_secret.undraw()
                replay.draw(win)
                break

            while not quit_txt.is_clicked(win.getMouse()):
                door_1_txt.color_door('grey')
                door_2_txt.color_door('grey')
                door_3_txt.color_door('grey')
                correct.undraw()
                incorrect.undraw()
                replay.undraw()
                play_again = False
                secret_door_txt.draw(win)
                click_guess_secret.draw(win)
                break


three_door_game()
