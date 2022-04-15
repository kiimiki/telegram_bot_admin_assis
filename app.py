from aiogram import executor
from handlers import dp


async def on_startup(_):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
