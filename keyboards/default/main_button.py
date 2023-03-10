from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram import types
from loader import dp

admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ð¤ Foydalanuvchiga xabar yuborish")

        ],
        [
            KeyboardButton(text="ð¤ Foydalanuvchilarga xabar yuborish"),

        ],
        [
KeyboardButton(text="ð¨ Viloyatlar bo'yicha xabar yuborish"),
            KeyboardButton(text="ð Foydalanuvchilar ro'yhati"),

        ]
    ],
    resize_keyboard=True

)
Send_users = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TEXT Xabar ð")

        ],
        [
            KeyboardButton(text="Video Xabar ð"),
            KeyboardButton(text="RASM Xabar ð")
        ],
        [
            KeyboardButton(text="â¬Orqaga")
        ],
    ],resize_keyboard=True

)
Send_message = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ð TEXT Xabar")

        ],
        [
            KeyboardButton(text="ð Video Xabar"),
            KeyboardButton(text="ð RASM Xabar")
        ],
        [
            KeyboardButton(text="â¬Orqaga")
        ],
    ],resize_keyboard=True

)
Send_viloyat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ð® TEXT Xabar")

        ],
        [
            KeyboardButton(text="ð® Video Xabar"),
            KeyboardButton(text="ð® RASM Xabar")
        ],
        [
            KeyboardButton(text="â¬Orqaga")
        ],
    ],resize_keyboard=True

)

menubutton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Andijon")
        ],
        [
            KeyboardButton(text="Fargona"),
            KeyboardButton(text="Samarqand", )
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Sirdaryo")
        ],
        [
            KeyboardButton(text="Jizzax"),
            KeyboardButton(text="Zarafshon")
        ],
        [
            KeyboardButton(text="Qarshi"),
            KeyboardButton(text="Navoiy")
        ],
        [
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Nukus")
        ],
        [
            KeyboardButton(text="Termiz"),
            KeyboardButton(text="Urganch",)
        ],
        [
            KeyboardButton(text="Xiva"),
            KeyboardButton(text="Margilon")
        ]
    ],resize_keyboard=True
)






