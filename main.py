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
        hlavicky = ""
        telo = ""
        while True:
            odpoved = conn.recv(1024)
            hlavicky += odpoved.decode("ascii")
            if odpoved == b"" or len(odpoved) < 1024:
                break

        while True:
            odpoved = conn.recv(1024)
            telo += odpoved.decode("ascii")
            if odpoved == b"" or len(odpoved) < 1024:
                break

        for ln in hlavicky.split("\n"):
            print(ln)

        for ln in telo.split("\n"):
            print(ln)
            if ln[:len('text=')] == "text=":
                zprava = ln[len("text="):]
                print("Mame zpravu, jdeme blikat `{zprava}`".format(zprava=zprava))
                zablikej_morseovkou(zprava)
                print("Doblikano jest")

    conn.close()
