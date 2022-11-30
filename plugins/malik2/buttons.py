from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.malik.mbin import malikk
from os import environ




NOTFOUN = InlineKeyboardMarkup([[InlineKeyboardButton("Request", url="https://t.me/iPapPrimeSPbot")]]) 

GSLB = InlineKeyboardMarkup([[InlineKeyboardButton("♻️ 𝐉𝐨𝐢𝐧 𝙂𝙧𝙤𝙪𝙥 ", url="https://t.me/+7p7DwzUq5WdmYWU1")],[ InlineKeyboardButton("♻️ 𝐉𝐨𝐢𝐧 𝙂𝙧𝙤𝙪𝙥 ", url="https://t.me/+7p7DwzUq5WdmYWU1")]]) 

HSTN = InlineKeyboardMarkup([[InlineKeyboardButton("❇️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ❇️", url=f"http://t.me/{malikk.u_name}?startgroup=true") ],[ InlineKeyboardButton('♻️ ʜᴇʟᴘ ♻️', callback_data='help'), InlineKeyboardButton('⚡️ᴜᴘᴅᴀᴛᴇs⚡️', url='https://t.me/iPapkornOfficial')],[InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')]])  

HSTNN = InlineKeyboardMarkup([[InlineKeyboardButton('❇️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ❇️', url=f'http://t.me/{malikk.u_name}?startgroup=true') ],[ InlineKeyboardButton('♻️ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ♻️', url='https://t.me/iPapkornOfficial')],[ InlineKeyboardButton('🔹 ʜᴇʟᴘ 🔹', url=f"http://t.me/{malikk.u_name}?start=help")]])




