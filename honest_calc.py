import ast

msg_0 = 'Enter an equation'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = 'Yes ... an interesting math operation. You\'ve slept through all ' \
        'classes, haven\'t you?'
msg_3 = 'Yeah... division by zero. Smart move...'
msg_4 = 'Do you want to store the result? (y / n):'
msg_5 = 'Do you want to continue calculations? (y / n):'
msg_6 = ' ... lazy'
msg_7 = ' ... very lazy'
msg_8 = ' ... very, very lazy'
msg_9 = 'You are'
valid_operations = {'+', '-', '*', '/'}
memory = 0
play_again = False
skip_check = False


def check(v1, v2, v3):
    global msg_6
    global msg_7
    global msg_8
    global msg_9

    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if v1 == 1 or v2 == 1 and v3 == '*':
        msg = msg + msg_7
    if v1 == 0 or v2 == 0 and v3 == '*' or v3 == '-':
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    return -10 < v < 10 and type(v) == int


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    try:
        if type(x) == str:
            x = ast.literal_eval(x)
        if type(y) == str:
            y = ast.literal_eval(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in valid_operations:
        print(msg_2)
        continue

    check(x, y, oper)

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print(msg_3)
            continue

    print(float(result))

    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
            memory = result
            break
        elif answer == 'n':
            break
        else:
            continue

    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            play_again = True
            break
        elif answer == 'n':
            play_again = False
            break
        else:
            continue

    if play_again:
        continue
    else:
        break
