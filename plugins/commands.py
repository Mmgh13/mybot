from pyrogram import Client, filters, enums



texts = {
    'start': "سلام من ربات **عارینح** هستم😎😁\n امیدوارم که بتونم به بهترین نحوه به **امیرحسن عارینح** --انرژی-- بدم \n فقط کافیه من رو توی گروهی که عارینح هست عضو کنی❤️🫡"
}



# start commands
@Client.on_message(filters.command(["start", 'help']))
async def start(client, message):
    client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    await message.reply(texts['start'], parse_mode=enums.ParseMode.MARKDOWN)
