from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from keyboards.inline.menu import menu, orqaga, Toshkent, mainmenu, asosiy

from handlers.users.vaqtlar import *
from states.holatlar import *
from loader import dp, base,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        id =message.from_user.id
        malumot = base.filter(tg_id=id)
        if malumot[3] == id:
            await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                                 f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n", reply_markup=mainmenu)

        else:

            await message.answer(
                f'<b>Assalomu alaykum {message.from_user.full_name}</b>. Namoz vaqtlari botga xush kelibsiz.\n\n'
                f'Ushbu bot yordamida hohlagan viloyatdagi namoz vaqtlarini bilib olishingiz mumkin.Hozir esa sizga kerakli viloyatni kiriting 😇',reply_markup=menu)
    except:
        await message.answer(f'<b>Assalomu alaykum {message.from_user.full_name}</b>. Namoz vaqtlari botga xush kelibsiz.\n\n'
                         f'Ushbu bot yordamida hohlagan viloyatdagi namoz vaqtlarini bilib olishingiz mumkin.Hozir esa sizga kerakli viloyatni kiriting 😇',reply_markup=menu)

        await Start.viloyat.set()

@dp.callback_query_handler(state=Start.viloyat)
async def bot_echo(message:types.CallbackQuery,state:FSMContext):

    try:
        ism = message.from_user.first_name
        fam = message.from_user.last_name
        telegram_id = message.from_user.id
        user_name = message.from_user.username
        base.user_qoshish(ism=ism, fam=fam, tg_id=telegram_id, username=user_name,viloyat=message.data)

        await message.message.edit_text(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                             f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n"
                         f"Sizga qaysi viloyat bo'yicha ma'lumot kerak!",reply_markup=mainmenu)



    except:
        await message.answer("Qayta urinib ko'ring!",show_alert=True)
    await state.finish()



@dp.message_handler(text="📑 Foydalanuvchilar ro'yhati")
async def call(message:types.Message):
    with open('data.xlsx', 'rb') as file:
        await bot.send_document(chat_id=message.from_user.id, document=file,caption='@NamazVaqtlariBot dagi foydalanuvchilar <b>Excel</b> formatda.')

    # with open('data.pdf', 'rb') as file2:
    #     await bot.send_document(chat_id=message.from_user.id, document=file2)
@dp.callback_query_handler(text="other")
async def call(message:types.CallbackQuery):
    await message.message.edit_text("<b>Sizga qaysi viloyat bo'yicha ma'lumot kerak!</b>",reply_markup=menu)

@dp.callback_query_handler(text="asosiy")
async def call(message:types.CallbackQuery):
    await message.message.edit_text(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                                 f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n", reply_markup=mainmenu)
@dp.callback_query_handler(text="orqaga")
async def bot_start(message: CallbackQuery):
    await message.message.edit_text(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                         f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n"
                         f"Sizga qaysi turdagi mintaqa bo'yicha ma'lumot kerak!",reply_markup=menu)

@dp.callback_query_handler(text="myviloyat")
async def call(message:types.CallbackQuery):
    try:
        id = message.from_user.id
        malumot = base.filter(tg_id=id)
        viloyat = malumot[5]
        await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
        await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                             f"<b>Bugun {bugun(f'{viloyat}')}"
                                             f"{hozirgi(f'{viloyat}')}\n</b>"
                                             f"( {viloyat} shahri )\n\n"
                                             f"🏙 <b>Bomdod</b>: {bomdod(viloyat)} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                             f"🌅 <b>Quyosh</b>: {quyosh(viloyat)} 🕰\n\n"
                                             f"🏞 <b>Peshin</b>: {peshin(viloyat)} 🕰\n\n"
                                             f"🌇 <b>Asr</b>: {asr(viloyat)} 🕰\n\n"
                                             f"🌆 <b>Shom</b>: {shom(viloyat)} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                             f"🌃 <b>Xufton</b>: {xufton(viloyat)} 🕰 \n\n"
                                             f"Manba : namozvaqti.uz", disable_web_page_preview=True, reply_markup=asosiy)
    except:
        await message.answer('Sizning mintaqangiz topilmadi!',show_alert=True)

@dp.callback_query_handler(text="Toshkent")
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

@dp.callback_query_handler(text="Andijon")
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

@dp.callback_query_handler(text="Fargona")
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

@dp.callback_query_handler(text="Samarqand")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('samarqand')}"
                                         f"{hozirgi('samarqand')}\n</b>"
                                         f"( Samarqand shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Samarqand')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('samarqand')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('samarqand')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('samarqand')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('samarqand')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('samarqand')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="Buxoro")
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

@dp.callback_query_handler(text="Sirdaryo")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Sirdaryo')}"
                                         f"{hozirgi('Sirdaryo')}\n</b>"
                                         f"( Sirdaryo shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Sirdaryo')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Sirdaryo')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Sirdaryo')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Sirdaryo')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Sirdaryo')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Sirdaryo')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="Jizzax")
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

@dp.callback_query_handler(text="Zarafshon")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Zarafshon')}"
                                         f"{hozirgi('Zarafshon')}\n</b>"
                                         f"( Zarafshon shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Zarafshon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Zarafshon')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Zarafshon')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Zarafshon')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Zarafshon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Zarafshon')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="Qarshi")
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

@dp.callback_query_handler(text="Navoiy")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('Navoiy')}"
                                         f"{hozirgi('Navoiy')}\n</b>"
                                         f"( Navoiy shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('Navoiy')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('Navoiy')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('Navoiy')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('Navoiy')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('Navoiy')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('Navoiy')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)

@dp.callback_query_handler(text="Namangan")
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

@dp.callback_query_handler(text="Nukus")
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

@dp.callback_query_handler(text="Termiz")
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

@dp.callback_query_handler(text="Urganch")
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

@dp.callback_query_handler(text="Xiva")
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

@dp.callback_query_handler(text="Margilan")
async def bots(message : CallbackQuery):
    await message.message.edit_text(text=f"☪️ Namoz vaqtlari:\n\n"
                                         f"<b>Bugun {bugun('margilon')}"
                                         f"{hozirgi('margilon')}\n</b>"
                                         f"( Marg'ilon shahri )\n\n"
                                         f"🏙 <b>Bomdod</b>: {bomdod('margilon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                         f"🌅 <b>Quyosh</b>: {quyosh('margilon')} 🕰\n\n"
                                         f"🏞 <b>Peshin</b>: {peshin('margilon')} 🕰\n\n"
                                         f"🌇 <b>Asr</b>: {asr('margilon')} 🕰\n\n"
                                         f"🌆 <b>Shom</b>: {shom('margilon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                         f"🌃 <b>Xufton</b>: {xufton('margilon')} 🕰 \n\n"
                                         f"Manba : namozvaqti.uz",disable_web_page_preview=True,reply_markup=orqaga)