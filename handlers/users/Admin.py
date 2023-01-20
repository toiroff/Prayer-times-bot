import types

from states.Send_message import *
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType, CallbackQuery

from keyboards.inline.tas_bek import sendphoto, sendtxt, sendvideo
from keyboards.default.main_button import *
from loader import dp, bot,base
from utils.db_api.baza import bot_stat


@dp.message_handler(commands='Admin',chat_id="917782961")
async def bot_echo(message:types.Message):
    await message.answer(f'<b>Muvaffaqqiyatli tasdiqlandi {message.from_user.full_name}</b> \n'
                         f'\nUshbu panelga faqat @UmarDeveloper kira oladi.',reply_markup=admin_panel)

@dp.message_handler(text="⬅Orqaga")
async def bot_echo(message:types.Message):
    await message.answer(f'<b>Muvaffaqqiyatli tasdiqlandi {message.from_user.full_name}</b> \n'
                         f'\nUshbu panelga faqat @UmarDeveloper kira oladi.',reply_markup=admin_panel)


# FOYDALANUVCHIGA XABAR YUBORISH -----------------------------------------------------------------------------------------------
@dp.message_handler(text="👤 Foydalanuvchiga xabar yuborish")
async def call(message:types.Message):
    await message.answer(text="👤 Foydalanuvchilarga xabar yuborish", reply_markup=Send_message)

@dp.message_handler(text="📝 TEXT Xabar")
async def bot1(message:types.Message):
    await message.answer(text="<b>👤 Foydalanuvchiga xabar yuborish Matin kiriting.\n\nIltimos xabar faqat TEXT formatda bo'lsin</b>")
    await Send_Message.Xabar.set()

@dp.message_handler(state=Send_Message.Xabar)
async def bots(message:types.Message,state:FSMContext):
    await state.update_data({'text':message.text})
    await message.answer('Foydalanuvchiga xabar yuborish uchun Userni Telegram idsini kiriting!')
    await Send_Message.ms_id.set()

@dp.message_handler(state=Send_Message.ms_id)
async def call(message:types.Message,state:FSMContext):
    await state.update_data({'ms_id':message.text})
    malumot = await state.get_data()

    xabri = malumot.get("text")

    ekranga_chiqarish = f"💬 <b>{xabri}</b>\n"

    await bot.send_message(chat_id=f"{message.from_user.id}", text=ekranga_chiqarish, reply_markup=sendtxt)
    await Send_Message.tasdiqlash.set()
@dp.callback_query_handler(state=Send_Message.tasdiqlash,text="tasdiqlashtxt")
async def call(message:types.CallbackQuery,state:FSMContext):
    malumot = await state.get_data()

    xabri = malumot.get("text")
    ms_id = malumot.get('ms_id')

    ekranga_chiqarish = f"💬 <b>{xabri}</b>\n"
    try:
        await bot.send_message(chat_id=f"{ms_id}",text=ekranga_chiqarish)
        await message.answer('Xabar foydalanuvchiga muvaffaqqiyatli yetib bordi', show_alert=True)
    except:
        await message.answer('Message idsi topilmadi',show_alert=True)

    await message.message.delete()
    await state.finish()

@dp.callback_query_handler(state=Send_Message.tasdiqlash,text="bekortxt")
async def call(message:types.CallbackQuery,state:FSMContext):
    await message.message.delete()
    await message.answer('Bekor qilindi',show_alert=True)
    await state.finish()


# SEND PHOTO FOR ONE MESSAGE __________________________________________________________________

@dp.message_handler(text="📝 RASM Xabar")
async def bot_echo(message: types.Message):
    await message.answer(text="RASM JONATING")
    await Send_photo.photo_xabar.set()

