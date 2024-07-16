from telethon import events
from config.config import client
from config.procCMD import *

@client.on(events.NewMessage(outgoing=True, pattern='/'))
async def message_handler(message):
    try:
        response = str(ApplicationCommands(message.text))
    except Exception:
        return
    
    await message.delete()
    await message.respond(response)

client.start()
client.run_until_disconnected()