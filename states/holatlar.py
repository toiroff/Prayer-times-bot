from aiogram.dispatcher.filters.state import State,StatesGroup

class Forma(StatesGroup):
    murojat= State()
    tasdiqlash = State()

class SendM(StatesGroup):
    tg_id = State()
    text = State()
    tasdiq = State()

class SendPhoto(StatesGroup):
    text_xabar = State()
    photo_xabar = State()
    button_habar = State()
    button_url = State()
    tasdiqlash = State()

class Sendbutton(StatesGroup):
    photo_xabar = State()
    txt_xabar = State()
    button_habar = State()
    button_url = State()
    tasdiqlash = State()

class Video(StatesGroup):
    video = State()
    text = State()
    button_habar = State()
    button_url = State()
    tasdiqlash = State()

class Start(StatesGroup):
    viloyat = State()