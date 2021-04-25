user_word = input("Enter a word which contains 10 characters : ")
letter_num = 10

def triangle_name(user_word):
    num=len(user_word)

    for row in range(0,letter_num):
        for col in range (row+1):
            print (user_word[col])

if len(user_word)>letter_num:
    print ("string too long")

elif len(user_word)<letter_num:
    print ("string not long enough")

else: triangle_name()


# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example: