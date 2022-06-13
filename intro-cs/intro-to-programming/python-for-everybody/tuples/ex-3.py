import string

f_name = input("Enter a file name: ")
f_handle = open(f_name)
letters_quantity = {}
letter_quantity_list = []

for line in f_handle:
    prepared_line = line.translate(str.maketrans('', '', string.punctuation + string.whitespace + string.digits)).lower()
    for letter in prepared_line:
        letters_quantity[letter] = letters_quantity.get(letter, 0) + 1

for key, value in list(letters_quantity.items()):
    letter_quantity_list.append((value, key))

letter_quantity_list.sort(reverse=True)

for value, key in letter_quantity_list:
    print(f"{key} {value}")