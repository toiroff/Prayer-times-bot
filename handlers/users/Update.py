from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.main_button import menubutton
from keyboards.inline.menu import mainmenu, menu
from states.Viloyat import Update
from loader import dp,base


@dp.callback_query_handler(text="update")
async def call(message:types.CallbackQuery):
    await message.message.edit_text(text="Sizga qaysi mintaqa bo'yicha ma'lumot olishni istaysiz!",reply_markup=menu)
    await Update.update.set()
@dp.callback_query_handler(state=Update.update,text="asosiy")
async def call(message:types.CallbackQuery,state:FSMContext):
    await message.message.edit_text(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\n"
                         f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n", reply_markup=mainmenu)

    await state.finish()
@dp.callback_query_handler(state=Update.update)
async def call(message:types.CallbackQuery,state:FSMContext):
    id = message.from_user.id
    base.update(viloyat=message.data,tg_id=id)
    await message.answer(f'Muvaffaqqiyatli amalga oshirildi ✅\n           {message.data}',show_alert=True)
    await message.message.edit_text(f"Assalomu alaykum, <b>{message.from_user.full_name}! Muvaffaqqiyatli yangilandI.</b>\n"
                         f"<b>Namoz vaqtlari botizga hush kelibsiz</b>\n\n", reply_markup=mainmenu)

    await state.finish()
