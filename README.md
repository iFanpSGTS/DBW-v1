## Discord Bot api wrapper
This discord bot api wrapper is make using python

Module is used in this program

- Module:
    - aiohttp
    - python-dateutil

## Information
This discord bot api wrapper i make only can send message, but if u want to remake this can do what you want? you can!

## Quick Example
```bash
> Make a folder then put all this file's on your folder then import it as a module
```
```Python
import Your-folder-name
from your-folder-name import Intents

session = punyakita.Session({
    # You can take the discord bot token from here https://discord.com/developers/applications
    "TOKEN": "your token. Ex: 01282xidasdm-91mcoamp",
    "INTENTS": Intents.ALL # You can see the intent here ./helpers/intents.py. Check all the privileged gateaways here if the bot don't on or get intents error : https://discord.com/developers/applications/BotID/bot
})

async def on_ready():
    print(f"Bot Online: {session.client.username}")
    
async def on_message_start(msg):
    if not msg.author.bot == "hi":
        await msg.reply({
            "content": "hi"
        })
        
#Setup event for on_message_start & on_ready & for start the session websocket
session.event("READY", on_ready) # "READY is event_name" "fn is you're function name "on_ready""
session.event("MESSAGE_CREATE", on_message_start)
session.start()
```

## Reference
- Rapptz (discord.py)
- RedBallG (selfdiscord "forgot the name HEHE")
- [Discord Developer Portal](https://discord.com/developers/applications)

## Credit
- iFanpS
