import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message

API_TOKEN = 'YOUR TOKEN'
CHAT_ID = 'YOUR ID'  # Замените на ID чата, куда нужно отправлять сообщения
MESSAGE = "text"
message1 = 'text 1'
INTERVAL = 1  # Интервал в секундах

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def send_periodic_message():
    while True:
        await bot.send_message(CHAT_ID, MESSAGE)
        await asyncio.sleep(INTERVAL)
        await bot.send_message(CHAT_ID, message1)
        await asyncio.sleep(INTERVAL)

if __name__ == '__main__':
    # Запускаем периодическую отправку сообщений
    asyncio.run(send_periodic_message())
