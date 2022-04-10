import re


def count(string, letter):
    count = 0
    index = 0

    while index < len(string):
        if string[index] == letter:
            count = count + 1

        index = index + 1


    return count

string = input("Enter a string: ")
letter = input("Enter a letter: ")

print(f"Total count of letter {letter} is {count(string, letter)}")