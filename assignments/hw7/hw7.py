"""
Long Tang
hw7.py
Develop programs using functions and files
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import encryption

in_file_name = 'sentence.txt'
out_file_name = 'number.txt'


def number_words(in_file_name, out_file_name):
    words = ''
    with open(in_file_name, 'r') as f:
        for i in f:
            words += i.replace("\n", " ")
        word_list = words.split(" ")
    f.close()
    with open(out_file_name, 'w') as n:
        for i in range(len(word_list)):
            print(str(i + 1) + " " + word_list[i])
            n.write(str(i + 1) + " " + word_list[i] + "\n")
    n.close()


in_file_name_1 = 'hourly_wages.txt'
out_file_name_1 = 'employees.txt'


def hourly_wages(in_file_name_1, out_file_name_1):
    with open(in_file_name_1, 'r') as money:
        with open(out_file_name_1, 'w') as salary:
            for i in money:
                employee = i.replace("\n", "").split(" ")
                wage = float(employee[2])
                hours = int(employee[3])
                bonus = 1.65 * hours
                income = wage * hours
                total_income = float(income + bonus)
                print(employee[0] + " " + employee[1] + ": " + str(total_income))
                salary.write(employee[0] + " " + employee[1] + ": " + str(total_income) + '\n')
        salary.close()
    money.close()


def calc_check_sum(isbn):
    n_isbn = []
    for i in isbn:
        if i != "-":
            n_isbn.append(i)
    sum = 0
    for i in range(0, 10, 1):
        sum += int(n_isbn[i]) * (10 - i)
    return sum


file_name = "friend_msg.txt"


def send_message(file_name, friend_name):
    with open(file_name, "r") as message:
        with open(friend_name + ".txt", "w") as send_msg:
            for i in message:
                send_msg.write(i)
        send_msg.close()
    message.close()


def send_safe_message(file_name, friend_name, key):
    with open(file_name, "r") as safe_msg:
        with open(friend_name + ".txt", "w") as send_msg:
            for i in safe_msg:
                send_msg.write(encryption.encode(i, key) + "\n")
        send_msg.close()
    safe_msg.close()


pad_file_name = "pad.txt"


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    with open(file_name, "r") as safe_msg:
        with open(pad_file_name, "r") as pad:
            for j in pad:
                key = j
        with open(friend_name + ".txt", "w") as send_msg:
            msg = ""
            for i in safe_msg:
                msg += i.replace("\n", " ")
            print(msg)
            send_msg.write(encryption.encode_better(msg, key))
        send_msg.close()
    safe_msg.close()


if __name__ == '__main__':
    number_words(in_file_name, out_file_name)
    hourly_wages(in_file_name_1, out_file_name_1)
    isbn = "0-072-94652-0"
    calc_check_sum(isbn)
    send_message(file_name, "Patrick")
    send_safe_message(file_name, "Daniel", 2)
    send_uncrackable_message(file_name, "Ian", pad_file_name)
