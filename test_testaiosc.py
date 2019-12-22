# pip3 install aiosc
# https://pypi.org/project/aiosc/
# https://github.com/artfwo/aiosc

import asyncio
import aiosc


''' sending works
address = "10.0.0.30"
port = 9000

loop = asyncio.get_event_loop()
loop.run_until_complete(aiosc.send((address, port), '/1/fader1', 5))
'''

def print_message(osc):
    aiosc.OSCProtocol({})


# OSC receiving server
def protocol_factory():
    osc = aiosc.OSCProtocol({'//*': lambda addr, path, *args: print(addr, path, args)})
    return osc

loop = asyncio.get_event_loop()
coro = loop.create_datagram_endpoint(protocol_factory, local_addr=('0.0.0.0', 8000))
transport, protocol = loop.run_until_complete(coro)
loop.run_forever()


'''
async def main():
    await asyncio.sleep(1)
    #osc = aiosc.OSCProtocol({'//*': lambda addr, path, *args: print(addr, path, args)})
    print('hello')
asyncio.run(main())
'''