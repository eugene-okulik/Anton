# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
from math import sqrt


x = 2
y = 1
average = (x + y) / 2
geometric = sqrt(x * y)
print(f'Среднее арифметическое x и y = {average}')
print(f'Cреднее геометрическое x и y = {round(geometric, 2)}')


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
#         average = (x + y) / 2
#         geometric = sqrt(x * y)
#         print(f'Среднее арифметическое x и y = {average}')
#         print(f'Cреднее геометрическое x и y = {round(geometric, 2)}')
