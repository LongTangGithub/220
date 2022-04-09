"""
Name: Long Tang
hw10.py
Problem: Develop programs that consist of boolean values, class/objects, and decision/repetition structures
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(n):
    # if the value of n is less than 1, return none
    if n < 1:
        return None
    # if the value of n is 1 or 2, return 1
    elif n == 1 or n == 2:
        return 1
    # if the value of n is greater than 2, find the nth number
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)  # using recursive method


print(fibonacci(3))
print(fibonacci(4))


def double_investments(principle, rate):
    years = 0
    double = principle * 2
    while principle < double:
        investment = principle + (1 + rate)
        principle = investment
        years += 1
    return years


def syracuse(n):
    # appending numbers to list
    lists = [n]

    while n != 1:
        if n % 2 == 0:  # check if number is even
            n = n / 2
        else:
            n = 3 * n + 1  # check if number is odd
        lists.append(int(n))  # append even and odds to list. Make the values an integer
    print(lists)


syracuse(5)


def goldbach(n):
    pass

