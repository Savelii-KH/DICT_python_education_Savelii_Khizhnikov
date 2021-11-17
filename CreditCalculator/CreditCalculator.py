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
    month = int(input("Enter the monthly payment: "))
    print(f"It will take {round(principal/month)} to repay the loan ")
if choice == "p":
    payment = int(input("Enter the number of months: "))
    print(f"Your month payment = {round(principal/payment)}")
pp = float(input())
print(round(pp))