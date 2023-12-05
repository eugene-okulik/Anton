empty = ''  # переменная для добавлениия в словарь my_dict
my_dict = {
    'tuple': ('tuple1', True, 123, empty, None),
    'list': ['list1', False, 321, empty, None],
    'dict': {
        'dict1': '1',
        'dict2': '2',
        'dict3': empty,
        'dict4': '4',
        'dict5': None
    },
    'set': {'set1', False, 1, empty, None}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('list6')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'test'
del my_dict['dict']['dict1']
my_dict['set'].add('python')
my_dict['set'] = list(my_dict['set'])
my_dict['set'].pop(False)
my_dict['set'] = set(my_dict['set'])
print(my_dict)
