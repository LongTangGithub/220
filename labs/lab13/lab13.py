"""
Name: Long Tang
lab13.py
Problem: Develop programs comparing search/sort algorithms
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    trade_data = open(filename, "r")
    volume = trade_data.readlines()
    warning = volume.split()
    for i in range(len(warning)):
        if eval(warning[i]) > 830:
            print('Trading volume exceeds 830 at {}!'.format(i + 1))
        elif eval(warning[i]) == 500:
            print('Trading volume exceeds 500 at {}!'.format(i + 1))
    trade_data.close()


if __name__ == "__main__":
    pass
