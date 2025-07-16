from pyrogram import Client, filters, enums
import time
from random import choice


texts = [
    "عاشقتم سید جون❤️❤️😍",
    "**امیررضا** ملک فدات شه جیگر💖😉",
    "حرف فقط حرف خودت نازنین 👌😁",
    "__من و آرین__ شما همه 😎✌️💪",
    "سلطان خودتی شیر خرته 👑🦁",
    "ما اینجا تا آخرش باهاتیم ستونننن 🥰🤤😇",
    "**تو فقط پیام بده‌٬ ما لذت میبریم عقاب ایران 🦅**",
    "جهان بی تو هرگز ||امیرجونم 💐🌹🌍||"
]
used = []

@Client.on_message(filters.group, group=1)
async def group(client, message):
    if message.from_user.username == 'Py_mahdi':
        await message.reply_chat_action(enums.ChatAction.TYPING)
        time.sleep(2)
        await message.reply_text(choice(texts), quote=True)