count = 0
sum = 0

while True:
    try:
        value = input('Enter a number: ')

        if value == 'done':
            break

        num = int(value)

        count = count + 1;
        sum = sum + num
    except:
        print('Invalid input')

print(sum, count, sum / count)