@dp.message_handler(state=Send_photo.photo_xabar, content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.photo[0].file_id

    await state.update_data({"rasm": rasm})
    await message.answer(text="RASMGA SARLAVHA KIRITNG")
    await Send_photo.text_xabar.set()

@dp.message_handler(state=Send_photo.text_xabar)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await Send_photo.button_habar.set()

@dp.message_handler(state=Send_photo.button_habar)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/UmarDeveloper</i> ")
    await Send_photo.button_url.set()

@dp.message_handler(state=Send_photo.button_url)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    await state.update_data({"silka": silka})
    await message.answer('Foydalanuvchiga xabar yuborish uchun Userni Telegram idsini kiriting!')
    await Send_photo.ms_id.set()
@dp.message_handler(state=Send_photo.ms_id)
async def call(message:types.Message,state:FSMContext):
    await state.update_data({'ms_id':message.text})
    malumot= await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    ekranga_chiqarish =  f"<b>{matn}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    await bot.send_photo(chat_id=f"{message.from_user.id}",photo=rasm, caption=ekranga_chiqarish,reply_markup=inline_tugma)
    try:
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=sendphoto)
    except Exception:
        pass
    await Send_photo.tasdiqlash.set()


@dp.callback_query_handler(state=Send_photo.tasdiqlash,text="tasdiqlashphoto")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    malumot = await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")
    ms_id = malumot.get('ms_id')
    try:
        await bot.send_chat_action(chat_id=f'{ms_id}',action='typing')
    except BotBlocked:
            await message.answer('Xatolik')
    await message.answer(text=f"Foidalanuvchiga xabar yuborildi ✅",show_alert=True)
    await state.finish()
    ekranga_chiqarish = f"<b>{matn}</b>"
    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    try:
        await bot.send_photo(chat_id=f"{ms_id}", photo=rasm, caption=ekranga_chiqarish, reply_markup=inline_tugma)
    except Exception:
        pass

@dp.callback_query_handler(state=Send_photo.tasdiqlash,text="bekorphoto")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",show_alert=True)
    await state.finish()

# SEND ONE MESSAGE VIDEO -----------------------------------------------------------------------------------------------------


@dp.message_handler(text="📝 Video Xabar")
async def bot_echo(message: types.Message):
    await message.answer(text="Video JONATING")
    await Send_video.video.set()

@dp.message_handler(state=Send_video.video, content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.video.file_id

    await state.update_data({"video": rasm})
    await message.answer(text="VIDEOGA SARLAVHA KIRITNG")
    await Send_video.text.set()

@dp.message_handler(state=Send_video.text)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await Send_video.button_habar.set()

@dp.message_handler(state=Send_video.button_habar)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/UmarDeveloper</i> ")
    await Send_video.button_url.set()

@dp.message_handler(state=Send_video.button_url)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    await state.update_data({"silka": silka})
    await message.answer('Foydalanuvchiga xabar yuborish uchun Userni Telegram idsini kiriting!')
    await Send_video.ms_id.set()

@dp.message_handler(state=Send_video.ms_id)
async def call(message:types.Message,state:FSMContext):
    await state.update_data({'ms_id':message.text})
    malumot= await state.get_data()

    video=malumot.get("video")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    ekranga_chiqarish =  f"<b>{matn}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    await bot.send_video(chat_id=f"{message.from_user.id}",video=video, caption=ekranga_chiqarish,reply_markup=inline_tugma)
    try:
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=sendvideo)
    except Exception:
        pass
    await Send_video.tasdiqlash.set()


@dp.callback_query_handler(state=Send_video.tasdiqlash,text="tasdiqlashv")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    malumot = await state.get_data()

    video=malumot.get("video")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")
    ms_id = malumot.get('ms_id')
    try:
        await bot.send_chat_action(chat_id=f"{ms_id}",action='typing')
        await message.answer('Foydalanuvchiga xabar yuborildi ✅',show_alert=True)
    except Exception:
        pass
    await state.finish()

    ekranga_chiqarish = f"<b>{matn}</b>"
    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    try:
        await bot.send_video(chat_id=f"{ms_id}", video=video, caption=ekranga_chiqarish, reply_markup=inline_tugma)
    except Exception:
        pass
    await message.message.delete()
    await state.finish()
@dp.callback_query_handler(state=Send_video.tasdiqlash,text="bekorv")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    await message.answer(text="Bekor qilindi ❌",show_alert=True)
    await message.message.delete()
    await state.finish()


