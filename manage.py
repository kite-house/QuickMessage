from os import getenv
from telethon import TelegramClient, events
from config.processingCommands import *

client = TelegramClient('client', getenv('api_id'), getenv('api_hash'))

@client.on(events.NewMessage(outgoing=True, pattern='/'))
async def command_handler(message):
    try:
        response = str(ExecuteCommand(message.text)).replace("&", " ")
    except Exception:
        return
    
    await message.delete()
    await message.respond(response)

@client.on(events.NewMessage(outgoing=True, pattern='/test'))
async def output_interface(message):
    await message.delete()
    #
    


client.start()
client.run_until_disconnected()
