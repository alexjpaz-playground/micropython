import env

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(env.wifi_ssid, env.wifi_password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()

import upip

upip.install("micropython-uasyncio")
upip.install('micropython-uasyncio.synchro')
upip.install('micropython-uasyncio.queues')
