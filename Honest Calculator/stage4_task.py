# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

memory = 0


def is_one_digit(v):
    if -10 < float(v) < 10 and float(v).is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    v1 = float(v1)
    v2 = float(v2)
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == 'M':
        x = memory
    else:
        if y == 'M':
            y = memory

    try:
        x = float(x)
        y = float(y)
    except Exception:
        print(msg_1)
        continue

    if oper not in ('*', '/', '+', '-'):
        print(msg_2)
    else:
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue

    print(result)
    ###
    while True:
        print(msg_4)
        answer = input()

        if answer == 'y':
            memory = result
        elif answer == 'n':
            pass
        else:
            continue
        break

    print(msg_5)
    answer = input()

    if answer == 'y':
        continue
    elif answer == 'n':
        break
