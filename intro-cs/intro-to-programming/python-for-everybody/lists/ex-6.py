numbers = []

while True:
    try:
        value = input("Enter a number: ") 

        if value == 'done':
            break

        number = float(value)
        numbers.append(number)
    except:
        print("Please enter the number")

print(f"Maximum: {max(numbers)}")
print(f"Minumum: {min(numbers)}")