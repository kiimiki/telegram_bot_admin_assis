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
btn_m1 = KeyboardButton('Меню 🏷')
btn_m2 = KeyboardButton('Оплата 💲')
btn_m3 = KeyboardButton('О проекте  📌')
mainMenu.add(btn_m3).insert(btn_m1).insert(btn_m2)

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

netAdminMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btnRouter = KeyboardButton('Маршрутизатор(ы)')
btnSwitch = KeyboardButton('Коммутатор(ы)')
btnRoSw = KeyboardButton('Маршрутизатор(ы)/Коммутатор(ы)/Точка WiFi')
btnWiFi = KeyboardButton('Точка WiFi')
netAdminMenu.add(btnRouter, btnSwitch, btnWiFi, btnRoSw).add(btnBack, btnMainM)
