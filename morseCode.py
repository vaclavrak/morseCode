#! python
'''
morseCode.py simulates a telegram machine, i.e. translates a string no longer than 80 char into morse code
'''

import json

with open('morseCode.json', 'r') as file:
    morseDict = json.load(file)

with open('diacritics.json', 'r') as file:
    diacriticsDict = json.load(file)

#TODO check that input is not longer than 80 char

request = input('Vložte větu, kterou chcete převést do morseova kódu: ')
letters = list(request)

#remove diacritics
for index, letter in enumerate(letters):
    if letter in diacriticsDict:
        letters[index] = diacriticsDict[letter]

#TODO translate letters to morse code


