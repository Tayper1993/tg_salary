from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb_salary = {
    'salary': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='60 000', callback_data='60000')],
            [InlineKeyboardButton(text='70 000', callback_data='70000')],
        ]
    ),
    'month': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Январь', callback_data='Январь'),
                InlineKeyboardButton(text='Февраль', callback_data='Февраль'),
                InlineKeyboardButton(text='Март', callback_data='Март'),
            ],
            [
                InlineKeyboardButton(text='Апрель', callback_data='Апрель'),
                InlineKeyboardButton(text='Май', callback_data='Май'),
                InlineKeyboardButton(text='Июнь', callback_data='Июнь'),
            ],
            [
                InlineKeyboardButton(text='Июль', callback_data='Июль'),
                InlineKeyboardButton(text='Август', callback_data='Август'),
                InlineKeyboardButton(text='Сентябрь', callback_data='Сентябрь'),
            ],
            [
                InlineKeyboardButton(text='Октябрь', callback_data='Октябрь'),
                InlineKeyboardButton(text='Ноябрь', callback_data='Ноябрь'),
                InlineKeyboardButton(text='Декабрь', callback_data='Декабрь'),
            ],
            [InlineKeyboardButton(text='Текущий месяц', callback_data='current_month')],
        ]
    ),
}
