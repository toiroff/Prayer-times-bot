from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

from keyboards.inline.tas_bek import sendphoto, sendtxt, sendvideo
from states.holatlar import *
from keyboards.default.main_button import *
from loader import dp, bot, base
from utils.db_api.baza import *
from keyboards.default.main_button import SendMS_panel
@dp.message_handler(text="RASM Xabar 📝")
async def bot_echo(message: types.Message):
    await message.answer(text="RASM JONATING")
    await SendPhoto.photo_xabar.set()

@dp.message_handler(state=SendPhoto.photo_xabar, content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.photo[0].file_id

    await state.update_data({"rasm": rasm})
    await message.answer(text="RASMGA SARLAVHA KIRITNG")
    await SendPhoto.text_xabar.set()

@dp.message_handler(state=SendPhoto.text_xabar)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await SendPhoto.button_habar.set()

@dp.message_handler(state=SendPhoto.button_habar)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/MistrUz</i> ")
    await SendPhoto.button_url.set()

@dp.message_handler(state=SendPhoto.button_url)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    user_id = message.from_user.id
    await state.update_data({"silka": silka})

    malumot= await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    ekranga_chiqarish =  f"<b>{matn}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    await bot.send_photo(chat_id="1625900856",photo=rasm, caption=ekranga_chiqarish,reply_markup=inline_tugma)
    try:
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=sendphoto)
    except Exception:
        pass
    await SendPhoto.tasdiqlash.set()


@dp.callback_query_handler(state=SendPhoto.tasdiqlash,text="tasdiqlashphoto")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_id = message.from_user.id

    malumot = await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    users = bot_stat()
    all_users = 0
    blocked_users = 0
    for x in users:
        try:
            await bot.send_chat_action(chat_id=x[0],action='typing')
            all_users += 1
        except BotBlocked:
            blocked_users += 1
    await bot.send_message(chat_id=user_id, text=f"<b>{all_users} ta foidalanuvchilarga reklama yuborildi ✅\n\n{blocked_users} ta odam botni bloklagan</b>", reply_markup=SendMS_panel)
    await state.finish()

    userlar= base.select_all_foidalanuvchilar()
    for user in userlar:
        user_id =user[3]
        ekranga_chiqarish = f"<b>{matn}</b>"
        inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
        try:
            await bot.send_photo(chat_id=user_id, photo=rasm, caption=ekranga_chiqarish, reply_markup=inline_tugma)
        except Exception:
            pass

@dp.callback_query_handler(state=SendPhoto.tasdiqlash,text="bekorphoto")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    txt = message.message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=SendMS_panel)
    await state.finish()


# mail_bt =InlineKeyboardButton(text="11-15 Dars",callback_data="3dars3")
#
# inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="1-5 Dars",callback_data="1dars1")]])
@dp.message_handler(text="TEXT Xabar 📝")
async def bot_echo(message: types.Message):
    await message.answer(text="<b>👤 Foydalanuvchilarga xabar yuborish Matin kiriting.\n\nIltimos xabar faqat TEXT formatda bo'lsin</b>")
    await SendM.text.set()

@dp.message_handler(state=SendM.text)
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await state.update_data({"text": txt})

    malumot= await state.get_data()

    xabri = malumot.get("text")

    ekranga_chiqarish =  f"💬<b>Murojat :</b> {xabri}\n"

    await bot.send_message(chat_id="917782961",text=ekranga_chiqarish,reply_markup=sendtxt)
    await SendM.tasdiq.set()


@dp.callback_query_handler(state=SendM.tasdiq,text="tasdiqlashtxt")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    txt = message.message.text
    user_id = message.from_user.id
    malumot = await state.get_data()

    xabri = malumot.get("text")
    users = bot_stat()
    all_users = 0
    blocked_users = 0
    for x in users:
        try:
            await bot.send_chat_action(chat_id=x[0],action='typing')
            all_users += 1
        except BotBlocked:
            blocked_users += 1
    await bot.send_message(chat_id=user_id, text=f"<b>{all_users} ta foidalanuvchilarga reklama yuborildi ✅\n\n{blocked_users} ta odam botni bloklagan</b>", reply_markup=SendMS_panel)
    await state.finish()

    userlar= base.select_all_foidalanuvchilar()
    for user in userlar:
        user_id =user[3]
        ekranga_chiqarish = f"<b>{xabri}</b>"
        try:
            await bot.send_message(chat_id=user_id,text=ekranga_chiqarish)
        except Exception:
            pass



@dp.callback_query_handler(state=SendM,text="bekortxt")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=SendMS_panel)
    await state.finish()

# photo
@dp.message_handler(text="Video Xabar 📝")
async def bot_echo(message: types.Message):
    await message.answer(text="Video JONATING")
    await Video.video.set()

@dp.message_handler(state=Video.video, content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.video.file_id

    await state.update_data({"video": rasm})
    await message.answer(text="VIDEOGA SARLAVHA KIRITNG")
    await Video.text.set()

@dp.message_handler(state=Video.text)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await Video.button_habar.set()

@dp.message_handler(state=Video.button_habar)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/UmarDeveloper</i> ")
    await Video.button_url.set()

@dp.message_handler(state=Video.button_url)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    user_id = message.from_user.id
    await state.update_data({"silka": silka})

    malumot= await state.get_data()

    video=malumot.get("video")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    ekranga_chiqarish =  f"<b>{matn}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    await bot.send_video(chat_id="917782961",video=video, caption=ekranga_chiqarish,reply_markup=inline_tugma)
    try:
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=sendvideo)
    except Exception:
        pass
    await Video.tasdiqlash.set()


@dp.callback_query_handler(state=Video.tasdiqlash,text="tasdiqlashv")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_id = message.from_user.id

    malumot = await state.get_data()

    video=malumot.get("video")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    users = bot_stat()
    all_users = 0
    blocked_users = 0
    for x in users:
        try:
            await bot.send_chat_action(chat_id=x[0],action='typing')
            all_users += 1
        except BotBlocked:
            blocked_users += 1
    await bot.send_message(chat_id=user_id, text=f"<b>{all_users} ta foidalanuvchilarga reklama yuborildi ✅\n\n{blocked_users} ta odam botni bloklagan</b>", reply_markup=SendMS_panel)
    await state.finish()

    userlar= base.select_all_foidalanuvchilar()
    for user in userlar:
        user_id =user[3]
        ekranga_chiqarish = f"<b>{matn}</b>"
        inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
        try:
            await bot.send_video(chat_id=user_id, video=video, caption=ekranga_chiqarish, reply_markup=inline_tugma)
        except Exception:
            pass

@dp.callback_query_handler(state=SendPhoto.tasdiqlash,text="bekorv")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    txt = message.message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=SendMS_panel)
    await state.finish()




