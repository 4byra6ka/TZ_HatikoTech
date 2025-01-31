import asyncio
import logging

import telebot
from django.conf import settings
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from telebot.types import Message

from imei.services import service_check_imei

bot = AsyncTeleBot(settings.TOKEN_BOT, state_storage=StateMemoryStorage(), parse_mode='HTML')
logger = telebot.logger
telebot.logger.setLevel(settings.LOG_LEVEL)

FileOutputHandler = logging.FileHandler('bot.log', encoding='utf-8')
server_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
FileOutputHandler.setFormatter(server_formatter)
telebot.logger.addHandler(FileOutputHandler)


@bot.message_handler(chat_id=settings.WHITE_LIST, commands=['start'])
async def handle_start(message: Message):
    """Команда /start"""
    print(message.chat.id)
    await bot.send_message(message.chat.id, 'Введите IMEI для проверки.')


@bot.message_handler(chat_id=settings.WHITE_LIST, regexp='^\\d{15}$')
async def handle_check_imei(message: Message):
    """Команда для проверки imei"""
    data_imei = await service_check_imei(message.text)
    if 'properties' in data_imei:
        text_imei = str(data_imei['properties']).replace(',', '\n').replace("'", "")
        await bot.send_message(message.chat.id, text_imei)
    else:
        await bot.send_message(message.chat.id, 'error: Внутренняя ошибка сервера')
