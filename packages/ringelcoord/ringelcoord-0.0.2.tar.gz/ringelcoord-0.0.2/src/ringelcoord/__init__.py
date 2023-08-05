import websockets
import os
import asyncio

class Client:
    def __init__(self, url):
        self.on_ready_funcs = []
        self.on_message_funcs = []
        self.msg_queue = asyncio.Queue(maxsize=20)
        self.user = ""
        self.url = url

    def run(self, token):
        try:
            asyncio.get_event_loop().run_until_complete(self.__actual_run(token))
        except KeyboardInterrupt:
            print("User cancel")

    def on_ready(self, func):
        self.on_ready_funcs.append(func)

    def on_message(self, func):
        self.on_message_funcs.append(func)

    async def send_msgs(self, sock):
        while True:
            content, context = await self.msg_queue.get()
            if isinstance(context, Message):
                await sock.send(f"CLIENT::NEW_MSG::{context.recipient}::<REPLY:{context.id}> {content}")


    
    async def __actual_run(self, token):
        async with websockets.connect("wss://{self.url}") as socket:
            asyncio.get_event_loop().create_task(self.send_msgs(socket))
            async for x in socket:
                if x.startswith("SERVER::VERSION"):
                    _, _, ver = x.split("::", 2)
                    assert ver == "0.4", "update ringelcoord"
                    await socket.send("CLIENT::VERSION::0.4")
                elif x.startswith("SERVER::REQUEST_LOGIN"):
                    await socket.send(f"CLIENT::LOGIN_INFO::{token}")
                elif x.startswith("SERVER::LOGIN_SUCCESS"):
                    self.user = x.split("::", 2)[2]
                    for func in self.on_ready_funcs:
                        await func()
                elif x.startswith("SERVER::MSG"):
                    msg = Message(x, self)
                    for func in self.on_message_funcs:
                        await func(msg)
class Message:
    def __init__(self, msg_string, owner):
        _, _, self.id, self.recipient, self.timestamp, self.author, self.content = msg_string.split("::", 6)
        self.owner = owner

    async def reply(self, content):
        await self.owner.msg_queue.put((content, self))
    async def add_reaction(self, emoji):
        await self.owner.msg_queue.put((f"<REACT:ADD:{emoji}>", self))
