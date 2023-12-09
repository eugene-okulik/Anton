range_numbers = list(range(1, 101))
for range_number in range_numbers:
    if (range_number % 3) == 0 and (range_number % 5) == 0:
        print('FuzzBuzz')
    elif (range_number % 3) == 0:
        print('fuzz')
    elif (range_number % 5) == 0:
        print('buzz')
    else:
        print(range_number)
