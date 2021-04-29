import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
hidden_word =list('*' * wordslist)
tries = 0
guessed_letters = []

while tries < 6 :

    print(''.join(hidden_word))-
    user_input = input('')
        if user_input in word:
            print("correct")
            for index, letter in enumerate(word):
                if letter == user_input:
                    hidden_word[index] = letter

        else:
            print('wrong !')
            tries += 1
        print(''.join(hidden_word))
        guessed_letters.append(user_input)
        print('you guessed the word is ', word)


def hangman_gui():
    body_parts = ['O','/|','\\','\']

        

print(hidden_word)
