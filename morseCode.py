'''
morseCode.py simulates a telegram machine, i.e. translates a string no longer than 80 char into morse code
'''

import json

with open('morseCode.json', 'r') as file:
    morseDict = json.load(file)

with open('diacritics.json', 'r') as file:
    diacriticsDict = json.load(file)

def toMorse(message):  # translates given string from text to morse code returned as a string
    # split message into list of separate words
    words = message.split()
    morseLetters = list()

    for word in words:
        for index, letter in enumerate(word):
            # remove diacritics
            if letter in diacriticsDict:
                letter = diacriticsDict[letter]
            morseLetters.append(morseDict[letter.lower()])
    telegram = '/'.join(morseLetters)
    return telegram

def fromMorse(message): # translates given string from morse code to text
    morseLetters = message.split('/')
    alphaLetters = list()
    for letter in morseLetters:
        for key, value in morseDict.items():
            if letter == value:
                letter = key
                alphaLetters.append(letter)
    telegram = ''.join(alphaLetters)
    return telegram

if __name__ == '__main__':
    message = input('Vložte větu, kterou chcete převést z/do morseova kódu: ')
    if message[:3].isalpha():
        while (len(message) - message.count(' ')) > 80: # telegram neposila mezery
            message = input('Zadaný text ja na telegram moc dlouhý. Maximální délka telegramu je 80 znaků bez mezer')
        print(toMorse(message))

    if message[0] in ['*', '-']:
        if len(message) > 80:
            print(fromMorse(message))

