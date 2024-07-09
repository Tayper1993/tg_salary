from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from keyboards.keyboards import kb_salary, kb_main

router = Router()


def salary(salary: int, month: str):
    data = {
        'Декабрь': {'days_to_avans': 10, 'work_day': 20},
        'Январь': {'days_to_avans': 5, 'work_day': 17},
        'Февраль': {'days_to_avans': 11, 'work_day': 20},

        'Март': {'days_to_avans': 10, 'work_day': 20},
        'Апрель': {'days_to_avans': 11, 'work_day': 21},
        'Май': {'days_to_avans': 8, 'work_day': 20},

        'Июнь': {'days_to_avans': 9, 'work_day': 19},
        'Июль': {'days_to_avans': 11, 'work_day': 23},
        'Август': {'days_to_avans': 11, 'work_day': 22},

        'Сентябрь': {'days_to_avans': 10, 'work_day': 21},
        'Октябрь': {'days_to_avans': 11, 'work_day': 23},
        'Ноябрь': {'days_to_avans': 10, 'work_day': 21},
    }

    month = data.get(month)
    wd = month.get('work_day')
    dta = month.get('days_to_avans')

    avans = (int(salary) / wd) * dta
    zepeshka = int(salary) - avans
    return round(avans), round(zepeshka)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.full_name}', reply_markup=kb_main)


@router.message(F.text == 'Очистка')
async def clear_state(message: Message, state: FSMContext):
    await state.clear()
    await message.reply("История очищена!", reply_markup=kb_main)


class Reg(StatesGroup):
    salary = State()
    month = State()


@router.message(F.text == 'Подсчитать зарплату и аванс')
async def process_confirm(message: Message, state: FSMContext):
    await state.set_state(Reg.salary)
    await message.answer('Какая у Вас месячная зарплата?', reply_markup=kb_salary['salary'])


# Обработчик выбора зарплаты
@router.callback_query(lambda c: c.data in ('60000', '70000'))
async def process_salary(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.update_data(salary=callback.data)
    await state.set_state(Reg.month)
    await callback.message.answer('За какой месяц считаем зарплату?', reply_markup=kb_salary['month'])


@router.callback_query(Reg.month)
async def result_salary(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.update_data(month=callback.data)
    data = await state.get_data()
    sal = salary(data.get('salary'), data.get('month'))
    await callback.message.answer(f'Месяц: {data["month"]}\nОбщая зарплата: {data["salary"]}\nАванс и Зарплата:{sal}')
