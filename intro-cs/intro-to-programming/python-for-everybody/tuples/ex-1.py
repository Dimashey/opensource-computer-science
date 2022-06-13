f_name = input("Enter a file name: ")
f_handle = open(f_name)

emails_quantity = {}
emails_quantity_list = []

for line in f_handle:
    if line.startswith('From:'):
        words = line.split()
        email = words[1]
        emails_quantity[email] = emails_quantity.get(email, 0) + 1

for key, value in list(emails_quantity.items()):
    emails_quantity_list.append((value, key))

emails_quantity_list.sort(reverse=True)

quantity, email = emails_quantity_list[0]

print(f"{email} {quantity}")
