hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
extraPay = 0
pay = hours * rate

if hours > 40:
    extraHours = hours - 40
    extraRate = rate * 0.5
    extraPay = extraHours * extraRate

print("Pay: " + str(pay + extraPay))


