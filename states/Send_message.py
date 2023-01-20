from aiogram.dispatcher.filters.state import State,StatesGroup

class Send_Message(StatesGroup):
    ms_id = State()
    Xabar = State()
    tasdiqlash = State()

class Send_photo(StatesGroup):
    text_xabar = State()
    photo_xabar = State()
    button_habar = State()
    button_url = State()
    ms_id = State()
    tasdiqlash = State()

class Send_video(StatesGroup):
    video = State()
    text = State()
    button_habar = State()
    button_url = State()
    ms_id = State()
    tasdiqlash = State()