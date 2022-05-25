f_handle = open('../files/mbox-short.txt')

daysOfTheWeekCount = dict()

for line in f_handle:
    if line.strip().startswith('From'):
        words = line.split()
        if (len(words) > 2):
            day = words[2]
            daysOfTheWeekCount[day]  = daysOfTheWeekCount.get(day, 0) + 1

print(daysOfTheWeekCount)
