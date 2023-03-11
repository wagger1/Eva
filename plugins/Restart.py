import re, asyncio, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import ADMINS

    
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**Hᴇʏ 🦇⃝🍂ꜱᴀᴄʜᴜ℡ Aʟʟ Mʏ Pʀᴏᴄᴇꜱꜱ Aʀᴇ Sᴛᴏᴘᴘᴇᴅ ⚙️ Wᴀɪᴛ Fᴏʀ 𝟻 Sᴇᴄꜱ 🤷‍♀️**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**⚙️ Rᴇꜱᴛᴀʀᴛᴇᴅ ‼️ Nᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ 🙃**")
    os.execl(sys.executable, sys.executable, *sys.argv)
