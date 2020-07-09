'''
vysilac.py - pomocí vývojové desky ESP8266 převede zadaný text do morseovy abecedy a pomocí
LED diody na kontaktu D1 je odvysílá jako světelné signály
'''
import machine, time

from morseCode import toMorse

def preloz_signal(telegram):
    '''
    prelozi řetězec do světelných signálu
    :param telegram: řetězec
    :return: vyšle zadaný řetězec morseovkou skrz kontakt D1 na vývojové desce ESP8266
    '''
    # preklad do morseovky
    morseovka = toMorse(telegram)

    # preklad do blikani
    pin = machine.Pin(5, machine.Pin.OUT)

    # nastavení trvání tečky(*), čárky(-), a mezery mezi slovama(/)
    znakyNaCas = {
        '*': 0.2,
        '-': 0.5,
        '/': 1
    }

    # prevede jednotlivé znaky světelných signálů
    for znak in morseovka:
        # print(znak)
        if znak == '/':
            time.sleep(znakyNaCas[znak])
            continue
        pin.on()
        time.sleep(znakyNaCas[znak])
        pin.off()
        time.sleep(0.2)

while True:
    preloz_signal(input())

