
import re


f_name = input('Enter file name: ')
f_handle = open(f_name)


def get_domain_from_email(email):
    startFrom = email.find('@') + 1
    return email[startFrom:]

histogram = dict()

for line in f_handle:
    if line.startswith('From:'):
        words = line.split()
        domain = get_domain_from_email(words[1])
        histogram[domain] = histogram.get(domain, 0) + 1

print(histogram)