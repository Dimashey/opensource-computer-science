import urllib.request

f_handle = urllib.request.urlopen('http://data.pr4e.org/mbox.txt')

count = 0

for line in f_handle:
    handling_line = line.decode().strip()
    count += len(handling_line.split())

    if count >= 3000:
        end = 3000 - len(handling_line.split())
        print(handling_line[:end])
        break

    print(handling_line)
