import uasyncio as asyncio

import socket

import ujson

from machine import Pin

server = '10.239.13.43'
port = 8023

async def sleep_5sec(state):
    while True:
        print('sleep 5 seconds - {}'.format(str(state)))
        await asyncio.sleep(5)

async def toggle_led(state):
    led = Pin(2, Pin.OUT)

    while True:
        led.value(not led.value())
        await asyncio.sleep(state.led_sleep)

async def poll_socket(state):
    while True:
        print("top of the loop")
        sock = socket.socket()

        def close():
            sock.close()
            print('Server disconnect.')

        try:
            serv = socket.getaddrinfo(server, port)[0][-1]
            sock.connect(serv)
        except OSError as e:
            print('Cannot connect to {} on port {}'.format(server, port))
            sock.close()
            await asyncio.sleep(2)
            continue

        sreader = asyncio.StreamReader(sock)
        swriter = asyncio.StreamWriter(sock, {})
        data = {'status':'ok'}
        res = ""
        while True:
            try:
                await swriter.awrite('{}\n'.format(ujson.dumps(data)))
                res = await sreader.readline()
            except OSError:
                print("OSError")
                close()
                break
            try:
                body = ujson.loads(res)

                print('Received', body)

                if 'led_sleep' in body:
                    state.led_sleep = body['led_sleep']

            except ValueError:
                close()
                break

            await asyncio.sleep(0.5)

if __name__ == '__main__':
    state = type('test', (), {})()  # https://stackoverflow.com/questions/19476816/creating-an-empty-object-in-python/19476841#19476841
    state.led_sleep = 1

    loop = asyncio.get_event_loop()
    loop.create_task(sleep_5sec(state))  # schedule asap
    loop.create_task(toggle_led(state))
    loop.create_task(poll_socket(state))
    loop.run_forever()
