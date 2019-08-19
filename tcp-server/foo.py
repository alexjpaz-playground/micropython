import socket
import machine
import network
import time

led = machine.Pin(2, machine.Pin.OUT)

sta_if = network.WLAN(network.STA_IF)

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('WIFI', 'WIRELESS')
    while not sta_if.isconnected():
        pass

print('network config:', sta_if.ifconfig())

led.on()

addr_info = socket.getaddrinfo("10.239.13.43", 8023)
addr = addr_info[0][-1]

s = socket.socket()
s.connect(addr)

led.on()

while True:
    data = s.recv(1)
    print(str(data, 'utf8'), end='')

