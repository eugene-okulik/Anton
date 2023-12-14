from random import randint, choice


def salary_bonus(salary_for_bonus):
    return salary_for_bonus + randint(int(salary_for_bonus * 5 / 100), int(salary_for_bonus * 20 / 100))


def print_salary_with_bonus(salary, bonus, salary_plus_bonus):
    if bonus:
        print(f"{salary}, {bonus} - '${salary_plus_bonus}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")


def enter_salary():
    return int(input('Enter your salary in USD \n' 'Only the numbers, without currency: '))


def random_bonus():
    return bool(choice([True, False]))
