from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = '7368163380:AAFXPIDqjR64Vw62Fq4GqsbOSPZgR7o6v_0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text=['urban','ff','Goody'])
async def all_message(message):
    print("Сообщение: Urban")
    await message.answer(f"Ответ {message.text * 10}")

@dp.message_handler(commands=['urban','ff','Goody'])
async def all_message(message):
    print(f"Сообщение: command {message.text}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)