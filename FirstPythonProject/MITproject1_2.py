total_cost = 0.0
portion_down_payment = 0.25
annual_rate_of_return = 0.04
annual_salary = 0.0
portion_saved = 0.0

def calc_months_to_save():
    # monthly_savings_from_investments = current_savings*annual_rate_of_return/12
    monthly_salary = annual_salary/12

    down_payment = total_cost * portion_down_payment
    print("down payment: ", down_payment)

    current_savings = 0
    number_of_months_to_save = 0

    monthly_saving_from_salary_alone = monthly_salary * portion_saved
    print("monthly savings from salary alone: ", monthly_saving_from_salary_alone)

    while (current_savings <= down_payment):
        investment_gains = current_savings * annual_rate_of_return/12
        current_savings = current_savings + investment_gains + monthly_saving_from_salary_alone
        number_of_months_to_save += 1
        # print("current savings:", current_savings)

    print("number of months to save:", number_of_months_to_save)
    
#calc_months_to_save()

loop_counter = 0
loop_limit = 1
while (loop_counter < 1):
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of you salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    print("annual salary: ", annual_salary)
    print("portion saved: ", portion_saved)
    print("total cost: ", total_cost)
    calc_months_to_save()
    loop_counter += 1

