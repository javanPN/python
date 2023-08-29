total_cost = 1000000
portion_down_payment = 0.25
current_savings = 10000
annual_rate_of_return = 0.04
portion_saved = 0.25
annual_salary = 100000
six_monthly_salary_with_raise = annual_salary + annual_salary*.10


def calc_months_to_save():
    monthly_savings_from_investments = current_savings*annual_rate_of_return/12
    monthly_salary = annual_salary/12
    down_payment = total_cost*portion_down_payment
    monthly_savings_from_salary = monthly_salary*portion_saved
    total_monthly_savings = monthly_savings_from_investments+monthly_savings_from_salary
    number_of_months_to_save = (down_payment - current_savings)/total_monthly_savings
    print(annual_salary)
    print(portion_saved)
    print(total_cost)
    print(down_payment)
    print(total_monthly_savings)
    print(number_of_months_to_save)

#calc_months_to_save()

loop_counter = 0
while (loop_counter < 3):
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of you salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    calc_months_to_save()
    loop_counter = loop_counter + 1

