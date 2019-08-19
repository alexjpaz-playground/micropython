import machine
import time
import ujson
import sys

def loop():
    print("lol")
    sys.exit(1)

def main():
    ready_led = machine.Pin(2, machine.Pin.OUT)
    ready_led.on()

    try:
        while 1:
            loop()
    except Exception as e:
        print(e)

main()
