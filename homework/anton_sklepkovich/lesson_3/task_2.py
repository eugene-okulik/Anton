# Даны числа x и y. Получить x − y / 1 + xy

x = 2
y = 1
answer = x - y / 1 + x * y
print(f'Ответ = {answer}')


# # Не понял формулировку: "Все начальные данные задаются произвольно. поэтому тут вариант с вводом от пользоваетля"
# try:
#     x = float(input('x= '))
# except ValueError:
#     print('Введен неверный тип данных для x, доступны только числа')
# else:
#     try:
#         y = float(input('y= '))
#     except ValueError:
#         print('Введен неверный тип данных для y, доступны только числа')
#     else:
#         answer = x - y / 1 + x * y
#         print(f'x − y / 1 + xy = {answer}')
