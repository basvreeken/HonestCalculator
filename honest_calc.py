import ast

msg_0 = 'Enter an equation'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = 'Yes ... an interesting math operation. You\'ve slept through all ' \
        'classes, haven\'t you?'
msg_3 = 'Yeah... division by zero. Smart move...'
valid_operations = {'+', '-', '*', '/'}

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

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
    break

print(float(result))
