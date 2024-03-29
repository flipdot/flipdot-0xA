#!/usr/bin/env python3
import asyncio
import telnetlib3

TELNET_PORT = 6023

@asyncio.coroutine
def shell(reader, writer):
    writer.write('\r\nWould you like to play a game? ')
    inp = yield from reader.read(1)
    if inp:
        writer.echo(inp)
        writer.write('\r\nThey say the only way to win '
                     'is to not play at all.\r\n')
        yield from writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=TELNET_PORT, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())
