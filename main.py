# libraries
from pyrogram import Client, filters
from api import *

proxy = {
    "scheme": "mtproto",
    'hostname':'Focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.info',
    'port': 443,

}

# settings
app = Client("my_account", api_hash=api_hash, api_id=api_id, bot_token=token, proxy=proxy)


# body

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, 'hello bro mahdi')

# with app:
#     session_string = app.export_session_string()
#     print((session_string, 'is this'))
app.run()




