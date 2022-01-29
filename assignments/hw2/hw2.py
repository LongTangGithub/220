"""
Name: Long Tang
hw2.py

Problem: <Developed Python programns that involves arithmetic, which requires the input and output >

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""



def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    s = 0
    for i in range(3, upper_bound + 1, 3):
        print(i, end =" ")
        s+= i
    print()
    print("sum of three is ",s )


    


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, "\t" , end = "")
        print()


import math
def triangle_area():
    a = eval(input("Enter side a length: "))
    b = eval(input("Enter side b length: "))
    c = eval(input("Enter side c length: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("area is ",area )




def sum_squares():
    lower_range = eval(input("Enter the lower range: "))
    upper_range = eval(input("Enter the upper range: "))
    sum = 0
    for i in range(lower_range, upper_range + 1):
        sum = sum + i * i
        i += 1
    print(sum)





def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    x = 1
    for i in range (exponent):
        x = x * base
    print(base, "^", exponent, "=", x)


if __name__ == '__main__':
    pass
sum_of_threes()
multiplication_table()
triangle_area()
sum_squares()
power()
