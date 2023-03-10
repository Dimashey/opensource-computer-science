import numpy
annual_salary = int(input("Enter the starting salary: "))
month_salary = annual_salary / 12
semi_annual_rise = .07
down_payment = 250000

def get_investemtns(current_savings):
    return (current_savings * .04) / 12

def get_saved_money(salary_portion, month_salary):
    current_savings = 0

    for month in range(1, 37):
        save_money = month_salary * salary_portion
        current_savings += save_money + get_investemtns(current_savings)

        if month % 6 == 0:
            month_salary += month_salary * semi_annual_rise

    return current_savings


def bisection_search(start, end, depth, max_depth):
    depth += 1
    mid = int((start + end) / 2)

    if depth > int(max_depth):
        return None, None

    portion = float(mid) / 10000
    saved_money = get_saved_money(portion, month_salary)

    if saved_money > down_payment and saved_money <= down_payment + 100:
        return portion, depth
    elif saved_money > down_payment:
        return bisection_search(start, mid, depth, max_depth)
    else:
        return bisection_search(mid, end, depth, max_depth)

portion, depth = bisection_search(0, 10000, 0, numpy.log2(10000))

if portion:
    print(f"Best savings rate: {str(round(portion, 4))}")
    print(f"Steps in bisection search: {depth}")
else:
    print("It is not possible to pay the down payment in three years.")



