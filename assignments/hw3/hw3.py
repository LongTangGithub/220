"""
Name: Long Tang
hw3.py

Problem: Using loops to create simple Python programs that do input, output, and arithmetic.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""


def average():
    num_grades = eval(input("how many grades will you enter? "))
    total_grades = 0
    for i in range(1, num_grades + 1):
        grade = eval(input("Enter grade: "))
        total_grades = total_grades + grade
    avg = total_grades / num_grades
    print("average is ", avg)


average()


def tip_jar():
    donate = eval(input("how much would you like to donate? "))  # 5 people
    tips = 0
    for i in range(donate):
        donation = eval(input("how much would you like to donate? "))
        tips = tips + donation
    print("total tips: ", tips)


tip_jar()


def newton():
    num = eval(input("What number do you want to square root? "))
    approx = eval(input("How many times should we improve the approximation? "))
    for i in range(approx):
        approx = (approx + (float(num) / approx)) / 2
    print("the square root is approximately ", approx)   # odd num % 2 = 1,   even num % 2 = 0


newton()


def sequence():
    term = eval(input("how many terms would you like? "))
    for i in range(1, term + 1):
        print((i - (i - 1) % 2), end=" ")


sequence()


def pi():
    terms = eval(input("how many terms in the series? "))
    num = float(1)
    for i in range(1, terms + 1):
        num = num * (((i + 1) - ((i - 1) % 2)) / (i - ((i - 1) % 2)))
    print(num)


pi()

if __name__ == '__main__':
    pass
