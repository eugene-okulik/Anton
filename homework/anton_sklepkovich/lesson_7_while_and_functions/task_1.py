from random import randint


guess_the_number_min = 0
guess_the_number_max = 9
guess_the_number = randint(guess_the_number_min, guess_the_number_max)
check_number = False
counter_fails = 0
while not check_number:
    try:
        enter_number = int(input('Please enter a number to guess а random number: \n'))
    except ValueError:
        print('Invalid data format,')
    else:
        if enter_number == guess_the_number:
            check_number = True
            print('Congratulations! You guessed!')
            break
        else:
            counter_fails += 1
            print('Sorry, try one more \n')
            if counter_fails == 3:
                print(f'А hint for you. The number between {guess_the_number_min} and {guess_the_number_max} ')
