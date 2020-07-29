'''
vysilac.py - pomocí vývojové desky ESP8266 převede zadaný text do morseovy abecedy a pomocí
LED diody na kontaktu D1 je odvysílá jako světelné signály
'''
import machine, time

from morseCode import toMorse

def zablikej_morseovkou(zprava):
    '''
    prelozi řetězec do světelných signálu
    :param telegram: řetězec
    :return: vyšle zadaný řetězec morseovkou skrz kontakt D1 na vývojové desce ESP8266
    '''
    # preklad do morseovky
    morseovka = toMorse(zprava)

    # preklad do blikani (interni je 2)
    pin = machine.Pin(2, machine.Pin.OUT)

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
        # interni dioda sviti pri OFF
        pin.off()
        # pin.on()
        time.sleep(znakyNaCas[znak])
        pin.on()
        # pin.off()
        time.sleep(0.2)


