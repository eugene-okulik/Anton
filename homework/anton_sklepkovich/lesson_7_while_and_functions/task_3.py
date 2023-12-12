result_work_1 = 'результат операции: 42'
result_work_2 = 'результат операции: 54'
result_work_3 = 'результат работы программы: 209'
result_work_4 = 'результат: 2'
plus_number = 10


def call(numb: int):
    print(numb + plus_number)


def get_number(primer: str):
    return int(primer[primer.index(':') + 1:])


number = get_number(result_work_1)
call(number)
number = get_number(result_work_2)
call(number)
number = get_number(result_work_3)
call(number)
number = get_number(result_work_4)
call(number)
