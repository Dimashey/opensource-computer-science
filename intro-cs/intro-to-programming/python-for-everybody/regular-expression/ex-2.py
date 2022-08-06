import re

f_name = input("Enter file: ")
f_handle = open(f_name)
revisions = []

for line in f_handle:
    line_revisions = re.findall("New Revision: ([0-9]+)", line.strip())
    if len(line_revisions) > 0: revisions.append(int(line_revisions[0]))

print(int(sum(revisions) / len(revisions)))

