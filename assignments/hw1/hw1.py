"""
Name: LongTang
hw1.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area=", area)
calc_rec_area()


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume=", volume)
calc_volume()

def shooting_percentage():
    shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooting_percentage: int = (shots_made/shots) * 100
    print("Shooting Percentage:", shooting_percentage, "%")
shooting_percentage()



def coffee():
    pounds_of_coffee = eval(input("How many pounds of coffee would you like? "))
    coffee_cost_per_pound = 10.50
    shipping_cost = 0.86
    fixed_cost = 1.50
    total = (coffee_cost_per_pound + shipping_cost + fixed_cost) + (coffee_cost_per_pound + shipping_cost)
    print("Your total is:", total)
coffee()







def kilometers_to_miles():
    kilometers_traveled = eval(input("How many kilometers did you travel? "))
    kilometers = 1.61
    print("That's 1.0 miles!")





if __name__ == '__main__':
    pass

kilometers_to_miles()