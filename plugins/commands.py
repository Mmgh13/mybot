from pyrogram import Client, filters

# start commands
@Client.on_message(filters.command("start") & filters.text)
async def start(client, message):
    await message.reply('hello')