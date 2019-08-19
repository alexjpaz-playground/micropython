def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WIFI', 'PASSWORD')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

    led = machine.Pin(15, machine.Pin.OUT)
    led.on()

def main():
    try:
        do_connect()
    except Exception as e:
        print(e)

main()
