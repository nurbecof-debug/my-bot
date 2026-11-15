import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.environ["BOT_TOKEN"]

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Салам! Дүкөнгө кош келиңиз.")

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    print("Бот ишке кирди...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
