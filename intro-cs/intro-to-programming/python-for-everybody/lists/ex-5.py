file_name = input("Enter a file name: ")

count = 0

try:
    f_handle = open(file_name)

    for line in f_handle:
        if line.startswith('From'):
            words = line.split()
            print(words[1])
            count = count + 1
except:
    print('There is no file with with this name')

print(f"There were {count} lines in the file with From as the first word")
