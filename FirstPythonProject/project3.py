MAX_LINES = 3


def deposite():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return lines

def get_number_of_lines():
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount


def main():
    balance = deposite()

main()