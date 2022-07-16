import asyncio
import socket
from websockets import connect

#pip install websockets

async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.run(hello("ws://localhost:8765"))