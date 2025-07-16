# libraries
from pyrogram import Client
from api import *

# settings
plugins = dict(root='plugins')
Client('my_bot', api_id, api_hash, bot_token, plugins=plugins).run()


