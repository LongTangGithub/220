"""
Name: <Long Tang>
<hw5>.py

Problem: Manipulating strings, lists through slicing and indexing.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("enter a name (first and last): ")  # Wendy Darling
    first = name[0:5]  # slicing the first name starting with first letter until the space which is 5
    last = name[6:]  # slicing the last name starting with the 6th letter to all the way
    print(last + ",", first)  # Last name + comma + first name = Darling, Wendy


def company_name():
    domain = input("enter a domain: ")  # www.Amazon.com
    website = domain[4:10]  # slicing from 4 to 10
    print(website)  # output: Amazon


def initials():
    students = input("how many students are in the class? ")  # Ask user for input. The input is "3" students
    print(students)

    name1 = input("what is the name of student 1? ")  # Atticus Finch
    student_1 = name1[0] + name1[8]
    print(student_1)

    name2 = input("what is the name of student 2? ")  # Dill Harris
    student_2 = name2[0] + name2[5]
    print(student_2)

    name3 = input("what is the name of student 3? ")  # Arthur Radley
    student_3 = name3[0] + name3[7]
    print(student_3)


def names():
    name_list = input("enter a list of names: ")  # Neil Armstrong, Michael Collins, Edwin Aldrin
    astronaut = name_list.split(" ")  # split the astronaut names
    initial = " "  # make the initial variable hold the first of each word from the input
    for name in astronaut:  # loop through each name
        initial += name[0]  # appending the names
    print(initial)


def thirds():
    sentence_num = eval(input("enter the number of sentences: "))  # ask the input; 4
    for i in range(sentence_num):  # create a for loop that loop the amount of times that sentence_num equals
        sentences = input("\nenter sentence: ")  # input sentence; \n creates a new line instead of the same line

        for j in range(0, len(sentences), 3):  # nested loop; print the 1st letter of sentence and every 3rd after that
            print("", sentences[j], end="")


def word_average():
    sentence = input("enter a sentence: ")  # Ask user for input; the quick brown fox jumps over the lazy dog
    total = 0  # initializing total and word_count to 0
    word_count = 0
    for words in sentence.split():  # loop through each words from the input; split the sentence
        length = len(words)  # initializing length equal to the length of the next word inside the loop
        total += length  # adding length to total variable
        word_count += 1  # adding 1 to each word count
    average = word_count / total  # divide the two variables to find the average of word length
    print(average)  # output = 3.888888888888889; average word length in a sentence


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")  # input; The time has come the Walrus said
    words = sentence.split()  # split the sentence into words
    word = ""  # Initializing the variable word
    for pig in words:  # Loop through words
        word += pig[1:] + pig[0] + "ay "  # take the second letter from the word and put it to the front
        # ; concatenate to the front and ay
        word = word.lower()  # make all words lowercase
    print(word)


if __name__ == '__main__':
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    pass
