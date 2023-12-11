example_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
                'facilisis vitae se mper at, dignissim vitae libero')
text_list = example_text.split()
new_text = []
for text in text_list:
    if ',' in text:
        new_text.append(text.replace(',', 'ing,'))
    elif '.' in text:
        new_text.append(text.replace('.', 'ing.'))
    else:
        new_text.append(text + 'ing')
new_text = ' '.join(new_text)
print(new_text)
