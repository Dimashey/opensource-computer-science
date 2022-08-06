import re

f_handle = open("../files/mbox.txt")
regex = input("Enter a regular expression: ")

count = 0

for line in f_handle:
    if re.search(regex, line.strip()):
        count += 1

print(f"mbox.tx had {count} line that matches {regex}")
