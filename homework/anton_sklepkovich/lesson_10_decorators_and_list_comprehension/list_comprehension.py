PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = [line.split() for line in PRICE_LIST.split('\n') if line]
price_dict = {key: int(value[:-1]) for key, value in price_list}
print(price_dict)
