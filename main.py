import machine, time, math, network, vysilac

# zablikani LED na desce, uspesny boot
led = machine.PWM(machine.Pin(2), freq=1000)

for i in range(10):
    for i in range(20):
        led.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(20)

# spusteni vysilace
vysilac.run()