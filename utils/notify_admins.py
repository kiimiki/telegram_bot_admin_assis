import logging
from aiogram import Dispatcher
from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            )
            text = "Бот запущен!"
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
