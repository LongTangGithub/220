"""
Long Tang
lab1.py
Computing for the monthly interest charge on a credit card account
Certification of Authenticity:
I certify that this assignment is entirely my own work.
Long Tang
"""

def monthly_interest():
    annual_interest_rate = eval(input("Annual Interest Rate: "))
    days_in_cycle = eval(input("Number of days in billing cycle: "))
    previous_net_balance = eval(input("Previous (net) balance: "))
    payment_amount = eval(input("Payment amount: "))
    day_of_payment = eval(input("Day of cycle payment was made: "))
    monthly_interest = (annual_interest_rate / 12)/100
    # monthly_interest_charge = eval(input("Monthly interest charge: "))

    step_1 = previous_net_balance * days_in_cycle
    step_2 = payment_amount * (days_in_cycle - day_of_payment)
    step_3 = step_1 - step_2
    average_daily_balance = step_3 / days_in_cycle  #step_4 result is avg daily balance
    monthly_interest_charge = average_daily_balance * monthly_interest
    print("Monthly interest charge:", monthly_interest_charge)

monthly_interest()
