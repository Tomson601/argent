# Find out about hardware:
# import os

# if os.uname().machine == "Raspberry Pi Pico W with RP2040":
#     print("RP2")

import network
import socket
import time
import argent

ssid = '2.4GHz wifi'
password = 'secret_password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)


@argent.route("/hello/world")
def hello_world_url(request):
    return(200, {}, "Hello world!")

# Listen for connections
while True:
    argent.listen(s)

