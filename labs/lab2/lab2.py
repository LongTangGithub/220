"""
Long Tang
lab1.py
Computing for the monthly interest charge on a credit card account
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
def means():
    number_of_values = eval(input("enter the values to be entered: "))
    rms = 0
    harmonic_mean = 0
    geometric_mean = 1
    for i in range(number_of_values):
        values = eval(input("enter the value: "))
        rms = rms + values ** 2
        harmonic_mean = harmonic_mean + 1/values
        geometric_mean = (geometric_mean * values)

    rms = math.sqrt(rms/number_of_values)
    harmonic_mean = (number_of_values / harmonic_mean)
    geometric_mean = geometric_mean ** (1/number_of_values)

    print("The RMS is: ", rms)
    print("The Harmonic Mean is: ", harmonic_mean)
    print("The Geometric Mean is: ", geometric_mean)

means()




