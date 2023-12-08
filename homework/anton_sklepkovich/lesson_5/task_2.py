string_result = """результат операции: 42

результат операции: 514

результат работы программы: 9
"""
list_result = string_result.split('\n')
while '' in list_result:
    list_result.remove('')
count_result = len(list_result)
count = 0
while count_result != 0:
    result_answer = list_result[count].index(':')
    result_answer += 2
    result_answer = int(list_result[count][result_answer:])
    result_answer += 10
    print(result_answer)
    count_result -= 1
    count += 1
