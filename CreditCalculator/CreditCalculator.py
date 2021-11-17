import math

print("""What do you want calculate?
type \"n\" for number of monthly payments,
type \"a\" for annuity monthly payment amount,
type \"p\" for loan principal:""")
choice = str(input())
if choice == "n":
    principal = int(input("Enter the loan principal: "))
    payment = int(input("Enter the monthly payment: "))
    interest = int(input("Enter the loan interest: "))
    percent = float(interest/(12 * 100))
    month = math.ceil(math.log(payment/(payment - percent * principal), 1 + percent))
    years = round(month/12)
    months = month - years * 12
    print(f"It will take {years} years and {months} months to repay this loan!")
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    if months == 0:
        print(f"It will take {years} years to repay this loan!")
if choice == "a":
    principal = int(input("Enter the loan principal: "))
    month = int(input("Enter the number of periods: "))
    interest = int(input("Enter the loan interest: "))
    percent = float(interest/(12 * 100))
    payment = math.ceil(principal * ((percent * ((1 + percent) ** month)) / (((1 + percent) ** month) - 1)))
    print(f"Your monthly payment = {payment}!")
if choice == "p":
    payment = float(input("Enter the monthly payment: "))
    month = float(input("Enter the number of periods: "))
    interest = float(input("Enter the loan interest: "))
    percent = float(interest/(12 * 100))
    principal = round(payment / ((percent * ((1 + percent) ** month)) / (((1 + percent) ** month) - 1)))
    print(f"Your loan principal = {principal}!")
