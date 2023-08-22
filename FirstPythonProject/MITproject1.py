total_cost = 1000000
portion_down_payment = 0.25
current_savings = 10000
annual_rate_of_return = 0.04
monthly_savings_from_investmants = current_savings*annual_rate_of_return/12
annual_salary = 100000
portion_saved = 0.10
monthly_salary = annual_salary/12
down_payment = total_cost*portion_down_payment
monthly_savings_from_salary = annual_salary*portion_saved/12
total_montyly_savings = monthly_savings_from_investmants+monthly_savings_from_salary
# annual_salary = input("Enter your annual salary: ")
# portion_saved = input("Enter the percent of you salary to save, as a decimal: ")
# total_cost = input("Enter the cost of your dream home: ")
#monthly_savings_from_investmants = input("Number of Months: ")

print(annual_salary)
print(portion_saved)
print(total_cost)
print(down_payment)
print(monthly_savings_from_investmants+monthly_savings_from_salary)
print(down_payment/total_montyly_savings)