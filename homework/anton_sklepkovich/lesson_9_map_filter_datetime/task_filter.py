temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]
new_temperatures_filter = list(filter(lambda temperature: temperature > 28, temperatures))
print(new_temperatures_filter)
print(max(new_temperatures_filter))
print(min(new_temperatures_filter))
print(int(sum(new_temperatures_filter) / len(new_temperatures_filter)))
