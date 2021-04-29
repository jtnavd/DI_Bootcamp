import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
hidden_word = list('*' * len(word))
tries = 0
guessed_letters = []
def gallows_to_print():
    body_parts = ['0','|','/','\\', '/','\\']
    copy_of_part = []
    for num in range(tries):
        copy_of_part.append(body_parts[num])
    while len(copy_of_part) < 6:
        copy_of_part.append(' ')
    fgallows = f'''
    |--------
    |   {copy_of_part[0]}
    |  {copy_of_part[2]}{copy_of_part[1]}{copy_of_part[3]}
    |  {copy_of_part[4]} {copy_of_part[5]}
    '''
    print(fgallows)
def is_valid_input(text):
    '''verify the input is one letter, only alpha, and not in guessed letters''' 
    if len(text) != 1 or not text.isalpha() or text in guessed_letters:
        return False
    else:
        return True
while tries < 6 :
    if ''.join(hidden_word) == word:
        # check to make sure he hasnt guessed the complete word
        print('you win!')
        break
    user_input = input('Guess a letter')
    while not is_valid_input(user_input):
        print('Input wasnt valid, make sure its one char, alpha, and not guessed')
        user_input = input('Guess a letter')
    if user_input in word:
        print('You guessed correctly!!')
        for index, letter in enumerate(word):
            if letter == user_input:
                # print('replacing letter')
                hidden_word[index] = letter
                # print(hidden_word[index], letter)
    else:
        print('You guessed terribly, you should feel bad')
        tries += 1
    print(''.join(hidden_word))
    guessed_letters.append(user_input)
    print('you\'ve guessed the following letters:', *guessed_letters)
    print(f'Number of incorrect tries: {tries}/6')
    gallows_to_print()
print('You killed him Jim')