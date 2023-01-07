from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery


from keyboards.inline.menu import menu, orqaga, Toshkent
from loader import dp, base
from handlers.users.vaqtlar import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        ism = message.from_user.first_name
        fam = message.from_user.last_name
        telegram_id = message.from_user.id
        user_name = message.from_user.username
        base.user_qoshish(ism=ism, fam=fam, tg_id=telegram_id, username=user_name)
    except Exception:
        pass
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                         f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n"
                         f"Sizga qaysi viloyat bo'yicha ma'lumot kerak!",reply_markup=menu)
@dp.callback_query_handler(text="orqaga")
async def bot_start(message: CallbackQuery):
    await message.message.edit_text(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                         f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n"
                         f"Sizga qaysi turdagi mintaqa bo'yicha ma'lumot kerak!",reply_markup=menu)

@dp.callback_query_handler(text="region_1")
async def bots(message : CallbackQuery):
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
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="region_2")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('andijon')}"
                                         f"{hozirgi('andijon')}\n</b>"
                                         f"( Andijon shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('andijon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('andijon')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('andijon')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('andijon')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('andijon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('andijon')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="fargona")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('fargona')}"
                                         f"{hozirgi('fargona')}\n</b>"
                                         f"( Farg'ona shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('fargona')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('fargona')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('fargona')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('fargona')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('fargona')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('fargona')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="samarqand")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('samarqand')}"
                                         f"{hozirgi('samarqand')}\n</b>"
                                         f"( Samarqand shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('samarqand')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('samarqand')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('samarqand')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('samarqand')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('samarqand')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('samarqand')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="buxoro")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('buxoro')}"
                                         f"{hozirgi('buxoro')}\n</b>"
                                         f"( Buxoro shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('buxoro')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('buxoro')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('buxoro')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('buxoro')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('buxoro')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('buxoro')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="sirdaryo")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('sirdaryo')}"
                                         f"{hozirgi('sirdaryo')}\n</b>"
                                         f"( Sirdaryo shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('sirdaryo')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('sirdaryo')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('sirdaryo')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('sirdaryo')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('sirdaryo')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('sirdaryo')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="jizzax")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Jizzax')}"
                                         f"{hozirgi('guliston')}\n</b>"
                                         f"( Jizzax shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Jizzax')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Jizzax')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Jizzax')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Jizzax')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Jizzax')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Jizzax')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="surxondaryo")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Surxondaryo')}"
                                         f"{hozirgi('Surxondaryo')}\n</b>"
                                         f"( Surxondaryo shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Surxondaryo')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Surxondaryo')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Surxondaryo')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Surxondaryo')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Surxondaryo')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Surxondaryo')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="qarshi")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Qarshi')}"
                                         f"{hozirgi('Qarshi')}\n</b>"
                                         f"( Qarshi shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Qarshi')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Qarshi')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Qarshi')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Qarshi')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Qarshi')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Qarshi')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="navoiy")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('navoiy')}"
                                         f"{hozirgi('navoiy')}\n</b>"
                                         f"( Navoiy shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('navoiy')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('navoiy')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('navoiy')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('navoiy')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('navoiy')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('navoiy')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="namangan")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Namangan')}"
                                         f"{hozirgi('Namangan')}\n</b>"
                                         f"( Namangan shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Namangan')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Namangan')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Namangan')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Namangan')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Namangan')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Namangan')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="nukus")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Nukus')}"
                                         f"{hozirgi('Nukus')}\n</b>"
                                         f"( Nukus shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Nukus')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Nukus')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Nukus')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Nukus')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Nukus')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Nukus')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="termiz")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Termiz')}"
                                         f"{hozirgi('Termiz')}\n</b>"
                                         f"( Termiz shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Termiz')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Termiz')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Termiz')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Termiz')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Termiz')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Termiz')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="urganch")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Urganch')}"
                                         f"{hozirgi('Urganch')}\n</b>"
                                         f"( Urganch shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Urganch')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Urganch')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Urganch')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Urganch')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Urganch')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Urganch')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="xiva")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Xiva')}"
                                         f"{hozirgi('Xiva')}\n</b>"
                                         f"( Xiva shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Xiva')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Xiva')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Xiva')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Xiva')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Xiva')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Xiva')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)