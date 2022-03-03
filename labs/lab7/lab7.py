"""
Long Tang
lab7.py
Developed a Python software that uses numeric data from a text file to solve a problem.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

in_file_name = "grades"
out_file_name = "avg"


def weighted_average(in_file_name, out_file_name):
    with open(in_file_name, 'r') as grades:
        with open(out_file_name, 'w') as average:
            class_average_nums = []
            class_average = 0
            num_lines = 0
            for k in grades:
                grades_list = k.replace("\n", "").replace(":", "").split(" ")
                hundred_chk = 0
                avg = 0
                for i in range(1, len(grades_list), 2):
                    hundred_chk += int(grades_list[i])

                if hundred_chk < 100:
                    for i in range(1, len(grades_list), 1):
                        if i % 2 == 0:
                            avg += (int(grades_list[i - 1]) * int(grades_list[i]))
                    avg = avg / 100
                    class_average_nums.append(avg)
                    print(grades_list[0] + " average: Error: The weights are less than 100.")
                    average.write(grades_list[0] + " average: Error: The weights are less than 100.\n")
                    num_lines += 1
                elif hundred_chk > 100:
                    for i in range(1, len(grades_list), 1):
                        if i % 2 == 0:
                            avg += (int(grades_list[i - 1]) * int(grades_list[i]))
                    avg = avg / 100
                    class_average_nums.append(avg)
                    print(grades_list[0] + " average: Error: The weights are more than 100.")
                    average.write(grades_list[0] + " average: Error: The weights are more than 100.\n")
                    num_lines += 1
                else:
                    for i in range(1, len(grades_list), 1):
                        if i % 2 == 0:
                            avg += (int(grades_list[i - 1]) * int(grades_list[i]))
                    avg = avg / 100
                    class_average_nums.append(avg)
                    av = (grades_list[0] + " average: " + str(avg))
                    print(av)
                    average.write(av+"\n")
                    num_lines += 1

            for i in class_average_nums:
                class_average += i
            print("Class average: " + str(class_average / num_lines))
            average.write("Class average: " + str(class_average / num_lines)+"\n")


if __name__ == '__main__':
    weighted_average(in_file_name, out_file_name)
