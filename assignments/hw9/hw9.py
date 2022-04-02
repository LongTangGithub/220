"""
Name: Long Tang
hw9.py
Problem: Develop a hangman game using functions, conditionals, and decision structures
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *


def get_words(file_name):
    file = open(file_name, 'r')
    return file.readlines()


def get_random_word(words):
    num_words = randint(0, len(words) - 1)
    return words[num_words]


def letter_in_secret_word(letter, secret_word):
    return letter in secret_word


def already_guessed(letter, guesses):
    return letter in guesses


def make_hidden_secret(secret_word, guesses):
    word = []
    for i in range(len(secret_word) - 1):
        word.append("_ ")

    for k in range(len(secret_word) - 1):
        letter = secret_word[k]
        for j in guesses:
            if j == letter:
                word[k] = letter + " "
    return "".join(word)


def won(guessed):
    n_guessed = guessed.replace(" ", "")
    return "_" not in n_guessed


def play_graphics(secret_word):
    win = GraphWin("Hangman", 500, 500)
    win.setBackground("white")
    guessed_letters = []
    guessed = " "
    turns = 6

    gallows_1 = Line(Point(250, 400), Point(250, 100))
    gallows_1.draw(win)

    gallows_2 = Line(Point(140, 400), Point(310, 400))
    gallows_2.draw(win)

    gallows_3 = Line(Point(250, 100), Point(140, 100))
    gallows_3.draw(win)

    gallows_4 = Line(Point(140, 100), Point(140, 165))
    gallows_4.draw(win)

    guess_lttr = Text(Point(155, 473), "Guess a Letter: ")
    guess_lttr.setSize(15)
    guess_lttr.draw(win)

    while turns > 0:

        secret_wrd = Text(Point(250, 450), make_hidden_secret(secret_word, guessed_letters))
        secret_wrd.setSize(15)
        secret_wrd.draw(win)

        user_input = Entry(Point(250, 475), 5)
        user_input.draw(win)
        win.getMouse()

        if already_guessed(user_input.getText(), guessed_letters):
            pass
        elif not letter_in_secret_word(user_input.getText(), secret_word):
            turns -= 1
            guessed_letters.append(user_input.getText())
        else:
            guessed_letters.append(user_input.getText())

        if turns == 5:
            head = Circle(Point(140, 190), 25.5)
            head.draw(win)

        elif turns == 4:
            body = Line(Point(140, 215), Point(140, 355))
            body.draw(win)
        elif turns == 3:
            left_arm = Line(Point(140, 215), Point(80, 250))
            left_arm.draw(win)
        elif turns == 2:
            right_arm = Line(Point(140, 215), Point(200, 250))
            right_arm.draw(win)
        elif turns == 1:
            left_leg = Line(Point(140, 355), Point(90, 390))
            left_leg.draw(win)
        elif turns < 1:
            right_leg = Line(Point(140, 355), Point(190, 390))
            right_leg.draw(win)

        guessed = make_hidden_secret(secret_word, guessed_letters)
        win_lose = Text(Point(250, 50), "Winner\n" + secret_word)
        if won(guessed):
            win_lose.draw(win)
            break

    lose_win = Text(Point(250, 50), "sorry, you did not guess the word\n the secret word was " + secret_word)
    if not won(guessed):
        lose_win.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guessed_letters = []
    guessed = " "
    turns = 6
    while turns > 0:
        print("Already guess: ", guessed_letters)
        print("Guesses remaining: ", turns)
        print(make_hidden_secret(secret_word, guessed_letters))
        user_input = input("Enter letter: ")

        if already_guessed(user_input, guessed_letters):
            pass
        elif not letter_in_secret_word(user_input, secret_word):
            turns -= 1
            guessed_letters.append(user_input)
        else:
            guessed_letters.append(user_input)

        guessed = make_hidden_secret(secret_word, guessed_letters)
        if won(guessed):
            print("winner\n", secret_word)
            break

    if not won(guessed):
        print("sorry, you did not guess the word.")
        print("the secret word was", secret_word)


if __name__ == '__main__':
    words = get_words("words.txt")
    sec_word = get_random_word(words)

    play_command_line(sec_word)
    play_graphics(sec_word)
