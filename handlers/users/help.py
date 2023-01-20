from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp,base


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/static = Botning statistikasi\n",
            "<b>Ushbu bot Uzbekistondagi barcha Viloyatlar NamozVaqtlarini ko'rsatib beruvchi kreativ bot</b>")
    await message.answer("\n".join(text))

@dp.message_handler(commands='static')
async def stat(message:types.Message):
    users = base.count()
    kun1 =base.count_1kun()
    oy = base.count_1oy()
    for userlar in users:
        obunachilar = userlar
    for kun in kun1:
        kecha = kun
    for oyda in oy:
        oylab = oyda
    await message.answer(f"👨🏻‍💻 Obunachilar soni — {obunachilar} ta.\n\n"

f"• Oxirgi 24 soatda — {kecha} ta obunachi qo'shildi.\n"
f"• Oxirgi 1 oyda — {oylab} ta obunachi qo'shildi.\n\n"

"📊  @NamazVaqtlariBot statistikasi")