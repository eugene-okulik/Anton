def finish(func):

    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result
    return wrapper


@finish
def fatality(text):
    print(text)


fatality('Fatality')
