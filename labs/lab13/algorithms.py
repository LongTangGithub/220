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


def selection_sort(values):
    for i in range(len(values)):
        sort = i
        for j in range(i + 1, len(values)):
            if values[sort] > values[j]:
                sort = j
        values[i], values[sort] = values[sort], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    area = length * width
    return area


def rect_sort(rectangles):
    value = 0
    while value < len(rectangles):
        sort = value
        for i in range(value, len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[sort]):
                sort += 1
                rectangles[sort], rectangles[value] = rectangles[value], rectangles[sort]


if __name__ == "__main__":
    pass
