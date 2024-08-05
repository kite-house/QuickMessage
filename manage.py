from telethon import events
from config.processingCommands import *
from multiprocessing import Process
from gui.main import launch
from auth import client, User, CheckAuth


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
    GuiProcess = Process(target=launch, name = 'GuiProcess', daemon=True)
    GuiProcess.start()

    
def launch_telegram():
    CheckAuth()

    if not User.is_authorized:
        GuiProcess = Process(target=launch, name = 'GuiProcessAuth', daemon=True)
        GuiProcess.start()
        GuiProcess.join()

    client.start()
    client.run_until_disconnected()

if __name__ == '__main__':
    MainProcess = Process(target=launch_telegram, name = 'TelegramPluginProcess')
    MainProcess.start()
    MainProcess.join()