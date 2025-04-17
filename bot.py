from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiohttp import web
import asyncio
import os

TOKEN = '7044056826:AAEKMk8i2Q7SdpRBCQTqGvGGqPwTgQcjboA'

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# Команда /start
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Привет! Я бот 🤖\n\n"
        "Вот мои команды:\n"
        "/start — Приветствие\n"
        "/resume — Резюме\n"
        "/contact — Контакты\n"
        "/projects — Проекты\n"
    )

# Команда /resume
@dp.message(Command("resume"))
async def resume_cmd(message: Message):
    await message.answer("📄 Резюме Бейбарыса: https://biko222.github.io/Beibarys/")

# Заглушка: простой веб-сервер для Render
async def handle(request):
    return web.Response(text="Бот работает!")

async def start_web_app():
    app = web.Application()
    app.add_routes([web.get("/", handle)])

    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# Главный запуск
async def main():
    await asyncio.gather(
        dp.start_polling(bot),
        start_web_app()
    )

if __name__ == "__main__":
    asyncio.run(main())