# SEND VILOYAT ____________________________________________________________________________________________________________________________________

from states.Viloyat import *

@dp.message_handler(text="📨 Viloyatlar bo'yicha xabar yuborish")
async def call(message:types.Message):
    await message.answer("📨 Viloyatlar bo'yicha xabar yuborish",reply_markup=Send_viloyat)

@dp.message_handler(text="📮 TEXT Xabar")
async def bot_echo(message: types.Message):
    await message.answer(
        text="<b>👤 Foydalanuvchilarga xabar yuborish Matin kiriting.\n\nIltimos xabar faqat TEXT formatda bo'lsin</b>")
    await SendViloyat.text.set()

@dp.message_handler(state=SendViloyat.text)
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    await state.update_data({"text": txt})
    await message.answer('<b>Qaysi viloyatdagi foydalanuvchilarga xabar yuborish kerak.</b>',reply_markup=menubutton)

    await SendViloyat.viloyat.set()
#
@dp.message_handler(state=SendViloyat.viloyat)
async def call(message:types.Message,state:FSMContext):
    await state.update_data({'viloyat':message.text})
    malumot = await state.get_data()

    xabri = malumot.get("text")

    ekranga_chiqarish = f"💬{xabri}\n\nViloyat: <b>{malumot.get('viloyat')}</b>"

    await bot.send_message(chat_id=f"{message.from_user.id}", text=ekranga_chiqarish, reply_markup=sendtxt)
    await SendViloyat.tasdiq.set()

@dp.callback_query_handler(state=SendViloyat.tasdiq, text="tasdiqlashtxt")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    malumot = await state.get_data()
    xabri = malumot.get("text")
    viloyat = malumot.get('viloyat')
    # await bot.send_chat_action(chat_id=, action='typing')

    await state.finish()
    users = 0
    try:
        userlar = base.filter_users(viloyat=viloyat)
        for user in userlar:
            user_id = user[3]
            print('user_id',user_id)
            ekranga_chiqarish = f"<b>{xabri}</b>"

            await bot.send_chat_action(chat_id=user_id, action='typing')
            await bot.send_message(chat_id=user_id, text=ekranga_chiqarish)
            users += 1
    except :
        await message.answer('Xatolik yuz berdi!',show_alert=True)

    await message.message.answer(f'{users}ta foydalanuvchilarga xabar yuborildi ✅', reply_markup=admin_panel)

@dp.callback_query_handler(state=SendViloyat.tasdiq, text="bekortxt")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Bekor qilindi ❌", reply_markup=Send_users)
    await state.finish()


#  SEND PHOTO USERS FOR VILOYAT ________________________________________________________________________________________________--

@dp.message_handler(text="📮 RASM Xabar")
async def bot_echo(message: types.Message):
    await message.answer(text="RASM JONATING")
    await ViloyatPhoto.photo_xabar.set()

@dp.message_handler(state=ViloyatPhoto.photo_xabar, content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.photo[0].file_id

    await state.update_data({"rasm": rasm})
    await message.answer(text="RASMGA SARLAVHA KIRITNG")
    await ViloyatPhoto.text_xabar.set()

@dp.message_handler(state=ViloyatPhoto.text_xabar)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await ViloyatPhoto.button_habar.set()

@dp.message_handler(state=ViloyatPhoto.button_habar)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/UmarDeveloper</i> ")
    await ViloyatPhoto.button_url.set()

@dp.message_handler(state=ViloyatPhoto.button_url)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    await state.update_data({"silka": silka})
    await message.answer('<b>Qaysi viloyatdagi foydalanuvchilarga xabar yuborishim kerak!</b>',reply_markup=menubutton)
    await ViloyatPhoto.viloyat.set()
@dp.message_handler(state=ViloyatPhoto.viloyat)
async def call(message:types.Message,state:FSMContext):
    await state.update_data({'viloyat':message.text})
    malumot= await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")
    vil = malumot.get('viloyat')

    ekranga_chiqarish =  f"<b>{matn}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    try:
        await bot.send_photo(chat_id=f"{message.from_user.id}",photo=rasm, caption=ekranga_chiqarish,reply_markup=inline_tugma)
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=sendphoto)
    except Exception:
        pass
    await ViloyatPhoto.tasdiqlash.set()


