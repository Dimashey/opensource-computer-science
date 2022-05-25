f_handle = open('words.txt')

words_dict = dict()
count = 0

for line in f_handle:
    for word in line.split():
        if word not in words_dict:
            words_dict[word] = count
            count = count + 1

print(words_dict)