f_name = input('Enter file name: ')
f_handle = open(f_name)

histogram = dict()

for line in f_handle:
    if line.startswith('From:'):
        words = line.split()
        email = words[1]
        histogram[email] = histogram.get(email, 0) + 1

print(histogram)