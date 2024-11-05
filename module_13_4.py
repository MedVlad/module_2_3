from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = '7368163380:AAFXPIDqjR64Vw62Fq4GqsbOSPZgR7o6v_0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.\n'
                         'Введите команду /Calories для рассчета нормы калорий')

@dp.message_handler(text = ['/Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Вам необходимо следующее количество килокалорий (ккал) в сутки: {10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])+5}")
    await state.finish()

@dp.message_handler()
async def echo_message(message):
    await message.answer(f'вы написали мне: {message.text}\n'
                         f'Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)