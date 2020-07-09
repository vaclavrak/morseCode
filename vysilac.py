import machine, time

from morseCode import toMorse

def preloz_signal(telegram):
    # preklad do morseovky
    morseovka = toMorse(telegram)

    # preklad do blikani
    pin = machine.Pin(5, machine.Pin.OUT)

    znakyNaCas = {
        '*': 0.2,
        '-': 0.5,
        '/': 1
    }

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

