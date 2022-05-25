
f_name = input('Enter file name: ')
f_handle = open(f_name)

histogram = dict()

for line in f_handle:
    if line.startswith('From:'):
        words = line.split()
        email = words[1]
        histogram[email] = histogram.get(email, 0) + 1


email = None
quantity = None

for k in histogram:
    if quantity is None or histogram[k] > quantity:
        email = k
        quantity = histogram[k]

print(f"{email} {quantity}")
        