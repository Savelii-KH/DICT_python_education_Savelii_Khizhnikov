import math

print("""Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!
""")
principal = int(input("Enter the loan principal: "))
print("""What do you want calculate?
type \"m\" - for number of  monthly payments
type \"p\" - for the monthly payment""")
choice = str(input())
if choice == "m":
    payments = int(input("Enter the monthly payment: "))
    print(f"It will take {round(principal/payments)} to repay the loan ")
if choice == "p":
    month = int(input("Enter the number of months: "))
    payment = math.ceil(principal/month)
    lat_payment = int(principal - (month - 1) * payment)
    if lat_payment == payment:
        print(f"Your month payment = {payment}")
    else:
        print(f"Your month payment = {payment}, and the last payment = {lat_payment}")
