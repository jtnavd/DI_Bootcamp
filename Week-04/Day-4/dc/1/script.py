matrix = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    '^r!',
]
ordered_sentence = ''
for i in range(0,len(matrix[0])):
    for string_list in matrix:
        ordered_sentence += string_list[i]
print(ordered_sentence)
cleaned = ''
for index, char in enumerate(ordered_sentence):
    # print(index, char)
    if char.isalpha():
        cleaned += char
        print(cleaned)
    else:
        if not ordered_sentence[index-1].isalpha():
            # print(ordered_sentence[index-1:index+1])
            cleaned += ' '
            print(cleaned)
print(cleaned)
cleaned = ' '.join(cleaned.split())
print(cleaned)