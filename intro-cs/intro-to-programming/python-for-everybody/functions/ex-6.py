import re


def computepay(hours, rate):
    extraPay = 0
    pay = hours * rate

    if hours > 40:
        extraHours = hours - 40
        extraRate = rate * 0.5
        extraPay = extraHours * extraRate

    return pay + extraPay



try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
    pay = computepay(hours, rate)

    print("Pay: " + str(pay))
except:
    print("Error, please enter numeric input")
