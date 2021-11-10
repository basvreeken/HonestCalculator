import ast

msg_0 = 'Enter an equation'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = 'Yes ... an interesting math operation. You\'ve slept through all ' \
        'classes, haven\'t you?'
msg_3 = 'Yeah... division by zero. Smart move...'
msg_4 = 'Do you want to store the result? (y / n):'
msg_5 = 'Do you want to continue calculations? (y / n):'
valid_operations = {'+', '-', '*', '/'}
memory = float(0)
play_again = False
skip_check = False

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == 'M':
        x = str(memory)
    if y == 'M':
        y = str(memory)

    try:
        x = ast.literal_eval(x)
        y = ast.literal_eval(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in valid_operations:
        print(msg_2)
        continue

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
