


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unssuported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["days"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid number")
        else:
            print("You entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a valid number, please don't crash my program")

user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter a number of days and conversion unit\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days" : days_and_unit[0], "unit": "hours"}
    print(days_and_unit_dictionary)
    validate_and_execute()

my_list = ["20", "30", "100"]
print(my_list[2])

my_dictionary = {"days": 20, "unit": "hours"}
print(my_dictionary["days"])