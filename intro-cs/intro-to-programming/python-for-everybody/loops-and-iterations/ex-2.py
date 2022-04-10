min = None
max = None

while True:
    try:
        value = input('Enter a number: ')

        if value == 'done':
            break

        num = int(value)

        if max is None or num > max:
            max = num

        if min is None or num < min:
            min = num

    except:
        print('Invalid data')


print(f"Min: {min}, Max: {max}")