f_handle = open('romeo.txt')
word_list = []

for line in f_handle:
    for word in line.split():
        if word not in word_list:
            word_list.append(word)

word_list.sort()

print(word_list)