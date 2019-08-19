import _thread
import machine
import time

sleep = 5

def thread_blinky():
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(not led.value())
        time.sleep(sleep)

def thread_server():
    global sleep
    while True:
        sleep = sleep * 0.75
        time.sleep(1)

def main():
    _thread.start_new_thread(thread_server, ())
    _thread.start_new_thread(thread_blinky, ())

main()
