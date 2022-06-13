f_name = input("Enter a file name: ")
f_handle = open(f_name)

hours_quantity = {}

for line in f_handle:
    if line.startswith("From") and len(line.split()) > 3:
        words = line.split()[5].split(':')
        hour = words[0]
        hours_quantity[hour] = hours_quantity.get(hour, 0) + 1


print(hours_quantity)