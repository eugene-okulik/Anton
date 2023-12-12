from copy import deepcopy


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
words_copy = deepcopy(words)
for word in words_copy:
    counter = words_copy[word]
    word_print = ''
    while counter != 0:
        word_print += word
        counter -= 1
    print(word_print)
