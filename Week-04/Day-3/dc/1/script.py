text = input("encrypted message : ")

def cipher(text,s):
    result = ''

    for i in range(len(text)):
        char = text[i]

        if text.str.lower():
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s-97) % 26 + 97)

        return result

s = 3

print ("original text : " + text)
print ("=============================")
print ("shifted text : " + cipher(text,s))




#     In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, the user entries the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.