def repeat_me(func):

    def wrapper(*args, count=1):
        count_while = 0
        while count_while != int(abs(count)):
            result = func(*args)
            count_while += 1
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def repeat_me_2(count=2):

    def decorator(func):

        def wrapper(*args):
            while_count = 0
            while while_count != int(abs(count)):
                result = func(*args)
                while_count += 1
            return result
        return wrapper

    return decorator


@repeat_me_2(count=3)
def example_2(text):
    print(text)


example_2('print me 2')
