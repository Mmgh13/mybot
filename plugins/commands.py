from pyrogram import Client, filters



texts = {
    'start': "سلام من ربات **عارینح** هستم😎😁\n امیدوارم که بتونم به بهترین نحوه به **امیرحسن عارینح** --انرژی-- بدم"
}



# start commands
@Client.on_message(filters.command(["start", 'help']))
async def start(client, message):
    await message.reply_text(texts['start'])