from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "**πΌπ°π³π΄ π±π [HARSH](https://t.me/backup_MovieLand4K)**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("ππΏπ³π°ππ΄π π²π·π°π½π½π΄π»", url="https://t.me/backup_MovieLand4K")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "**ππ΄πΏπ»π ππΎ π°π½π ππ΄ππ πΌπ΄πππ°πΆπ΄ ππΎ πΌπ°πΊπ΄ π²π°ππ±πΎπ½.**"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "**ππ΄πΏπ»π ππΎ π°π½π ππ΄ππ πΌπ΄πππ°πΆπ΄ ππΎ πΌπ°πΊπ΄ π²π°ππ±πΎπ½.**"
        )
    user_id = message.from_user.id
    m = await message.reply_text("**π²ππ΄π°ππΈπ½πΆ π²π°ππ±πΎπ½...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**ππΏπ»πΎπ°π³πΈπ½πΆ π²π°ππ±πΎπ½...**")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
