import math
import argparse

parser = argparse.ArgumentParser(description="Welcome to the Loan Calculator")
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

if args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
elif args.type == 'diff' and str(args.payment) == 'None':
    print("Incorrect parameters")
elif str(args.interest) == 'None':
    print("Incorrect parameters")
elif int(args.periods or 0) < 0:
    print("Incorrect parameters")
elif 'NoneNone' == str(args.principal) + str(args.payment) or 'NoneNone' == str(args.principal) + str(args.periods) or 'NoneNone' == str(args.payment) + str(args.periods):
    print("Incorrect parameters")

lp = int(args.principal or 0)
mp = int(args.payment or 0)
ap = int(args.payment or 0)
np = int(args.periods or 0)
lt = str(args.type)
li = float(args.interest or 1)

month_amnt = 999999
op = 0

def monthly_payments(lp, mp, li):
    nominal_ir = li/(12*100)
    n_month = math.log(mp / (mp - nominal_ir * lp), 1 + nominal_ir)
    month_amnt = math.ceil(n_month)
    op = -lp + math.ceil(n_month) * mp
    return month_amnt, op

def annuity_mpa(lp, np, li):
    nominal_ir = li/(12*100)
    map = lp * (nominal_ir * (1 + nominal_ir)**np / ((1 + nominal_ir)**np - 1))
    return math.ceil(map)

def loan_principal(ap, np, li):
    nominal_ir = li/(12*100)
    p = ap / (nominal_ir * (1 + nominal_ir)**np / ((1 + nominal_ir)**np - 1))
    return round(p)

def diff_mpa(lp, np, li):
    nominal_ir = li/(12*100)
    op = -lp
    dm = 0
    for i in range(1, np + 1):
        dm = math.ceil(lp / np + nominal_ir * (lp - lp * (i - 1) / np))
        op += dm
        print(f'Month {i}: payment is {dm}')
        i += 1
    print()
    print(f'Overpayment = {op}')

def month_pretty(month_amnt):
    n_years = month_amnt // 12
    n_months = month_amnt % 12
    if n_years == 0 and n_months == 1:
        print(f'It will take {n_months} month to repay this loan!')
    elif n_years == 0 and n_months != 1:
        print(f'It will take {n_months} months to repay this loan!')
    elif n_years == 1 and n_months == 0:
        print(f'It will take {n_years} year to repay this loan!')
    elif n_years != 1 and n_months == 0:
        print(f'It will take {n_years} years to repay this loan!')
    elif n_years != 0 and n_months == 1:
        print(f'It will take {n_years} years and {n_months} month to repay this loan!')
    elif n_years != 0 and n_months != 1:
        print(f'It will take {n_years} years and {n_months} months to repay this loan!')

if args.type == 'annuity' and str(args.periods) == 'None':
    month_amnt = monthly_payments(lp, mp, li)[0]
    op = monthly_payments(lp, mp, li)[1]
    month_pretty(month_amnt)
    print(f'Overpayment = {op}')
elif args.type == 'annuity' and str(args.payment) == 'None':
    mpa = annuity_mpa(lp, np, li)
    print(f'Your monthly payment = {mpa}!')
elif args.type == 'annuity' and str(args.principal) == 'None':
    lp = loan_principal(ap, np, li)
    print(f'Your loan principal = {lp}!')
elif args.type == 'diff':
    diff_mpa(lp, np, li)
