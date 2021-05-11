# import json
# # import list_word
import random

words = open('list_word.txt', 'r')
length = input(int('how many words do you want in your sentence?'))

def get_words_from_file():
    data = words.read()
    coll = []
    for i in words:
        coll.append(i)
        return coll

def get_random_sentence(lenght):
    length = input(int('how many words do you want in your sentence?'))