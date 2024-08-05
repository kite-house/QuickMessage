from telethon import TelegramClient
from os import getenv

client = TelegramClient('client', getenv('api_id'), getenv('api_hash'))

class User:
    number:str = None
    code:str = None
    is_authorized:bool = False

class SendCode:
    def __init__(self, number: str):
        User.number = number
        client.loop.run_until_complete(self.send())

    async def send(self):
        try:
            await client.connect()
            await client.send_code_request(User.number)
            await client.disconnect()
        except Exception:
            raise SystemError('Номер телефона введен неправильно!')

class Sign:
    def __init__(self, code: str):
        User.code = code
        client.loop.run_until_complete(self.sign())

    async def sign(self):
        try:
            await client.connect()
            await client.sign_in(User.number, User.code)
            await client.disconnect()    
        except Exception:
            raise SystemError('Неверный код!')
        
        CheckAuth()

class CheckAuth:
    def __init__(self):
        client.loop.run_until_complete(self.check())

    async def check(self):
        try:
            await client.connect()
            if await client.is_user_authorized():
                User.is_authorized = True
            await client.disconnect()
        except Exception:
            User.is_authorized = False