from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

tas_bekor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash✅",callback_data='tasdiqlash'),

        ],
        [
            InlineKeyboardButton(text="Bekor qilish❌",callback_data='bekor')
        ]
    ]
)
sendtxt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash✅",callback_data='tasdiqlashtxt'),
        ],
        [
            InlineKeyboardButton(text="Bekor qilish❌",callback_data='bekortxt')
        ]
    ]
)
sendphoto = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash✅",callback_data='tasdiqlashphoto'),
        ],
        [
            InlineKeyboardButton(text="Bekor qilish❌",callback_data='bekorphoto')
        ]
    ]
)
tasbutton = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash✅",callback_data='tasdiqlashbut'),
        ],
        [
            InlineKeyboardButton(text="Bekor qilish❌",callback_data='bekorbut')
        ]
    ]
)
sendvideo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash✅",callback_data='tasdiqlashv'),
        ],
        [
            InlineKeyboardButton(text="Bekor qilish❌",callback_data='bekorv')
        ]
    ]
)