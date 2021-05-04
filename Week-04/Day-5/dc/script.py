while True:
    pr = input('Enter word seoarated with spaces : ')
    if pr == "" :
            print('Goodbye')

    list_word = pr.split(',')
    print('\n' + ','.join(list_word))
    list_word.sort()
    print(','.join(list_word) + '\n')