
import time
import network
import esp
import gc
# from machine import Pin

esp.osdebug(None)

gc.collect()

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
    pass

print('Connection successful')
print(ap.ifconfig())
# led = Pin(2, Pin.OUT)
#
# for i in range(10):
#     led.on()
#     time.sleep(0.5)
#     led.off()
#     time.sleep(0.5)