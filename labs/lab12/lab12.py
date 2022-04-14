"""
Name: Long Tang
lab12.py
Problem: Develop programs using while control structures, built-in list methods, and linear search on data
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint


def first_and_remove_first(list, value):
    i = 0
    while list[i] != value:
        i += 1
    else:
        list.pop(i)
        list.insert(i, "L.T")


def good_input():
    while True:
        num = eval(input("Enter a number: "))
        if 0 < num < 11:
            print(num)
        elif num < 1:
            print("too low")
        elif num > 10:
            print("too high")
        else:
            print("Number should be in range from 1 to 10 ")


def num_digits():
    positive = True
    while positive:
        n = eval(input("Enter positive number: "))
        count = 0
        if n == 0 or n < 0:
            positive = False
        else:
            while n != 0:
                if (n // 10) == 0:
                    n //= 10
                    count += 1
                else:
                    n //= 10
                    count += 1

            print("this number has",count,"digits.")


def hi_lo_game():
    number = randint(1, 100)
    i = 0
    while i < 7:
        guess = int(input("Guess the Number : "))
        if i == 6:
            print("Sorry,you lose.The number was ", number)
        if guess == number:
            print("Correct \n You win in ", i + 1, " guesses!")
            i = 7
        elif guess > number:
            print("too high")
        elif guess < number:
            print("too low")
        i += 1


if __name__ == "__main__":
    pass
