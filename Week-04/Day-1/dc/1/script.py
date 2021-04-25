import random

user_word = input("Enter a word which contains 10 characters : ")
letter_num = 10

def triangle_name(user_word):
    counter = 0
    constructed = ""
    if letter_num == len(user_word):
        
        for letter in user_word:
            constructed += letters
            print(constructed)
            counter +=1

            if counter == 10:
                rand_word = list(user_word)
                # [char for char in rand_word]
                random.shuffle(rand_word)
                shuffled = ''.join(rand_word)
                print(shuffled)
    else:
        print("not enough letters")