from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Подсчитать зарплату и аванс')],
        [KeyboardButton(text='Очистка')],
    ],
    resize_keyboard=True,
)
