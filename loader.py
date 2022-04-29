from aiogram import Bot, Dispatcher, types
from data import config
import mysql.connector
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

db = mysql.connector.connect(
  host="localhost",
  user=config.mysql_user,
  password=config.mysql_password,
  database=config.mysql_db
)

cursor = db.cursor()
