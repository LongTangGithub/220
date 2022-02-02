"""
Long Tang
lab3.py
Using loop variables and nested loops to find total and average number of vehicles on roads
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    sum_acc = 0
    road = eval(input("How many roads were surveyed? "))
    for i in range(road):
        print("How many days was road", i + 1, "surveyed? ")
        day = eval(input(""))
        road_acc = 0

        for j in range(day):
            print("How many cars travelled on", j + 1, "?")
            cars = eval(input(""))
            road_acc = road_acc + cars
            sum_acc = sum_acc + cars
        road_avg = road_acc / day
        print("Road", i + 1, "average vehicles per day: ", road_avg)
    avg_cars = sum_acc / road

    print("Total number of vehicles traveled on all roads: ", sum_acc)
    print("Average number of vehicles per road: ", avg_cars)

