from os import getenv
from telethon import TelegramClient, events
from config.procCMD import *

client = TelegramClient('client', getenv('api_id'), getenv('api_hash'))


@client.on(events.NewMessage(outgoing=True, pattern='/'))
async def command_handler(message):
    try:
        response = str(ApplicationCommands(message.text)).replace("&", " ")
    except Exception as error:
        print(error)
        return
    
    await message.delete()
    await message.respond(response)

@client.on(events.NewMessage(outgoing=True, pattern='/editCommand'))
async def edit_commands_handler(message):
    try:
        EditCommand(message.text)
    except Exception:
        return 
    await message.delete()
    


client.start()
client.run_until_disconnected()