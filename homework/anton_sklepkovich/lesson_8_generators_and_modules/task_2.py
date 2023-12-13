def fibonnaci(limit=1000):
    fib_1, fib_2 = 0, 0.1
    count = 1
    while count < limit:
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


count = 1
for number in fibonnaci(100000):
    if count == 5:
        print(round(number, 2))
    elif count == 1000:
        print(round(number, 2))
    elif count == 100000:
        print(round(number, 2))
        break
    count += 1
