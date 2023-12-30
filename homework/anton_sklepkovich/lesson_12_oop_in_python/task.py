class Flowers:

    def __init__(self, freshness, color, stem_length, price, life_time):
        self.__freshness = freshness
        self.__color = color
        self.__stem_length = stem_length
        self.__price = price
        self.__life_time = life_time

    def name_day(self):
        day_tuple = (2, 3, 4)
        return 'дня' if int(self.life_time) in day_tuple else 'дней'

    def info_flower(self, name, info):
        return (
            f'{name} options:\n'
            f'Fresh: {self.freshness}\n'
            f'Color: {self.color}\n'
            f'Stem_length: {self.stem_length} см.\n'
            f'Price: {self.price} рублей\n'
            f'Life time: {self.life_time} {self.name_day()}\n'
            f'{info}'
        )

    @property
    def freshness(self):
        return self.__freshness

    @property
    def color(self):
        return self.__color

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def price(self):
        return self.__price

    @property
    def life_time(self):
        return self.__life_time


class Peonies(Flowers):

    def __init__(self, freshness, color, stem_length, price, life_time, leaves: bool):
        super().__init__(freshness, color, stem_length, price, life_time)
        self.__leaves = leaves

    @property
    def leaves(self):
        return self.__leaves

    def __repr__(self):
        leaves = '' if self.leaves else 'no '
        return self.info_flower('Peony', leaves)


class Roses(Flowers):

    def __init__(self, freshness, color, stem_length, price, life_time, number_of_buds=1):
        super().__init__(freshness, color, stem_length, price, life_time)
        self.__number_of_buds = number_of_buds

    @property
    def number_of_buds(self):
        return self.__number_of_buds

    def __repr__(self):
        info = f'Number of buds: {self.number_of_buds}\n'
        return self.info_flower('Rose', info)


class Bouquet:

    def __init__(self, *args):
        self.flowers_list = list(args)

    def expire_bouquet(self):
        life_time_list = list(map(lambda x: int(x.life_time), self.flowers_list))
        return f'Avg expire bouquet: {int(sum(life_time_list) / len(self.flowers_list))}'

    def sort_flowers(self, arg):
        sort_info = sorted(self.flowers_list, key=lambda flower: getattr(flower, arg))
        return (
            f'Sorted list of flowers in a bouquet in ascending order of {arg}:\n'
            f'{sort_info}'
        )

    def search_flower(self, arg, value):
        find = list(filter(lambda flower: value == getattr(flower, arg), self.flowers_list))
        return (
            f'The following flowers were found by value {arg}\n'
            f'{find}'
        )

    def search_avg_time_life(self):
        avg = self.expire_bouquet().split(': ')[1]
        return (
            f'The following flowers were found by avg value {avg}\n '
            f'{list(filter(lambda flower: int(avg) == int(flower.life_time), self.flowers_list))}'
        )


piony = Peonies('Свежий', 'Синий', '14', '100', '0', True)
rose = Roses('Нужно освежить', 'Красный', '10', '100', '6', 3)
rose_yellow = Roses('Простоит один день', 'Желтый', '11', '130', '3')

bouquet = Bouquet(piony, rose, rose_yellow)
print(bouquet.expire_bouquet())
print(bouquet.sort_flowers('freshness'))
print(bouquet.sort_flowers('color'))
print(bouquet.sort_flowers('stem_length'))
print(bouquet.sort_flowers('price'))
print(bouquet.search_flower('freshness', 'Свежий'))
print(bouquet.search_flower('price', '100'))
print(bouquet.search_flower('life_time', '3'))
print(bouquet.search_avg_time_life())
