import asyncio
import logging

import telebot
from django.conf import settings
from django.core.management.base import BaseCommand
from telebot import util

from bot.main_bot import bot, logger


class Command(BaseCommand):
    help = "Запускаем бота"

    def handle(self, *args, **options):
        try:
            asyncio.run(run_bot())
        except Exception as err:
            logger.error(f'Ошибка: {err}')


async def run_bot():
    await bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("start", "Главное меню")
        ],
    )
    bot.add_custom_filter(telebot.asyncio_filters.ChatFilter())
    await bot.infinity_polling(logger_level=settings.LOG_LEVEL, allowed_updates=util.update_types)
