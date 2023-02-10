import network
import socket
import gerent
import time
import machine


ssid = ''
password = ''

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
print(station.ifconfig())

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

# Define gerent route:


@gerent.route("/hello")
def api(request):
    return (200, {}, "Hello from ESP8266!")


led = machine.Pin(2, machine.Pin.OUT)
led.on()

# Listen for connections
while True:
    gerent.listen(s)
    for i in range(5):
        led.off()
        time.sleep(0.05)
        led.on()
        time.sleep(0.05)
