"""
Name: Long Tang
lab12.py
Problem: Develop programs using while control structures, built-in list methods, and linear search on data
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    data_list = []
    file_read = open(filename, "r")
    each_line = file_read.readlines()
    datas = 0
    while each_line:
        line = each_line.strip()
        line_list = line.split(" ")
        while datas < len(line_list):
            data_list.append(line_list[datas])
            datas += 1
    return data_list


def is_in_linear(search_val, values):
    i = 0
    found = False
    while i < len(values) and found == False:
        if values[i] == search_val:
            found = True
        else:
            i += 1
    return found


if __name__ == "__main__":
    pass