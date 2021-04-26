import random

user_word = input("Enter a word which contains 10 characters : ")
letter_num = 10

    counter = 0
    constructed = ""
    if letter_num == len(user_word):
        
        for letter in user_word:
            constructed += letter
            print(constructed)
            counter +=1

            if counter == 10:
                rand_word = list(user_word)
                # [char for char in rand_word]
                random.shuffle(rand_word)
                shuffled = ''.join(rand_word)
                print(shuffled)

    elif letter_num > len(user_word):
        print('too many letters')
    else:
        print("not enough letters")
