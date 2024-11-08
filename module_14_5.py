from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

import asyncio

initiate_db()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

ikb_buy = InlineKeyboardMarkup(resize_keyboard=True)
prod1_ib = InlineKeyboardButton('Product1', callback_data='product_buying')
prod2_ib = InlineKeyboardButton('Product2', callback_data='product_buying')
prod3_ib = InlineKeyboardButton('Product3', callback_data='product_buying')
prod4_ib = InlineKeyboardButton('Product4', callback_data='product_buying')

ikb_buy.row(prod1_ib, prod2_ib, prod3_ib, prod4_ib)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
calc_ib = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
formula_ib = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')

ikb.row(calc_ib, formula_ib)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_button = KeyboardButton(text="Информация")
calc_button = KeyboardButton(text='Рассчитать')
buy_button = KeyboardButton(text='Купить')
reg_button = KeyboardButton(text="Регистрация")

kb.row(start_button, calc_button)
kb.row(buy_button, reg_button)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    j = 1
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(f'Vitamin{j}.png', 'rb') as img:
            await  message.answer_photo(img, f"Продукт{j}")
            j += 1

    await message.answer('Выберите продукт для покупки:', reply_markup=ikb_buy)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def get_formula(call):
    await call.message.answer('Упрощенный вариант формулы Миффлина-Сан Жеора: \n'
                              '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='product_buying')
async def get_formula(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью .', reply_markup=kb)


@dp.message_handler(text="Информация")
async def info_message(message):
    await message.answer('Нажмите кнопку "Рассчитать" для рассчета нормы калорий ', reply_markup=kb)

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя:')



@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Вы успешно зарегистрированы:',  reply_markup=kb)
    await state.finish()



@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=int(message.text))
        await message.answer('Введите свой рост (см):')
        await UserState.growth.set()
    else:
        await message.answer('Пожалуйста, введите корректный возраст (число).')


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(growth=int(message.text))
        await message.answer('Введите свой вес (кг):')
        await UserState.weight.set()
    else:
        await message.answer('Пожалуйста, введите корректный рост (число).')


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(weight=int(message.text))
        data = await state.get_data()

        calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
        await message.answer(f"Вам необходимо следующее количество килокалорий (ккал) в сутки: {calories}")
        await state.finish()
    else:
        await message.answer('Пожалуйста, введите корректный вес (число).')


@dp.message_handler()
async def echo_message(message):
    await message.answer(f'Зачем вы написали мне?: {message.text}\n'
                         f'Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
