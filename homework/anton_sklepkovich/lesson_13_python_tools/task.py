import os
import datetime

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_task = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(file_task)


def read_file_task():
    with open(file_task, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file_task():
    date_list = data_line.split()
    date = (datetime.datetime.strptime(f'{date_list[1]} {date_list[2]}', '%Y-%m-%d %H:%M:%S.%f'))
    if data_line.startswith('1.'):
        date = date - datetime.timedelta(weeks=1)
    elif data_line.startswith('2.'):
        date = datetime.datetime.strftime(date, '%A')
    elif data_line.startswith('3.'):
        date_now = datetime.datetime.now()
        date = (date_now - date).days
    print(date)
