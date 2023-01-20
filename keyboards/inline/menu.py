from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


mainmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugungi namoz vaqtlari ⏳",callback_data='myviloyat')
        ],
        [
            InlineKeyboardButton(text="Viloyatlar",callback_data='other'),
            InlineKeyboardButton(text="Update Viloyat 🔄",callback_data='update'),
        ],
        [

            InlineKeyboardButton(text="Qur'on va Nashidalar 🕌",url='https://t.me/Quran_nasheedsbot'),

        ]
    ]
)
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Toshkent",callback_data="Toshkent"),
            InlineKeyboardButton(text="Andijon",callback_data="Andijon")
        ],
        [
            InlineKeyboardButton(text="Farg'ona",callback_data="Fargona"),
            InlineKeyboardButton(text="Samarqand", callback_data="Samarqand")
        ],
        [
            InlineKeyboardButton(text="Buxoro", callback_data="Buxoro"),
            InlineKeyboardButton(text="Sirdaryo", callback_data="Sirdaryo")
        ],
        [
            InlineKeyboardButton(text="Jizzax", callback_data="Jizzax"),
            InlineKeyboardButton(text="Zarafshon", callback_data="Zarafshon")
        ],
        [
            InlineKeyboardButton(text="Qarshi", callback_data="Qarshi"),
            InlineKeyboardButton(text="Navoiy", callback_data="Navoiy")
        ],
        [
            InlineKeyboardButton(text="Namangan", callback_data="Namangan"),
            InlineKeyboardButton(text="Nukus", callback_data="Nukus")
        ],
        [
            InlineKeyboardButton(text="Termiz", callback_data="Termiz"),
            InlineKeyboardButton(text="Urganch", callback_data="Urganch")
        ],
        [
            InlineKeyboardButton(text="Xiva", callback_data="Xiva"),
            InlineKeyboardButton(text="Margilan",callback_data="Margilon")

        ],
        [
            InlineKeyboardButton(text="⬆️ Menu",callback_data='asosiy')
        ]
    ]
)

asosiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬆️ Menu",callback_data='asosiy')
        ]
    ]
)

orqaga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Orqaga",callback_data="orqaga")
        ]
    ]
)
# Toshkent -----------------------------------------------------------------------
Toshkent = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tumanlar",callback_data="ttuman"),
            InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")
        ]
    ]
)
Ttuman = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bekobod",callback_data="bekobod"),
            InlineKeyboardButton(text="Olmaliq",callback_data="olmaliq")
        ],
        [
            InlineKeyboardButton(text="Nurafshon",callback_data="nurafshon"),
            InlineKeyboardButton(text="Angren", callback_data="Angren")
        ],
        [
            InlineKeyboardButton(text="Parket", callback_data="Parket"),
            InlineKeyboardButton(text="Bo'ka", callback_data="boka")
        ],
        [
            InlineKeyboardButton(text="Piskent", callback_data="nurafshon"),
            InlineKeyboardButton(text="Go'zalkent", callback_data="gozalkent")
        ],
        [
            InlineKeyboardButton(text="Yangi yo'l", callback_data="yangiyo'l"),
            InlineKeyboardButton(text="🔙Orqaga", callback_data="torqa")
        ]
    ]
)
ttorqaga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Orqaga", callback_data="ttorqaga"),
            InlineKeyboardButton(text="🔝Asosiy menyu",callback_data="ttasosiy")
        ]
    ]
)