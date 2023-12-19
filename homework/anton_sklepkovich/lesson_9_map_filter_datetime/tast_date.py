import datetime


task_time = 'Jan 15, 2023 - 12:05:33'
new_task_time = datetime.datetime.strptime(task_time, '%b %d, %Y - %H:%M:%S')
print(datetime.datetime.strftime(new_task_time, '%B'))
print(datetime.datetime.strftime(new_task_time, '%d.%m.%Y, %H:%M'))
