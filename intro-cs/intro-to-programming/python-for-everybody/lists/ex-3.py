fhand = open('../files/mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' or len(words) < 3: continue
    print(words[2])