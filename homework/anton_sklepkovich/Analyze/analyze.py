import argparse
import os
import re
import datetime
from colorama import Fore, Style, init
init()


# Display found logs to the user
def print_logs(l_logs, full):
    print('For the given arguments it was found:')
    for elm in l_logs:
        time_key = list(elm.keys())[0]
        time_str = datetime.datetime.strftime(time_key, '%Y-%m-%d %H:%M:%S.%f')
        if full:
            print(Fore.LIGHTYELLOW_EX + f'{time_str[:-3]} ' + Style.RESET_ALL + f'{elm[time_key]}')
        elif args_test.text:
            print(
                Fore.LIGHTYELLOW_EX + f'{time_str[:-3]} ' + Style.RESET_ALL
                + f'{elm[time_key][:300].replace(args_test.text, Fore.GREEN + args_test.text + Style.RESET_ALL)}'
            )
        elif args_test.text and full:
            print(
                Fore.LIGHTYELLOW_EX + f'{time_str[:-3]} ' + Style.RESET_ALL
                + f'{elm[time_key].replace(args_test.text, Fore.GREEN + args_test.text + Style.RESET_ALL)}'
            )
        else:
            print(Fore.LIGHTYELLOW_EX + f'{time_str[:-3]} ' + Style.RESET_ALL + f'{elm[time_key][:300]}')
    print(Fore.YELLOW + 'Total log counts = ' + Style.RESET_ALL + Fore.CYAN + f'{len(logs_test)}' + Style.RESET_ALL)
    print(Fore.YELLOW + 'Total result counts = ' + Style.RESET_ALL + Fore.CYAN + f'{len(l_logs)}' + Style.RESET_ALL)


# Reading a file line by line
def read_file(file):
    with open(file, 'r') as data_file:
        for line in data_file:
            yield line


# Create a list from a file in which the key is the date and the value is everything else up to the next date
def list_logs(logs_str):
    time_and_data = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3})', logs_str)
    if time_and_data:
        time = time_and_data.group(1)
        return {datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f'): logs_str[time_and_data.end():].strip()}
    return None


def process_log_file(file, list_log):
    for line in read_file(file):
        log_entry = list_logs(line)
        if log_entry:
            list_log.append(log_entry)


# File or file folder definition, returns a list with all log entries
def file_or_files(file):
    list_log = []

    if os.path.isfile(file):
        print('One file will be read')
        process_log_file(file, list_log)
    elif os.path.isdir(file):
        print('All files with the .log extension will be read')
        for filename in os.listdir(file):
            if filename.endswith('.log'):
                file_path = os.path.join(file, filename)
                process_log_file(file_path, list_log)
    else:
        print('You have entered an unknown path or a non-existent file name')

    return list_log


# Search by date and condition in the list of logs
def search_date_in_logs(time, l_logs, condition):
    find_logs = []
    for elm in l_logs:
        key = list(elm.keys())[0]
        if condition(time, key):
            find_logs.append({key: elm[key]})
    return find_logs


def parse_datetime(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')


def find_time(time, l_logs):
    if '../' in time:
        time = parse_datetime(time[3:])
        l_find_time = search_date_in_logs(time, l_logs, lambda t, k: t > k)
    elif '/..' in time:
        time = parse_datetime(time[:-3])
        l_find_time = search_date_in_logs(time, l_logs, lambda t, k: t < k)
    else:
        time, time1 = time.split('/')
        time = parse_datetime(time)
        time1 = parse_datetime(time1)
        l_find_time = search_date_in_logs(time, l_logs, lambda t, k: t <= k <= time1)
    return l_find_time


# Search by text in the log list
def find_text(text, l_logs):
    l_find_text = []
    print(text)
    for elm in l_logs:
        key = list(elm.keys())[0]
        if text in elm[key]:
            l_find_text.append({key: elm[key]})
    return l_find_text


def exclusion_unwanted(unwanted, l_logs):
    text = [string.strip() for string in unwanted.split(',')]
    l_find_text = []
    for elm in l_logs:
        key = list(elm.keys())[0]
        if not any(element in elm[key] for element in text):
            l_find_text.append({key: elm[key]})
    return l_find_text


def parse_logs():
    parser = argparse.ArgumentParser(
        description='Find logs according to the given options. By default it print the first 300 simbols'
    )
    parser.add_argument(
        'file',
        help='File name or directory. '
             'If the file or folder is in the same directory as the script, just specify the file name, '
             'if there are several files in the current directory, specify ./.'
             'If the file is located elsewhere, specify the absolute path to the file'
    )
    parser.add_argument(
        '-d',
        '--date',
        help='Date for search. less than: "../2024-01-17 00:00:00.000", more than: "2024-01-18 00:00:00.000/..",'
             'from - to "2024-01-17 00:00:00.000/2024-01-18 00:00:00.000", exact: "2024-01-15 00:00:00.000"'
    )
    parser.add_argument(
        '-t',
        '--text',
        help='Text for search. Can be a string(e.g. "out of memory"). There will be an exact match search'
    )
    parser.add_argument(
        '-n',
        '--unwanted',
        help='A text to filter out logs. Logs with this text will be excluded from the results. '
             'Can be a string or a list divided by commas (e.g. "out of memory, info")'
    )
    parser.add_argument('--full', help='Return full log entry instead of default symbols', action='store_true')
    return parser.parse_args()


def chose(args, logs):
    if args.date and args.text and args.unwanted:
        print_logs(exclusion_unwanted(args.unwanted, find_text(args.text, find_time(args.date, logs))), args.full)
    elif args.date and args.text:
        print_logs(find_text(args.text, find_time(args.date, logs)), args.full)
    elif args.date and args.unwanted:
        print_logs(exclusion_unwanted(args.unwanted, find_time(args.date, logs)), args.full)
    elif args.text and args.unwanted:
        print_logs(exclusion_unwanted(args.unwanted, find_text(args.text, logs)), args.full)
    elif args.date:
        print_logs(find_time(args.date, logs), args.full)
    elif args.text:
        print_logs(find_text(args.text, logs), args.full)
    elif args.unwanted:
        print_logs(exclusion_unwanted(args.unwanted, logs), args.full)


args_test = parse_logs()
logs_test = file_or_files(args_test.file)
chose(args_test, logs_test)
