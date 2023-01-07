from aiogram.types import CallbackQuery

from handlers.users.vaqtlar import *
from keyboards.inline.menu import Ttuman, ttorqaga, Toshkent
from loader import dp


@dp.callback_query_handler(text="ttuman")
async def bot1(message : CallbackQuery):
    await message.message.edit_text(text="<b>Shaharlar ro'yhati. Toshkent viloyati</b>",reply_markup=Ttuman)

@dp.callback_query_handler(text="ttorqaga")
async def br(message : CallbackQuery):
    await message.message.edit_text(text="<b>Shaharlar ro'yhati. Toshkent viloyati</b>",reply_markup=Ttuman)



@dp.callback_query_handler(text="bekobod")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Bekobod')}"
                                         f"{hozirgi('Bekobod')}\n</b>"
                                         f"( Bekobod shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Bekobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Bekobod')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Bekobod')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Bekobod')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Bekobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Bekobod')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=ttorqaga)

@dp.callback_query_handler(text="torqa")
async def bot5(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('toshkent')}"
                                         f"{hozirgi('toshkent')}\n</b>"
                                         f"( Toshkent shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('toshkent')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('toshkent')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('toshkent')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('toshkent')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('toshkent')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('toshkent')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=Toshkent)