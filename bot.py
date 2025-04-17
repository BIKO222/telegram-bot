from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

TOKEN = '7044056826:AAEKMk8i2Q7SdpRBCQTqGvGGqPwTgQcjboA'

# Создание бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)  # Pass bot as a keyword argument

# Команда /start
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Привет! Я бот 🤖\n\n"
        "Я могу помочь тебе с информацией о твоём резюме, проекте и многом другом.\n"
        "Вот мои доступные команды:\n\n"
        "/start — Приветственное сообщение\n"
        "/resume — Посмотреть резюме\n"
        "/contact — Контактная информация\n"
        "/projects — Мои проекты\n",
        parse_mode="HTML"  # Specify parse_mode directly when sending messages
    )

# Команда /resume
@dp.message(Command("resume"))
async def resume_cmd(message: Message):
    await message.answer("📄 Резюме Бейбарыса: https://biko222.github.io/Beibarys/", parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
