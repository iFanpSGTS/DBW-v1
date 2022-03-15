import your-folder-name
from your-folder-name import Intents

session = your-folder-name.Session({
    "TOKEN": "TOKEN, EX: 10m2c2mok0qkd0dkamsa0od",
    "INTENTS": Intents.ALL 
})

async def on_ready(a):
    print(f"Bot Online: {session.client.username}")
    
async def on_msg(msg):
    if msg.content.startswith("!reply"):
        await msg.reply({"content":"before"})

session.event("READY", on_ready)
session.event("MESSAGE_CREATE", on_msg)
session.start()