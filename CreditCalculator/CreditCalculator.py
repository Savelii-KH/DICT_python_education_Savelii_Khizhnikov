import math
import argparse

pars = argparse.ArgumentParser()
pars.add_argument("--principal", type=int)
pars.add_argument("--payment", type=int)
pars.add_argument("--interest", type=int)
pars.add_argument("--periods", type=int)
pars.add_argument("--annuity", type=float)
pars.add_argument("--type", type=str)
args = pars.parse_args()


def n(principal, payment, interest):
    percent = float(interest/(12 * 100))
    month = math.ceil(math.log(payment/(payment - percent * principal), 1 + percent))
    years = round(month/12)
    months = month - years * 12
    print(f"It will take {years} years and {months} months to repay this loan!")
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    if months == 0:
        print(f"It will take {years} years to repay this loan!")


def a(principal, periods, interest):
    percent = float(interest/(12 * 100))
    payment = math.ceil(principal * ((percent * ((1 + percent) ** periods)) / (((1 + percent) ** periods) - 1)))
    print(f"Your monthly payment = {payment}!")


def p(payment, periods, interest):
    percent = float(interest/(12 * 100))
    principal = round(payment / ((percent * ((1 + percent) ** periods)) / (((1 + percent) ** periods) - 1)))
    print(f"Your loan principal = {principal}!")


def d(principal, periods, interest):
    percent = float(interest/(12 * 100))
    steps = list(reversed(range(2, periods + 2)))
    month = 0
    result = 0
    for months in steps:
        months -= 1
        diff = math.ceil(principal / periods) + percent * ((principal * months) / periods)
        result += diff
        month += 1
        print(f"Month {month}: payment is {math.ceil(diff)}")


try:
    if args.type == "annuity":
        if args.payment is not None and args.principal is not None:
            if args.principal > 0 and args.paymen > 0 and args.interest > 0:
                n(args.principal, args.payment, args.interest)
            else:
                print("Incorrect parameters!")
        if args.principal is not None and args.periods is not None:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                a(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters!")
        if args.payment is not None:
            if args.payment > 0 and args.periods > 0 and args.interest > 0:
                p(args.payment, args.periods, float(args.interest))
            else:
                print("Incorrect parameters!")
    if args.type == "diff":
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            d(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters!")
    else:
        print("Incorrect parameters!")
except TypeError:
    print("Incorrect parameters!")
