def change_calc(func):

    def wrapper(*args):
        if args[0] < 0 or args[1] < 0:
            operator, name = '*', 'Multiplication'
        elif args[0] > args[1]:
            operator, name = '-', 'Subtraction'
        elif args[0] < args[1]:
            operator, name = '/', 'Division'
        elif args[0] == args[1]:
            operator, name = '+', 'Addition'
        print(f'It happened {name}')
        return func(*args, operator)
    return wrapper


def enter_number(number_text):
    success_input = False
    while not success_input:
        try:
            result = float(input(f'Enter {number_text} number: '))
        except ValueError:
            print('Invalid data, please try again')
        else:
            success_input = True
    return result


@change_calc
def calc(first_n, second_n, operator):
    if operator == '+':
        return first_n + second_n
    elif operator == '-':
        return first_n - second_n
    elif operator == '/':
        return first_n / second_n
    elif operator == '*':
        return first_n * second_n


first_n = enter_number('first')
second_n = enter_number('second')


print(calc(first_n, second_n))
