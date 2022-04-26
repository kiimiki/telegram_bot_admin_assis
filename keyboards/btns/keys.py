from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# --- Main BTNs ---

btnMainM = KeyboardButton('Главное меню')
btnBack = KeyboardButton('Назад')

# --- Order Menu ---

orderMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btnAccept = KeyboardButton('Подтвердить заказ')
btnCancel = KeyboardButton('Отменить Заказ')
orderMenu.add(btnAccept, btnCancel)

# --- Main menu ---

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btn_m1 = KeyboardButton('Услуги 🏷')
btn_m2 = KeyboardButton('Товары 💲')
btn_m3 = KeyboardButton('Корзина 📌')
mainMenu.add(btn_m1).insert(btn_m2).insert(btn_m3)

# --- Sub Menu ---

subMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btn_s1 = KeyboardButton('Нстройка сетевого оборудования')
btn_s2 = KeyboardButton('Нстройка OS Linux/Windows/MacOS')
subMenu.add(btn_s1).insert(btn_s2).add(btnMainM)

# --- OS Admin ---

osAdminMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btnLinux = KeyboardButton('Linux')
btnWindows = KeyboardButton('Windows')
btnMac = KeyboardButton('MacOS')
osAdminMenu.add(btnLinux, btnWindows, btnMac).add(btnBack, btnMainM)

# --- Network Admin menu---

netMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btnRouter = KeyboardButton('Маршрутизатор(ы)')
btnSwitch = KeyboardButton('Коммутатор(ы)')
btnRoSw = KeyboardButton('Маршрутизатор(ы)/Коммутатор(ы)/Точка WiFi')
btnWiFi = KeyboardButton('Точка WiFi')
netMenu.add(btnRouter, btnSwitch, btnWiFi, btnRoSw).add(btnBack, btnMainM)

# --- Network Equipment Goods ---

netEquipment = ReplyKeyboardMarkup(resize_keyboard=True)
btnMikrotik = KeyboardButton('Mikrotik')
btnUbiquiti = KeyboardButton('Ubiquiti')
btnLinksys = KeyboardButton('Linksys')
netEquipment.add(btnMikrotik, btnUbiquiti, btnLinksys).add(btnMainM)
