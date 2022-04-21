fhandle = open('mbox-short.txt')

for line in fhandle:
    print(line.rstrip().upper())
