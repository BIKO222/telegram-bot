# bot.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import os

TOKEN = os.getenv("BOT_TOKEN")  # Убедись, что переменная окружения задана

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def start_cmd(message: Message):
    await message.answer("Привет! Я бот 🤖")

@dp.message(commands=["resume"])
async def resume_cmd(message: Message):
    await message.answer("📄 Резюме Бейбарыса: https://biko222.github.io/Beibarys/")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
