from aiogram.dispatcher.filters.state import StatesGroup,State


class SendViloyat(StatesGroup):
    tg_id = State()
    text = State()
    viloyat = State()
    tasdiq = State()

class ViloyatPhoto(StatesGroup):
    text_xabar = State()
    photo_xabar = State()
    button_habar = State()
    button_url = State()
    viloyat = State()
    tasdiqlash = State()
class ViloyatVideo(StatesGroup):
    video = State()
    text = State()
    button_habar = State()
    button_url = State()
    viloyat = State()
    tasdiqlash = State()



class Update(StatesGroup):
    update = State()