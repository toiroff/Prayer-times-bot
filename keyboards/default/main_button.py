from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message

from loader import dp

admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Foydalanuvchiga xabar yuborish")

        ],
        [
            KeyboardButton(text="👤 Foydalanuvchilarga xabar yuborish")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True

)
SendMS_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TEXT Xabar 📝")

        ],
        [
            KeyboardButton(text="Video Xabar 📝"),
            KeyboardButton(text="RASM Xabar 📝")
        ],
    ],
    resize_keyboard=True

)
@dp.message_handler(text="👤 Foydalanuvchilarga xabar yuborish")
async def bot(message : Message):
    await message.answer(f"Xabarlardan birini tanlang",reply_markup=SendMS_panel)

@dp.message_handler(commands='reklama',chat_id="917782961")
async def bot(message : Message):
    await message.answer(f"Muvafaqqiyatli Tasdiqlandi✅,@UmarDeveloper",reply_markup=admin_panel)



