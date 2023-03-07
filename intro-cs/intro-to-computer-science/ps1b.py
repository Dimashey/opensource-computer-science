annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your fream home: "))
semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
month_salary = annual_salary / 12

down_payment = total_cost * portion_down_payment

def get_investemtns():
    return (current_savings * 0.04) / 12

months = 0

while current_savings < down_payment:
    save_money = month_salary * portion_saved
    current_savings += save_money + get_investemtns()
    months += 1

    if months % 6 == 0:
        month_salary += month_salary * semi_annual_rise

print(f"Number of months: {months}")

