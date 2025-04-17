# bot.py

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.reply("Привет! Напиши /resume чтобы посмотреть резюме Бейбарыса.")

@dp.message_handler(commands=["resume"])
async def send_resume(message: Message):
    text = (
        "📄 Резюме Бейбарыса\n"
        "🌐 Сайт: https://biko222.github.io/Beibarys/\n\n"
        "💡 Кратко:\n"
        "— Ученик 8 класса\n"
        "— Интересуется искусственным интеллектом\n"
        "— Участвует в олимпиадах по информатике и математике\n"
        "— Создаёт сайты и изучает Python/Django\n"
    )
    await message.reply(text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