@dp.callback_query_handler(state=ViloyatPhoto.tasdiqlash,text="tasdiqlashphoto")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    malumot = await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")
    viloyat = malumot.get('viloyat')

    userlar = base.filter_users(viloyat=viloyat)
    users = 0
    try:
        for user in userlar:
            user_id = user[3]
            print('user_id', user_id)
            ekranga_chiqarish = f"<b>{matn}</b>"

            await bot.send_chat_action(chat_id=user_id, action='typing')
            await bot.send_photo(chat_id=user_id, photo=rasm,caption=ekranga_chiqarish,reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text=text,url=silka)
                    ]
                ]
            ))
            users += 1

        await message.message.answer(f'{users}ta Foydalanuvchilarga xabar yuborildi ✅', reply_markup=admin_panel)
    except:
        await message.answer('Xatolik yuz berdi!', show_alert=True)
    await state.finish()

@dp.callback_query_handler(state=ViloyatPhoto.tasdiqlash,text="bekorphoto")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    txt = message.message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=Send_users)
    await state.finish()

# SEND VIDEO for VILOYAT______________________________________________________________________________________________________________________________

@dp.message_handler(text="📮 Video Xabar")
async def bot_echo(message: types.Message):
    await message.answer(text="Send me video")
    await ViloyatVideo.video.set()

@dp.message_handler(state=ViloyatVideo.video, content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.video.file_id

    await state.update_data({"video": rasm})
    await message.answer(text="VIDEOGA SARLAVHA KIRITNG")
    await ViloyatVideo.text.set()

@dp.message_handler(state=ViloyatVideo.text)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await ViloyatVideo.button_habar.set()

@dp.message_handler(state=ViloyatVideo.button_habar)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/UmarDeveloper</i> ")
    await ViloyatVideo.button_url.set()

@dp.message_handler(state=ViloyatVideo.button_url)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    await state.update_data({"silka": silka})
    await message.answer("Qaysi viloyat bo'yicha xabar yuborishim kerak?",reply_markup=menubutton)
    await ViloyatVideo.viloyat.set()

@dp.message_handler(state=ViloyatVideo.viloyat)
async def call(message:types.Message,state:FSMContext):
    await state.update_data({'viloyat':message.text})
    malumot= await state.get_data()

    video=malumot.get("video")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")
    viloyat = malumot.get('viloyat')

    ekranga_chiqarish =  f"<b>{matn}</b>\n\nViloyat: <b>{viloyat}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    await bot.send_video(chat_id=message.from_user.id,video=video, caption=ekranga_chiqarish,reply_markup=inline_tugma)
    try:
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=sendvideo)
    except Exception:
        pass
    await ViloyatVideo.tasdiqlash.set()


@dp.callback_query_handler(state=ViloyatVideo.tasdiqlash,text="tasdiqlashv")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    malumot = await state.get_data()

    video=malumot.get("video")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")
    viloyat = malumot.get('viloyat')
    userlar = base.filter_users(viloyat=viloyat)
    users = 0
    try:
        for user in userlar:
            user_id = user[3]
            print('user_id', user_id)
            ekranga_chiqarish = f"<b>{matn}</b>"

            await bot.send_chat_action(chat_id=user_id, action='typing')
            await bot.send_video(chat_id=user_id, video=video,caption=ekranga_chiqarish,reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text=text,url=silka)
                    ]
                ]
            ))
            users += 1

        await message.message.answer(f'{users}ta Foydalanuvchilarga xabar yuborildi ✅', reply_markup=admin_panel)
    except:
        await message.answer('Xatolik yuz berdi!', show_alert=True)
    await message.message.delete()
    await state.finish()

@dp.callback_query_handler(state=ViloyatVideo.tasdiqlash,text="bekorv")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=Send_users)
    await message.message.delete()
    await state.finish()
