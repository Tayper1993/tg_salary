from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from utils import get_salary

from keyboards.kb_main import kb_main
from keyboards.kb_salary import kb_salary


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.full_name}', reply_markup=kb_main)


@router.message(F.text == 'Очистка')
async def clear_state(message: Message, state: FSMContext):
    await state.clear()
    await message.reply('История очищена!', reply_markup=kb_main)


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
    salary = get_salary(data.get('salary'), data.get('month'))
    await callback.message.answer(
        f'Месяц: {data["month"]}\nОбщая зарплата: {data["salary"]}\nАванс и Зарплата:{salary}'
    )
