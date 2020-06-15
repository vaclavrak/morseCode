#! python
'''
morseCode.py simulates a telegram machine, i.e. translates a string no longer than 80 char into morse code
'''

import json

with open('morseCode.json', 'r') as file:
    morseDict = json.load(file)

with open('diacritics.json', 'r') as file:
    diacriticsDict = json.load(file)

telegram = list() # empty list to insert morse code in
message = input('Vložte větu, kterou chcete převést do morseova kódu: ')
while len(message) > 80:
    message = input('Zadaný text ja na telegram moc dlouhý. Maximální délka telegramu je 80 znaků')

# split message into list of separate words
words = message.split()

for word in words:
    morseWord = list()
    for index, letter in enumerate(word):
        if letter in diacriticsDict:  # remove diacritics
            letter = diacriticsDict[letter]
        morseWord.append(morseDict[letter.lower()])
    telegram.append(morseWord)

for word in telegram:
    for letter in word:
        print(letter, end='/')
