import re, asyncio, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *


    
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**π πΏππΎπ²π΄πππ΄π πππΎπΏπ΄π³. π±πΎπ πΈπ ππ΄πππ°πππΈπ½πΆ...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**βοΈ π±πΎπ πΈπ ππ΄πππ°πππ΄π³. π½πΎπ ππΎπ π²π°π½ πππ΄ πΌπ΄**")
    os.execl(sys.executable, sys.executable, *sys.argv)
