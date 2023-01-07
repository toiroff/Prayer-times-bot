from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Toshkent",callback_data="region_1"),
            InlineKeyboardButton(text="Andijon",callback_data="region_2")
        ],
        [
            InlineKeyboardButton(text="Farg'ona",callback_data="fargona"),
            InlineKeyboardButton(text="Samarqand", callback_data="samarqand")
        ],
        [
            InlineKeyboardButton(text="Buxoro", callback_data="buxoro"),
            InlineKeyboardButton(text="Sirdaryo", callback_data="sirdaryo")
        ],
        [
            InlineKeyboardButton(text="Jizzax", callback_data="jizzax"),
            InlineKeyboardButton(text="Zarafshon", callback_data="zarafshon")
        ],
        [
            InlineKeyboardButton(text="Qarshi", callback_data="qarshi"),
            InlineKeyboardButton(text="Navoiy", callback_data="navoiy")
        ],
        [
            InlineKeyboardButton(text="Namangan", callback_data="namangan"),
            InlineKeyboardButton(text="Nukus", callback_data="nukus")
        ],
        [
            InlineKeyboardButton(text="Termiz", callback_data="termiz"),
            InlineKeyboardButton(text="Urganch", callback_data="urganch")
        ],
        [
            InlineKeyboardButton(text="Xiva", callback_data="xiva")
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