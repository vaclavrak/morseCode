import machine
import time
import math
import network
from vysilac  import zablikej_morseovkou

try:
    import usocket as socket
except:
    import socket
# zablikani LED na desce, uspesny boot
# led = machine.PWM(machine.Pin(2), freq=1000)

def web_page(zprava = ""):
    html = """<html>
    <head> 
        <title>ESP Web Server</title> 
        <link rel="icon" href="data:,">
    </head>
    <body>
        <form action="zprava" method="post">
            <h1>Morseovka</h1>
            <b>Vlozte text</b>: <input type="text" name="text" value='""" + zprava + """' />
            <br/>
            <input type="submit" value="Send" />
        </form>
    </body>
    </html>"""


    return html

if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    conn, addr = s.accept()

    response = web_page("")
    conn.send(response)
    while True:
        print('Got a connection from %s' % str(addr))
        while True:
            zprava = ""
            request = conn.recv(8000)
            for ln in request.decode("ascii").split("\n"):
                print(ln)
            if request == b"":
                print("prazdny radek, koncim")
                break
            for ln in request.decode("ascii").split("\n"):
                print(ln)
                if ln[:len('text=')] == "text=":
                    zprava = ln[len("text="):]
                    print("Mame zpravu!!! jdeme blikat!!!", zprava)
                    zablikej_morseovkou(zprava)
                    print("Dolikano jest")
        response = web_page(zprava)
        conn.send(response)
        conn.close()


