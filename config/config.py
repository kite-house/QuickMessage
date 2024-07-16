from os import getenv 
from telethon import TelegramClient

api_id = getenv('api_id')
api_hash = getenv('api_hash')
client = TelegramClient('client', api_id, api_hash)

